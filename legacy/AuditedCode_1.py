import numpy as np
try:
    import pandas as pd
except Exception as exc:
    pd = None
    print(f"Warning: pandas import failed ({exc}). Some CSV/summary features may be unavailable.")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Patch
from matplotlib.colors import LinearSegmentedColormap
from scipy.spatial.distance import cdist
import itertools
from tqdm import tqdm
import warnings
import os
from datetime import datetime
import json
import copy
warnings.filterwarnings('ignore')

# =============================================================================

# SHARED REFERENCE-CUTOFF CALIBRATION (study-wide, computed ONCE)

# =============================================================================

def calibrate_global_reference_cutoffs(grid, cooling_model, species_list,
reference_n_trees=None, n_trees_range=(1, 6),
n_samples=100, random_seed=42):
    """
    Computes FIXED Q1/Q2/Q3 cooling-classification cutoffs ONCE per study,
    via Monte Carlo pooling of random valid placements. These cutoffs must
    be reused identically across every AntColonySystemACO instance in a study run
    (sensitivity sweeps, morphological robustness validation, k=1..6
    scenario comparisons, and the main optimization run) -- otherwise
    area_proportions/SECPI are not comparable across those analyses, which
    defeats the purpose of fixing the classification scheme. See audit note
    in AntColonySystemACO.evaluate_secpi.

    RESOLVED (per audit conversation): each of the n_samples draws now
    independently samples its own tree count uniformly from n_trees_range
    (inclusive), matching the full k=1..6 range used elsewhere in the study,
    rather than pooling only at one fixed reference_n_trees. This avoids
    anchoring the reference frame to a single k value while still applying
    it uniformly across every k in the sweep. Pass reference_n_trees (a
    single int) instead of n_trees_range to restore the old fixed-k
    behavior if ever needed.
    """
    if random_seed is not None:
        np.random.seed(random_seed)

    n_plantable = len(grid.plantable_coords)

    if reference_n_trees is not None:
        tree_count_choices = [min(reference_n_trees, n_plantable)] * n_samples
    else:
        lo, hi = n_trees_range
        tree_count_choices = np.random.randint(lo, hi + 1, size=n_samples)
        tree_count_choices = np.minimum(tree_count_choices, n_plantable)

    pooled_values = []
    for n_place in tree_count_choices:
        n_place = int(n_place)
        if n_place <= 0:
            continue
        idxs = np.random.choice(n_plantable, size=n_place, replace=False)
        coords = [grid.plantable_coords[i] for i in idxs]
        species = list(np.random.choice(species_list, size=n_place, replace=True))
        total_cooling, _ = cooling_model.calculate_total_cooling(
            coords, species, grid.fine_grid_points
        )
        pooled_values.append(total_cooling.flatten())

    pooled = np.concatenate(pooled_values)
    q1, q2, q3 = np.percentile(pooled, [25, 50, 75])
    return (q1, q2, q3)

# =============================================================================

# AUTOMATED INTERPRETATION ENGINE

# =============================================================================

class AutomatedInterpreter:
    """
    Generates automated interpretations for all analysis outputs.
    Provides context-aware insights based on SECPI manuscript methodology.
    """

    def __init__(self, output_dir):
        self.output_dir = output_dir
        self.interpretations = {}

    def interpret_grid_generation(self, grid, ca_params):
        """Interpret the CA-generated urban grid."""
        unique, counts = np.unique(grid.coarse_grid, return_counts=True)
        stats = dict(zip(unique, counts))
        total = grid.coarse_width * grid.coarse_height

        prohibited_pct = stats.get(1, 0) / total * 100
        available_pct = stats.get(3, 0) / total * 100
        vulnerable_pct = stats.get(4, 0) / total * 100

        interpretation = []
        interpretation.append("=" * 80)
        interpretation.append("AUTOMATED INTERPRETATION: URBAN GRID GENERATION")
        interpretation.append("=" * 80)

        interpretation.append("\n1. GRID COMPOSITION ANALYSIS")
        interpretation.append("-" * 40)
        interpretation.append(f"   Total Cells: {total} ({grid.coarse_width}x{grid.coarse_height})")
        interpretation.append(f"   Prohibited (Buildings): {stats.get(1, 0)} cells ({prohibited_pct:.1f}%)")
        interpretation.append(f"   Available (Plantable): {stats.get(3, 0)} cells ({available_pct:.1f}%)")
        interpretation.append(f"   Vulnerable Zones: {stats.get(4, 0)} cells ({vulnerable_pct:.1f}%)")

        interpretation.append("\n2. URBAN MORPHOLOGY ASSESSMENT")
        interpretation.append("-" * 40)

        if prohibited_pct > 40:
            density_class = "HIGH DENSITY"
            density_desc = "Limited planting opportunities; strategic placement critical"
        elif prohibited_pct > 25:
            density_class = "MEDIUM DENSITY"
            density_desc = "Moderate planting opportunities; balanced approach recommended"
        else:
            density_class = "LOW DENSITY"
            density_desc = "Abundant planting opportunities; coverage optimization feasible"

        interpretation.append(f"   Density Classification: {density_class}")
        interpretation.append(f"   Implication: {density_desc}")

        interpretation.append("\n3. VULNERABILITY CONTEXT")
        interpretation.append("-" * 40)

        if vulnerable_pct > 30:
            vuln_level = "HIGH"
            vuln_implication = "Strong equity weighting expected to significantly influence optimization"
        elif vulnerable_pct > 15:
            vuln_level = "MODERATE"
            vuln_implication = "Equity considerations will moderately affect tree placement"
        else:
            vuln_level = "LOW"
            vuln_implication = "Efficiency-driven placement likely to dominate"

        interpretation.append(f"   Vulnerability Level: {vuln_level} ({vulnerable_pct:.1f}%)")
        interpretation.append(f"   Implication: {vuln_implication}")

        interpretation.append("\n4. CA PARAMETERS INFLUENCE")
        interpretation.append("-" * 40)
        interpretation.append(f"   Initial Seed Probability (p_init): {ca_params.get('p_init', 'N/A')}")
        interpretation.append(f"   Growth Rate (alpha): {ca_params.get('alpha', 'N/A')}")
        interpretation.append(f"   Neighbor Influence (beta): {ca_params.get('beta', 'N/A')}")
        interpretation.append(f"   Clustering Threshold (theta): {ca_params.get('theta', 'N/A')}")
        interpretation.append(f"   Morphology Type: {ca_params.get('morphology', 'organic')}")

        interpretation.append("\n5. RECOMMENDATIONS")
        interpretation.append("-" * 40)
        if available_pct < 20:
            interpretation.append("   WARNING: Limited plantable area (<20%)")
            interpretation.append("     Consider reducing n_trees or using smaller-crown species")
        if vulnerable_pct > 25:
            interpretation.append("   [OK] High vulnerability zones present")
            interpretation.append("     Equity-weighted optimization highly relevant")

        self.interpretations['grid_generation'] = "\n".join(interpretation)
        return self.interpretations['grid_generation']

    def interpret_equity_weights(self, grid):
        """Interpret the vulnerability-based equity weight distribution."""
        weights = grid.vulnerability_weights

        w_high = np.sum(weights >= 2.0)
        w_med = np.sum((weights >= 1.5) & (weights < 2.0))
        w_low = np.sum(weights < 1.5)
        total = len(weights)

        interpretation = []
        interpretation.append("=" * 80)
        interpretation.append("AUTOMATED INTERPRETATION: EQUITY WEIGHT DISTRIBUTION")
        interpretation.append("=" * 80)

        interpretation.append("\n1. WEIGHT DISTRIBUTION (Fine Grid)")
        interpretation.append("-" * 40)
        interpretation.append(f"   High Priority (w=2.0): {w_high} cells ({w_high/total*100:.1f}%)")
        interpretation.append(f"   Medium Priority (w=1.5): {w_med} cells ({w_med/total*100:.1f}%)")
        interpretation.append(f"   Low Priority (w=1.0): {w_low} cells ({w_low/total*100:.1f}%)")

        interpretation.append("\n2. EQUITY IMPLICATION")
        interpretation.append("-" * 40)

        weighted_avg = np.mean(weights)
        interpretation.append(f"   Mean Equity Weight: {weighted_avg:.3f}")

        if weighted_avg > 1.4:
            interpretation.append("   Assessment: HIGH equity sensitivity")
            interpretation.append("     Optimization will strongly prioritize vulnerable zones")
            interpretation.append("     Expect concentrated cooling near high-weight areas")
        elif weighted_avg > 1.2:
            interpretation.append("   Assessment: MODERATE equity sensitivity")
            interpretation.append("     Balanced consideration of efficiency and equity")
        else:
            interpretation.append("   Assessment: LOW equity sensitivity")
            interpretation.append("     Efficiency-driven optimization will dominate")

        interpretation.append("\n3. SECPI SCORING IMPACT")
        interpretation.append("-" * 40)
        interpretation.append("   The SECPI formula multiplies cooling class scores by equity weights:")
        interpretation.append("   SECPI = Σ[(A_k - A_baseline) × W_k × E_k]")
        interpretation.append("   Where E_k is the mean equity weight per cooling class.")
        interpretation.append(f"   With current distribution, high-cooling zones in vulnerable areas")
        interpretation.append(f"   will receive up to {weighted_avg/1.0:.1f}x scoring boost.")

        self.interpretations['equity_weights'] = "\n".join(interpretation)
        return self.interpretations['equity_weights']

    def interpret_species_characteristics(self, tree_species):
        """Interpret species biophysical characteristics."""
        interpretation = []
        interpretation.append("=" * 80)
        interpretation.append("AUTOMATED INTERPRETATION: SPECIES CHARACTERISTICS")
        interpretation.append("=" * 80)

        interpretation.append("\n1. SPECIES RANKING BY COOLING POTENTIAL (D_j)")
        interpretation.append("-" * 40)

        species_data = []
        for species in tree_species.species_list:
            params = tree_species.get_species_params(species)
            d_j = tree_species.get_normalized_cooling_potential(species)
            species_data.append({
                'name': species,
                'CPA': params['CPA'],
                'LAI': params['LAI'],
                'CD': params['crown_diameter_m'],
                'D_j': d_j
            })

        species_data.sort(key=lambda x: x['D_j'], reverse=True)

        for rank, sp in enumerate(species_data, 1):
            interpretation.append(f"   {rank}. {sp['name']}: D_j = {sp['D_j']:.4f}")
            interpretation.append(f"      CPA = {sp['CPA']:.1f}m², LAI = {sp['LAI']:.2f}, CD = {sp['CD']:.1f}m")

        interpretation.append("\n2. COOLING MECHANISM BREAKDOWN")
        interpretation.append("-" * 40)
        interpretation.append("   Cooling Potential Formula: D_j = 0.7×(CPA/CPA_max) + 0.3×(LAI/LAI_max)")
        interpretation.append(f"   - Shade Component (CPA): 70% weight")
        interpretation.append(f"   - Evapotranspiration Component (LAI): 30% weight")

        top_species = species_data[0]
        bottom_species = species_data[-1]

        interpretation.append("\n3. KEY FINDINGS")
        interpretation.append("-" * 40)
        interpretation.append(f"   Best Performer: {top_species['name']} (D_j = {top_species['D_j']:.4f})")
        interpretation.append(f"   - Large crown ({top_species['CPA']:.1f}m^2) provides extensive shade coverage")

        if top_species['LAI'] == max(sp['LAI'] for sp in species_data):
            interpretation.append(f"   - Also has highest LAI ({top_species['LAI']:.2f}) for maximum evapotranspiration")

        interpretation.append(f"\n   Lowest Performer: {bottom_species['name']} (D_j = {bottom_species['D_j']:.4f})")
        interpretation.append(f"   - May still be optimal in space-constrained scenarios")

        interpretation.append("\n4. OPTIMIZATION IMPLICATIONS")
        interpretation.append("-" * 40)
        interpretation.append("   Without diversity constraints, ACO will likely favor:")
        interpretation.append(f"   - {species_data[0]['name']} for maximum cooling intensity")
        interpretation.append(f"   - {species_data[1]['name']} as secondary choice")
        interpretation.append("   Mono-species solutions may emerge if single species dominates.")

        self.interpretations['species'] = "\n".join(interpretation)
        return self.interpretations['species']

    def interpret_optimization_result(self, aco, tree_species_obj, grid):
        """Interpret ACO optimization results."""
        interpretation = []
        interpretation.append("=" * 80)
        interpretation.append("AUTOMATED INTERPRETATION: ACO OPTIMIZATION RESULTS")
        interpretation.append("=" * 80)

        if not aco.best_solution:
            interpretation.append("\n⚠ ERROR: No valid solution found.")
            self.interpretations['optimization'] = "\n".join(interpretation)
            return self.interpretations['optimization']

        tree_coords, tree_species = aco.best_solution
        unique_species = list(set(tree_species))
        species_counts = {sp: tree_species.count(sp) for sp in unique_species}

        interpretation.append("\n1. SOLUTION SUMMARY")
        interpretation.append("-" * 40)
        interpretation.append(f"   Best SECPI Score: {aco.best_secpi:.4f}")
        interpretation.append(f"   Number of Trees: {len(tree_coords)}")
        interpretation.append(f"   Unique Species: {len(unique_species)}")

        interpretation.append("\n2. SPECIES COMPOSITION")
        interpretation.append("-" * 40)
        for sp, count in sorted(species_counts.items(), key=lambda x: x[1], reverse=True):
            pct = count / len(tree_species) * 100
            d_j = tree_species_obj.get_normalized_cooling_potential(sp)
            interpretation.append(f"   {sp}: {count} trees ({pct:.0f}%) - D_j = {d_j:.4f}")

        interpretation.append("\n3. DIVERSITY ASSESSMENT")
        interpretation.append("-" * 40)
        diversity_ratio = len(unique_species) / len(tree_species)

        if len(unique_species) == 1:
            interpretation.append("   Pattern: MONO-SPECIES SOLUTION")
            interpretation.append("     ACO converged on single highest-performing species")
            interpretation.append("     Maximum cooling intensity achieved")
            interpretation.append("     Consider: ecological diversity vs. cooling efficiency trade-off")
        elif diversity_ratio > 0.6:
            interpretation.append("   Pattern: HIGH DIVERSITY SOLUTION")
            interpretation.append("     Multiple species selected")
            interpretation.append("     May indicate spatial heterogeneity in vulnerability")
        else:
            interpretation.append("   Pattern: MODERATE DIVERSITY SOLUTION")
            interpretation.append(f"     Diversity ratio: {diversity_ratio:.2f}")

        interpretation.append("\n4. SPATIAL DISTRIBUTION ANALYSIS")
        interpretation.append("-" * 40)

        # Check if trees are near vulnerable zones
        if len(grid.vulnerable_coords) > 0:
            near_vuln_count = 0
            for tx, ty in tree_coords:
                min_dist = np.min(cdist([(tx, ty)], grid.vulnerable_coords, 'euclidean'))
                if min_dist <= 20:
                    near_vuln_count += 1

            interpretation.append(f"   Trees near vulnerable zones (≤20m): {near_vuln_count}/{len(tree_coords)}")

            if near_vuln_count / len(tree_coords) > 0.6:
                interpretation.append("   → Strong equity-driven placement")
            else:
                interpretation.append("   → Efficiency-driven or balanced placement")

        interpretation.append("\n5. COOLING PERFORMANCE METRICS")
        interpretation.append("-" * 40)
        if aco.best_cooling is not None:
            cooling = aco.best_cooling
            interpretation.append(f"   Mean Cooling Intensity: {np.mean(cooling):.4f}")
            interpretation.append(f"   Max Cooling Intensity: {np.max(cooling):.4f}")
            interpretation.append(f"   Std Dev: {np.std(cooling):.4f}")
            interpretation.append(f"   Coverage (>0.01): {np.sum(cooling > 0.01)/len(cooling)*100:.1f}%")

        interpretation.append("\n6. SECPI SCORE INTERPRETATION")
        interpretation.append("-" * 40)
        if aco.best_secpi > 3.0:
            interpretation.append("   Rating: EXCELLENT cooling distribution")
            interpretation.append("   → High proportion of cells in upper cooling quartiles")
        elif aco.best_secpi > 2.0:
            interpretation.append("   Rating: GOOD cooling distribution")
            interpretation.append("   → Significant improvement over baseline")
        elif aco.best_secpi > 1.0:
            interpretation.append("   Rating: MODERATE cooling distribution")
            interpretation.append("   → Some cooling benefit achieved")
        else:
            interpretation.append("   Rating: LIMITED cooling distribution")
            interpretation.append("   → Consider increasing n_trees or using larger-crown species")

        self.interpretations['optimization'] = "\n".join(interpretation)
        return self.interpretations['optimization']

    def interpret_zonal_efficiency(self, cooling_values, vulnerability_weights):
        """Interpret zonal cooling efficiency results."""
        interpretation = []
        interpretation.append("=" * 80)
        interpretation.append("AUTOMATED INTERPRETATION: ZONAL COOLING EFFICIENCY")
        interpretation.append("=" * 80)

        # Categorize zones
        zone_data = {'High (w=2.0)': [], 'Medium (w=1.5)': [], 'Low (w=1.0)': []}

        for i, weight in enumerate(vulnerability_weights):
            if weight >= 2.0:
                zone_data['High (w=2.0)'].append(cooling_values[i])
            elif weight >= 1.5:
                zone_data['Medium (w=1.5)'].append(cooling_values[i])
            else:
                zone_data['Low (w=1.0)'].append(cooling_values[i])

        interpretation.append("\n1. ZONE-WISE COOLING STATISTICS")
        interpretation.append("-" * 40)

        zone_means = {}
        for zone, vals in zone_data.items():
            if vals:
                zone_means[zone] = np.mean(vals)
                interpretation.append(f"   {zone}:")
                interpretation.append(f"      Mean Cooling: {np.mean(vals):.4f}")
                interpretation.append(f"      Std Dev: {np.std(vals):.4f}")
                interpretation.append(f"      Cell Count: {len(vals)}")

        interpretation.append("\n2. EQUITY ACHIEVEMENT ANALYSIS")
        interpretation.append("-" * 40)

        high_mean = zone_means.get('High (w=2.0)', 0)
        low_mean = zone_means.get('Low (w=1.0)', 0)

        if high_mean > 0 and low_mean > 0:
            ratio = high_mean / low_mean
            interpretation.append(f"   High-to-Low Zone Cooling Ratio: {ratio:.2f}")

            if ratio > 1.2:
                interpretation.append("   [OK] EQUITY GOAL ACHIEVED")
                interpretation.append("   → Vulnerable zones receive MORE cooling than average")
                interpretation.append("   → Optimization successfully prioritized equity")
            elif ratio > 0.8:
                interpretation.append("   ~ EQUITY NEUTRAL")
                interpretation.append("   → Similar cooling across all zones")
                interpretation.append("   → Neither equity nor efficiency dominated")
            else:
                interpretation.append("   [UH-OH] EFFICIENCY-DOMINATED")
                interpretation.append("   → Low-priority zones received more cooling")
                interpretation.append("   → Consider increasing vulnerability weights")

        interpretation.append("\n3. WEIGHTED CONTRIBUTION ANALYSIS")
        interpretation.append("-" * 40)

        total_weighted = 0
        for zone, vals in zone_data.items():
            if vals:
                weight = 2.0 if 'High' in zone else (1.5 if 'Medium' in zone else 1.0)
                contribution = np.mean(vals) * weight * len(vals)
                total_weighted += contribution
                interpretation.append(f"   {zone} contribution: {contribution:.2f}")

        interpretation.append(f"   Total Weighted Cooling: {total_weighted:.2f}")

        interpretation.append("\n4. RECOMMENDATIONS")
        interpretation.append("-" * 40)

        if high_mean < low_mean:
            interpretation.append("   → Consider: Increase weight differential (e.g., w=3.0 for high priority)")
            interpretation.append("   → Consider: Force placement constraints near vulnerable zones")
        else:
            interpretation.append("   → Current configuration achieves equity goals")
            interpretation.append("   → Cooling resources appropriately allocated to vulnerable populations")

        self.interpretations['zonal_efficiency'] = "\n".join(interpretation)
        return self.interpretations['zonal_efficiency']

    def interpret_scenario_comparison(self, results_with, results_without):
        """Interpret WITH vs WITHOUT vulnerability scenario comparison."""
        interpretation = []
        interpretation.append("=" * 80)
        interpretation.append("AUTOMATED INTERPRETATION: SCENARIO COMPARISON")
        interpretation.append("WITH vs WITHOUT VULNERABLE CELLS")
        interpretation.append("=" * 80)

        w_secpi = results_with.get('best_secpi', 0) if results_with else 0
        wo_secpi = results_without.get('best_secpi', 0) if results_without else 0
        diff = w_secpi - wo_secpi

        interpretation.append("\n1. SECPI SCORE COMPARISON")
        interpretation.append("-" * 40)
        interpretation.append(f"   WITH VULNERABLE:    {w_secpi:.4f}")
        interpretation.append(f"   WITHOUT VULNERABLE: {wo_secpi:.4f}")
        interpretation.append(f"   Absolute Difference: {diff:+.4f}")

        if w_secpi > 0:
            pct_diff = (diff / w_secpi) * 100
            interpretation.append(f"   Relative Difference: {pct_diff:+.1f}%")

        interpretation.append("\n2. STATISTICAL SIGNIFICANCE")
        interpretation.append("-" * 40)

        if abs(diff) > 0.1:
            interpretation.append("   Difference: SIGNIFICANT (|Δ| > 0.1)")
        elif abs(diff) > 0.05:
            interpretation.append("   Difference: MODERATE (0.05 < |Δ| < 0.1)")
        else:
            interpretation.append("   Difference: NEGLIGIBLE (|Δ| < 0.05)")

        interpretation.append("\n3. INTERPRETATION")
        interpretation.append("-" * 40)

        if diff > 0.05:
            interpretation.append("   Finding: WITH VULNERABLE performs BETTER")
            interpretation.append("   Implication:")
            interpretation.append("   → Equity weighting improves SECPI score")
            interpretation.append("   → Vulnerable zones benefit from targeted cooling")
            interpretation.append("   → Equity and efficiency are SYNERGISTIC in this configuration")
        elif diff < -0.05:
            interpretation.append("   Finding: WITHOUT VULNERABLE performs BETTER")
            interpretation.append("   Implication:")
            interpretation.append("   → Pure efficiency optimization yields higher SECPI")
            interpretation.append("   → Equity weighting may be misaligned with optimal placement")
            interpretation.append("   → Consider revising vulnerability zone definitions")
        else:
            interpretation.append("   Finding: COMPARABLE PERFORMANCE")
            interpretation.append("   Implication:")
            interpretation.append("   → Vulnerability consideration has minimal impact")
            interpretation.append("   → Optimal placements similar regardless of equity weighting")

        interpretation.append("\n4. SPECIES SELECTION COMPARISON")
        interpretation.append("-" * 40)

        if results_with and results_without:
            sp_with = set(results_with.get('unique_species', []))
            sp_without = set(results_without.get('unique_species', []))

            interpretation.append(f"   WITH VULN species: {sp_with}")
            interpretation.append(f"   WITHOUT VULN species: {sp_without}")

            if sp_with == sp_without:
                interpretation.append("   → Same species selected (robust solution)")
            else:
                diff_species = sp_with.symmetric_difference(sp_without)
                interpretation.append(f"   → Different species: {diff_species}")
                interpretation.append("   → Vulnerability context affects species selection")

        interpretation.append("\n5. POLICY RECOMMENDATION")
        interpretation.append("-" * 40)

        if diff > 0:
            interpretation.append("   RECOMMEND: Use WITH VULNERABLE configuration")
            interpretation.append("   Rationale: Better cooling for vulnerable populations")
            interpretation.append("   without sacrificing overall performance")
        else:
            interpretation.append("   RECOMMEND: Evaluate trade-offs carefully")
            interpretation.append("   Consider: Is the SECPI loss justified by equity gains?")

        self.interpretations['scenario_comparison'] = "\n".join(interpretation)
        return self.interpretations['scenario_comparison']

    def interpret_sensitivity_analysis(self, sensitivity_df):
        """Interpret sensitivity analysis results."""
        interpretation = []
        interpretation.append("=" * 80)
        interpretation.append("AUTOMATED INTERPRETATION: SENSITIVITY ANALYSIS")
        interpretation.append("=" * 80)

        if pd is not None and hasattr(sensitivity_df, 'nlargest'):
            rows = list(sensitivity_df.to_dict('records'))
            top_10 = sensitivity_df.nlargest(10, 'sensitivity_index')
            top_3 = sensitivity_df.nlargest(3, 'sensitivity_index')
            category_sensitivity = sensitivity_df.groupby('category')['sensitivity_index'].agg(['mean', 'max', 'sum'])
            category_sensitivity = category_sensitivity.sort_values('sum', ascending=False)
            most_sensitive = sensitivity_df.loc[sensitivity_df['sensitivity_index'].idxmax()]
            high_sensitivity_mask = sensitivity_df['sensitivity_index'] > 0.1
            low_sensitivity_mask = sensitivity_df['sensitivity_index'] < 0.01
        else:
            rows = list(sensitivity_df) if isinstance(sensitivity_df, list) else []
            rows = sorted(rows, key=lambda row: row['sensitivity_index'], reverse=True)
            top_10 = rows[:10]
            top_3 = rows[:3]
            category_totals = {}
            for row in rows:
                cat = row['category']
                category_totals[cat] = category_totals.get(cat, 0.0) + row['sensitivity_index']
            category_sensitivity = []
            for cat, total in category_totals.items():
                max_val = max(r['sensitivity_index'] for r in rows if r['category'] == cat)
                mean_val = sum(r['sensitivity_index'] for r in rows if r['category'] == cat) / sum(1 for r in rows if r['category'] == cat)
                category_sensitivity.append((cat, {'sum': total, 'max': max_val, 'mean': mean_val}))
            category_sensitivity = sorted(category_sensitivity, key=lambda x: x[1]['sum'], reverse=True)
            most_sensitive = rows[0] if rows else None
            high_sensitivity_mask = [row['sensitivity_index'] > 0.1 for row in rows]
            low_sensitivity_mask = [row['sensitivity_index'] < 0.01 for row in rows]

        interpretation.append("\n1. MOST INFLUENTIAL PARAMETERS (Top 10)")
        interpretation.append("-" * 40)

        if pd is not None and hasattr(sensitivity_df, 'nlargest'):
            for _, row in top_10.iterrows():
                interpretation.append(f"   {row['parameter']}")
                interpretation.append(f"      Category: {row['category']}")
                interpretation.append(f"      Sensitivity Index: {row['sensitivity_index']:.6f}")
                interpretation.append(f"      SECPI Range: [{row['secpi_low']:.4f}, {row['secpi_high']:.4f}]")
        else:
            for row in top_10:
                interpretation.append(f"   {row['parameter']}")
                interpretation.append(f"      Category: {row['category']}")
                interpretation.append(f"      Sensitivity Index: {row['sensitivity_index']:.6f}")
                interpretation.append(f"      SECPI Range: [{row['secpi_low']:.4f}, {row['secpi_high']:.4f}]")

        interpretation.append("\n2. CATEGORY-LEVEL SENSITIVITY")
        interpretation.append("-" * 40)

        if pd is not None and hasattr(sensitivity_df, 'nlargest'):
            for cat, row in category_sensitivity.iterrows():
                interpretation.append(f"   {cat}:")
                interpretation.append(f"      Total Sensitivity: {row['sum']:.6f}")
                interpretation.append(f"      Max Single Parameter: {row['max']:.6f}")
                interpretation.append(f"      Mean Sensitivity: {row['mean']:.6f}")
        else:
            for cat, stats in category_sensitivity:
                interpretation.append(f"   {cat}:")
                interpretation.append(f"      Total Sensitivity: {stats['sum']:.6f}")
                interpretation.append(f"      Max Single Parameter: {stats['max']:.6f}")
                interpretation.append(f"      Mean Sensitivity: {stats['mean']:.6f}")

        interpretation.append("\n3. CRITICAL FINDINGS")
        interpretation.append("-" * 40)

        if pd is not None and hasattr(sensitivity_df, 'nlargest'):
            dominant_cat = category_sensitivity.index[0]
            interpretation.append(f"   Most Influential Category: {dominant_cat}")
            interpretation.append(f"   Most Sensitive Parameter: {most_sensitive['parameter']}")
            interpretation.append(f"   → Changing this parameter causes {most_sensitive['sensitivity_index']*100:.2f}% SECPI variation")
        else:
            dominant_cat = category_sensitivity[0][0] if category_sensitivity else 'N/A'
            interpretation.append(f"   Most Influential Category: {dominant_cat}")
            if most_sensitive is not None:
                interpretation.append(f"   Most Sensitive Parameter: {most_sensitive['parameter']}")
                interpretation.append(f"   → Changing this parameter causes {most_sensitive['sensitivity_index']*100:.2f}% SECPI variation")

        interpretation.append("\n4. ROBUSTNESS ASSESSMENT")
        interpretation.append("-" * 40)

        if pd is not None and hasattr(sensitivity_df, 'nlargest'):
            high_sensitivity_count = len(sensitivity_df[sensitivity_df['sensitivity_index'] > 0.1])
            total_params = len(sensitivity_df)
        else:
            high_sensitivity_count = sum(1 for flag in high_sensitivity_mask if flag)
            total_params = len(rows)

        interpretation.append(f"   Parameters with high sensitivity (>0.1): {high_sensitivity_count}/{total_params}")

        if high_sensitivity_count == 0:
            interpretation.append("   Assessment: HIGHLY ROBUST")
            interpretation.append("   → Model results stable across parameter variations")
        elif high_sensitivity_count <= 3:
            interpretation.append("   Assessment: MODERATELY ROBUST")
            interpretation.append("   → Few parameters significantly affect results")
            interpretation.append("   → Focus calibration efforts on top sensitive parameters")
        else:
            interpretation.append("   Assessment: SENSITIVE")
            interpretation.append("   → Multiple parameters significantly affect results")
            interpretation.append("   → Careful calibration required")

        interpretation.append("\n5. CALIBRATION RECOMMENDATIONS")
        interpretation.append("-" * 40)

        if pd is not None and hasattr(sensitivity_df, 'nlargest'):
            for i, (_, row) in enumerate(top_3.iterrows(), 1):
                interpretation.append(f"   {i}. {row['parameter']} ({row['category']})")
            low_sens = sensitivity_df[sensitivity_df['sensitivity_index'] < 0.01]
            interpretation.append(f"\n   Low-priority parameters (sensitivity < 0.01):")
            interpretation.append(f"   → {len(low_sens)} parameters can use default values")
        else:
            for i, row in enumerate(top_3, 1):
                interpretation.append(f"   {i}. {row['parameter']} ({row['category']})")
            interpretation.append(f"\n   Low-priority parameters (sensitivity < 0.01):")
            interpretation.append(f"   → {sum(1 for flag in low_sensitivity_mask if flag)} parameters can use default values")

        self.interpretations['sensitivity'] = "\n".join(interpretation)
        return self.interpretations['sensitivity']

    def interpret_morphological_robustness(self, robustness_results):
        """Interpret morphological robustness validation results."""
        interpretation = []
        interpretation.append("=" * 80)
        interpretation.append("AUTOMATED INTERPRETATION: MORPHOLOGICAL ROBUSTNESS")
        interpretation.append("=" * 80)

        interpretation.append("\n1. PERFORMANCE BY MORPHOLOGY")
        interpretation.append("-" * 40)

        morph_stats = []
        for morph, data in robustness_results.items():
            if data['secpi_values']:
                morph_stats.append({
                    'name': morph,
                    'mean': data['mean_secpi'],
                    'std': data['std_secpi'],
                    'cv': data['std_secpi'] / data['mean_secpi'] if data['mean_secpi'] > 0 else 0,
                    'n': data['n_successful']
                })

        morph_stats.sort(key=lambda x: x['mean'], reverse=True)

        for ms in morph_stats:
            interpretation.append(f"   {ms['name']}:")
            interpretation.append(f"      Mean SECPI: {ms['mean']:.4f} ± {ms['std']:.4f}")
            interpretation.append(f"      CV: {ms['cv']:.3f}, n={ms['n']}")

        interpretation.append("\n2. CROSS-MORPHOLOGY CONSISTENCY")
        interpretation.append("-" * 40)

        means = [ms['mean'] for ms in morph_stats]
        overall_mean = np.mean(means)
        overall_std = np.std(means)
        overall_cv = overall_std / overall_mean if overall_mean > 0 else 0

        interpretation.append(f"   Overall Mean SECPI: {overall_mean:.4f}")
        interpretation.append(f"   Cross-Morphology Std: {overall_std:.4f}")
        interpretation.append(f"   Cross-Morphology CV: {overall_cv:.3f}")

        if overall_cv < 0.15:
            interpretation.append("\n   Assessment: HIGHLY ROBUST")
            interpretation.append("   → Algorithm performs consistently across morphologies")
            interpretation.append("   → Results generalizable to various urban forms")
        elif overall_cv < 0.30:
            interpretation.append("\n   Assessment: MODERATELY ROBUST")
            interpretation.append("   → Some variation across morphologies")
            interpretation.append("   → Consider morphology-specific parameter tuning")
        else:
            interpretation.append("\n   Assessment: MORPHOLOGY-SENSITIVE")
            interpretation.append("   → Significant performance variation")
            interpretation.append("   → Algorithm may need morphology-specific adaptations")

        interpretation.append("\n3. BEST/WORST PERFORMING MORPHOLOGIES")
        interpretation.append("-" * 40)

        best = morph_stats[0]
        worst = morph_stats[-1]

        interpretation.append(f"   Best: {best['name']} (SECPI = {best['mean']:.4f})")
        interpretation.append(f"   Worst: {worst['name']} (SECPI = {worst['mean']:.4f})")
        interpretation.append(f"   Performance Gap: {best['mean'] - worst['mean']:.4f}")

        interpretation.append("\n4. RELIABILITY ASSESSMENT")
        interpretation.append("-" * 40)

        # Check within-morphology consistency
        high_cv_morphs = [ms for ms in morph_stats if ms['cv'] > 0.2]

        if not high_cv_morphs:
            interpretation.append("   All morphologies show consistent results (CV < 0.2)")
            interpretation.append("   → High confidence in single-run results")
        else:
            interpretation.append("   Morphologies with high variability:")
            for ms in high_cv_morphs:
                interpretation.append(f"   - {ms['name']} (CV = {ms['cv']:.3f})")
            interpretation.append("   → Multiple runs recommended for these morphologies")

        self.interpretations['morphological_robustness'] = "\n".join(interpretation)
        return self.interpretations['morphological_robustness']

    def save_all_interpretations(self):
        """Save all interpretations to files."""
        for name, interpretation in self.interpretations.items():
            filepath = os.path.join(self.output_dir, f'interpretation_{name}.txt')
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(interpretation)
            print(f"Saved interpretation: {filepath}")

        # Save combined interpretation
        combined = []
        combined.append("=" * 100)
        combined.append("COMPREHENSIVE AUTOMATED INTERPRETATION REPORT")
        combined.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        combined.append("=" * 100)

        for name, interpretation in self.interpretations.items():
            combined.append(f"\n\n{'#' * 80}")
            combined.append(f"# SECTION: {name.upper()}")
            combined.append(f"{'#' * 80}\n")
            combined.append(interpretation)

        combined_path = os.path.join(self.output_dir, 'COMPLETE_INTERPRETATION_REPORT.txt')
        with open(combined_path, 'w', encoding='utf-8') as f:
            f.write("\n".join(combined))
        print(f"\nSaved complete report: {combined_path}")

        return combined_path

# =============================================================================

# SENSITIVITY ANALYSIS MODULE (OAT - One At a Time)

# =============================================================================

class SensitivityAnalyzer:
    """
    Performs One-At-a-Time (OAT) sensitivity analysis on model parameters.
    Outputs CSV with parameter sensitivities and visualizations.
    """

    def __init__(self, base_grid, base_cooling_model, base_aco_config, output_dir,
                 reference_cutoffs=None):
        self.base_grid = base_grid
        self.base_cooling_model = base_cooling_model
        self.base_aco_config = base_aco_config
        self.output_dir = output_dir
        # Fixed, study-wide cutoffs -- see calibrate_global_reference_cutoffs().
        # Passed through to every AntColonySystemACO created during sensitivity
        # evaluation so results stay comparable with the rest of the study.
        self.reference_cutoffs = reference_cutoffs

        # Define parameter categories and ranges
        self.parameter_definitions = self._define_parameters()
        self.results = []
        self.baseline_secpi = None

    def _define_parameters(self):
        """Define all parameters for sensitivity analysis."""
        params = {
            # Cooling Model Parameters
            'Cooling_Model': {
                'decay_lambda': {'base': 1.9, 'range': [0.5, 3.0]},
                'cca_threshold': {'base': 1.2, 'range': [0.5, 2.0]},
                'competition_k': {'base': 5.0, 'range': [1.0, 10.0]},
            },
            # Weighting Parameters
            'Weighting': {
                'shade_weight': {'base': 0.7, 'range': [0.5, 0.9]},
            },
            # Species Morphology Parameters
            'Species_Morphology': {},
            # Species Allometry Parameters (LAI-related)
            'Species_Allometry': {},
        }

        # Add species-specific parameters
        tree_species = TreeSpecies()
        for species in tree_species.species_list:
            sp_params = tree_species.get_species_params(species)

            # Crown diameter
            base_cd = sp_params['crown_diameter_m']
            params['Species_Morphology'][f'{species}.crown_diameter_m'] = {
                'base': base_cd,
                'range': [base_cd * 0.8, base_cd * 1.2],
                'species': species,
                'param_name': 'crown_diameter_m'
            }

            # Height
            base_h = sp_params['height_m']
            params['Species_Morphology'][f'{species}.height_m'] = {
                'base': base_h,
                'range': [base_h * 0.8, base_h * 1.2],
                'species': species,
                'param_name': 'height_m'
            }

            # Allometric constants -- Table 4's own values (author-team
            # estimates: DBH=(h/h0)^(1/h1), LAI=l0*DBH^l1), perturbed +/-20%
            # for methodological consistency with crown_diameter/height above.
            # (Previously these were arbitrary fractions of LAI/height with
            # no connection to Table 4 or the allometric formula -- see audit.)
            for pname in ('l0', 'l1', 'h0', 'h1'):
                base_val = sp_params[pname]
                params['Species_Allometry'][f'{species}.{pname}'] = {
                    'base': base_val,
                    'range': [base_val * 0.8, base_val * 1.2],
                    'species': species,
                    'param_name': pname
                }

        return params

    def _run_single_evaluation(self, cooling_params, species_modifications=None):
        """Run a single ACO evaluation with specified parameters.

        State isolation (decision D-12, Flag #96): `TreeSpecies.SPECIES_DATA` is
        a CLASS attribute shared by every `TreeSpecies` instance in the process,
        so the species perturbations below are writes to global state. Before
        this guard existed they were never restored, which meant (a) the LAI
        write compounded geometrically across repeated identical evaluations, so
        the routine was not idempotent; (b) every evaluation after the first
        species perturbation ran against contaminated data, so "all other
        parameters held at baseline" -- the definition of a one-at-a-time sweep
        -- was false; and (c) the contamination escaped the sweep entirely into
        any later pipeline step in the same process.

        The snapshot is taken before ANY write point executes, including the
        `CorrectedCoolingModel` construction below (which builds a `TreeSpecies`
        and so rewrites every species' CPA), and is restored in an unconditional
        `finally` so that an exception mid-evaluation still leaves shared state
        clean.

        Three things are snapshotted, not one. `_calculate_cpa_and_normalize()`
        caches `max_CPA` and `max_LAI` as INSTANCE attributes, and
        `get_normalized_cooling_potential()` divides by both -- they are live
        denominators in the cooling term. Restoring only the dict would leave any
        `TreeSpecies` outliving this call with denominators computed from
        contaminated data. They are restored from the snapshot directly rather
        than by re-running `_calculate_cpa_and_normalize()`, so the restored
        values are bit-identical by construction rather than by assumption.

        The dict is restored IN PLACE at both levels -- the outer mapping and
        each species' inner mapping -- rather than by rebinding the class
        attribute, so that any code holding a reference to either (for example
        via `get_species_params()`, which returns the inner dict itself) sees
        the restored values.
        """
        species_data_snapshot = copy.deepcopy(TreeSpecies.SPECIES_DATA)
        normalization_snapshot = None

        try:
            # Create modified cooling model
            cooling_model = CorrectedCoolingModel(
                decay_lambda=cooling_params.get('decay_lambda', 1.9),
                cca_threshold=cooling_params.get('cca_threshold', 1.2),
                competition_k=cooling_params.get('competition_k', 5.0),
                shade_weight=cooling_params.get('shade_weight', 0.7),
                evap_weight=1.0 - cooling_params.get('shade_weight', 0.7)
            )

            # Apply species modifications if any
            if species_modifications:
                ts = cooling_model.tree_species
                # Capture the cached normalization denominators of the very
                # instance that will run _calculate_cpa_and_normalize() below,
                # before any perturbation is applied. See the docstring.
                normalization_snapshot = (ts, ts.max_CPA, ts.max_LAI)
                for species, param_name, value in species_modifications:
                    if species not in ts.SPECIES_DATA:
                        continue
                    if param_name in ('l0', 'l1', 'h0', 'h1'):
                        # Real allometric pipeline: perturb the constant,
                        # recompute LAI via DBH=(h/h0)^(1/h1), LAI=l0*DBH^l1,
                        # then apply the *relative* change to the currently
                        # adopted hardcoded LAI baseline. This measures the
                        # genuine marginal sensitivity of the allometric
                        # constant without letting the absolute-magnitude gap
                        # between computed LAI (~0.01-0.09) and adopted LAI
                        # (~3.15-6.07) swamp the result. See audit note.
                        baseline_computed_lai = ts.get_computed_lai(species)
                        perturbed_computed_lai = ts.get_computed_lai(
                            species, **{f'{param_name}_override': value}
                        )
                        ratio = (perturbed_computed_lai / baseline_computed_lai
                                 if baseline_computed_lai > 0 else 1.0)
                        hardcoded_lai = ts.SPECIES_DATA[species]['LAI']
                        ts.SPECIES_DATA[species]['LAI'] = hardcoded_lai * ratio
                    else:
                        ts.SPECIES_DATA[species][param_name] = value
                        # Recalculate CPA if crown diameter changed
                        if param_name == 'crown_diameter_m':
                            ts.SPECIES_DATA[species]['CPA'] = \
                                (np.pi / 4) * (value ** 2)
                # Recalculate normalization
                ts._calculate_cpa_and_normalize()

            # Run ACO at PRODUCTION settings (matches the main optimization
            # run) so sensitivity indices are computed on the same-fidelity
            # optimizer as the headline results -- previously hardcoded to
            # n_ants=10/n_iterations=15 regardless of production config,
            # an undisclosed inconsistency; see audit conversation.
            aco = AntColonySystemACO(
                self.base_grid, cooling_model,
                n_trees=self.base_aco_config['n_trees'],
                n_ants=self.base_aco_config['n_ants'],
                n_iterations=self.base_aco_config['n_iterations'],
                evaporation_rate=self.base_aco_config['evaporation_rate'],
                alpha=self.base_aco_config['alpha'],
                beta=self.base_aco_config['beta'],
                q0=self.base_aco_config['q0'],
                reference_cutoffs=self.reference_cutoffs
            )
            aco.run(verbose=False)

            return aco.best_secpi if aco.best_secpi else 0

        except Exception as e:
            print(f"Evaluation error: {e}")
            return 0

        finally:
            # Restore the shared species dict in place, at both levels, so that
            # object identity is preserved for any held reference.
            live_species_data = TreeSpecies.SPECIES_DATA
            for species_name in list(live_species_data.keys()):
                if species_name not in species_data_snapshot:
                    del live_species_data[species_name]
            for species_name, saved_fields in species_data_snapshot.items():
                live_fields = live_species_data.get(species_name)
                if live_fields is None:
                    live_species_data[species_name] = copy.deepcopy(saved_fields)
                else:
                    live_fields.clear()
                    live_fields.update(copy.deepcopy(saved_fields))

            # Restore the cached normalization denominators from the snapshot
            # rather than recomputing them, so they are bit-identical.
            if normalization_snapshot is not None:
                snapshot_ts, saved_max_cpa, saved_max_lai = normalization_snapshot
                snapshot_ts.max_CPA = saved_max_cpa
                snapshot_ts.max_LAI = saved_max_lai

    def run_oat_analysis(self, n_samples=3):
        """
        Run One-At-a-Time sensitivity analysis.
        For each parameter, evaluate at low and high bounds while keeping others at baseline.
        """
        print("\n" + "=" * 80)
        print("SENSITIVITY ANALYSIS: ONE-AT-A-TIME (OAT) PARAMETER SWEEPING")
        print("=" * 80)

        # First, get baseline SECPI
        print("\nCalculating baseline SECPI...")
        baseline_scores = []
        for _ in range(n_samples):
            score = self._run_single_evaluation({
                'decay_lambda': 1.9,
                'cca_threshold': 1.2,
                'competition_k': 5.0,
                'shade_weight': 0.7
            })
            baseline_scores.append(score)

        self.baseline_secpi = np.mean(baseline_scores)
        print(f"Baseline SECPI: {self.baseline_secpi:.4f}")

        # Iterate through all parameters
        total_params = sum(len(params) for params in self.parameter_definitions.values())

        with tqdm(total=total_params, desc="Sensitivity Analysis") as pbar:
            for category, params in self.parameter_definitions.items():
                for param_name, param_info in params.items():

                    low_val = param_info['range'][0]
                    high_val = param_info['range'][1]

                    # Evaluate at low bound
                    low_scores = []
                    high_scores = []

                    for _ in range(n_samples):
                        if category in ['Cooling_Model', 'Weighting']:
                            # Cooling model parameters
                            cooling_params = {
                                'decay_lambda': 1.9,
                                'cca_threshold': 1.2,
                                'competition_k': 5.0,
                                'shade_weight': 0.7
                            }

                            # Low evaluation
                            cooling_params_low = cooling_params.copy()
                            cooling_params_low[param_name] = low_val
                            low_scores.append(self._run_single_evaluation(cooling_params_low))

                            # High evaluation
                            cooling_params_high = cooling_params.copy()
                            cooling_params_high[param_name] = high_val
                            high_scores.append(self._run_single_evaluation(cooling_params_high))

                        else:
                            # Species parameters
                            species = param_info.get('species')
                            actual_param = param_info.get('param_name')

                            if actual_param in ['crown_diameter_m', 'height_m']:
                                # Low evaluation
                                mods_low = [(species, actual_param, low_val)]
                                low_scores.append(self._run_single_evaluation({}, mods_low))

                                # High evaluation
                                mods_high = [(species, actual_param, high_val)]
                                high_scores.append(self._run_single_evaluation({}, mods_high))
                            else:
                                # Allometry parameters (l0, l1, h0, h1) --
                                # now genuinely evaluated through the
                                # allometric pipeline (see _run_single_evaluation),
                                # not random noise.
                                mods_low = [(species, actual_param, low_val)]
                                low_scores.append(self._run_single_evaluation({}, mods_low))

                                mods_high = [(species, actual_param, high_val)]
                                high_scores.append(self._run_single_evaluation({}, mods_high))

                    # Calculate statistics
                    secpi_low = np.mean(low_scores)
                    secpi_high = np.mean(high_scores)
                    absolute_effect = abs(secpi_high - secpi_low)
                    sensitivity_index = absolute_effect / self.baseline_secpi if self.baseline_secpi > 0 else 0

                    self.results.append({
                        'parameter': param_name,
                        'category': category,
                        'secpi_low': secpi_low,
                        'secpi_high': secpi_high,
                        'absolute_effect': absolute_effect,
                        'sensitivity_index': sensitivity_index
                    })

                    pbar.update(1)

        # Create DataFrame and sort
        if pd is not None:
            self.results_df = pd.DataFrame(self.results)
            self.results_df = self.results_df.sort_values('sensitivity_index', ascending=False)
        else:
            self.results_df = None

        return self.results_df

    def save_results(self):
        """Save sensitivity analysis results to CSV."""
        csv_path = os.path.join(self.output_dir, 'sensitivity_analysis_oat.csv')
        if self.results_df is None:
            print("Skipping CSV export because pandas is unavailable.")
            return None, None

        self.results_df.to_csv(csv_path, index=False)
        print(f"Saved: {csv_path}")

        # Also save category summary
        category_summary = self.results_df.groupby('category').agg({
            'sensitivity_index': ['mean', 'max', 'sum', 'count']
        }).round(6)
        category_summary.columns = ['mean_sensitivity', 'max_sensitivity', 'total_sensitivity', 'param_count']
        category_summary = category_summary.sort_values('total_sensitivity', ascending=False)

        category_csv_path = os.path.join(self.output_dir, 'sensitivity_analysis_by_category.csv')
        category_summary.to_csv(category_csv_path)
        print(f"Saved: {category_csv_path}")

        return csv_path, category_csv_path

    def plot_sensitivity_results(self):
        """Generate sensitivity analysis visualizations."""
        if self.results_df is None:
            if not self.results:
                print("No sensitivity results available to plot.")
                return None, None, None
            self.results_df = [
                {
                    'parameter': row['parameter'],
                    'category': row['category'],
                    'sensitivity_index': row['sensitivity_index'],
                    'secpi_low': row['secpi_low'],
                    'secpi_high': row['secpi_high'],
                }
                for row in self.results
            ]

        if pd is not None and hasattr(self.results_df, 'nlargest'):
            df = self.results_df
            top_15 = df.nlargest(15, 'sensitivity_index')
            top_20 = df.nlargest(20, 'sensitivity_index')
            category_totals = df.groupby('category')['sensitivity_index'].sum().sort_values(ascending=True)
            rows = [
                {
                    'parameter': row['parameter'],
                    'category': row['category'],
                    'sensitivity_index': row['sensitivity_index'],
                    'secpi_low': row['secpi_low'],
                    'secpi_high': row['secpi_high'],
                }
                for _, row in top_20.iterrows()
            ]
        else:
            rows = sorted(self.results_df, key=lambda x: x['sensitivity_index'], reverse=True)
            top_15 = rows[:15]
            top_20 = rows[:20]
            category_totals = {}
            for item in rows:
                category_totals[item['category']] = category_totals.get(item['category'], 0.0) + item['sensitivity_index']
            category_totals = dict(sorted(category_totals.items(), key=lambda x: x[1]))

        # 1. Tornado Plot (Top 15 parameters)
        fig, ax = plt.subplots(figsize=(12, 10))

        y_pos = np.arange(len(top_15))
        colors = []
        category_colors = {
            'Species_Morphology': '#E74C3C',
            'Species_Allometry': '#3498DB',
            'Cooling_Model': '#2ECC71',
            'Weighting': '#9B59B6'
        }

        for item in top_15:
            cat = item['category'] if isinstance(item, dict) else item['category']
            colors.append(category_colors.get(cat, 'gray'))

        values = [item['sensitivity_index'] for item in top_15]
        bars = ax.barh(y_pos, values, color=colors, edgecolor='black')
        ax.set_yticks(y_pos)
        ax.set_yticklabels([item['parameter'] for item in top_15], fontsize=10)
        ax.invert_yaxis()
        ax.set_xlabel('Sensitivity Index', fontsize=12)
        ax.set_title('Parameter Sensitivity Analysis (Top 15)\nOne-At-a-Time Sweeping',
                    fontsize=14, fontweight='bold')
        ax.grid(True, alpha=0.3, axis='x')

        # Legend
        legend_patches = [Patch(facecolor=c, label=cat, edgecolor='black')
                         for cat, c in category_colors.items()]
        ax.legend(handles=legend_patches, loc='lower right', fontsize=10)

        tornado_path = os.path.join(self.output_dir, 'sensitivity_tornado_plot.png')
        plt.tight_layout()
        plt.savefig(tornado_path, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"Saved: {tornado_path}")

        # 2. Category-level sensitivity
        fig, ax = plt.subplots(figsize=(10, 6))

        if pd is not None and hasattr(self.results_df, 'groupby'):
            category_labels = list(category_totals.index)
            category_values = list(category_totals.values)
        else:
            category_labels = list(category_totals.keys())
            category_values = list(category_totals.values())

        colors = [category_colors.get(cat, 'gray') for cat in category_labels]
        bars = ax.barh(category_labels, category_values, color=colors, edgecolor='black')

        for bar, val in zip(bars, category_values):
            ax.annotate(f'{val:.4f}', xy=(bar.get_width(), bar.get_y() + bar.get_height()/2),
                       xytext=(5, 0), textcoords='offset points', va='center', fontsize=11)

        ax.set_xlabel('Total Sensitivity Index', fontsize=12)
        ax.set_title('Sensitivity by Parameter Category', fontsize=14, fontweight='bold')
        ax.grid(True, alpha=0.3, axis='x')

        category_path = os.path.join(self.output_dir, 'sensitivity_by_category.png')
        plt.tight_layout()
        plt.savefig(category_path, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"Saved: {category_path}")

        # 3. SECPI Range Plot
        fig, ax = plt.subplots(figsize=(14, 8))

        y_pos = np.arange(len(top_20))

        # Plot ranges
        for i, row in enumerate(top_20):
            color = category_colors.get(row['category'], 'gray')
            ax.plot([row['secpi_low'], row['secpi_high']], [i, i],
                   color=color, linewidth=3, marker='o', markersize=8)

        ax.axvline(self.baseline_secpi, color='black', linestyle='--',
                   linewidth=2, label=f'Baseline ({self.baseline_secpi:.4f})')

        ax.set_yticks(y_pos)
        ax.set_yticklabels([row['parameter'] for row in top_20], fontsize=9)
        ax.invert_yaxis()
        ax.set_xlabel('SECPI Score', fontsize=12)
        ax.set_title('SECPI Range by Parameter (Top 20)', fontsize=14, fontweight='bold')
        ax.legend(loc='lower right')
        ax.grid(True, alpha=0.3, axis='x')

        range_path = os.path.join(self.output_dir, 'sensitivity_secpi_ranges.png')
        plt.tight_layout()
        plt.savefig(range_path, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"Saved: {range_path}")

        return tornado_path, category_path, range_path

# =============================================================================

# CORE GRID CLASS

# =============================================================================

class TwoLevelUrbanGrid:
    """
    Generates coarse grid using Cellular Automata (CA) logic from SECPI
    Manuscript and handles fine grid discretization for cooling evaluation.
    """

    def __init__(self, coarse_width=10, coarse_height=10,
                 coarse_cell_size=10.0, fine_cell_size=1.0):
        self.coarse_width = coarse_width
        self.coarse_height = coarse_height
        self.coarse_cell_size = coarse_cell_size

        self.fine_width = coarse_width * coarse_cell_size
        self.fine_height = coarse_height * coarse_cell_size
        self.fine_cell_size = fine_cell_size

        self.n_cols_fine = int(self.fine_width / self.fine_cell_size)
        self.n_rows_fine = int(self.fine_height / self.fine_cell_size)
        self.total_fine_cells = self.n_rows_fine * self.n_cols_fine

        self.fine_x_coords = np.arange(0, self.fine_width, fine_cell_size)
        self.fine_y_coords = np.arange(0, self.fine_height, fine_cell_size)
        self.fine_grid_points = np.array([(x, y) for x in self.fine_x_coords
                                          for y in self.fine_y_coords])

        self.coarse_x_centers = np.arange(coarse_cell_size / 2,
                                          self.fine_width, coarse_cell_size)
        self.coarse_y_centers = np.arange(coarse_cell_size / 2,
                                          self.fine_height, coarse_cell_size)
        self.coarse_centers = np.array([(x, y) for x in self.coarse_x_centers
                                        for y in self.coarse_y_centers])

        self.coarse_grid = None
        self.fine_grid = None
        self.plantable_coords = []
        self.vulnerable_coords = []

        print(f"Two-level grid: {coarse_width}x{coarse_height} coarse cells, "
              f"{self.n_cols_fine}x{self.n_rows_fine} fine cells")

    def get_moore_neighborhood(self, grid, x, y):
        rows, cols = grid.shape
        p_count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                nx, ny = x + i, y + j
                if 0 <= nx < rows and 0 <= ny < cols:
                    if grid[nx, ny] == 1:
                        p_count += 1
        return p_count

    def generate_ca_archetype(self, params, morphology="organic", max_iterations=40,
                               p_target_range=(0.55, 0.65), v_target_range=(0.05, 0.10)):
        """
        Two-phase land-use generation:

        PHASE 1 (Almeida-style CA growth): generates realistic clustering
        structure using a recursive, neighborhood-weighted transition
        probability, per the manuscript's cited Almeida et al. formalism:

            p_i^{kl}(t+1) = gamma * [ sum_{j in Omega_i} N_j^l(t) / 8 ] * p_i^{kl}(t)

        where k=0 ("empty/available"), l=1 ("Prohibited/built"), Omega_i is
        the Moore neighborhood of cell i, N_j^l(t) in {0,1} indicates
        whether neighbor j is in state l at time t, and gamma is a global
        growth-rate calibration constant. p_i^{kl}(t) is clipped to [0,1]
        after each update and used as a Bernoulli trial: cell i transitions
        to state l at t+1 with probability p_i^{kl}(t+1).

        A morphology-dependent spatial weighting multiplies the neighbor
        fraction term (a standard extension in CA urban-growth literature,
        analogous to a zoning/suitability factor):

            Omega_i(t) *= 1.5   if morphology="organic" and n_p(i,t) >= theta
            Omega_i(t) *= 1.5   if morphology="linear"  and |row(i) - H/2| < 2

        Initial condition: p_i^{kl}(0) = p0 for every initially-empty cell
        (a uniform baseline susceptibility to conversion).

        AUDIT NOTE (corrected formula): as originally transcribed in the
        manuscript, this equation was self-referential -- p_i^{kl}(t+1)
        appeared on BOTH sides, making it mathematically degenerate (solving
        for p_i^{kl}(t+1) forces it to 0 whenever gamma*Omega_i(t) != 1).
        The right-hand probability term has been corrected to p_i^{kl}(t)
        (the prior time step), consistent with a standard first-order
        recursive Markov formulation and with how Almeida-style transition
        potentials are actually applied in the cited literature. This also
        fixes the previous (non-Almeida, additive-heuristic) implementation's
        pathology: because that rule gave every empty cell an unconditional
        alpha>0 chance of transitioning regardless of neighbor count, with
        no reversion, it had no interior equilibrium and saturated toward
        100% Prohibited within a handful of iterations (emergency fallback
        fired in ~87% of runs -- see audit conversation). The corrected
        Almeida-style rule instead requires p_i^{kl}(t) > 0 (from a nonzero
        p0) AND a nonzero neighbor fraction for growth, so isolated cells
        far from any built cluster do not spontaneously convert -- consistent
        with agglomeration-driven urban growth and empirically confirmed
        (gamma=4.0, p0=0.5) to reach the target density band on its own in
        54/60 seeded runs; Phase 2 below makes the remainder exact.

        PHASE 2 (density calibration): natural CA growth is stochastic and
        proceeds in discrete multi-cell jumps, so it will not reliably land
        inside a narrow target band on its own. To guarantee the study's
        target land-use composition on every run, cells are trimmed or added
        after Phase 1:

            target_N_P = round(p_mid * N_total) + N_V

        where p_mid is the midpoint of p_target_range and N_V is the planned
        Phase-3 Vulnerable-cell count (added here because Phase 3 converts
        that many Prohibited cells to Vulnerable -- see below). If the
        Phase-1 output exceeds target_N_P, the lowest-Moore-connectivity
        Prohibited cells are reverted first (preserving cluster cores); if
        below, empty cells adjacent to existing clusters are preferentially
        added (preserving morphology) until target_N_P is reached.

        PHASE 3 (target-based Vulnerable-zone carving): the ORIGINAL
        implementation picked num_centers = 0.05*N_total buffer centers at
        Manhattan-distance radius=3 (a 25-cell diamond per center).
        AUDIT NOTE: on a 10x10 grid this requests up to 5*25=125
        cell-conversions against only 100 available cells -- guaranteed
        heavy overlap. Measured empirically, this converted 48-81% of the
        grid to Vulnerable even on an already-correctly-sized 60%-P grid,
        against a manuscript target of 5-10%. Phase 3 instead grows
        Vulnerable zones cell-by-cell via 4-connected BFS expansion from a
        small number of Prohibited-cell seeds, stopping exactly at:

            N_V = round(v_mid * N_total),  v_mid = midpoint of v_target_range

        This guarantees |V|/N_total lands within v_target_range on every
        run, independent of grid size.

        Empirical validation (see audit conversation): 100/100 runs across
        both organic and linear morphologies landed simultaneously within
        p_target_range, the complementary Available range, and
        v_target_range, with visibly organic/contiguous clustering
        preserved in Phase 1 output.

        NOTE FOR MANUSCRIPT: this is a two-phase process (stochastic Almeida-
        style growth for realistic clustering, then deterministic calibration
        to a target density), not unconstrained emergent CA behavior. Methods
        section should describe both phases explicitly, matching the
        equations above -- and should present the corrected (t) right-hand
        side, not the original self-referential (t+1) form.
        """
        p_init = params.get('p_init', 0.15)
        gamma = params.get('gamma', 4.0)
        p0 = params.get('p0', 0.5)
        theta = params.get('theta', 3)

        total_cells = self.coarse_height * self.coarse_width
        p_low, p_high = p_target_range
        p_mid = (p_low + p_high) / 2
        v_low, v_high = v_target_range
        v_mid = (v_low + v_high) / 2
        n_v_target = int(round(v_mid * total_cells))

        # --- PHASE 1: Almeida-style recursive multiplicative CA growth ---
        self.coarse_grid = np.zeros((self.coarse_height, self.coarse_width), dtype=int)
        n_seeds = int(total_cells * p_init)
        indices = [(r, c) for r in range(self.coarse_height)
                   for c in range(self.coarse_width)]
        np.random.shuffle(indices)
        for r, c in indices[:n_seeds]:
            self.coarse_grid[r, c] = 1

        transition_prob = np.full((self.coarse_height, self.coarse_width), p0, dtype=float)

        for _ in range(max_iterations):
            density = np.sum(self.coarse_grid == 1) / total_cells
            if p_low <= density <= p_high:
                break
            new_grid = self.coarse_grid.copy()
            new_prob = transition_prob.copy()
            for r in range(self.coarse_height):
                for c in range(self.coarse_width):
                    if self.coarse_grid[r, c] == 0:
                        n_p = self.get_moore_neighborhood(self.coarse_grid, r, c)
                        omega = n_p / 8.0
                        if morphology == "organic":
                            if n_p >= theta:
                                omega *= 1.5
                        elif morphology == "linear":
                            if abs(r - self.coarse_height // 2) < 2:
                                omega *= 1.5
                        p_next = gamma * omega * transition_prob[r, c]
                        p_next = min(max(p_next, 0.0), 1.0)
                        new_prob[r, c] = p_next
                        if np.random.random() < p_next:
                            new_grid[r, c] = 1
            self.coarse_grid = new_grid
            transition_prob = new_prob

        # --- PHASE 2: exact trim/top-up, compensating for Phase 3's P->V conversions ---
        target_n_p = int(round(p_mid * total_cells)) + n_v_target
        current_n_p = int(np.sum(self.coarse_grid == 1))

        if current_n_p > target_n_p:
            excess = current_n_p - target_n_p
            p_coords = np.argwhere(self.coarse_grid == 1)
            neighbor_counts = np.array([
                self.get_moore_neighborhood(self.coarse_grid, r, c) for r, c in p_coords
            ])
            order = np.argsort(neighbor_counts)  # revert lowest-connectivity cells first
            for idx in order[:excess]:
                r, c = p_coords[idx]
                self.coarse_grid[r, c] = 0
        elif current_n_p < target_n_p:
            needed = target_n_p - current_n_p
            added = 0
            attempts = 0
            max_attempts = total_cells * 20
            while added < needed and attempts < max_attempts:
                attempts += 1
                r = np.random.randint(0, self.coarse_height)
                c = np.random.randint(0, self.coarse_width)
                if self.coarse_grid[r, c] == 0:
                    n_p = self.get_moore_neighborhood(self.coarse_grid, r, c)
                    if n_p > 0 or np.random.random() < 0.5:
                        self.coarse_grid[r, c] = 1
                        added += 1

        # --- PHASE 3: target-based Vulnerable-zone carving (BFS from P-cell seeds) ---
        p_cells = np.argwhere(self.coarse_grid == 1)
        v_count = 0
        if len(p_cells) > 0:
            n_seed_centers = max(1, int(total_cells * 0.02))
            seed_idx = np.random.choice(len(p_cells),
                                        min(n_seed_centers, len(p_cells)),
                                        replace=False)
            queue = [tuple(p_cells[i]) for i in seed_idx]
            visited = set()
            qi = 0
            while v_count < n_v_target and qi < len(queue):
                cr, cc = queue[qi]
                qi += 1
                if (cr, cc) in visited:
                    continue
                visited.add((cr, cc))
                if self.coarse_grid[cr, cc] != 4:
                    self.coarse_grid[cr, cc] = 4
                    v_count += 1
                if v_count >= n_v_target:
                    break
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = cr + dr, cc + dc
                    if (0 <= nr < self.coarse_height and 0 <= nc < self.coarse_width
                            and (nr, nc) not in visited):
                        queue.append((nr, nc))

        self.coarse_grid[self.coarse_grid == 0] = 3

        # Safety net only -- should not fire given Phases 1-3 above guarantee
        # target compliance, but retained in case of pathological parameter
        # combinations (e.g. p_target_range spanning >95%).
        if 3 not in self.coarse_grid:
            print("Warning: CA generation could not reach target Available "
                  "share with the given parameters. Forcing plantable spots.")
            empty_indices = np.random.choice(total_cells, int(total_cells * 0.2),
                                             replace=False)
            flat_grid = self.coarse_grid.flatten()
            flat_grid[empty_indices] = 3
            self.coarse_grid = flat_grid.reshape(self.coarse_height, self.coarse_width)

        expansion_factor = int(self.coarse_cell_size / self.fine_cell_size)
        self.fine_grid = np.zeros((self.n_rows_fine, self.n_cols_fine), dtype=int)
        for i in range(self.coarse_height):
            for j in range(self.coarse_width):
                start_row = i * expansion_factor
                end_row = (i + 1) * expansion_factor
                start_col = j * expansion_factor
                end_col = (j + 1) * expansion_factor
                self.fine_grid[start_row:end_row, start_col:end_col] = self.coarse_grid[i, j]

        self.plantable_coords = []
        for i in range(self.coarse_height):
            for j in range(self.coarse_width):
                if self.coarse_grid[i, j] == 3:
                    X = self.coarse_x_centers[j]
                    Y = self.coarse_y_centers[i]
                    self.plantable_coords.append((X, Y))

        self.vulnerable_coords = []
        vulnerable_fine = np.argwhere(self.fine_grid == 4)
        self.vulnerable_coords = np.array([
            (self.fine_x_coords[col], self.fine_y_coords[row])
            for row, col in vulnerable_fine
        ])

        self.plantable_coords = np.array(self.plantable_coords)
        self.vulnerability_weights = self._calculate_vulnerability_weights()

        unique, counts = np.unique(self.coarse_grid, return_counts=True)
        stats = dict(zip(unique, counts))
        print(f"CA Generation Complete. Stats (1=P, 3=A, 4=V): {stats}")
        return self.coarse_grid, self.fine_grid

    def _calculate_vulnerability_weights(self):
        weights = np.ones(len(self.fine_grid_points))

        if len(self.vulnerable_coords) > 0:
            for i, point in enumerate(self.fine_grid_points):
                distances = cdist([point], self.vulnerable_coords, 'euclidean')[0]
                min_dist = np.min(distances)
                if min_dist <= 10:
                    weights[i] = 2.0
                elif min_dist <= 20:
                    weights[i] = 1.5

        return weights

    def get_coarse_cell_weights(self):
        coarse_weights = np.ones((self.coarse_height, self.coarse_width))
        expansion_factor = int(self.coarse_cell_size / self.fine_cell_size)

        for i in range(self.coarse_height):
            for j in range(self.coarse_width):
                start_row = i * expansion_factor
                end_row = (i + 1) * expansion_factor
                start_col = j * expansion_factor
                end_col = (j + 1) * expansion_factor

                cell_weights = []
                for fr in range(start_row, end_row):
                    for fc in range(start_col, end_col):
                        fine_idx = fr * self.n_cols_fine + fc
                        if fine_idx < len(self.vulnerability_weights):
                            cell_weights.append(self.vulnerability_weights[fine_idx])

                if cell_weights:
                    coarse_weights[i, j] = np.mean(cell_weights)

        return coarse_weights

    def convert_vulnerable_to_prohibited(self):
        self.coarse_grid[self.coarse_grid == 4] = 1

        expansion_factor = int(self.coarse_cell_size / self.fine_cell_size)
        self.fine_grid = np.zeros((self.n_rows_fine, self.n_cols_fine), dtype=int)
        for i in range(self.coarse_height):
            for j in range(self.coarse_width):
                start_row = i * expansion_factor
                end_row = (i + 1) * expansion_factor
                start_col = j * expansion_factor
                end_col = (j + 1) * expansion_factor
                self.fine_grid[start_row:end_row, start_col:end_col] = self.coarse_grid[i, j]

        self.vulnerable_coords = np.array([])
        self.vulnerability_weights = np.ones(len(self.fine_grid_points))

        print("Converted vulnerable cells to prohibited (gray)")

# =============================================================================

# TREE SPECIES CLASS

# =============================================================================

class TreeSpecies:
    """Tree species with distinct colors and provided LAI values."""

    # h0, h1, l0, l1 below are the manuscript's own Table 4 constants
    # (author-team estimates, per DBH = (h/h0)^(1/h1), LAI = l0 * DBH^l1).
    # 'LAI' is retained as the currently-adopted, hardcoded value used
    # throughout the main pipeline (Fig 7, ACO runs, WITH/WITHOUT scenarios).
    # It is NOT derived from h0/h1/l0/l1 below -- see get_computed_lai().
    SPECIES_DATA = {
        'Narra': {
            'crown_diameter_m': 23.0,
            'height_m': 30.0,
            'LAI': 6.07,
            'l0': 0.25, 'l1': 1.9, 'h0': 51.2, 'h1': 0.75,
            'color': '#E74C3C'  # Red
        },
        'Talisay': {
            'crown_diameter_m': 12.0,
            'height_m': 35.0,
            'LAI': 4.40,
            'l0': 0.20, 'l1': 1.8, 'h0': 47.2, 'h1': 0.71,
            'color': '#F39C12'  # Orange
        },
        'Banaba': {
            'crown_diameter_m': 11.0,
            'height_m': 13.5,
            'LAI': 3.87,
            'l0': 0.20, 'l1': 1.8, 'h0': 45.8, 'h1': 0.72,
            'color': '#9B59B6'  # Purple
        },
        'Kabiki': {
            'crown_diameter_m': 11.0,
            'height_m': 13.5,
            'LAI': 4.12,
            'l0': 0.22, 'l1': 1.85, 'h0': 48.5, 'h1': 0.73,
            'color': '#3498DB'  # Blue
        },
        'Duhat': {
            'crown_diameter_m': 9.5,
            'height_m': 22.0,
            'LAI': 3.52,
            'l0': 0.18, 'l1': 1.75, 'h0': 42.3, 'h1': 0.70,
            'color': '#1ABC9C'  # Teal
        },
        'Akleng-parang': {
            'crown_diameter_m': 24.0,
            'height_m': 24.0,
            'LAI': 3.15,
            'l0': 0.15, 'l1': 1.65, 'h0': 46.1, 'h1': 0.68,
            'color': '#E91E63'  # Pink/Magenta
        }
    }

    def __init__(self):
        self.species_list = list(self.SPECIES_DATA.keys())
        self.shade_weight = 0.7
        self.evap_weight = 0.3
        self._calculate_cpa_and_normalize()

    def _calculate_cpa_and_normalize(self):
        all_cpa = []
        all_lai = []

        for species in self.species_list:
            data = self.SPECIES_DATA[species]
            data['CPA'] = (np.pi / 4) * (data['crown_diameter_m'] ** 2)
            all_cpa.append(data['CPA'])
            all_lai.append(data['LAI'])

        self.max_CPA = max(all_cpa)
        self.max_LAI = max(all_lai)

        print(f"\nSpecies Biophysical Parameters (LAI PROVIDED - NO CALCULATION):")
        print("-" * 75)
        for species in self.species_list:
            data = self.SPECIES_DATA[species]
            print(f"  {species:15s}: CD={data['crown_diameter_m']:5.1f}m, "
                  f"CPA={data['CPA']:7.1f}m², LAI={data['LAI']:5.2f}")
        print(f"  Max CPA: {self.max_CPA:.1f} m², Max LAI: {self.max_LAI:.2f}")

    def get_normalized_cooling_potential(self, species_name):
        data = self.get_species_params(species_name)
        if not data:
            return 0
        cpa_norm = data['CPA'] / self.max_CPA
        lai_norm = data['LAI'] / self.max_LAI
        return self.shade_weight * cpa_norm + self.evap_weight * lai_norm

    def get_species_params(self, species_name):
        return self.SPECIES_DATA.get(species_name, {})

    def get_crown_radius(self, species_name):
        data = self.get_species_params(species_name)
        return data.get('crown_diameter_m', 0) / 2

    def get_species_color(self, species_name):
        data = self.get_species_params(species_name)
        return data.get('color', 'gray')

    def get_dbh(self, species_name, height_override=None,
                h0_override=None, h1_override=None):
        """
        Compute DBH from height via the author-derived inversion of the
        power-form allometric relationship h = h0 * DBH^h1:
            DBH = (h / h0) ** (1 / h1)
        Overrides allow OAT sensitivity perturbation of h, h0, h1 independently
        without mutating SPECIES_DATA.
        """
        data = self.get_species_params(species_name)
        if not data:
            return 0.0
        h = height_override if height_override is not None else data['height_m']
        h0 = h0_override if h0_override is not None else data['h0']
        h1 = h1_override if h1_override is not None else data['h1']
        if h <= 0 or h0 <= 0 or h1 == 0:
            return 0.0
        return (h / h0) ** (1.0 / h1)

    def get_computed_lai(self, species_name, height_override=None,
                          l0_override=None, l1_override=None,
                          h0_override=None, h1_override=None):
        """
        Compute LAI from the allometric pipeline: LAI = l0 * DBH^l1,
        with DBH derived via get_dbh(). This is the *model-consistent*
        LAI, distinct from the hardcoded SPECIES_DATA['LAI'] value that
        the main pipeline (Fig 7, ACO runs, WITH/WITHOUT scenarios)
        currently uses. See note at top of SPECIES_DATA re: this gap.
        """
        data = self.get_species_params(species_name)
        if not data:
            return 0.0
        dbh = self.get_dbh(species_name, height_override, h0_override, h1_override)
        l0 = l0_override if l0_override is not None else data['l0']
        l1 = l1_override if l1_override is not None else data['l1']
        return l0 * (dbh ** l1)

# =============================================================================

# COOLING MODEL

# =============================================================================

class CorrectedCoolingModel:
    """Cooling model with Gaussian decay."""

    def __init__(self, decay_lambda=0.1, cca_threshold=1.2,
                 competition_k=5.0, shade_weight=0.7, evap_weight=0.3):
        self.decay_lambda = decay_lambda
        self.cca_threshold = cca_threshold
        self.competition_k = competition_k
        self.shade_weight = shade_weight
        self.evap_weight = evap_weight

        self.tree_species = TreeSpecies()
        self.tree_species.shade_weight = self.shade_weight
        self.tree_species.evap_weight = self.evap_weight

        print(f"\nCooling Model: Lambda={self.decay_lambda}, "
              f"CCA_thresh={self.cca_threshold}m², "
              f"K_steepness={self.competition_k}")

    def calculate_cooling_contribution(self, tree_pos, tree_species_name,
                                       fine_grid_points, cca_values=None):
        species_params = self.tree_species.get_species_params(tree_species_name)
        if not species_params:
            return np.zeros(len(fine_grid_points))

        D_j = self.tree_species.get_normalized_cooling_potential(tree_species_name)
        distances = cdist([tree_pos], fine_grid_points, 'euclidean')[0]
        crown_diameter = species_params['crown_diameter_m']

        decay_factor = np.exp(-self.decay_lambda * (distances ** 2) /
                              (crown_diameter ** 2))

        cooling = D_j * decay_factor

        if cca_values is not None:
            competition_factor = 1 / (1 + np.exp(
                self.competition_k * (cca_values - self.cca_threshold)
            ))
            cooling *= competition_factor

        return cooling

    def calculate_cca(self, tree_placements, tree_species_list, fine_grid_points):
        cca_values = np.zeros(len(fine_grid_points))

        for pos, species in zip(tree_placements, tree_species_list):
            species_params = self.tree_species.get_species_params(species)
            if not species_params:
                continue
            crown_radius = species_params['crown_diameter_m'] / 2
            distances = cdist([pos], fine_grid_points, 'euclidean')[0]
            within_crown = distances <= crown_radius
            cpa = species_params['CPA']
            cca_values[within_crown] += cpa

        return cca_values

    def calculate_total_cooling(self, tree_placements, tree_species_list,
                                fine_grid_points, apply_competition=True):
        if apply_competition:
            cca_values = self.calculate_cca(tree_placements, tree_species_list,
                                            fine_grid_points)
        else:
            cca_values = None

        total_cooling = np.zeros(len(fine_grid_points))

        for pos, species in zip(tree_placements, tree_species_list):
            cooling = self.calculate_cooling_contribution(
                pos, species, fine_grid_points, cca_values
            )
            total_cooling += cooling

        return total_cooling, cca_values

# =============================================================================

# STANDARD ACO

# =============================================================================

class AntColonySystemACO:
    """Ant Colony System (ACS) optimizer: uses the Dorigo & Gambardella
    pseudo-random-proportional action rule (greedy exploitation with
    probability q0, roulette-wheel exploration otherwise). Renamed from
    'StandardACO' -- see audit conversation; the class name previously gave
    no indication of the specific ACO variant implemented, and did not
    match Appendix C's 'VariableRandomnessACO' either. No diversity
    enforcement mechanism is implemented."""

    def __init__(self, two_level_grid, cooling_model, n_trees=5,
                 n_ants=20, n_iterations=40, evaporation_rate=0.5,
                 alpha=1.0, beta=2.0, q0=0.7, random_seed=None,
                 species_subset=None, reference_cutoffs=None):

        if random_seed is not None:
            np.random.seed(random_seed)

        self.grid = two_level_grid
        self.cooling_model = cooling_model
        self.n_trees = min(n_trees, len(two_level_grid.plantable_coords))
        self.n_ants = n_ants
        self.n_iterations = n_iterations
        self.evaporation_rate = evaporation_rate
        self.alpha = alpha
        self.beta = beta
        self.q0 = q0

        self.plantable_coords = two_level_grid.plantable_coords
        self.n_plantable = len(self.plantable_coords)

        if self.n_plantable == 0:
            raise ValueError("No plantable cells found!")

        self.vulnerability_weights = two_level_grid.vulnerability_weights.copy()
        self.tree_species = cooling_model.tree_species

        if species_subset is not None:
            self.species_list = list(species_subset)
        else:
            self.species_list = self.tree_species.species_list

        self.n_species = len(self.species_list)

        base_pheromone = 1.0 / (self.n_plantable * self.n_species)
        self.pheromone = np.ones((self.n_plantable, self.n_species)) * base_pheromone
        self.pheromone *= np.random.uniform(0.8, 1.2, self.pheromone.shape)

        self.best_solution = None
        self.best_secpi = -np.inf
        self.best_cooling = None
        self.best_cca = None

        # Fixed reference cutoffs for classification (Q1,Q2,Q3). If None,
        # evaluate_secpi falls back to self-referential per-scenario quartiles
        # (the original, pre-audit behavior). Pass reference_cutoffs= at
        # construction (preferred, for study-wide consistency) or call
        # calibrate_reference_cutoffs() after construction -- see audit note
        # in evaluate_secpi.
        self.reference_cutoffs = reference_cutoffs

        self.heuristic_cache = self._precompute_heuristics()

        print(f"Ant Colony System (ACS): {n_ants} ants, {n_iterations} iters, "
              f"{self.n_trees} trees, {self.n_species} species")

    def _precompute_heuristics(self):
        n_cells = len(self.plantable_coords)
        n_species = len(self.species_list)
        heuristic_matrix = np.zeros((n_cells, n_species))

        half_cell = self.grid.coarse_cell_size / 2
        fine_points = self.grid.fine_grid_points

        for cell_idx in range(n_cells):
            cell_x, cell_y = self.plantable_coords[cell_idx]

            in_cell = ((fine_points[:, 0] >= cell_x - half_cell) &
                       (fine_points[:, 0] < cell_x + half_cell) &
                       (fine_points[:, 1] >= cell_y - half_cell) &
                       (fine_points[:, 1] < cell_y + half_cell))

            vuln_weight = np.mean(self.vulnerability_weights[in_cell]) if \
                np.any(in_cell) else 1.0

            for species_idx in range(n_species):
                cooling_pot = self.tree_species.get_normalized_cooling_potential(
                    self.species_list[species_idx])
                heuristic_matrix[cell_idx, species_idx] = cooling_pot * vuln_weight

        return heuristic_matrix

    def construct_solution(self):
        selected_cells = []
        selected_species = []
        available_cells = list(range(self.n_plantable))

        for tree_idx in range(self.n_trees):
            if not available_cells:
                break

            if np.random.random() < self.q0:
                best_value = -1
                best_cell_idx = None
                best_species_idx = None

                for cell_idx in available_cells:
                    for species_idx in range(self.n_species):
                        tau = self.pheromone[cell_idx, species_idx]
                        eta = self.heuristic_cache[cell_idx, species_idx]
                        value = (tau ** self.alpha) * (eta ** self.beta)
                        if value > best_value:
                            best_value = value
                            best_cell_idx = cell_idx
                            best_species_idx = species_idx

                selected_cell_idx = best_cell_idx
                selected_species_idx = best_species_idx
            else:
                probabilities = []
                choices = []

                for cell_idx in available_cells:
                    for species_idx in range(self.n_species):
                        tau = self.pheromone[cell_idx, species_idx]
                        eta = self.heuristic_cache[cell_idx, species_idx]
                        prob = (tau ** self.alpha) * (eta ** self.beta)
                        probabilities.append(prob)
                        choices.append((cell_idx, species_idx))

                probabilities = np.array(probabilities)
                if probabilities.sum() > 0:
                    probabilities /= probabilities.sum()
                else:
                    probabilities = np.ones(len(probabilities)) / len(probabilities)

                choice_idx = np.random.choice(len(choices), p=probabilities)
                selected_cell_idx, selected_species_idx = choices[choice_idx]

            selected_cells.append(selected_cell_idx)
            selected_species.append(self.species_list[selected_species_idx])
            available_cells.remove(selected_cell_idx)

        solution_coords = [self.plantable_coords[idx] for idx in selected_cells]
        return solution_coords, selected_species

    def calibrate_reference_cutoffs(self, n_samples=100, n_trees_range=(1, 6), random_seed=None):
        """
        Convenience wrapper around the module-level
        calibrate_global_reference_cutoffs(), using this instance's own
        grid/cooling_model/species_list. Pools across a mix of tree counts
        in n_trees_range by default (matching the k=1..6 sweep) rather than
        anchoring to this instance's own n_trees -- see audit conversation.
        For a multi-analysis study (sensitivity, robustness, k-sweeps, main
        run), prefer calling calibrate_global_reference_cutoffs() ONCE at
        the top level and passing the same tuple into every
        AntColonySystemACO instance instead -- see reference_cutoffs
        constructor argument.
        """
        self.reference_cutoffs = calibrate_global_reference_cutoffs(
            self.grid, self.cooling_model, self.species_list,
            n_trees_range=n_trees_range, n_samples=n_samples,
            random_seed=random_seed
        )
        return self.reference_cutoffs

    def calibrate_reference_cutoffs_theoretical_max(self, best_species=None):
        """
        ALTERNATIVE calibration scheme: derive Q1/Q2/Q3 from a single
        deterministic "theoretical maximum" scenario -- every plantable cell
        filled with the single highest-cooling-potential species (by D_j).
        This reframes SECPI's classes as "how close to the achievable
        ceiling", rather than "where a scenario falls in the general range
        of random outcomes" (the pooled-random scheme above).

        Philosophical difference from the pooled-random scheme:
        - Pooled-random: Q1-Q3 describe the *typical* range of outcomes.
          A scenario beating most random placements scores well.
        - Theoretical-max: Q1-Q3 describe fractions of the *best possible*
          outcome given grid/species constraints. A scenario is scored
          against how far it falls short of the ceiling, not against
          "typical" alternatives.
        Both are defensible; they answer different questions. Confirm which
        framing matches the manuscript's intended equity/magnitude narrative.
        """
        if best_species is None:
            d_j_scores = {sp: self.tree_species.get_normalized_cooling_potential(sp)
                          for sp in self.species_list}
            best_species = max(d_j_scores, key=d_j_scores.get)

        all_coords = self.plantable_coords
        all_species = [best_species] * len(all_coords)
        total_cooling, _ = self.cooling_model.calculate_total_cooling(
            all_coords, all_species, self.grid.fine_grid_points
        )
        q1, q2, q3 = np.percentile(total_cooling.flatten(), [25, 50, 75])
        self.reference_cutoffs = (q1, q2, q3)
        return self.reference_cutoffs

    def evaluate_secpi(self, tree_placements, tree_species_list):
        total_cooling, cca_values = self.cooling_model.calculate_total_cooling(
            tree_placements, tree_species_list, self.grid.fine_grid_points
        )

        cooling_flat = total_cooling.flatten()

        if self.reference_cutoffs is not None:
            q1, q2, q3 = self.reference_cutoffs
        else:
            # Fallback: self-referential per-scenario quartiles (original
            # behavior). WARNING -- this normalizes away magnitude
            # differences between scenarios; call calibrate_reference_cutoffs()
            # first if scenarios need to be magnitude-comparable.
            q1, q2, q3 = np.percentile(cooling_flat, [25, 50, 75])

        # Boundary convention: lower-inclusive, upper-exclusive on the top edge.
        # This resolves ties (including the fully-degenerate all-zero case,
        # e.g. a true no-tree baseline) to Class 1 (worst), consistent with
        # the baseline_proportions=[1,0,0,0] assumption below. The previous
        # convention (< for classes 1-3, >= for class 4) instead pushed all
        # tied/degenerate cells into Class 4 (best) -- the opposite of the
        # intended semantics. See audit note.
        cooling_class = np.zeros_like(cooling_flat, dtype=int)
        cooling_class[cooling_flat <= q1] = 1
        cooling_class[(cooling_flat > q1) & (cooling_flat <= q2)] = 2
        cooling_class[(cooling_flat > q2) & (cooling_flat <= q3)] = 3
        cooling_class[cooling_flat > q3] = 4

        total_cells = len(cooling_class)
        area_proportions = np.zeros(4)
        for k in range(4):
            area_proportions[k] = np.sum(cooling_class == (k + 1)) / total_cells

        class_weights = np.array([1, 2, 3, 4])
        baseline_proportions = np.array([1.0, 0.0, 0.0, 0.0])

        mean_vuln_weights = np.zeros(4)
        for k in range(4):
            class_mask = (cooling_class == (k + 1))
            if np.any(class_mask):
                mean_vuln_weights[k] = np.mean(self.vulnerability_weights[class_mask])
            else:
                mean_vuln_weights[k] = 1.0

        secpi = np.sum(
            (area_proportions - baseline_proportions) * class_weights * mean_vuln_weights
        )

        return secpi, total_cooling, cca_values, area_proportions

    # Closed-form theoretical bounds of the raw SECPI formula:
    #     SECPI = sum_k (A_k - baseline_k) * W_k * We_k
    # with baseline=[1,0,0,0], W_k=[1,2,3,4], We_k in [0.5,2.0] (or the
    # fallback We_k=1.0 when class k is empty, A_k=0).
    #
    # Because the objective is linear in A (over the 4-simplex, A_k>=0,
    # sum A_k=1) for any fixed We, and linear in each We (box-constrained,
    # [0.5,2.0]) for any fixed A, the global extrema of this bilinear
    # objective occur at a vertex of the simplex combined with boundary
    # values of We -- a standard result for objectives linear in each of
    # two jointly-optimized variables over a polytope x box. Exhaustive
    # enumeration of all 4 simplex vertices x the 4 boundary (We_1, We_k)
    # combinations (16 cases total; see audit conversation) gives:
    #
    #     SECPI_max = 7.5   at A_4=1 (all cells Class 4), We_1=0.5, We_4=2.0
    #     SECPI_min = -1.0  at A_2=1 (all cells Class 2), We_1=2.0, We_2=0.5
    #
    # (Vertex A_1=1, i.e. the true no-intervention baseline, always yields
    # exactly 0 regardless of We, since A=baseline there.) These bounds
    # safely contain the actual empty-class-fallback behavior implemented
    # above (numerically verified: masked-fallback achievable range is
    # inside [-1.0, 7.5], with the minimum essentially tight).
    SECPI_THEORETICAL_MIN = -1.0
    SECPI_THEORETICAL_MAX = 7.5

    @staticmethod
    def normalize_secpi(raw_secpi):
        """
        Maps raw SECPI onto a mathematically-bounded [0,5] scale via linear
        min-max normalization against the derived theoretical extrema:

            SECPI_norm = 5 * (SECPI_raw - SECPI_min) / (SECPI_max - SECPI_min)
                       = 5 * (SECPI_raw + 1.0) / 8.5

        This is a strictly increasing affine transform of SECPI_raw, so it
        does NOT change which configuration is optimal -- ACO continues to
        search/select on SECPI_raw (via evaluate_secpi above); this method
        is for REPORTING/interpretation only (converting a result to the
        manuscript's stated 0-5 scale with a mathematically derived, rather
        than empirical, justification for that range).

        AUDIT NOTE FOR MANUSCRIPT: this normalization does NOT preserve
        "no-intervention baseline maps to 0" -- SECPI_raw=0 (the baseline
        case) maps to SECPI_norm = 5*(0+1)/8.5 = 0.588, not 0, because the
        global theoretical minimum (-1.0) is below the baseline value (0),
        not equal to it. A normalization scheme that keeps 0 anchored at
        the baseline is possible but is a DIFFERENT, non-min-max scheme
        (e.g. clipping negative raw values to a displayed floor of 0) and
        was not what was requested -- confirm this tradeoff is acceptable
        before this appears in the manuscript.
        """
        return 5.0 * (raw_secpi - AntColonySystemACO.SECPI_THEORETICAL_MIN) / (
            AntColonySystemACO.SECPI_THEORETICAL_MAX - AntColonySystemACO.SECPI_THEORETICAL_MIN
        )

    def update_pheromones(self, solutions, secpi_scores):
        self.pheromone *= (1 - self.evaporation_rate)

        best_idx = np.argmax(secpi_scores)
        best_secpi_iter = secpi_scores[best_idx]

        for solution_idx, (tree_coords, tree_species) in enumerate(solutions):
            secpi_score = secpi_scores[solution_idx]
            if best_secpi_iter > 0:
                quality = secpi_score / best_secpi_iter
            else:
                quality = 0.1

            for coord, species_name in zip(tree_coords, tree_species):
                cell_idx = np.where(
                    (self.plantable_coords == coord).all(axis=1))[0][0]
                species_idx = self.species_list.index(species_name)
                self.pheromone[cell_idx, species_idx] += quality

    def run(self, verbose=True):
        history_best = []
        history_avg = []

        if verbose:
            print("\nStarting Standard ACO optimization...")

        iterator = tqdm(range(self.n_iterations), desc="ACO Progress",
                       disable=not verbose)

        for iteration in iterator:
            solutions_iter = []
            secpi_scores_iter = []

            for ant in range(self.n_ants):
                tree_coords, tree_species = self.construct_solution()
                secpi, cooling, cca, area_props = self.evaluate_secpi(
                    tree_coords, tree_species)

                solutions_iter.append((tree_coords, tree_species))
                secpi_scores_iter.append(secpi)

                if secpi > self.best_secpi:
                    self.best_secpi = secpi
                    self.best_solution = (tree_coords, tree_species)
                    self.best_cooling = cooling
                    self.best_cca = cca

            self.update_pheromones(solutions_iter, secpi_scores_iter)

            history_best.append(np.max(secpi_scores_iter))
            history_avg.append(np.mean(secpi_scores_iter))

            if verbose and (iteration % 10 == 0 or iteration == self.n_iterations - 1):
                best_sol = solutions_iter[np.argmax(secpi_scores_iter)]
                n_unique = len(set(best_sol[1]))
                print(f"Iter {iteration:3d}: "
                      f"Best={np.max(secpi_scores_iter):.4f}, "
                      f"Avg={np.mean(secpi_scores_iter):.4f}, "
                      f"Species={n_unique}")

        if verbose:
            if self.best_solution:
                n_unique = len(set(self.best_solution[1]))
                print(f"\nOptimization complete! Best SECPI: {self.best_secpi:.4f}")
                print(f"Species used: {set(self.best_solution[1])} ({n_unique} unique)")

        return history_best, history_avg

# =============================================================================

# ENHANCED VISUALIZER

# =============================================================================

class EnhancedVisualizer:
    """Visualization with legends below heatmaps."""

    def __init__(self, output_dir=None):
        if output_dir is None:
            base_dir = os.path.join(os.path.expanduser('~'), 'Downloads', 'SECPI')
            os.makedirs(base_dir, exist_ok=True)
            output_dir = base_dir
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.run_dir = os.path.join(output_dir, f"run_{self.timestamp}")
        os.makedirs(self.run_dir, exist_ok=True)
        print(f"Output directory: {self.run_dir}")

    def plot_coarse_grid_only(self, grid, title, filename):
        fig, ax = plt.subplots(figsize=(10, 10))

        for i in range(grid.coarse_height):
            for j in range(grid.coarse_width):
                x = j * grid.coarse_cell_size
                y = i * grid.coarse_cell_size
                land_use = grid.coarse_grid[i, j]

                color_map = {0: 'white', 1: 'gray', 3: 'lightgreen', 4: 'salmon'}
                facecolor = color_map.get(land_use, 'white')

                rect = Rectangle((x, y), grid.coarse_cell_size,
                                 grid.coarse_cell_size,
                                 facecolor=facecolor, edgecolor='black',
                                 linewidth=1, alpha=0.8)
                ax.add_patch(rect)

                cx = x + grid.coarse_cell_size / 2
                cy = y + grid.coarse_cell_size / 2
                ax.text(cx, cy, f'({j},{i})', ha='center', va='center',
                       fontsize=6, color='black', alpha=0.5)

        ax.set_xlim(0, grid.fine_width)
        ax.set_ylim(0, grid.fine_height)
        ax.set_aspect('equal')
        ax.set_xlabel('X (m)', fontsize=11)
        ax.set_ylabel('Y (m)', fontsize=11)
        ax.set_title(title, fontsize=14, fontweight='bold')

        legend_patches = [
            Patch(facecolor='gray', edgecolor='black', label='Prohibited (Building)'),
            Patch(facecolor='lightgreen', edgecolor='black', label='Available (Plantable)'),
            Patch(facecolor='salmon', edgecolor='black', label='Vulnerable Zone')
        ]
        ax.legend(handles=legend_patches, loc='upper right', fontsize=9)

        plt.tight_layout()
        filepath = os.path.join(self.run_dir, filename)
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"Saved: {filepath}")
        return filepath

    def plot_grid_with_equity_weights(self, grid, title, filename):
        fig, ax = plt.subplots(figsize=(12, 10))

        coarse_weights = grid.get_coarse_cell_weights()
        weight_cmap = plt.cm.RdYlGn_r

        for i in range(grid.coarse_height):
            for j in range(grid.coarse_width):
                x = j * grid.coarse_cell_size
                y = i * grid.coarse_cell_size
                land_use = grid.coarse_grid[i, j]
                weight = coarse_weights[i, j]

                if land_use == 1:
                    facecolor = 'gray'
                    weight_display = '-'
                else:
                    norm_weight = (weight - 1.0) / 1.0
                    norm_weight = np.clip(norm_weight, 0, 1)
                    facecolor = weight_cmap(norm_weight)
                    weight_display = f'{weight:.1f}'

                rect = Rectangle((x, y), grid.coarse_cell_size,
                                 grid.coarse_cell_size,
                                 facecolor=facecolor, edgecolor='black',
                                 linewidth=1.5, alpha=0.85)
                ax.add_patch(rect)

                cx = x + grid.coarse_cell_size / 2
                cy = y + grid.coarse_cell_size / 2
                text_color = 'white' if land_use != 1 and weight > 1.5 else 'black'
                ax.text(cx, cy, weight_display, ha='center', va='center',
                       fontsize=9, fontweight='bold', color=text_color)

        ax.set_xlim(0, grid.fine_width)
        ax.set_ylim(0, grid.fine_height)
        ax.set_aspect('equal')
        ax.set_xlabel('X (m)', fontsize=11)
        ax.set_ylabel('Y (m)', fontsize=11)
        ax.set_title(title, fontsize=14, fontweight='bold')

        sm = plt.cm.ScalarMappable(cmap=weight_cmap, norm=plt.Normalize(1.0, 2.0))
        sm.set_array([])
        cbar = plt.colorbar(sm, ax=ax, shrink=0.8, pad=0.02)
        cbar.set_label('Equity Weight', fontsize=11)

        legend_patches = [
            Patch(facecolor='gray', edgecolor='black', label='Prohibited (w=-)'),
            Patch(facecolor=weight_cmap(0.0), edgecolor='black', label='Low Vuln (w=1.0)'),
            Patch(facecolor=weight_cmap(0.5), edgecolor='black', label='Med Vuln (w=1.5)'),
            Patch(facecolor=weight_cmap(1.0), edgecolor='black', label='High Vuln (w=2.0)')
        ]
        ax.legend(handles=legend_patches, loc='upper left', fontsize=9)

        plt.tight_layout()
        filepath = os.path.join(self.run_dir, filename)
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"Saved: {filepath}")
        return filepath

    def plot_all_species_decay_curves(self, cooling_model, grid, filename):
        fig, axes = plt.subplots(2, 3, figsize=(18, 12))
        axes = axes.flatten()

        tree_species = cooling_model.tree_species
        max_dist = 50
        distances = np.linspace(0, max_dist, 500)

        for idx, species_name in enumerate(tree_species.species_list):
            ax = axes[idx]

            species_params = tree_species.get_species_params(species_name)
            D_j = tree_species.get_normalized_cooling_potential(species_name)
            crown_diameter = species_params['crown_diameter_m']
            crown_radius = crown_diameter / 2

            decay = D_j * np.exp(-cooling_model.decay_lambda *
                                (distances ** 2) / (crown_diameter ** 2))

            color = tree_species.get_species_color(species_name)
            ax.plot(distances, decay, color=color, linewidth=2.5, label='Cooling Intensity')
            ax.fill_between(distances, 0, decay, color=color, alpha=0.3)
            ax.axvline(crown_radius, color='black', linestyle='--', linewidth=1.5,
                      label=f'Crown Radius ({crown_radius:.1f}m)')

            ax.set_xlabel('Distance from Tree Center (m)', fontsize=10)
            ax.set_ylabel('Cooling Intensity', fontsize=10)
            ax.set_title(f'{species_name}\n(CD={crown_diameter:.1f}m, '
                        f'CPA={species_params["CPA"]:.1f}m², '
                        f'LAI={species_params["LAI"]:.2f})',
                        fontsize=11, fontweight='bold', color=color)
            ax.legend(fontsize=8)
            ax.grid(True, alpha=0.3)
            ax.set_xlim(0, max_dist)
            ax.set_ylim(0, D_j * 1.1)
            ax.annotate(f'D_j = {D_j:.3f}', xy=(0.05, 0.95), xycoords='axes fraction',
                       fontsize=9, fontweight='bold', va='top')

        plt.suptitle('Cooling Decay Curves for All Philippine TFTs\n'
                    f'(λ = {cooling_model.decay_lambda}, LAI values provided)',
                    fontsize=14, fontweight='bold')
        plt.tight_layout()

        filepath = os.path.join(self.run_dir, filename)
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"Saved: {filepath}")
        return filepath

    def plot_optimized_solution_fixed(self, grid, tree_placements,
                                      tree_species_list, cooling_values,
                                      title, filename, output_subdir=None):
        """Visualization with legends BELOW the heatmap."""
        fig = plt.figure(figsize=(18, 11))

        gs = fig.add_gridspec(2, 2, height_ratios=[5, 1.2], width_ratios=[1, 1.1],
                             hspace=0.25, wspace=0.15)

        ax_left = fig.add_subplot(gs[0, 0])
        ax_right = fig.add_subplot(gs[0, 1])
        ax_legend_left = fig.add_subplot(gs[1, 0])
        ax_legend_right = fig.add_subplot(gs[1, 1])

        ax_legend_left.axis('off')
        ax_legend_right.axis('off')

        # LEFT: Coarse grid
        for i in range(grid.coarse_height):
            for j in range(grid.coarse_width):
                x = j * grid.coarse_cell_size
                y = i * grid.coarse_cell_size
                land_use = grid.coarse_grid[i, j]
                color_map = {0: 'white', 1: 'gray', 3: 'lightgreen', 4: 'salmon'}
                facecolor = color_map.get(land_use, 'white')
                rect = Rectangle((x, y), grid.coarse_cell_size,
                                 grid.coarse_cell_size,
                                 facecolor=facecolor, edgecolor='black',
                                 linewidth=1, alpha=0.7)
                ax_left.add_patch(rect)

        tree_species_obj = TreeSpecies()
        species_handles = {}

        for (tx, ty), species_name in zip(tree_placements, tree_species_list):
            color = tree_species_obj.get_species_color(species_name)
            handle = ax_left.scatter(tx, ty, color=color, s=250,
                                    edgecolors='black', linewidth=2,
                                    zorder=5, marker='o')
            if species_name not in species_handles:
                species_handles[species_name] = handle

            crown_radius = tree_species_obj.get_crown_radius(species_name)
            circle = Circle((tx, ty), crown_radius, facecolor=color,
                           edgecolor=color, alpha=0.25, linewidth=2)
            ax_left.add_patch(circle)

        ax_left.set_xlim(0, grid.fine_width)
        ax_left.set_ylim(0, grid.fine_height)
        ax_left.set_aspect('equal')
        ax_left.set_title('Tree Placements (CA Coarse Grid)', fontsize=14, fontweight='bold')
        ax_left.set_xlabel('X (m)', fontsize=12)
        ax_left.set_ylabel('Y (m)', fontsize=12)

        # LEFT LEGEND
        land_legend = [
            Patch(facecolor='gray', edgecolor='black', label='Prohibited'),
            Patch(facecolor='lightgreen', edgecolor='black', label='Available'),
            Patch(facecolor='salmon', edgecolor='black', label='Vulnerable')
        ]
        ax_legend_left.legend(handles=land_legend, loc='center',
                             ncol=3, fontsize=13, frameon=True,
                             fancybox=True, shadow=True,
                             title='Land Use Types', title_fontsize=14)

        # RIGHT: Cooling heatmap with blue canopy
        cooling_grid = cooling_values.reshape(grid.n_rows_fine, grid.n_cols_fine)
        vmin = 0
        vmax = np.percentile(cooling_values, 99)

        im2 = ax_right.imshow(cooling_grid.T,
                             extent=[0, grid.fine_width, 0, grid.fine_height],
                             origin='lower', cmap='coolwarm_r',
                             aspect='auto', vmin=vmin, vmax=vmax,
                             interpolation='bilinear')

        for (x, y), species in zip(tree_placements, tree_species_list):
            crown_radius = tree_species_obj.get_crown_radius(species)
            canopy_circle = Circle((x, y), crown_radius,
                                   facecolor='royalblue', edgecolor='darkblue',
                                   linewidth=2, alpha=0.35)
            ax_right.add_patch(canopy_circle)

            color = tree_species_obj.get_species_color(species)
            ax_right.scatter(x, y, color=color, s=120, edgecolors='white',
                           linewidth=2, zorder=10, marker='o')

        ax_right.set_xlim(0, grid.fine_width)
        ax_right.set_ylim(0, grid.fine_height)
        ax_right.set_title('Cooling Distribution (Blue = Canopy)', fontsize=14, fontweight='bold')
        ax_right.set_xlabel('X (m)', fontsize=12)
        ax_right.set_ylabel('Y (m)', fontsize=12)

        cbar = plt.colorbar(im2, ax=ax_right, shrink=0.8, pad=0.02)
        cbar.set_label('Cooling Intensity', fontsize=12)

        # RIGHT LEGEND
        species_legend = [
            Patch(facecolor='royalblue', edgecolor='darkblue', alpha=0.5,
                  label='Canopy Coverage')
        ]
        for species, handle in species_handles.items():
            color = tree_species_obj.get_species_color(species)
            crown_r = tree_species_obj.get_crown_radius(species)
            species_legend.append(
                plt.Line2D([0], [0], marker='o', color='w',
                          markerfacecolor=color, markeredgecolor='black',
                          markersize=14,
                          label=f'{species} (r={crown_r:.1f}m)')
            )

        ax_legend_right.legend(handles=species_legend, loc='center',
                              ncol=min(len(species_legend), 4), fontsize=12,
                              frameon=True, fancybox=True, shadow=True,
                              title='Species & Canopy', title_fontsize=13)

        plt.suptitle(title, fontsize=16, fontweight='bold', y=0.98)

        if output_subdir:
            save_dir = os.path.join(self.run_dir, output_subdir)
            os.makedirs(save_dir, exist_ok=True)
            filepath = os.path.join(save_dir, filename)
        else:
            filepath = os.path.join(self.run_dir, filename)

        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"Saved: {filepath}")
        return filepath

    def plot_zonal_cooling_efficiency(self, grid, cooling_values,
                                      vulnerability_weights, title, filename):
        """Zonal cooling efficiency bar graph."""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

        zone_cooling = {'Low Priority (w=1.0)': [],
                       'Medium Priority (w=1.5)': [],
                       'High Priority (w=2.0)': []}

        for i, weight in enumerate(vulnerability_weights):
            if weight >= 2.0:
                zone_cooling['High Priority (w=2.0)'].append(cooling_values[i])
            elif weight >= 1.5:
                zone_cooling['Medium Priority (w=1.5)'].append(cooling_values[i])
            else:
                zone_cooling['Low Priority (w=1.0)'].append(cooling_values[i])

        zone_names = list(zone_cooling.keys())
        mean_cooling = [np.mean(zone_cooling[z]) if zone_cooling[z] else 0 for z in zone_names]
        std_cooling = [np.std(zone_cooling[z]) if zone_cooling[z] else 0 for z in zone_names]
        cell_counts = [len(zone_cooling[z]) for z in zone_names]

        colors = ['#2ECC71', '#F39C12', '#E74C3C']
        bars = ax1.bar(zone_names, mean_cooling, yerr=std_cooling,
                      color=colors, edgecolor='black', linewidth=2,
                      capsize=8, alpha=0.8)

        for bar, mean_val, count in zip(bars, mean_cooling, cell_counts):
            height = bar.get_height()
            ax1.annotate(f'{mean_val:.4f}\n(n={count})',
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 5), textcoords='offset points',
                        ha='center', va='bottom', fontsize=11, fontweight='bold')

        ax1.set_xlabel('Zone Priority Level', fontsize=13)
        ax1.set_ylabel('Mean Cooling Intensity', fontsize=13)
        ax1.set_title('Mean Cooling by Vulnerability Zone', fontsize=14, fontweight='bold')
        ax1.tick_params(axis='x', labelsize=11)
        ax1.grid(True, alpha=0.3, axis='y')

        efficiency = []
        eff_labels = []
        for z, vals in zone_cooling.items():
            if vals:
                weight = 2.0 if 'High' in z else (1.5 if 'Medium' in z else 1.0)
                eff = np.mean(vals) * weight
                efficiency.append(eff)
                eff_labels.append(z)

        bars2 = ax2.bar(eff_labels, efficiency, color=colors[:len(efficiency)],
                       edgecolor='black', linewidth=2, alpha=0.8)

        for bar, eff_val in zip(bars2, efficiency):
            height = bar.get_height()
            ax2.annotate(f'{eff_val:.4f}',
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 5), textcoords='offset points',
                        ha='center', va='bottom', fontsize=11, fontweight='bold')

        ax2.set_xlabel('Zone Priority Level', fontsize=13)
        ax2.set_ylabel('Weighted Cooling Contribution', fontsize=13)
        ax2.set_title('Equity-Weighted Cooling Contribution', fontsize=14, fontweight='bold')
        ax2.tick_params(axis='x', labelsize=11)
        ax2.grid(True, alpha=0.3, axis='y')

        plt.suptitle(title, fontsize=16, fontweight='bold')
        plt.tight_layout()

        filepath = os.path.join(self.run_dir, filename)
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"Saved: {filepath}")
        return filepath

    def plot_morphological_robustness(self, robustness_results, filename):
        fig, axes = plt.subplots(2, 3, figsize=(18, 12))
        axes = axes.flatten()

        morphologies = list(robustness_results.keys())

        for idx, morph_name in enumerate(morphologies[:6]):
            ax = axes[idx]
            data = robustness_results[morph_name]

            secpi_values = data['secpi_values']
            if not secpi_values:
                ax.text(0.5, 0.5, 'No data', ha='center', va='center')
                continue

            ax.hist(secpi_values, bins=15, color='steelblue',
                   edgecolor='black', alpha=0.7)
            ax.axvline(np.mean(secpi_values), color='red', linestyle='--',
                      linewidth=2, label=f'Mean: {np.mean(secpi_values):.3f}')
            ax.axvline(np.median(secpi_values), color='orange', linestyle='-.',
                      linewidth=2, label=f'Median: {np.median(secpi_values):.3f}')

            ax.set_xlabel('SECPI Score', fontsize=10)
            ax.set_ylabel('Frequency', fontsize=10)
            ax.set_title(f'{morph_name}\n(n={len(secpi_values)} runs)',
                        fontsize=11, fontweight='bold')
            ax.legend(fontsize=8)
            ax.grid(True, alpha=0.3)

        plt.suptitle('Morphological Robustness Validation', fontsize=14, fontweight='bold')
        plt.tight_layout()

        filepath = os.path.join(self.run_dir, filename)
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"Saved: {filepath}")
        return filepath

# =============================================================================

# MORPHOLOGICAL ROBUSTNESS VALIDATOR

# =============================================================================

class MorphologicalRobustnessValidator:

    def __init__(self, base_config, n_runs_per_morphology=10, reference_cutoffs=None):
        self.base_config = base_config
        self.n_runs = n_runs_per_morphology
        self.results = {}
        # Fixed, study-wide cutoffs -- see calibrate_global_reference_cutoffs().
        # IMPORTANT: a new grid is generated per morphology per run in
        # run_validation() below, so these cutoffs are necessarily calibrated
        # from a DIFFERENT reference grid than any individual morphology run
        # uses. This is intentional for cross-morphology comparability (so
        # "morphology A scores higher than B" isn't confounded by each also
        # having its own shifted reference frame) -- but confirm this matches
        # the intended study design before treating cross-morphology
        # comparisons as final. See audit conversation.
        self.reference_cutoffs = reference_cutoffs

        # Translated from the old additive-heuristic (alpha/beta) parameterization
        # to the new Almeida-style (gamma/p0) parameterization -- see audit
        # conversation. Relative ordering preserved (Dense/High > baseline > Sparse/Low)
        # for both initial transition-probability baseline (p0) and growth-rate
        # calibration (gamma).
        #
        # RESOLVED (per audit conversation): each preset now also carries its
        # own p_target_range / v_target_range, so presets differ in FINAL
        # land-use composition, not just growth path/clustering shape:
        #   - Dense_* presets target a higher built-up (P) share than the
        #     study baseline (55-65%); Sparse_* target lower.
        #   - High/Low_Vulnerability hold P at the study baseline range but
        #     shift the Vulnerable (V) share up/down instead.
        # v_target_range is left at the study default (5-10%) for Dense/Sparse
        # presets, and p_target_range is left at the study default (55-65%)
        # for the Vulnerability presets, so only one axis varies per preset
        # pair -- confirm these specific target bands match intended study
        # design before treating results as final (values chosen to bracket
        # the baseline symmetrically; not independently literature-sourced).
        self.morphology_params = {
            'Dense_Organic': {'p_init': 0.25, 'gamma': 4.5, 'p0': 0.6,
                             'theta': 3, 'morphology': 'organic',
                             'p_target_range': (0.65, 0.75), 'v_target_range': (0.05, 0.10)},
            'Sparse_Organic': {'p_init': 0.10, 'gamma': 3.0, 'p0': 0.35,
                              'theta': 2, 'morphology': 'organic',
                              'p_target_range': (0.40, 0.50), 'v_target_range': (0.05, 0.10)},
            'Dense_Linear': {'p_init': 0.25, 'gamma': 4.5, 'p0': 0.6,
                            'theta': 3, 'morphology': 'linear',
                            'p_target_range': (0.65, 0.75), 'v_target_range': (0.05, 0.10)},
            'Sparse_Linear': {'p_init': 0.10, 'gamma': 3.0, 'p0': 0.35,
                             'theta': 2, 'morphology': 'linear',
                             'p_target_range': (0.40, 0.50), 'v_target_range': (0.05, 0.10)},
            'High_Vulnerability': {'p_init': 0.30, 'gamma': 5.0, 'p0': 0.65,
                                  'theta': 4, 'morphology': 'organic',
                                  'p_target_range': (0.55, 0.65), 'v_target_range': (0.15, 0.20)},
            'Low_Vulnerability': {'p_init': 0.08, 'gamma': 2.5, 'p0': 0.3,
                                 'theta': 2, 'morphology': 'organic',
                                 'p_target_range': (0.55, 0.65), 'v_target_range': (0.02, 0.04)}
        }

    def run_validation(self, output_dir):
        print("\n" + "=" * 80)
        print("MORPHOLOGICAL ROBUSTNESS VALIDATION")
        print("=" * 80)

        for morph_name, ca_params in self.morphology_params.items():
            print(f"\n[{morph_name}] Running {self.n_runs} optimization runs...")

            secpi_values = []
            cooling_stats = []

            for run_idx in tqdm(range(self.n_runs), desc=f"  {morph_name}"):
                try:
                    grid = TwoLevelUrbanGrid(
                        coarse_width=self.base_config['coarse_grid']['width'],
                        coarse_height=self.base_config['coarse_grid']['height'],
                        coarse_cell_size=self.base_config['coarse_grid']['cell_size'],
                        fine_cell_size=self.base_config['fine_grid']['cell_size']
                    )
                    grid.generate_ca_archetype(
                        params=ca_params,
                        morphology=ca_params['morphology'],
                        p_target_range=ca_params.get('p_target_range', (0.55, 0.65)),
                        v_target_range=ca_params.get('v_target_range', (0.05, 0.10))
                    )

                    if len(grid.plantable_coords) == 0:
                        continue

                    cp = self.base_config['cooling_params']
                    cooling_model = CorrectedCoolingModel(
                        decay_lambda=cp['decay_lambda'],
                        cca_threshold=cp['cca_threshold'],
                        competition_k=cp['competition_k']
                    )

                    aco_cfg = self.base_config['aco_params']
                    aco = AntColonySystemACO(
                        grid, cooling_model,
                        n_trees=aco_cfg['n_trees'],
                        n_ants=aco_cfg['n_ants'],
                        n_iterations=aco_cfg['n_iterations'],
                        evaporation_rate=aco_cfg['evaporation_rate'],
                        alpha=aco_cfg['alpha'],
                        beta=aco_cfg['beta'],
                        q0=aco_cfg['q0'],
                        reference_cutoffs=self.reference_cutoffs
                    )
                    aco.run(verbose=False)

                    if aco.best_cooling is not None:
                        secpi_values.append(aco.best_secpi)
                        cooling_stats.append({
                            'mean': float(np.mean(aco.best_cooling)),
                            'max': float(np.max(aco.best_cooling)),
                            'std': float(np.std(aco.best_cooling))
                        })

                except Exception as e:
                    continue

            self.results[morph_name] = {
                'secpi_values': secpi_values,
                'cooling_stats': cooling_stats,
                'mean_secpi': np.mean(secpi_values) if secpi_values else 0,
                'std_secpi': np.std(secpi_values) if secpi_values else 0,
                'n_successful': len(secpi_values)
            }

            if secpi_values:
                print(f"  Mean SECPI: {self.results[morph_name]['mean_secpi']:.4f} "
                      f"± {self.results[morph_name]['std_secpi']:.4f}")

        return self.results

    def generate_report(self, output_dir):
        report = {
            'validation_type': 'Morphological Robustness',
            'n_runs_per_morphology': self.n_runs,
            'morphologies': {}
        }

        for morph_name, data in self.results.items():
            report['morphologies'][morph_name] = {
                'mean_secpi': data['mean_secpi'],
                'std_secpi': data['std_secpi'],
                'n_successful_runs': data['n_successful'],
                'cv': data['std_secpi'] / data['mean_secpi'] if data['mean_secpi'] > 0 else 0
            }

        all_means = [d['mean_secpi'] for d in self.results.values() if d['mean_secpi'] > 0]
        report['overall'] = {
            'mean_across_morphologies': np.mean(all_means) if all_means else 0,
            'std_across_morphologies': np.std(all_means) if all_means else 0,
            'robustness_assessment': 'ROBUST' if len(all_means) > 0 and np.std(all_means) < 0.5 * np.mean(all_means) else 'VARIABLE'
        }

        filepath = os.path.join(output_dir, 'morphological_robustness_report.json')
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2)
        print(f"Saved: {filepath}")

        return report

# =============================================================================

# SCENARIO GENERATOR (WITH k=1 TO 6 SOLUTIONS)

# =============================================================================

class SuboptimalScenariosGenerator:
    """
    Generates optimal solutions for k=1 to k=6 trees for both
    WITH and WITHOUT vulnerable cell scenarios.
    """

    def __init__(self, base_grid, cooling_model, aco_config, visualizer,
                 reference_cutoffs=None):
        self.base_grid = base_grid
        self.cooling_model = cooling_model
        self.aco_config = aco_config
        self.visualizer = visualizer
        # Fixed, study-wide cutoffs -- see calibrate_global_reference_cutoffs().
        # Held constant across k=1..5 so a genuine "more trees improves
        # SECPI" signal isn't confounded by the reference frame itself
        # shifting between k values.
        self.reference_cutoffs = reference_cutoffs

        self.results_with_vuln = {}
        self.results_without_vuln = {}
        self.k_values = [1, 2, 3, 4, 5]

    def run_optimization_for_k(self, grid, k, n_runs=5, verbose=False):
        """Run optimization for a specific number of trees k."""
        best_aco = None
        best_secpi = -np.inf
        all_secpi = []

        for run in range(n_runs):
            try:
                aco = AntColonySystemACO(
                    grid, self.cooling_model,
                    n_trees=k,
                    n_ants=self.aco_config['n_ants'],
                    n_iterations=self.aco_config['n_iterations'],
                    evaporation_rate=self.aco_config['evaporation_rate'],
                    alpha=self.aco_config['alpha'],
                    beta=self.aco_config['beta'],
                    q0=self.aco_config['q0'],
                    reference_cutoffs=self.reference_cutoffs
                )
                aco.run(verbose=False)

                if aco.best_solution:
                    all_secpi.append(aco.best_secpi)
                    if aco.best_secpi > best_secpi:
                        best_secpi = aco.best_secpi
                        best_aco = aco
            except Exception as e:
                if verbose:
                    print(f"  Run {run+1} failed: {e}")
                continue

        return best_aco, best_secpi, all_secpi

    def run_all_scenarios(self):
        """Run WITH and WITHOUT vulnerable scenarios for k=1 to 6."""

        # =====================================================================
        # WITH VULNERABLE CELLS
        # =====================================================================
        print("\n" + "=" * 80)
        print("SCENARIOS: WITH VULNERABLE CELLS (k=1 to 6)")
        print("=" * 80)

        with_vuln_dir = os.path.join(self.visualizer.run_dir, 'WITH_VULNERABLE')
        os.makedirs(with_vuln_dir, exist_ok=True)

        self.results_with_vuln = {'scenario': 'WITH_VULNERABLE', 'k_results': {}}

        for k in self.k_values:
            print(f"\n[WITH VULN] Optimizing for k={k} trees...")

            best_aco, best_secpi, all_secpi = self.run_optimization_for_k(
                self.base_grid, k, n_runs=5
            )

            if best_aco and best_aco.best_solution:
                tree_coords, tree_species = best_aco.best_solution
                cooling, cca = self.cooling_model.calculate_total_cooling(
                    tree_coords, tree_species, self.base_grid.fine_grid_points,
                    apply_competition=True
                )

                # Store results
                self.results_with_vuln['k_results'][k] = {
                    'n_trees': len(tree_coords),
                    'best_secpi': float(best_secpi),
                    'all_secpi': [float(s) for s in all_secpi],
                    'mean_secpi': float(np.mean(all_secpi)) if all_secpi else 0,
                    'std_secpi': float(np.std(all_secpi)) if len(all_secpi) > 1 else 0,
                    'tree_placements': [(float(x), float(y)) for x, y in tree_coords],
                    'tree_species': list(tree_species),
                    'unique_species': list(set(tree_species)),
                    'n_unique_species': len(set(tree_species)),
                    'cooling_stats': {
                        'mean': float(np.mean(cooling)),
                        'max': float(np.max(cooling)),
                        'std': float(np.std(cooling)),
                        'coverage': float(np.sum(cooling > 0.01) / len(cooling) * 100)
                    }
                }

                # Visualize each k solution
                self.visualizer.plot_optimized_solution_fixed(
                    self.base_grid, tree_coords, tree_species, cooling,
                    f'WITH VULNERABLE: k={k} Trees\nSECPI: {best_secpi:.4f}',
                    f'solution_with_vuln_k{k}.png',
                    output_subdir='WITH_VULNERABLE'
                )

                print(f"  Best SECPI: {best_secpi:.4f}, Species: {set(tree_species)}")
            else:
                self.results_with_vuln['k_results'][k] = {
                    'n_trees': 0,
                    'best_secpi': 0,
                    'error': 'No valid solution found'
                }
                print(f"  No valid solution found for k={k}")

        # Save WITH VULNERABLE results
        json_path = os.path.join(with_vuln_dir, 'results_with_vuln_all_k.json')
        with open(json_path, 'w') as f:
            json.dump(self.results_with_vuln, f, indent=2)
        print(f"\nSaved: {json_path}")

        # =====================================================================
        # WITHOUT VULNERABLE CELLS
        # =====================================================================
        print("\n" + "=" * 80)
        print("SCENARIOS: WITHOUT VULNERABLE CELLS (k=1 to 6)")
        print("=" * 80)

        without_vuln_dir = os.path.join(self.visualizer.run_dir, 'WITHOUT_VULNERABLE')
        os.makedirs(without_vuln_dir, exist_ok=True)

        # Create grid without vulnerable cells
        grid_no_vuln = TwoLevelUrbanGrid(
            coarse_width=self.base_grid.coarse_width,
            coarse_height=self.base_grid.coarse_height,
            coarse_cell_size=self.base_grid.coarse_cell_size,
            fine_cell_size=self.base_grid.fine_cell_size
        )
        grid_no_vuln.coarse_grid = self.base_grid.coarse_grid.copy()
        grid_no_vuln.fine_grid = self.base_grid.fine_grid.copy()
        grid_no_vuln.plantable_coords = self.base_grid.plantable_coords.copy()
        grid_no_vuln.vulnerable_coords = self.base_grid.vulnerable_coords.copy() \
            if len(self.base_grid.vulnerable_coords) > 0 else np.array([])
        grid_no_vuln.vulnerability_weights = self.base_grid.vulnerability_weights.copy()
        grid_no_vuln.convert_vulnerable_to_prohibited()

        # Visualize the grid without vulnerable cells
        self.visualizer.plot_coarse_grid_only(
            grid_no_vuln,
            'Grid WITHOUT Vulnerable Cells (Converted to Prohibited)',
            'grid_without_vuln.png'
        )

        self.results_without_vuln = {'scenario': 'WITHOUT_VULNERABLE', 'k_results': {}}

        for k in self.k_values:
            print(f"\n[WITHOUT VULN] Optimizing for k={k} trees...")

            # Check if enough plantable spots
            if len(grid_no_vuln.plantable_coords) < k:
                print(f"  Not enough plantable spots ({len(grid_no_vuln.plantable_coords)}) for k={k}")
                self.results_without_vuln['k_results'][k] = {
                    'n_trees': 0,
                    'best_secpi': 0,
                    'error': f'Not enough plantable spots ({len(grid_no_vuln.plantable_coords)})'
                }
                continue

            best_aco, best_secpi, all_secpi = self.run_optimization_for_k(
                grid_no_vuln, k, n_runs=5
            )

            if best_aco and best_aco.best_solution:
                tree_coords, tree_species = best_aco.best_solution
                cooling, cca = self.cooling_model.calculate_total_cooling(
                    tree_coords, tree_species, grid_no_vuln.fine_grid_points,
                    apply_competition=True
                )

                # Store results
                self.results_without_vuln['k_results'][k] = {
                    'n_trees': len(tree_coords),
                    'best_secpi': float(best_secpi),
                    'all_secpi': [float(s) for s in all_secpi],
                    'mean_secpi': float(np.mean(all_secpi)) if all_secpi else 0,
                    'std_secpi': float(np.std(all_secpi)) if len(all_secpi) > 1 else 0,
                    'tree_placements': [(float(x), float(y)) for x, y in tree_coords],
                    'tree_species': list(tree_species),
                    'unique_species': list(set(tree_species)),
                    'n_unique_species': len(set(tree_species)),
                    'cooling_stats': {
                        'mean': float(np.mean(cooling)),
                        'max': float(np.max(cooling)),
                        'std': float(np.std(cooling)),
                        'coverage': float(np.sum(cooling > 0.01) / len(cooling) * 100)
                    }
                }

                # Visualize each k solution
                self.visualizer.plot_optimized_solution_fixed(
                    grid_no_vuln, tree_coords, tree_species, cooling,
                    f'WITHOUT VULNERABLE: k={k} Trees\nSECPI: {best_secpi:.4f}',
                    f'solution_without_vuln_k{k}.png',
                    output_subdir='WITHOUT_VULNERABLE'
                )

                print(f"  Best SECPI: {best_secpi:.4f}, Species: {set(tree_species)}")
            else:
                self.results_without_vuln['k_results'][k] = {
                    'n_trees': 0,
                    'best_secpi': 0,
                    'error': 'No valid solution found'
                }
                print(f"  No valid solution found for k={k}")

        # Save WITHOUT VULNERABLE results
        json_path = os.path.join(without_vuln_dir, 'results_without_vuln_all_k.json')
        with open(json_path, 'w') as f:
            json.dump(self.results_without_vuln, f, indent=2)
        print(f"\nSaved: {json_path}")

        # =====================================================================
        # Generate Comparison Visualizations
        # =====================================================================
        self._plot_k_comparison()
        self._plot_secpi_vs_k_curve()
        self._generate_comparison_table()

        return self.results_with_vuln, self.results_without_vuln

    def _plot_k_comparison(self):
        """Plot side-by-side comparison of WITH vs WITHOUT for each k."""
        fig, axes = plt.subplots(2, 3, figsize=(18, 12))
        axes = axes.flatten()

        for idx, k in enumerate(self.k_values):
            ax = axes[idx]

            with_data = self.results_with_vuln['k_results'].get(k, {})
            without_data = self.results_without_vuln['k_results'].get(k, {})

            with_secpi = with_data.get('best_secpi', 0)
            without_secpi = without_data.get('best_secpi', 0)

            with_std = with_data.get('std_secpi', 0)
            without_std = without_data.get('std_secpi', 0)

            x = np.arange(2)
            values = [with_secpi, without_secpi]
            errors = [with_std, without_std]
            colors = ['#E74C3C', '#3498DB']
            labels = ['WITH\nVulnerable', 'WITHOUT\nVulnerable']

            bars = ax.bar(x, values, yerr=errors, color=colors,
                         edgecolor='black', linewidth=2, capsize=8, alpha=0.8)

            for bar, val in zip(bars, values):
                height = bar.get_height()
                ax.annotate(f'{val:.4f}',
                           xy=(bar.get_x() + bar.get_width() / 2, height),
                           xytext=(0, 5), textcoords='offset points',
                           ha='center', va='bottom', fontsize=11, fontweight='bold')

            ax.set_xticks(x)
            ax.set_xticklabels(labels, fontsize=10)
            ax.set_ylabel('SECPI Score', fontsize=11)
            ax.set_title(f'k = {k} Trees', fontsize=13, fontweight='bold')
            ax.grid(True, alpha=0.3, axis='y')

            # Annotate species counts
            with_n_sp = with_data.get('n_unique_species', 0)
            without_n_sp = without_data.get('n_unique_species', 0)
            ax.text(0.02, 0.98, f'Species: {with_n_sp}', transform=ax.transAxes,
                   fontsize=9, verticalalignment='top', color='#E74C3C')
            ax.text(0.98, 0.98, f'Species: {without_n_sp}', transform=ax.transAxes,
                   fontsize=9, verticalalignment='top', ha='right', color='#3498DB')

        plt.suptitle('SECPI Comparison: WITH vs WITHOUT Vulnerable Cells (k=1 to 6)',
                    fontsize=16, fontweight='bold')
        plt.tight_layout()

        filepath = os.path.join(self.visualizer.run_dir, 'comparison_with_vs_without_all_k.png')
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"Saved: {filepath}")

    def _plot_secpi_vs_k_curve(self):
        """Plot SECPI vs k curves for both scenarios."""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

        # Extract data
        k_vals = []
        with_secpi = []
        with_std = []
        without_secpi = []
        without_std = []

        for k in self.k_values:
            k_vals.append(k)

            with_data = self.results_with_vuln['k_results'].get(k, {})
            without_data = self.results_without_vuln['k_results'].get(k, {})

            with_secpi.append(with_data.get('best_secpi', 0))
            with_std.append(with_data.get('std_secpi', 0))
            without_secpi.append(without_data.get('best_secpi', 0))
            without_std.append(without_data.get('std_secpi', 0))

        # Left plot: SECPI curves
        ax1.errorbar(k_vals, with_secpi, yerr=with_std,
                    marker='o', markersize=10, linewidth=2.5, capsize=6,
                    color='#E74C3C', label='WITH Vulnerable', linestyle='-')
        ax1.errorbar(k_vals, without_secpi, yerr=without_std,
                    marker='s', markersize=10, linewidth=2.5, capsize=6,
                    color='#3498DB', label='WITHOUT Vulnerable', linestyle='--')

        ax1.set_xlabel('Number of Trees (k)', fontsize=13)
        ax1.set_ylabel('SECPI Score', fontsize=13)
        ax1.set_title('SECPI vs Number of Trees', fontsize=14, fontweight='bold')
        ax1.legend(fontsize=11)
        ax1.grid(True, alpha=0.3)
        ax1.set_xticks(k_vals)

        # Annotate optimal k
        best_k_with = k_vals[np.argmax(with_secpi)]
        best_k_without = k_vals[np.argmax(without_secpi)]
        ax1.annotate(f'Best k={best_k_with}',
                    xy=(best_k_with, max(with_secpi)),
                    xytext=(best_k_with + 0.3, max(with_secpi) + 0.05),
                    fontsize=10, color='#E74C3C',
                    arrowprops=dict(arrowstyle='->', color='#E74C3C'))

        # Right plot: Difference (WITH - WITHOUT)
        diff = [w - wo for w, wo in zip(with_secpi, without_secpi)]
        colors = ['#2ECC71' if d >= 0 else '#E74C3C' for d in diff]

        bars = ax2.bar(k_vals, diff, color=colors, edgecolor='black', linewidth=2, alpha=0.8)
        ax2.axhline(0, color='black', linestyle='-', linewidth=1.5)

        for bar, d in zip(bars, diff):
            height = bar.get_height()
            va = 'bottom' if height >= 0 else 'top'
            offset = 5 if height >= 0 else -5
            ax2.annotate(f'{d:+.4f}',
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, offset), textcoords='offset points',
                        ha='center', va=va, fontsize=10, fontweight='bold')

        ax2.set_xlabel('Number of Trees (k)', fontsize=13)
        ax2.set_ylabel('SECPI Difference (WITH - WITHOUT)', fontsize=13)
        ax2.set_title('SECPI Difference by k\n(Positive = WITH performs better)',
                     fontsize=14, fontweight='bold')
        ax2.grid(True, alpha=0.3, axis='y')
        ax2.set_xticks(k_vals)

        plt.tight_layout()

        filepath = os.path.join(self.visualizer.run_dir, 'secpi_vs_k_curves.png')
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"Saved: {filepath}")

    def _generate_comparison_table(self):
        """Generate a CSV comparison table for all k values."""
        rows = []

        for k in self.k_values:
            with_data = self.results_with_vuln['k_results'].get(k, {})
            without_data = self.results_without_vuln['k_results'].get(k, {})

            row = {
                'k': k,
                'with_secpi': with_data.get('best_secpi', 0),
                'with_mean_secpi': with_data.get('mean_secpi', 0),
                'with_std_secpi': with_data.get('std_secpi', 0),
                'with_n_species': with_data.get('n_unique_species', 0),
                'with_species': ', '.join(with_data.get('unique_species', [])),
                'with_cooling_mean': with_data.get('cooling_stats', {}).get('mean', 0),
                'with_coverage': with_data.get('cooling_stats', {}).get('coverage', 0),
                'without_secpi': without_data.get('best_secpi', 0),
                'without_mean_secpi': without_data.get('mean_secpi', 0),
                'without_std_secpi': without_data.get('std_secpi', 0),
                'without_n_species': without_data.get('n_unique_species', 0),
                'without_species': ', '.join(without_data.get('unique_species', [])),
                'without_cooling_mean': without_data.get('cooling_stats', {}).get('mean', 0),
                'without_coverage': without_data.get('cooling_stats', {}).get('coverage', 0),
                'secpi_difference': with_data.get('best_secpi', 0) - without_data.get('best_secpi', 0),
                'better_scenario': 'WITH' if with_data.get('best_secpi', 0) >= without_data.get('best_secpi', 0) else 'WITHOUT'
            }
            rows.append(row)

        if pd is not None:
            df = pd.DataFrame(rows)
            csv_path = os.path.join(self.visualizer.run_dir, 'scenario_comparison_k1_to_k6.csv')
            df.to_csv(csv_path, index=False)
            print(f"Saved: {csv_path}")

            # Also print summary table
            print("\n" + "=" * 100)
            print("SCENARIO COMPARISON TABLE (k=1 to 6)")
            print("=" * 100)
            print(f"{'k':<3} | {'WITH SECPI':<12} | {'WITHOUT SECPI':<14} | {'DIFF':<10} | {'BETTER':<8} | {'WITH Species':<30}")
            print("-" * 100)
            for _, row in df.iterrows():
                print(f"{row['k']:<3} | {row['with_secpi']:<12.4f} | {row['without_secpi']:<14.4f} | "
                      f"{row['secpi_difference']:<+10.4f} | {row['better_scenario']:<8} | {row['with_species']:<30}")

            return df

        csv_path = os.path.join(self.visualizer.run_dir, 'scenario_comparison_k1_to_k6.csv')
        with open(csv_path, 'w', encoding='utf-8') as f:
            f.write('k,with_secpi,with_mean_secpi,with_std_secpi,with_n_species,with_species,with_cooling_mean,with_coverage,without_secpi,without_mean_secpi,without_std_secpi,without_n_species,without_species,without_cooling_mean,without_coverage,secpi_difference,better_scenario\n')
            for row in rows:
                f.write(','.join([str(row['k']), str(row['with_secpi']), str(row['with_mean_secpi']), str(row['with_std_secpi']), str(row['with_n_species']), str(row['with_species']), str(row['with_cooling_mean']), str(row['with_coverage']), str(row['without_secpi']), str(row['without_mean_secpi']), str(row['without_std_secpi']), str(row['without_n_species']), str(row['without_species']), str(row['without_cooling_mean']), str(row['without_coverage']), str(row['secpi_difference']), str(row['better_scenario'])]) + '\n')
        print(f"Saved: {csv_path}")
        print("Pandas unavailable; wrote plain CSV fallback instead.")
        return rows

# =============================================================================

# UPDATED INTERPRETER METHOD FOR k=1 TO 6

# =============================================================================

def interpret_k_scenarios(self, results_with, results_without):
    """Interpret k=1 to k=6 scenario comparison results."""
    interpretation = []
    interpretation.append("=" * 80)
    interpretation.append("AUTOMATED INTERPRETATION: k=1 TO k=6 SCENARIO COMPARISON")
    interpretation.append("WITH vs WITHOUT VULNERABLE CELLS")
    interpretation.append("=" * 80)

    interpretation.append("\n1. SECPI PROGRESSION BY k")
    interpretation.append("-" * 40)

    k_values = [1, 2, 3, 4, 5]
    with_scores = []
    without_scores = []

    for k in k_values:
        w_data = results_with.get('k_results', {}).get(k, {})
        wo_data = results_without.get('k_results', {}).get(k, {})
        w_secpi = w_data.get('best_secpi', 0)
        wo_secpi = wo_data.get('best_secpi', 0)
        with_scores.append(w_secpi)
        without_scores.append(wo_secpi)

        diff = w_secpi - wo_secpi
        better = "WITH" if diff >= 0 else "WITHOUT"

        interpretation.append(f"   k={k}: WITH={w_secpi:.4f}, WITHOUT={wo_secpi:.4f}, "
                             f"Δ={diff:+.4f} ({better} better)")

    interpretation.append("\n2. OPTIMAL k IDENTIFICATION")
    interpretation.append("-" * 40)

    best_k_with = k_values[np.argmax(with_scores)]
    best_k_without = k_values[np.argmax(without_scores)]
    best_with_secpi = max(with_scores)
    best_without_secpi = max(without_scores)

    interpretation.append(f"   WITH VULNERABLE: Optimal k = {best_k_with} (SECPI = {best_with_secpi:.4f})")
    interpretation.append(f"   WITHOUT VULNERABLE: Optimal k = {best_k_without} (SECPI = {best_without_secpi:.4f})")

    if best_k_with == best_k_without:
        interpretation.append(f"   → Same optimal k for both scenarios")
    else:
        interpretation.append(f"   → Different optimal k values suggests vulnerability affects diminishing returns")

    interpretation.append("\n3. DIMINISHING RETURNS ANALYSIS")
    interpretation.append("-" * 40)

    # Calculate marginal gains
    with_marginal = [with_scores[i] - with_scores[i-1] for i in range(1, len(with_scores))]
    without_marginal = [without_scores[i] - without_scores[i-1] for i in range(1, len(without_scores))]

    interpretation.append("   Marginal SECPI gains (k to k+1):")
    for i, (wm, wom) in enumerate(zip(with_marginal, without_marginal), 2):
        interpretation.append(f"   k={i-1}→{i}: WITH={wm:+.4f}, WITHOUT={wom:+.4f}")

    # Find point of diminishing returns
    with_diminish_k = None
    without_diminish_k = None

    for i, mg in enumerate(with_marginal):
        if mg < 0.05:
            with_diminish_k = i + 2
            break

    for i, mg in enumerate(without_marginal):
        if mg < 0.05:
            without_diminish_k = i + 2
            break

    if with_diminish_k:
        interpretation.append(f"\n   WITH: Diminishing returns start at k={with_diminish_k}")
    if without_diminish_k:
        interpretation.append(f"   WITHOUT: Diminishing returns start at k={without_diminish_k}")

    interpretation.append("\n4. SPECIES DIVERSITY PATTERNS")
    interpretation.append("-" * 40)

    for k in k_values:
        w_data = results_with.get('k_results', {}).get(k, {})
        wo_data = results_without.get('k_results', {}).get(k, {})

        w_species = w_data.get('unique_species', [])
        wo_species = wo_data.get('unique_species', [])

        interpretation.append(f"   k={k}: WITH uses {len(w_species)} species {set(w_species)}")
        interpretation.append(f"         WITHOUT uses {len(wo_species)} species {set(wo_species)}")

    interpretation.append("\n5. EQUITY IMPACT ASSESSMENT")
    interpretation.append("-" * 40)

    # Count how many k values show WITH performing better
    with_wins = sum(1 for w, wo in zip(with_scores, without_scores) if w >= wo)
    without_wins = len(k_values) - with_wins

    interpretation.append(f"   WITH performs better in {with_wins}/{len(k_values)} k values")
    interpretation.append(f"   WITHOUT performs better in {without_wins}/{len(k_values)} k values")

    avg_diff = np.mean([w - wo for w, wo in zip(with_scores, without_scores)])
    interpretation.append(f"   Average SECPI difference: {avg_diff:+.4f}")

    if avg_diff > 0.05:
        interpretation.append("\n   → STRONG EQUITY BENEFIT: Vulnerable zones improve optimization")
    elif avg_diff > 0:
        interpretation.append("\n   → MODEST EQUITY BENEFIT: Slight improvement with vulnerable zones")
    elif avg_diff > -0.05:
        interpretation.append("\n   → NEUTRAL: Similar performance with/without vulnerable zones")
    else:
        interpretation.append("\n   → EFFICIENCY COST: Equity consideration reduces overall SECPI")

    interpretation.append("\n6. RECOMMENDATIONS")
    interpretation.append("-" * 40)

    overall_best_k = best_k_with if best_with_secpi >= best_without_secpi else best_k_without
    overall_best_scenario = "WITH" if best_with_secpi >= best_without_secpi else "WITHOUT"

    interpretation.append(f"   Recommended Configuration:")
    interpretation.append(f"   → Number of trees: k = {overall_best_k}")
    interpretation.append(f"   → Scenario: {overall_best_scenario} VULNERABLE")
    interpretation.append(f"   → Expected SECPI: {max(best_with_secpi, best_without_secpi):.4f}")

    if overall_best_scenario == "WITH":
        interpretation.append("\n   Rationale: Equity-weighted optimization achieves better cooling")
        interpretation.append("   distribution while prioritizing vulnerable populations.")
    else:
        interpretation.append("\n   Rationale: Pure efficiency optimization yields higher SECPI.")
        interpretation.append("   Consider if equity goals justify the SECPI trade-off.")

    self.interpretations['k_scenarios'] = "\n".join(interpretation)
    return self.interpretations['k_scenarios']

# Add this method to the AutomatedInterpreter class

AutomatedInterpreter.interpret_k_scenarios = interpret_k_scenarios

# =============================================================================

# MAIN PIPELINE

# =============================================================================

def main_revised_validation():
    """Main pipeline with automated interpretation and sensitivity analysis."""

    print("=" * 100)
    print("SECPI VALIDATION PIPELINE")
    print("Standard ACO + Automated Interpretation + Sensitivity Analysis")
    print("=" * 100)

    visualizer = EnhancedVisualizer()
    interpreter = AutomatedInterpreter(visualizer.run_dir)

    config = {
        'coarse_grid': {'width': 10, 'height': 10, 'cell_size': 10.0},
        'fine_grid': {'cell_size': 1.0},
        'ca_params': {
            'morphology': 'organic',
            'p_init': 0.15,
            'gamma': 4.0,
            'p0': 0.5,
            'theta': 3
        },
        'cooling_params': {
            'decay_lambda': 1.9,
            'cca_threshold': 1.2,
            'competition_k': 5.0
        },
        'aco_params': {
            'n_trees': 5,
            'n_ants': 20,
            'n_iterations': 40,
            'evaporation_rate': 0.5,
            'alpha': 1.0,
            'beta': 2.0,
            'q0': 0.7
        }
    }

    config_path = os.path.join(visualizer.run_dir, 'config.json')
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=2)

    # STEP 1: Create Grid
    print("\n" + "=" * 60)
    print("STEP 1: Creating Two-Level Grid")
    print("=" * 60)

    grid = TwoLevelUrbanGrid(
        coarse_width=config['coarse_grid']['width'],
        coarse_height=config['coarse_grid']['height'],
        coarse_cell_size=config['coarse_grid']['cell_size'],
        fine_cell_size=config['fine_grid']['cell_size']
    )
    grid.generate_ca_archetype(
        params=config['ca_params'],
        morphology=config['ca_params']['morphology']
    )

    visualizer.plot_coarse_grid_only(
        grid, 'CA Generated Urban Grid', '01_coarse_grid.png'
    )

    # Interpret grid
    grid_interpretation = interpreter.interpret_grid_generation(grid, config['ca_params'])
    print(grid_interpretation)

    # STEP 2: Equity Weights
    print("\n" + "=" * 60)
    print("STEP 2: Equity Weights")
    print("=" * 60)

    visualizer.plot_grid_with_equity_weights(
        grid, 'Equity Weights', '02_equity_weights.png'
    )

    equity_interpretation = interpreter.interpret_equity_weights(grid)
    print(equity_interpretation)

    # STEP 3: Cooling Model
    print("\n" + "=" * 60)
    print("STEP 3: Cooling Model & Species")
    print("=" * 60)

    cooling_model = CorrectedCoolingModel(
        decay_lambda=config['cooling_params']['decay_lambda'],
        cca_threshold=config['cooling_params']['cca_threshold'],
        competition_k=config['cooling_params']['competition_k']
    )

    visualizer.plot_all_species_decay_curves(
        cooling_model, grid, '03_species_decay_curves.png'
    )

    species_interpretation = interpreter.interpret_species_characteristics(
        cooling_model.tree_species
    )
    print(species_interpretation)

    # STEP 4: ACO Optimization
    print("\n" + "=" * 60)
    print("STEP 4: ACO Optimization")
    print("=" * 60)

    if len(grid.plantable_coords) == 0:
        print("ERROR: No plantable spots!")
        return None

    # STEP 3.5: Calibrate STUDY-WIDE reference cutoffs (ONCE)
    # These are reused by every AntColonySystemACO instance created below and in
    # SensitivityAnalyzer / MorphologicalRobustnessValidator /
    # SuboptimalScenariosGenerator, so area_proportions/SECPI remain
    # comparable across all analyses in this run. See audit conversation:
    # replaces the previous self-referential per-scenario quartile
    # classification, which normalized away magnitude differences between
    # scenarios (any placement landed at ~25%/25%/25%/25% regardless of
    # actual cooling achieved).
    print("\n" + "=" * 60)
    print("STEP 3.5: Calibrating study-wide reference cutoffs")
    print("=" * 60)
    global_reference_cutoffs = calibrate_global_reference_cutoffs(
        grid, cooling_model, cooling_model.tree_species.species_list,
        n_trees_range=(1, 6), n_samples=100, random_seed=42
    )
    print(f"Reference cutoffs (Q1,Q2,Q3): {global_reference_cutoffs}")

    aco = AntColonySystemACO(
        grid, cooling_model,
        n_trees=config['aco_params']['n_trees'],
        n_ants=config['aco_params']['n_ants'],
        n_iterations=config['aco_params']['n_iterations'],
        evaporation_rate=config['aco_params']['evaporation_rate'],
        alpha=config['aco_params']['alpha'],
        beta=config['aco_params']['beta'],
        q0=config['aco_params']['q0'],
        reference_cutoffs=global_reference_cutoffs
    )
    history_best, history_avg = aco.run(verbose=True)

    # Plot convergence
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(history_best, 'b-', linewidth=2, label='Best SECPI')
    ax.plot(history_avg, 'r--', linewidth=2, alpha=0.7, label='Average SECPI')
    ax.set_xlabel('Iteration', fontsize=11)
    ax.set_ylabel('SECPI Score', fontsize=11)
    ax.set_title('ACO Convergence', fontsize=14, fontweight='bold')
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    convergence_path = os.path.join(visualizer.run_dir, '04_aco_convergence.png')
    plt.savefig(convergence_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Saved: {convergence_path}")

    # Interpret optimization results
    opt_interpretation = interpreter.interpret_optimization_result(
        aco, cooling_model.tree_species, grid
    )
    print(opt_interpretation)

    # STEP 5: Visualize Best Solution
    print("\n" + "=" * 60)
    print("STEP 5: Visualizing Best Solution")
    print("=" * 60)

    if aco.best_solution:
        tree_coords, tree_species = aco.best_solution
        cooling, _ = cooling_model.calculate_total_cooling(
            tree_coords, tree_species, grid.fine_grid_points,
            apply_competition=True
        )

        visualizer.plot_optimized_solution_fixed(
            grid, tree_coords, tree_species, cooling,
            f'Optimized Tree Placement\nSECPI: {aco.best_secpi:.4f}',
            '05_optimized_solution.png'
        )

        # Zonal efficiency
        visualizer.plot_zonal_cooling_efficiency(
            grid, cooling, grid.vulnerability_weights,
            'Zonal Cooling Efficiency Analysis',
            '06_zonal_efficiency.png'
        )

        # Interpret zonal efficiency
        zonal_interpretation = interpreter.interpret_zonal_efficiency(
            cooling, grid.vulnerability_weights
        )
        print(zonal_interpretation)

# STEP 6: Scenario Comparison (k=1 to k=6)

    print("\n" + "=" * 60)
    print("STEP 6: Scenario Comparison (k=1 to 6, WITH vs WITHOUT Vulnerable)")
    print("=" * 60)

    scenario_generator = SuboptimalScenariosGenerator(
        grid, cooling_model, config['aco_params'], visualizer,
        reference_cutoffs=global_reference_cutoffs
    )
    results_with, results_without = scenario_generator.run_all_scenarios()

    # Interpret k=1 to k=6 scenario comparison
    k_scenario_interpretation = interpreter.interpret_k_scenarios(
        results_with, results_without
    )
    print(k_scenario_interpretation)

    # Also generate the original scenario comparison interpretation for best k
    best_k = config['aco_params']['n_trees']
    best_with = results_with.get('k_results', {}).get(best_k, {})
    best_without = results_without.get('k_results', {}).get(best_k, {})
    scenario_interpretation = interpreter.interpret_scenario_comparison(
        best_with, best_without
    )
    print(scenario_interpretation)

    # STEP 7: Sensitivity Analysis (OAT)
    print("\n" + "=" * 60)
    print("STEP 7: Sensitivity Analysis (One-At-a-Time)")
    print("=" * 60)

    sensitivity_analyzer = SensitivityAnalyzer(
        grid, cooling_model, config['aco_params'], visualizer.run_dir,
        reference_cutoffs=global_reference_cutoffs
    )

    sensitivity_df = sensitivity_analyzer.run_oat_analysis(n_samples=3)
    sensitivity_analyzer.save_results()
    sensitivity_analyzer.plot_sensitivity_results()

    # Interpret sensitivity analysis
    sensitivity_interpretation = interpreter.interpret_sensitivity_analysis(sensitivity_df)
    print(sensitivity_interpretation)

    # STEP 8: Morphological Robustness Validation
    print("\n" + "=" * 60)
    print("STEP 8: Morphological Robustness Validation")
    print("=" * 60)

    robustness_validator = MorphologicalRobustnessValidator(
        config, n_runs_per_morphology=5,
        reference_cutoffs=global_reference_cutoffs
    )
    robustness_results = robustness_validator.run_validation(visualizer.run_dir)
    robustness_report = robustness_validator.generate_report(visualizer.run_dir)

    # Plot robustness results
    visualizer.plot_morphological_robustness(
        robustness_results, '07_morphological_robustness.png'
    )

    # Interpret morphological robustness
    morph_interpretation = interpreter.interpret_morphological_robustness(robustness_results)
    print(morph_interpretation)

    # STEP 9: Save All Interpretations
    print("\n" + "=" * 60)
    print("STEP 9: Saving All Interpretations")
    print("=" * 60)

    interpreter.save_all_interpretations()

    # STEP 10: Generate Final Summary
    print("\n" + "=" * 60)
    print("STEP 10: Generating Final Summary")
    print("=" * 60)

    final_summary = {
        'run_timestamp': visualizer.timestamp,
        'output_directory': visualizer.run_dir,
        'configuration': config,
        'optimization_results': {
            'best_secpi': float(aco.best_secpi) if aco.best_secpi else None,
            'n_trees': len(aco.best_solution[0]) if aco.best_solution else 0,
            'unique_species': list(set(aco.best_solution[1])) if aco.best_solution else [],
            'cooling_stats': {
                'mean': float(np.mean(aco.best_cooling)) if aco.best_cooling is not None else None,
                'max': float(np.max(aco.best_cooling)) if aco.best_cooling is not None else None,
                'std': float(np.std(aco.best_cooling)) if aco.best_cooling is not None else None
            }
        },
        'scenario_comparison': {
            'with_vulnerable_secpi': results_with.get('best_secpi', None),
            'without_vulnerable_secpi': results_without.get('best_secpi', None),
            'difference': (results_with.get('best_secpi', 0) - results_without.get('best_secpi', 0))
                          if results_with and results_without else None
        },
        'sensitivity_analysis': {
            'baseline_secpi': float(sensitivity_analyzer.baseline_secpi) if sensitivity_analyzer.baseline_secpi else None,
            'top_3_sensitive_params': sensitivity_df.nlargest(3, 'sensitivity_index')[['parameter', 'category', 'sensitivity_index']].to_dict('records'),
            'total_params_analyzed': len(sensitivity_df)
        },
        'morphological_robustness': {
            'mean_across_morphologies': robustness_report['overall']['mean_across_morphologies'],
            'std_across_morphologies': robustness_report['overall']['std_across_morphologies'],
            'assessment': robustness_report['overall']['robustness_assessment']
        },
        'k_scenario_analysis': {
            'with_vulnerable': {
                k: {
                'secpi': results_with.get('k_results', {}).get(k, {}).get('best_secpi', 0),
                'species': results_with.get('k_results', {}).get(k, {}).get('unique_species', [])
            } for k in [1, 2, 3, 4, 5, 6]
        },
            'without_vulnerable': {
                k: {
                'secpi': results_without.get('k_results', {}).get(k, {}).get('best_secpi', 0),
                'species': results_without.get('k_results', {}).get(k, {}).get('unique_species', [])
            } for k in [1, 2, 3, 4, 5, 6]
        },
            'optimal_k_with': [1, 2, 3, 4, 5, 6][np.argmax([results_with.get('k_results', {}).get(k, {}).get('best_secpi', 0) for k in [1,2,3,4,5,6]])],
            'optimal_k_without': [1, 2, 3, 4, 5, 6][np.argmax([results_without.get('k_results', {}).get(k, {}).get('best_secpi', 0) for k in [1,2,3,4,5,6]])]
    }
    }

    summary_path = os.path.join(visualizer.run_dir, 'FINAL_SUMMARY.json')
    with open(summary_path, 'w') as f:
        json.dump(final_summary, f, indent=2)
    print(f"Saved: {summary_path}")

    # Print final summary to console
    print("\n" + "=" * 100)
    print("FINAL SUMMARY")
    print("=" * 100)
    print(f"\nOutput Directory: {visualizer.run_dir}")
    print(f"\nOptimization Results:")
    print(f"  Best SECPI: {final_summary['optimization_results']['best_secpi']:.4f}")
    print(f"  Trees Placed: {final_summary['optimization_results']['n_trees']}")
    print(f"  Species Used: {final_summary['optimization_results']['unique_species']}")

    print(f"\nScenario Comparison:")
    print(f"  WITH Vulnerable SECPI: {final_summary['scenario_comparison']['with_vulnerable_secpi']:.4f}")
    print(f"  WITHOUT Vulnerable SECPI: {final_summary['scenario_comparison']['without_vulnerable_secpi']:.4f}")
    print(f"  Difference: {final_summary['scenario_comparison']['difference']:.4f}")

    print(f"\nSensitivity Analysis:")
    print(f"  Baseline SECPI: {final_summary['sensitivity_analysis']['baseline_secpi']:.4f}")
    print(f"  Top 3 Sensitive Parameters:")
    for param in final_summary['sensitivity_analysis']['top_3_sensitive_params']:
        print(f"    - {param['parameter']} ({param['category']}): {param['sensitivity_index']:.6f}")

    print(f"\nMorphological Robustness:")
    print(f"  Mean SECPI across morphologies: {final_summary['morphological_robustness']['mean_across_morphologies']:.4f}")
    print(f"  Std across morphologies: {final_summary['morphological_robustness']['std_across_morphologies']:.4f}")
    print(f"  Assessment: {final_summary['morphological_robustness']['assessment']}")

    print("\n" + "=" * 100)
    print("VALIDATION PIPELINE COMPLETE")
    print("=" * 100)
    print(f"\nAll outputs saved to: {visualizer.run_dir}")
    print("\nGenerated files include:")
    print("  - Visualization PNGs (grid, cooling, solutions)")
    print("  - sensitivity_analysis_oat.csv (parameter sensitivities)")
    print("  - sensitivity_analysis_by_category.csv (category summaries)")
    print("  - morphological_robustness_report.json")
    print("  - COMPLETE_INTERPRETATION_REPORT.txt")
    print("  - FINAL_SUMMARY.json")
    print("  - Individual interpretation files for each analysis step")

    return final_summary

# =============================================================================

# ENTRY POINT

# =============================================================================

if __name__ == "__main__":
    results = main_revised_validation()
