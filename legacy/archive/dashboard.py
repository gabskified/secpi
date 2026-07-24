# New file: dashboard.py
# Run with: panel serve dashboard.py --show

import panel as pn
import param
import numpy as np
import json
import os
from datetime import datetime

# Import your existing classes (no modifications needed)
from secpi_main import (
    TwoLevelUrbanGrid, CorrectedCoolingModel, 
    VariableRandomnessACO, TreeSpecies, SensitivityAnalyzer
)

pn.extension('matplotlib')


class SECPIDashboard(param.Parameterized):
    """
    Interactive dashboard for SECPI exploration.
    Users adjust sliders and see results update live.
    """

    # --- CA Parameters ---
    morphology = param.Selector(
        default='organic', objects=['organic', 'linear'],
        doc="Urban growth pattern"
    )
    p_init = param.Number(default=0.15, bounds=(0.05, 0.40), step=0.05,
                          doc="Initial seed density")
    ca_alpha = param.Number(default=0.1, bounds=(0.0, 0.5), step=0.05,
                            doc="Base urbanization probability")
    ca_beta = param.Number(default=0.4, bounds=(0.1, 0.8), step=0.05,
                           doc="Neighborhood influence")

    # --- Cooling Model Parameters ---
    decay_lambda = param.Number(default=0.1, bounds=(0.01, 0.5), step=0.01,
                                doc="Gaussian decay rate")
    cca_threshold = param.Number(default=1.2, bounds=(0.5, 3.0), step=0.1,
                                 doc="CCA competition threshold (m²)")
    competition_k = param.Number(default=5.0, bounds=(1.0, 15.0), step=0.5,
                                 doc="Competition steepness")
    shade_weight = param.Number(default=0.7, bounds=(0.0, 1.0), step=0.05,
                                doc="Shade vs evapotranspiration weight")

    # --- ACO Parameters ---
    n_trees = param.Integer(default=5, bounds=(1, 15),
                            doc="Number of trees to place")
    n_ants = param.Integer(default=15, bounds=(5, 50))
    n_iterations = param.Integer(default=30, bounds=(5, 100))
    q0 = param.Number(default=0.7, bounds=(0.1, 1.0), step=0.05,
                      doc="Exploitation probability")
    n_species = param.Integer(default=6, bounds=(1, 6),
                              doc="Number of species available")

    # --- Actions ---
    run_optimization = param.Action(lambda self: self._run(), doc="Run ACO")
    run_sensitivity = param.Action(lambda self: self._run_sensitivity(),
                                   doc="Run Sensitivity Analysis")

    def __init__(self, **params):
        super().__init__(**params)
        self._grid = None
        self._cooling_model = None
        self._aco = None
        self._status = "Ready. Adjust parameters and click Run."
        self._fig_grid = None
        self._fig_solution = None
        self._fig_convergence = None
        self._results_text = ""

    @param.depends('morphology', 'p_init', 'ca_alpha', 'ca_beta')
    def _regenerate_grid(self):
        """Regenerate grid when CA parameters change."""
        self._grid = TwoLevelUrbanGrid(
            coarse_width=10, coarse_height=10,
            coarse_cell_size=10.0, fine_cell_size=1.0
        )
        self._grid.generate_ca_archetype(
            params={
                'p_init': self.p_init,
                'alpha': self.ca_alpha,
                'beta': self.ca_beta,
                'theta': 3
            },
            morphology=self.morphology
        )

    def _build_cooling_model(self):
        """Build cooling model from current slider values."""
        return CorrectedCoolingModel(
            decay_lambda=self.decay_lambda,
            cca_threshold=self.cca_threshold,
            competition_k=self.competition_k,
            shade_weight=self.shade_weight,
            evap_weight=1.0 - self.shade_weight
        )

    def _run(self):
        """Execute full optimization pipeline with current parameters."""
        import matplotlib.pyplot as plt
        from matplotlib.patches import Rectangle, Circle

        self._status = "Running optimization..."
        self._regenerate_grid()
        self._cooling_model = self._build_cooling_model()

        if len(self._grid.plantable_coords) == 0:
            self._status = "ERROR: No plantable cells generated."
            return

        aco = VariableRandomnessACO(
            self._grid, self._cooling_model,
            n_trees=self.n_trees,
            n_ants=self.n_ants,
            n_iterations=self.n_iterations,
            evaporation_rate=0.5,
            alpha=1.0, beta=2.0,
            q0=self.q0,
            random_seed=None,
            n_species_restricted=self.n_species
        )
        history_best, history_avg = aco.run(verbose=False)
        self._aco = aco

        # --- Generate Grid Visualization ---
        fig_grid, ax = plt.subplots(figsize=(6, 6))
        for i in range(self._grid.coarse_height):
            for j in range(self._grid.coarse_width):
                x = j * self._grid.coarse_cell_size
                y = i * self._grid.coarse_cell_size
                lu = self._grid.coarse_grid[i, j]
                cmap = {0: 'white', 1: 'gray', 3: 'lightgreen', 4: 'salmon'}
                rect = Rectangle((x, y),
                                 self._grid.coarse_cell_size,
                                 self._grid.coarse_cell_size,
                                 facecolor=cmap.get(lu, 'white'),
                                 edgecolor='black', linewidth=0.5, alpha=0.7)
                ax.add_patch(rect)
        ax.set_xlim(0, self._grid.fine_width)
        ax.set_ylim(0, self._grid.fine_height)
        ax.set_aspect('equal')
        ax.set_title('CA-Generated Urban Grid')
        plt.tight_layout()
        self._fig_grid = fig_grid

        # --- Generate Solution Visualization ---
        if aco.best_solution:
            tree_coords, tree_species = aco.best_solution
            display_cooling, _ = self._cooling_model.calculate_total_cooling(
                tree_coords, tree_species,
                self._grid.fine_grid_points, apply_competition=True
            )

            fig_sol, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

            # Left: placements
            for i in range(self._grid.coarse_height):
                for j in range(self._grid.coarse_width):
                    x = j * self._grid.coarse_cell_size
                    y = i * self._grid.coarse_cell_size
                    lu = self._grid.coarse_grid[i, j]
                    cmap = {0: 'white', 1: 'gray', 3: 'lightgreen', 4: 'salmon'}
                    rect = Rectangle((x, y),
                                     self._grid.coarse_cell_size,
                                     self._grid.coarse_cell_size,
                                     facecolor=cmap.get(lu, 'white'),
                                     edgecolor='black', linewidth=0.5, alpha=0.7)
                    ax1.add_patch(rect)

            ts_obj = TreeSpecies()
            for (tx, ty), sp in zip(tree_coords, tree_species):
                color = ts_obj.get_species_color(sp)
                ax1.scatter(tx, ty, color=color, s=150,
                            edgecolors='black', linewidth=1.5, zorder=5)
                cr = ts_obj.get_crown_radius(sp)
                circle = Circle((tx, ty), cr, color=color,
                                alpha=0.15, linewidth=1.5)
                ax1.add_patch(circle)

            ax1.set_xlim(0, self._grid.fine_width)
            ax1.set_ylim(0, self._grid.fine_height)
            ax1.set_aspect('equal')
            ax1.set_title('Tree Placements')

            # Right: cooling heatmap
            cg = display_cooling.reshape(
                self._grid.n_rows_fine, self._grid.n_cols_fine)
            im = ax2.imshow(cg.T,
                            extent=[0, self._grid.fine_width,
                                    0, self._grid.fine_height],
                            origin='lower', cmap='coolwarm_r', aspect='auto')
            for (tx, ty), sp in zip(tree_coords, tree_species):
                ax2.scatter(tx, ty, color='white', s=80,
                            edgecolors='black', linewidth=1, zorder=5)
            ax2.set_title('Cooling Distribution')
            plt.colorbar(im, ax=ax2, label='Cooling Intensity')
            plt.tight_layout()
            self._fig_solution = fig_sol

            # --- Convergence Plot ---
            fig_conv, ax_c = plt.subplots(figsize=(8, 4))
            ax_c.plot(history_best, 'b-', linewidth=2, label='Best')
            ax_c.plot(history_avg, 'r--', linewidth=1.5, label='Average')
            ax_c.set_xlabel('Iteration')
            ax_c.set_ylabel('SECPI')
            ax_c.set_title('ACO Convergence')
            ax_c.legend()
            ax_c.grid(True, alpha=0.3)
            plt.tight_layout()
            self._fig_convergence = fig_conv

            # --- Results Text ---
            species_summary = {}
            for sp in tree_species:
                species_summary[sp] = species_summary.get(sp, 0) + 1

            self._results_text = (
                f"SECPI: {aco.best_secpi:.4f}\n"
                f"Trees: {len(tree_coords)}\n"
                f"Species used: {species_summary}\n"
                f"Mean cooling: {np.mean(display_cooling):.4f}\n"
                f"Max cooling: {np.max(display_cooling):.4f}\n"
                f"Std cooling: {np.std(display_cooling):.4f}"
            )
        else:
            self._results_text = "No solution found."

        self._status = "Optimization complete."

    def _run_sensitivity(self):
        """Run sensitivity analysis with current parameters."""
        self._status = "Running sensitivity analysis (this takes a while)..."

        if self._grid is None:
            self._regenerate_grid()

        config = {
            'cooling_params': {
                'decay_lambda': self.decay_lambda,
                'cca_threshold': self.cca_threshold,
                'competition_k': self.competition_k,
            },
            'aco_params': {
                'n_trees': self.n_trees,
                'n_ants': self.n_ants,
                'n_iterations': self.n_iterations,
                'evaporation_rate': 0.5,
                'alpha': 1.0, 'beta': 2.0,
                'q0': self.q0,
                'random_seed': None
            }
        }

        sa_dir = os.path.join('interactive_outputs',
                              f'sensitivity_{datetime.now().strftime("%H%M%S")}')
        sa = SensitivityAnalyzer(self._grid, config, sa_dir)
        sa.run_full_sensitivity(n_runs_per_config=2)
        sa.compute_sensitivity_indices()
        sa.plot_tornado_diagram(top_n=12)
        sa.plot_category_summary()
        sa.save_results()

        self._status = f"Sensitivity analysis complete. Results in {sa_dir}"

    @param.depends('_status')
    def status_view(self):
        return pn.pane.Str(self._status, style={'font-size': '14px'})

    def panel(self):
        """Build the dashboard layout."""
        ca_controls = pn.Column(
            "### Urban Grid (CA)",
            self.param.morphology,
            self.param.p_init,
            self.param.ca_alpha,
            self.param.ca_beta,
        )
        cooling_controls = pn.Column(
            "### Cooling Model",
            self.param.decay_lambda,
            self.param.cca_threshold,
            self.param.competition_k,
            self.param.shade_weight,
        )
        aco_controls = pn.Column(
            "### ACO Settings",
            self.param.n_trees,
            self.param.n_species,
            self.param.n_ants,
            self.param.n_iterations,
            self.param.q0,
        )
        actions = pn.Column(
            pn.widgets.Button.from_param(self.param.run_optimization,
                                          button_type='primary'),
            pn.widgets.Button.from_param(self.param.run_sensitivity,
                                          button_type='warning'),
        )

        sidebar = pn.Column(ca_controls, cooling_controls,
                            aco_controls, actions, width=280)

        # Main content area with tabs
        grid_pane = pn.pane.Matplotlib(
            lambda: self._fig_grid, tight=True, dpi=100) if self._fig_grid else \
            pn.pane.Str("Run optimization to see grid.")
        solution_pane = pn.pane.Matplotlib(
            lambda: self._fig_solution, tight=True, dpi=100) if self._fig_solution else \
            pn.pane.Str("Run optimization to see solution.")
        convergence_pane = pn.pane.Matplotlib(
            lambda: self._fig_convergence, tight=True, dpi=100) if \
            self._fig_convergence else pn.pane.Str("Run optimization to see convergence.")
        results_pane = pn.pane.Str(
            lambda: self._results_text, style={'font-family': 'monospace'})

        tabs = pn.Tabs(
            ('Grid', grid_pane),
            ('Solution', solution_pane),
            ('Convergence', convergence_pane),
            ('Results', results_pane),
        )

        return pn.Row(sidebar, pn.Column(self.status_view, tabs))


# Launch
dashboard = SECPIDashboard()
dashboard.panel().servable(title="SECPI Optimizer")