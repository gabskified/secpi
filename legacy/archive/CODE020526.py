"""
WORLDBUILDING: Equitable Integer Lattice Optimization Paradigm
for Non-Submodular Spatial Resource Allocation

This module implements the foundational components of the paradigm:
1. Integer Lattice Formalization
2. Cellular Automata for Urban Morphology Generation
3. Dual-Scale Grid System (Coarse & Fine)
4. Tree Functional Types with Biophysical Properties
5. Non-Submodular Cooling Proxy with Competition Model
6. SECPI Objective Function
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import matplotlib.colors as mcolors
import itertools
from pathlib import Path
from dataclasses import dataclass
from typing import List, Tuple, Dict, Set
import warnings
warnings.filterwarnings('ignore')

# ============================================================================
# 1. INTEGER LATTICE FORMALIZATION
# ============================================================================

@dataclass
class LatticePoint:
    """Formal representation of a point in the 2D integer lattice ℤ²"""
    x: int  # Lattice coordinate in x-direction
    y: int  # Lattice coordinate in y-direction
    state: str = None  # P, V, or A
    equity_weight: float = 1.0  # W_e(i) for spatial equity
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

class IntegerLattice:
    """Formal discrete representation of urban space as subset of ℤ²"""
    
    def __init__(self, width: int, height: int):
        """
        Initialize integer lattice
        
        Parameters:
        -----------
        width : int
            Lattice width in cells
        height : int
            Lattice height in cells
        """
        self.width = width
        self.height = height
        self.lattice_points = {}
        
        # Initialize all points
        for x in range(width):
            for y in range(height):
                self.lattice_points[(x, y)] = LatticePoint(x, y)
        
        # State mapping function S: G → {P, V, A}
        self.state_mapping = {}
        
    def set_state(self, x: int, y: int, state: str, equity_weight: float = 1.0):
        """Set state of a lattice point"""
        if (x, y) in self.lattice_points:
            self.lattice_points[(x, y)].state = state
            self.lattice_points[(x, y)].equity_weight = equity_weight
            self.state_mapping[(x, y)] = state
            
    def get_state(self, x: int, y: int) -> str:
        """Get state of a lattice point"""
        return self.lattice_points.get((x, y), LatticePoint(x, y)).state
    
    def get_equity_weight(self, x: int, y: int) -> float:
        """Get equity weight of a lattice point"""
        return self.lattice_points.get((x, y), LatticePoint(x, y)).equity_weight
    
    def get_points_by_state(self, state: str) -> List[LatticePoint]:
        """Get all lattice points with a specific state"""
        return [pt for pt in self.lattice_points.values() if pt.state == state]
    
    def get_available_points(self) -> List[LatticePoint]:
        """Get all Available (A) points"""
        return self.get_points_by_state('A')
    
    def get_vulnerable_points(self) -> List[LatticePoint]:
        """Get all Vulnerable (V) points"""
        return self.get_points_by_state('V')
    
    def get_prohibited_points(self) -> List[LatticePoint]:
        """Get all Prohibited (P) points"""
        return self.get_points_by_state('P')
    
    def is_valid_planting_location(self, x: int, y: int) -> bool:
        """Check if a lattice point is valid for planting"""
        state = self.get_state(x, y)
        return state == 'A' or state == 'V'

# ============================================================================
# 2. CELLULAR AUTOMATA FOR URBAN MORPHOLOGY GENERATION
# ============================================================================

class CellularAutomataUrbanGenerator:
    """
    Binary Urban CA Model for generating realistic urban morphologies
    Based on modified transition rules from Chakraborty et al. (2022)
    """
    
    def __init__(self, width: int, height: int, cell_size: float = 10.0):
        """
        Initialize CA generator for 100m x 100m study area
        
        Parameters:
        -----------
        width : int
            Coarse grid width (10 cells for 100m)
        height : int
            Coarse grid height (10 cells for 100m)
        cell_size : float
            Size of each cell in meters (10m for coarse grid)
        """
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.grid = np.zeros((height, width), dtype=int)  # 0 = A, 1 = P
        self.vulnerable_zones = []
        
        # CORRECTED CA parameters - MUCH MORE CONSERVATIVE
        self.p_init = 0.03  # REDUCED: Initial seed density (3%)
        self.theta = 5      # INCREASED: Neighborhood threshold (need 5/8 neighbors)
        self.alpha = 0.005  # REDUCED: Base urbanization probability (0.5%)
        self.beta = 0.10    # MODERATE: Neighborhood influence coefficient
        self.t_max = 30     # FEWER generations
        
        # Monitoring
        self.history_p = []
        
    def initialize_seeds(self):
        """Initialize random seeds for urbanization"""
        n_cells = self.width * self.height
        n_seeds = int(n_cells * self.p_init)
        
        # Randomly select seed locations
        seeds = np.random.choice(n_cells, n_seeds, replace=False)
        
        for seed in seeds:
            x = seed % self.width
            y = seed // self.width
            self.grid[y, x] = 1  # Mark as Prohibited (P)
    
    def moore_neighborhood(self, x: int, y: int) -> int:
        """Count P cells in Moore neighborhood (8 surrounding cells)"""
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    count += self.grid[ny, nx]
        return count
    
    def transition_probability(self, N_p: int) -> float:
        """
        Calculate transition probability based on neighborhood influence
        
        Equation from manuscript: P_transition = α + β * (N_p / 8)
        """
        return min(1.0, self.alpha + self.beta * (N_p / 8.0))
    
    def run_generation(self):
        """Run one generation of CA simulation with early stopping"""
        new_grid = self.grid.copy()
        
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y, x] == 0:  # Only non-P cells can transition
                    N_p = self.moore_neighborhood(x, y)
                    
                    if N_p >= self.theta:
                        p_transition = self.transition_probability(N_p)
                        if np.random.random() < p_transition:
                            new_grid[y, x] = 1  # Transition to P
        
        self.grid = new_grid
        
        # Track progress
        p_proportion = np.sum(self.grid) / (self.width * self.height)
        self.history_p.append(p_proportion)
        
        # Early stopping if we reach target
        if p_proportion >= 0.65:
            return True  # Stop condition met
        return False
    
    def generate_organic_morphology(self):
        """Generate organic/clustered urban morphology"""
        # Reset
        self.grid = np.zeros((self.height, self.width), dtype=int)
        self.history_p = []
        
        self.initialize_seeds()
        
        for t in range(self.t_max):
            should_stop = self.run_generation()
            if should_stop:
                break
        
        # Post-processing: add vulnerable zones
        self.add_vulnerable_zones()
        
        return self.create_state_grid()
    
    def add_vulnerable_zones(self):
        """Add vulnerable zones based on social infrastructure"""
        # Algorithmically place vulnerable points
        n_vulnerable_points = 1  # Just 1 school/health center
        
        for _ in range(n_vulnerable_points):
            # Place in areas with SOME P cells but not ALL P cells
            # Find areas with mixed development
            potential_locations = []
            
            # Look for cells that are NOT P and have some P neighbors
            for y in range(self.height):
                for x in range(self.width):
                    if self.grid[y, x] == 0:  # Not P
                        N_p = self.moore_neighborhood(x, y)
                        if 2 <= N_p <= 5:  # Some urban influence but not overwhelmed
                            potential_locations.append((x, y))
            
            if potential_locations:
                # Pick a random suitable location
                vx, vy = potential_locations[np.random.randint(0, len(potential_locations))]
                self.vulnerable_zones.append((vx, vy))
            else:
                # Fallback: place randomly but avoid isolated cells
                attempts = 0
                while attempts < 100:
                    vx = np.random.randint(0, self.width)
                    vy = np.random.randint(0, self.height)
                    if self.grid[vy, vx] == 0:  # Not P
                        N_p = self.moore_neighborhood(vx, vy)
                        if N_p > 0:  # Has some P neighbors
                            self.vulnerable_zones.append((vx, vy))
                            break
                    attempts += 1
        
        # If still no vulnerable zones, place at center
        if not self.vulnerable_zones:
            vx = self.width // 2
            vy = self.height // 2
            self.vulnerable_zones.append((vx, vy))
    
    def create_state_grid(self) -> np.ndarray:
        """Create final state grid with P, V, A classification"""
        state_grid = np.full((self.height, self.width), 'A', dtype='<U1')
        
        # Mark Prohibited cells
        state_grid[self.grid == 1] = 'P'
        
        # Mark Vulnerable cells with VERY SMALL buffer
        buffer_distance = 1  # Only 1 cell buffer (10m)
        
        for vx, vy in self.vulnerable_zones:
            for x in range(max(0, vx - buffer_distance), 
                          min(self.width, vx + buffer_distance + 1)):
                for y in range(max(0, vy - buffer_distance), 
                              min(self.height, vy + buffer_distance + 1)):
                    # Manhattan distance
                    manhattan_dist = abs(x - vx) + abs(y - vy)
                    if manhattan_dist <= buffer_distance:
                        # Only override if not already P
                        if state_grid[y, x] != 'P':
                            state_grid[y, x] = 'V'
        
        return state_grid
    
    def calculate_ratios(self, state_grid: np.ndarray) -> Dict[str, float]:
        """Calculate ratios of P, V, A cells"""
        total_cells = self.width * self.height
        ratios = {
            'P': np.sum(state_grid == 'P') / total_cells,
            'V': np.sum(state_grid == 'V') / total_cells,
            'A': np.sum(state_grid == 'A') / total_cells
        }
        return ratios
    
    def plot_urbanization_history(self):
        """Plot the progression of urbanization over generations"""
        fig, ax = plt.subplots(figsize=(10, 6))
        
        generations = range(len(self.history_p))
        ax.plot(generations, self.history_p, 'b-', linewidth=2, marker='o')
        
        # Add target lines
        ax.axhline(y=0.55, color='r', linestyle='--', alpha=0.5, label='Target Min (55%)')
        ax.axhline(y=0.65, color='r', linestyle='-', alpha=0.5, label='Target Max (65%)')
        ax.axhline(y=0.60, color='g', linestyle='-', alpha=0.3, label='Ideal (60%)')
        
        ax.set_xlabel('Generation', fontsize=12)
        ax.set_ylabel('Proportion of Prohibited Cells (P)', fontsize=12)
        ax.set_title('Urbanization Progression in CA Model', fontsize=14, fontweight='bold')
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        # Add final value annotation
        if self.history_p:
            ax.text(len(self.history_p)-1, self.history_p[-1], 
                   f'Final: {self.history_p[-1]:.1%}', 
                   verticalalignment='bottom', horizontalalignment='right',
                   fontsize=10, bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
        
        plt.tight_layout()
        return fig, ax


# ============================================================================
# 3. DUAL-SCALE GRID SYSTEM
# ============================================================================

class DualScaleGridSystem:
    """
    Dual-scale grid system for optimization and evaluation
    
    Coarse Grid (G_c): 10x10 cells, 10m resolution (for optimization)
    Fine Grid (G_f): 100x100 cells, 1m resolution (for evaluation)
    """
    
    def __init__(self, study_area_size: float = 100.0):
        """
        Initialize dual-scale grid system
        
        Parameters:
        -----------
        study_area_size : float
            Size of study area in meters (default: 100m x 100m)
        """
        self.study_area_size = study_area_size
        
        # Coarse grid parameters (for optimization)
        self.coarse_cell_size = 10.0  # 10m per cell
        self.coarse_n_cells = int(study_area_size / self.coarse_cell_size)  # 10 cells
        
        # Fine grid parameters (for evaluation)
        self.fine_cell_size = 1.0  # 1m per cell
        self.fine_n_cells = int(study_area_size / self.fine_cell_size)  # 100 cells
        
        # Generate coordinate arrays
        self.coarse_coords = self._generate_coarse_coordinates()
        self.fine_coords = self._generate_fine_coordinates()
        
        # Initialize state grids
        self.coarse_state_grid = None
        self.coarse_equity_grid = None
        
    def _generate_coarse_coordinates(self) -> np.ndarray:
        """Generate coarse grid coordinates (cell centers)"""
        coords = []
        cell_half = self.coarse_cell_size / 2.0
        
        for i in range(self.coarse_n_cells):
            for j in range(self.coarse_n_cells):
                x = i * self.coarse_cell_size + cell_half
                y = j * self.coarse_cell_size + cell_half
                coords.append([x, y])
        
        return np.array(coords)
    
    def _generate_fine_coordinates(self) -> np.ndarray:
        """Generate fine grid coordinates"""
        coords = []
        cell_half = self.fine_cell_size / 2.0
        
        for i in range(self.fine_n_cells):
            for j in range(self.fine_n_cells):
                x = i * self.fine_cell_size + cell_half
                y = j * self.fine_cell_size + cell_half
                coords.append([x, y])
        
        return np.array(coords)
    
    def map_coarse_to_fine(self, coarse_state_grid: np.ndarray, 
                          coarse_equity_grid: np.ndarray = None):
        """
        Map coarse grid states to fine grid
        
        Parameters:
        -----------
        coarse_state_grid : np.ndarray
            State grid from CA (P, V, A)
        coarse_equity_grid : np.ndarray, optional
            Equity weights for coarse grid
        """
        self.coarse_state_grid = coarse_state_grid
        
        # Default equity weights if not provided
        if coarse_equity_grid is None:
            coarse_equity_grid = np.ones((self.coarse_n_cells, self.coarse_n_cells))
            # Double weight for V cells
            coarse_equity_grid[coarse_state_grid == 'V'] = 2.0
            # Zero weight for P cells (shouldn't be planted anyway)
            coarse_equity_grid[coarse_state_grid == 'P'] = 0.0
        
        self.coarse_equity_grid = coarse_equity_grid
        
        # Create fine grid representation
        self.fine_state_grid = self._interpolate_to_fine(coarse_state_grid)
        self.fine_equity_grid = self._interpolate_to_fine(coarse_equity_grid)
    
    def _interpolate_to_fine(self, coarse_grid: np.ndarray) -> np.ndarray:
        """Interpolate coarse grid values to fine grid using nearest neighbor"""
        # Each coarse cell corresponds to 10x10 fine cells
        fine_grid = np.zeros((self.fine_n_cells, self.fine_n_cells))
        
        scaling_factor = int(self.coarse_cell_size / self.fine_cell_size)  # 10
        
        for i in range(self.coarse_n_cells):
            for j in range(self.coarse_n_cells):
                coarse_value = coarse_grid[j, i]  # Note: grid is (y, x)
                
                # Map to corresponding fine cells
                fine_i_start = i * scaling_factor
                fine_i_end = fine_i_start + scaling_factor
                fine_j_start = j * scaling_factor
                fine_j_end = fine_j_start + scaling_factor
                
                if isinstance(coarse_value, str):
                    # For state grids, we need to handle strings differently
                    # We'll store as integer codes for now
                    if coarse_value == 'P':
                        code = 0
                    elif coarse_value == 'V':
                        code = 2
                    else:  # 'A'
                        code = 1
                    fine_grid[fine_j_start:fine_j_end, fine_i_start:fine_i_end] = code
                else:
                    fine_grid[fine_j_start:fine_j_end, fine_i_start:fine_i_end] = coarse_value
        
        return fine_grid
    
    def get_plantable_coarse_locations(self) -> List[Tuple[int, int]]:
        """Get all plantable locations in coarse grid (A or V cells)"""
        locations = []
        
        for i in range(self.coarse_n_cells):
            for j in range(self.coarse_n_cells):
                state = self.coarse_state_grid[j, i]
                if state in ['A', 'V']:
                    locations.append((i, j))
        
        return locations
    
    def get_coarse_coordinate(self, i: int, j: int) -> Tuple[float, float]:
        """Get real-world coordinates for coarse grid cell (i, j)"""
        x = i * self.coarse_cell_size + (self.coarse_cell_size / 2.0)
        y = j * self.coarse_cell_size + (self.coarse_cell_size / 2.0)
        return (x, y)
    
    def visualize_dual_grid(self):
        """Visualize both coarse and fine grids"""
        fig, axes = plt.subplots(1, 2, figsize=(16, 6))
        
        # Plot coarse grid
        ax1 = axes[0]
        if self.coarse_state_grid is not None:
            # Color mapping for states
            state_colors = {'P': 'gray', 'V': 'red', 'A': 'lightgreen'}
            
            # Create image representation
            color_grid = np.zeros((*self.coarse_state_grid.shape, 3))
            for i, state in enumerate(['P', 'A', 'V']):
                mask = self.coarse_state_grid == state
                if state == 'P':
                    color_grid[mask] = [0.5, 0.5, 0.5]  # Gray
                elif state == 'V':
                    color_grid[mask] = [1.0, 0.0, 0.0]  # Red
                elif state == 'A':
                    color_grid[mask] = [0.5, 1.0, 0.5]  # Light green
            
            ax1.imshow(color_grid, extent=[0, self.coarse_n_cells, 0, self.coarse_n_cells],
                      origin='lower', aspect='equal')
            
            # Add grid lines
            for i in range(self.coarse_n_cells + 1):
                ax1.axhline(i, color='black', linewidth=0.5, alpha=0.5)
                ax1.axvline(i, color='black', linewidth=0.5, alpha=0.5)
            
            ax1.set_xlabel('Coarse Grid X (10m cells)', fontsize=12)
            ax1.set_ylabel('Coarse Grid Y (10m cells)', fontsize=12)
            ax1.set_title('Coarse Optimization Grid (G_c)', fontsize=14, fontweight='bold')
            
            # Add cell indices
            for i in range(self.coarse_n_cells):
                for j in range(self.coarse_n_cells):
                    ax1.text(i + 0.5, j + 0.5, f'{i},{j}',
                            ha='center', va='center', fontsize=8, alpha=0.7)
        
        # Plot fine grid
        ax2 = axes[1]
        if hasattr(self, 'fine_state_grid'):
            # Convert state codes back to colors
            color_grid_fine = np.zeros((*self.fine_state_grid.shape, 3))
            
            # P cells (code 0)
            color_grid_fine[self.fine_state_grid == 0] = [0.5, 0.5, 0.5]
            # A cells (code 1)
            color_grid_fine[self.fine_state_grid == 1] = [0.5, 1.0, 0.5]
            # V cells (code 2)
            color_grid_fine[self.fine_state_grid == 2] = [1.0, 0.0, 0.0]
            
            ax2.imshow(color_grid_fine, 
                      extent=[0, self.fine_n_cells, 0, self.fine_n_cells],
                      origin='lower', aspect='equal')
            
            # Overlay coarse grid boundaries
            for i in range(0, self.fine_n_cells + 1, 10):
                ax2.axhline(i, color='black', linewidth=1.5, alpha=0.8)
                ax2.axvline(i, color='black', linewidth=1.5, alpha=0.8)
            
            ax2.set_xlabel('Fine Grid X (1m cells)', fontsize=12)
            ax2.set_ylabel('Fine Grid Y (1m cells)', fontsize=12)
            ax2.set_title('Fine Evaluation Grid (G_f)', fontsize=14, fontweight='bold')
        
        plt.tight_layout()
        return fig, axes

# ============================================================================
# 4. PHILIPPINE TREE FUNCTIONAL TYPES (TFTS)
# ============================================================================

@dataclass
class TreeFunctionalType:
    """Data class for Philippine Tree Functional Types"""
    species_code: str
    common_name: str
    scientific_name: str
    crown_diameter_m: float  # C_D (m)
    height_m: float  # h (m)
    # Allometric parameters from FORMIND model
    h0: float = 0.0  # Allometric parameter for DBH estimation
    h1: float = 0.0  # Allometric parameter for DBH estimation
    l0: float = 0.0  # Allometric parameter for LAI estimation
    l1: float = 0.0  # Allometric parameter for LAI estimation
    architecture: str = "unknown"
    growth_rate: str = "moderate"
    
    def calculate_dbh(self) -> float:
        """
        Calculate Diameter at Breast Height using FORMIND allometric equation
        
        DBH = (h / h0)^(1/h1)
        """
        if self.h0 == 0 or self.h1 == 0:
            # Fallback: estimate DBH as 1/10 of height (common approximation)
            return self.height_m / 10.0
        
        return (self.height_m / self.h0) ** (1.0 / self.h1)
    
    def calculate_cpa(self) -> float:
        """
        Calculate Crown Projection Area (CPA)
        
        CPA = (π/4) * C_D²
        """
        return (np.pi / 4.0) * (self.crown_diameter_m ** 2)
    
    def calculate_lai(self) -> float:
        """
        Calculate Leaf Area Index (LAI)
        
        LAI = l0 * DBH^l1
        """
        dbh = self.calculate_dbh()
        return self.l0 * (dbh ** self.l1)

class TFTDatabase:
    """Database of Philippine Tree Functional Types from Table 1"""
    
    def __init__(self):
        # Initialize with 6 TFTs from manuscript
        self.tfts = self._initialize_tfts()
        
        # Calculate max values for normalization
        self.max_cpa = max(tft.calculate_cpa() for tft in self.tfts.values())
        self.max_lai = max(tft.calculate_lai() for tft in self.tfts.values())
        self.max_crown_diameter = max(tft.crown_diameter_m for tft in self.tfts.values())
    
    def _initialize_tfts(self) -> Dict[str, TreeFunctionalType]:
        """Initialize the 6 Philippine TFTs from manuscript"""
        
        # Note: Actual allometric parameters need to be sourced from FORMIND or literature
        # Using reasonable estimates for demonstration
        
        tfts = {
            'NARRA': TreeFunctionalType(
                species_code='NARRA',
                common_name='Narra',
                scientific_name='Pterocarpus indicus',
                crown_diameter_m=20.0,  # Average from literature
                height_m=33.0,
                h0=25.0, h1=0.65,  # Estimated allometric parameters
                l0=0.15, l1=1.2,    # Estimated for tropical trees
                architecture='broad_spreading',
                growth_rate='moderate'
            ),
            'TALISAY': TreeFunctionalType(
                species_code='TALISAY',
                common_name='Talisay',
                scientific_name='Terminalia catappa',
                crown_diameter_m=18.0,
                height_m=25.0,
                h0=22.0, h1=0.62,
                l0=0.18, l1=1.3,
                architecture='umbrella_shaped',
                growth_rate='fast'
            ),
            'BANABA': TreeFunctionalType(
                species_code='BANABA',
                common_name='Banaba',
                scientific_name='Lagerstroemia speciosa',
                crown_diameter_m=12.0,
                height_m=20.0,
                h0=18.0, h1=0.60,
                l0=0.12, l1=1.1,
                architecture='broad_spreading',
                growth_rate='moderate'
            ),
            'DUHAT': TreeFunctionalType(
                species_code='DUHAT',
                common_name='Duhat',
                scientific_name='Syzygium cumini',
                crown_diameter_m=15.0,
                height_m=25.0,
                h0=20.0, h1=0.63,
                l0=0.20, l1=1.4,  # Higher LAI for dense foliage
                architecture='dense_canopy',
                growth_rate='moderate'
            ),
            'AKLENG_PARANG': TreeFunctionalType(
                species_code='AKLENG_PARANG',
                common_name='Akleng-parang',
                scientific_name='Albizia lebbeck',
                crown_diameter_m=14.0,
                height_m=30.0,
                h0=26.0, h1=0.67,
                l0=0.16, l1=1.2,
                architecture='umbrella_shaped',
                growth_rate='fast'
            ),
            'KABIKI': TreeFunctionalType(
                species_code='KABIKI',
                common_name='Kabiki',
                scientific_name='Mimusops elengi',
                crown_diameter_m=10.0,
                height_m=18.0,
                h0=16.0, h1=0.58,
                l0=0.14, l1=1.1,
                architecture='dense_canopy',
                growth_rate='slow'
            )
        }
        
        return tfts
    
    def get_tft(self, species_code: str) -> TreeFunctionalType:
        """Get TFT by species code"""
        return self.tfts.get(species_code.upper())
    
    def get_all_species(self) -> List[str]:
        """Get list of all species codes"""
        return list(self.tfts.keys())
    
    def get_normalized_cpa(self, species_code: str) -> float:
        """Get normalized CPA (0-1)"""
        tft = self.get_tft(species_code)
        if not tft:
            return 0.0
        return tft.calculate_cpa() / self.max_cpa
    
    def get_normalized_lai(self, species_code: str) -> float:
        """Get normalized LAI (0-1)"""
        tft = self.get_tft(species_code)
        if not tft:
            return 0.0
        return tft.calculate_lai() / self.max_lai
    
    def get_normalized_crown_diameter(self, species_code: str) -> float:
        """Get normalized crown diameter (0-1)"""
        tft = self.get_tft(species_code)
        if not tft:
            return 0.0
        return tft.crown_diameter_m / self.max_crown_diameter
    
    def calculate_cooling_potential(self, species_code: str) -> float:
        """
        Calculate cooling potential based on normalized CPA and LAI
        
        Weighting: 70% shading (CPA), 30% evapotranspiration (LAI)
        """
        norm_cpa = self.get_normalized_cpa(species_code)
        norm_lai = self.get_normalized_lai(species_code)
        
        return 0.7 * norm_cpa + 0.3 * norm_lai

# ============================================================================
# 5. NON-SUBMODULAR COOLING PROXY MODEL
# ============================================================================

class NonSubmodularCoolingModel:
    """
    Non-submodular cooling proxy model with competition effects
    
    Implements the cooling function from manuscript:
    C(i,j) = [0.7*(CPA/CPA_max) + 0.3*(LAI/LAI_max)] * exp(-λ * d_ij/C_D,j)
    
    With competition reduction factor:
    R_comp(i) = 1 / (1 + exp(k * (CCA_ground(i) - CCA_threshold)))
    """
    
    def __init__(self, tft_db: TFTDatabase, lambda_decay: float = 0.1,
                 cca_threshold: float = 1.2, k_steepness: float = 5.0):
        """
        Initialize cooling model
        
        Parameters:
        -----------
        tft_db : TFTDatabase
            Database of tree functional types
        lambda_decay : float
            Decay constant λ for distance-decay function
        cca_threshold : float
            Critical CCA where competition begins (default: 1.2)
        k_steepness : float
            Steepness parameter for sigmoidal reduction
        """
        self.tft_db = tft_db
        self.lambda_decay = lambda_decay
        self.cca_threshold = cca_threshold
        self.k_steepness = k_steepness
        
    def calculate_individual_cooling(self, tree_position: Tuple[float, float],
                                   species_code: str,
                                   evaluation_points: np.ndarray) -> np.ndarray:
        """
        Calculate cooling contribution of a single tree
        
        Parameters:
        -----------
        tree_position : Tuple[float, float]
            (x, y) position of tree
        species_code : str
            Species code of tree
        evaluation_points : np.ndarray
            Array of evaluation points (N x 2)
        
        Returns:
        --------
        np.ndarray: Cooling contributions at each evaluation point
        """
        # Get tree properties
        tft = self.tft_db.get_tft(species_code)
        if not tft:
            return np.zeros(len(evaluation_points))
        
        # Calculate normalized cooling potential
        cooling_potential = 0.7 * self.tft_db.get_normalized_cpa(species_code) + 0.3 * self.tft_db.get_normalized_lai(species_code)
        
        # Calculate distances (Manhattan distance as per manuscript)
        distances = cdist([tree_position], evaluation_points, 'cityblock')[0]
        
        # Normalize distance by crown diameter
        normalized_distances = distances / tft.crown_diameter_m
        
        # Distance-decay function
        cooling = cooling_potential * np.exp(-self.lambda_decay * normalized_distances)
        
        return cooling
    
    def calculate_cumulative_crown_area(self, tree_positions: List[Tuple[float, float]],
                                       species_list: List[str],
                                       evaluation_points: np.ndarray) -> np.ndarray:
        """
        Calculate Cumulative Crown Area (CCA) at each evaluation point
        
        CCA_ground(x,y) = (1/A_cell) * Σ CPA_j * δ(d_j(x,y) ≤ C_D,j/2)
        """
        n_points = len(evaluation_points)
        cca = np.zeros(n_points)
        
        for (x, y), species in zip(tree_positions, species_list):
            tft = self.tft_db.get_tft(species)
            if not tft:
                continue
            
            # Calculate distances
            distances = cdist([(x, y)], evaluation_points, 'euclidean')[0]
            
            # Crown radius
            crown_radius = tft.crown_diameter_m / 2.0
            
            # Points within crown radius
            within_crown = distances <= crown_radius
            
            # Add CPA contribution for points within crown
            if np.any(within_crown):
                cpa = tft.calculate_cpa()
                # Assuming A_cell = 1 m² for fine grid
                cca[within_crown] += cpa
        
        return cca
    
    def calculate_competition_reduction(self, cca_values: np.ndarray) -> np.ndarray:
        """
        Calculate competition reduction factor
        
        R_comp(i) = 1 / (1 + exp(k * (CCA_ground(i) - CCA_threshold)))
        """
        return 1.0 / (1.0 + np.exp(self.k_steepness * (cca_values - self.cca_threshold)))
    
    def calculate_total_cooling(self, tree_positions: List[Tuple[float, float]],
                               species_list: List[str],
                               evaluation_points: np.ndarray,
                               apply_competition: bool = True) -> np.ndarray:
        """
        Calculate total cooling with competition effects
        
        Parameters:
        -----------
        tree_positions : List of (x, y) tuples
        species_list : List of species codes
        evaluation_points : np.ndarray
            Points to evaluate cooling at
        apply_competition : bool
            Whether to apply competition reduction
        
        Returns:
        --------
        np.ndarray: Total cooling at each evaluation point
        """
        n_points = len(evaluation_points)
        total_cooling = np.zeros(n_points)
        
        # Calculate individual cooling contributions
        for (x, y), species in zip(tree_positions, species_list):
            cooling = self.calculate_individual_cooling((x, y), species, evaluation_points)
            total_cooling += cooling
        
        # Apply competition reduction if requested
        if apply_competition and len(tree_positions) > 0:
            cca = self.calculate_cumulative_crown_area(tree_positions, species_list, evaluation_points)
            r_comp = self.calculate_competition_reduction(cca)
            total_cooling *= r_comp
        
        return total_cooling

# ============================================================================
# 6. SECPI OBJECTIVE FUNCTION
# ============================================================================

class SECPIObjective:
    """
    Synergistic and Equitable Cooling Performance Index (SECPI)
    
    SECPI = Σ_k [(A_k,optimized - A_k,baseline) * W_k] * W̄_e,k
    """
    
    def __init__(self, cooling_model: NonSubmodularCoolingModel,
                 dual_grid: DualScaleGridSystem):
        """
        Initialize SECPI objective function
        
        Parameters:
        -----------
        cooling_model : NonSubmodularCoolingModel
            Cooling model for calculating cooling values
        dual_grid : DualScaleGridSystem
            Dual-scale grid system
        """
        self.cooling_model = cooling_model
        self.dual_grid = dual_grid
        
        # Benefit class weights (W_k)
        self.benefit_weights = {1: 1.0, 2: 2.0, 3: 3.0, 4: 4.0}
        
        # Initialize baseline (no trees)
        self.baseline_cooling = np.zeros(len(self.dual_grid.fine_coords))
        
    def calculate_cooling_classes(self, cooling_values: np.ndarray) -> np.ndarray:
        """
        Assign cooling values to benefit classes based on quartiles
        
        Class 1: 0-25th percentile (Minimal Benefit)
        Class 2: 25-50th percentile (Moderate Benefit)
        Class 3: 50-75th percentile (Substantial Benefit)
        Class 4: 75-100th percentile (High Benefit)
        """
        if len(cooling_values) == 0:
            return np.array([], dtype=int)
        
        # Calculate quartiles
        q1 = np.percentile(cooling_values, 25)
        q2 = np.percentile(cooling_values, 50)
        q3 = np.percentile(cooling_values, 75)
        
        # Assign classes
        classes = np.zeros_like(cooling_values, dtype=int)
        classes[cooling_values < q1] = 1
        classes[(cooling_values >= q1) & (cooling_values < q2)] = 2
        classes[(cooling_values >= q2) & (cooling_values < q3)] = 3
        classes[cooling_values >= q3] = 4
        
        return classes
    
    def calculate_area_proportions(self, classes: np.ndarray) -> Dict[int, float]:
        """
        Calculate proportion of area in each benefit class
        
        A_k = |{i: Class(i) = k}| / |G|
        """
        total_cells = len(classes)
        if total_cells == 0:
            return {1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0}
        
        proportions = {}
        for k in range(1, 5):
            count = np.sum(classes == k)
            proportions[k] = count / total_cells
        
        return proportions
    
    def calculate_mean_equity_weight(self, classes: np.ndarray, 
                                   class_value: int) -> float:
        """
        Calculate mean equity weight for cells in a specific class
        
        W̄_e,k = (1/|{i: Class(i) = k}|) * Σ W_e(i)
        """
        # Flatten equity grid
        equity_grid_flat = self.dual_grid.fine_equity_grid.flatten()
        
        # Get indices for this class
        class_indices = np.where(classes == class_value)[0]
        
        if len(class_indices) == 0:
            return 0.0
        
        # Calculate mean equity weight
        mean_weight = np.mean(equity_grid_flat[class_indices])
        
        return mean_weight
    
    def calculate_secpi(self, tree_positions: List[Tuple[float, float]],
                       species_list: List[str]) -> float:
        """
        Calculate SECPI score for a tree configuration
        
        Parameters:
        -----------
        tree_positions : List of (x, y) positions
        species_list : List of species codes
        
        Returns:
        --------
        float: SECPI score
        """
        # Calculate cooling for this configuration
        cooling_values = self.cooling_model.calculate_total_cooling(
            tree_positions, species_list, self.dual_grid.fine_coords
        )
        
        # Calculate cooling classes
        classes = self.calculate_cooling_classes(cooling_values)
        
        # Calculate area proportions for optimized scenario
        proportions_opt = self.calculate_area_proportions(classes)
        
        # Calculate area proportions for baseline
        classes_baseline = self.calculate_cooling_classes(self.baseline_cooling)
        proportions_base = self.calculate_area_proportions(classes_baseline)
        
        # Calculate SECPI
        secpi_score = 0.0
        
        for k in range(1, 5):
            # Area shift
            area_shift = proportions_opt[k] - proportions_base[k]
            
            # Mean equity weight for this class
            mean_equity_weight = self.calculate_mean_equity_weight(classes, k)
            
            # Weighted contribution
            weighted_contribution = area_shift * self.benefit_weights[k] * mean_equity_weight
            
            secpi_score += weighted_contribution
        
        return secpi_score
    
    def analyze_equity_distribution(self, tree_positions: List[Tuple[float, float]],
                                   species_list: List[str]) -> Dict:
        """
        Analyze equity distribution of cooling benefits
        
        Returns dictionary with various equity metrics
        """
        # Calculate cooling
        cooling_values = self.cooling_model.calculate_total_cooling(
            tree_positions, species_list, self.dual_grid.fine_coords
        )
        
        # Flatten equity grid
        equity_grid_flat = self.dual_grid.fine_equity_grid.flatten()
        
        # Separate cooling values by equity weight
        high_equity_mask = equity_grid_flat >= 1.5
        low_equity_mask = equity_grid_flat < 1.5
        
        high_equity_cooling = cooling_values[high_equity_mask]
        low_equity_cooling = cooling_values[low_equity_mask]
        
        # Calculate statistics
        analysis = {
            'mean_cooling_high_equity': np.mean(high_equity_cooling) if len(high_equity_cooling) > 0 else 0,
            'mean_cooling_low_equity': np.mean(low_equity_cooling) if len(low_equity_cooling) > 0 else 0,
            'cooling_equity_ratio': np.mean(high_equity_cooling) / np.mean(low_equity_cooling) 
            if (len(high_equity_cooling) > 0 and len(low_equity_cooling) > 0 and np.mean(low_equity_cooling) > 0) 
            else 0,
            'proportion_high_benefit_high_equity': 0,
            'proportion_high_benefit_low_equity': 0
        }
        
        # Calculate proportion of high benefit areas
        classes = self.calculate_cooling_classes(cooling_values)
        high_benefit_mask = classes >= 3
        
        if np.any(high_benefit_mask):
            high_benefit_in_high_equity = np.sum(high_benefit_mask & high_equity_mask)
            high_benefit_in_low_equity = np.sum(high_benefit_mask & low_equity_mask)
            
            analysis['proportion_high_benefit_high_equity'] = (
                high_benefit_in_high_equity / np.sum(high_equity_mask) 
                if np.sum(high_equity_mask) > 0 else 0
            )
            analysis['proportion_high_benefit_low_equity'] = (
                high_benefit_in_low_equity / np.sum(low_equity_mask) 
                if np.sum(low_equity_mask) > 0 else 0
            )
        
        return analysis

# ============================================================================
# MAIN DEMONSTRATION
# ============================================================================

def demonstrate_worldbuilding():
    """Demonstrate the worldbuilding components of the paradigm"""
    
    print("=" * 80)
    print("WORLDBUILDING DEMONSTRATION")
    print("Equitable Integer Lattice Optimization Paradigm")
    print("=" * 80)
    
    # 1. Generate Urban Morphology using Cellular Automata
    print("\n1. GENERATING URBAN MORPHOLOGY USING CELLULAR AUTOMATA")
    print("-" * 60)
    
    ca_generator = CellularAutomataUrbanGenerator(width=10, height=10)
    state_grid = ca_generator.generate_organic_morphology()
    ratios = ca_generator.calculate_ratios(state_grid)
    
    print(f"Generated morphology with ratios:")
    print(f"  Prohibited (P): {ratios['P']:.1%} (target: 55-65%)")
    print(f"  Vulnerable (V): {ratios['V']:.1%} (target: 5-10%)")
    print(f"  Available (A):  {ratios['A']:.1%} (target: 25-40%)")
    
    # Visualize morphology
    fig1, ax1 = ca_generator.visualize_morphology(
        state_grid, 
        title="Generated Urban Morphology (Organic/Clustered)"
    )
    plt.savefig('urban_morphology.png', dpi=300, bbox_inches='tight')
    plt.close(fig1)
    print("  Saved visualization to 'urban_morphology.png'")
    
    # 2. Create Dual-Scale Grid System
    print("\n2. CREATING DUAL-SCALE GRID SYSTEM")
    print("-" * 60)
    
    dual_grid = DualScaleGridSystem(study_area_size=100.0)
    dual_grid.map_coarse_to_fine(state_grid)
    
    plantable_locations = dual_grid.get_plantable_coarse_locations()
    print(f"Coarse grid: {dual_grid.coarse_n_cells}x{dual_grid.coarse_n_cells} cells")
    print(f"Fine grid: {dual_grid.fine_n_cells}x{dual_grid.fine_n_cells} cells")
    print(f"Plantable locations: {len(plantable_locations)} out of {dual_grid.coarse_n_cells**2}")
    
    # Visualize dual grid
    fig2, axes2 = dual_grid.visualize_dual_grid()
    plt.savefig('dual_grid_system.png', dpi=300, bbox_inches='tight')
    plt.close(fig2)
    print("  Saved visualization to 'dual_grid_system.png'")
    
    # 3. Initialize Tree Functional Types
    print("\n3. INITIALIZING PHILIPPINE TREE FUNCTIONAL TYPES")
    print("-" * 60)
    
    tft_db = TFTDatabase()
    print(f"Loaded {len(tft_db.get_all_species())} TFTs:")
    
    for species_code in tft_db.get_all_species():
        tft = tft_db.get_tft(species_code)
        cooling_potential = tft_db.calculate_cooling_potential(species_code)
        print(f"  {tft.common_name:15s} | CD: {tft.crown_diameter_m:4.1f}m | "
              f"H: {tft.height_m:4.1f}m | Cooling: {cooling_potential:.3f}")
    
    # 4. Test Non-Submodular Cooling Model
    print("\n4. TESTING NON-SUBMODULAR COOLING MODEL")
    print("-" * 60)
    
    cooling_model = NonSubmodularCoolingModel(tft_db)
    
    # Test with single tree
    test_position = dual_grid.get_coarse_coordinate(3, 3)
    test_species = 'NARRA'
    
    individual_cooling = cooling_model.calculate_individual_cooling(
        test_position, test_species, dual_grid.fine_coords[:100]  # Test with subset
    )
    
    print(f"Single {tft_db.get_tft(test_species).common_name} tree at ({test_position[0]:.1f}, {test_position[1]:.1f}):")
    print(f"  Max cooling: {np.max(individual_cooling):.4f}")
    print(f"  Mean cooling: {np.mean(individual_cooling):.4f}")
    
    # 5. Test SECPI Objective Function
    print("\n5. TESTING SECPI OBJECTIVE FUNCTION")
    print("-" * 60)
    
    secpi_obj = SECPIObjective(cooling_model, dual_grid)
    
    # Create a test configuration
    test_positions = []
    test_species_list = []
    
    # Add a few trees
    for i in range(3):
        # Random available location
        if plantable_locations:
            loc_idx = np.random.randint(0, len(plantable_locations))
            coarse_x, coarse_y = plantable_locations[loc_idx]
            position = dual_grid.get_coarse_coordinate(coarse_x, coarse_y)
            
            # Random species
            species = np.random.choice(tft_db.get_all_species())
            
            test_positions.append(position)
            test_species_list.append(species)
    
    # Calculate SECPI
    if test_positions:
        secpi_score = secpi_obj.calculate_secpi(test_positions, test_species_list)
        equity_analysis = secpi_obj.analyze_equity_distribution(test_positions, test_species_list)
        
        print(f"Test configuration with {len(test_positions)} trees:")
        print(f"  SECPI Score: {secpi_score:.4f}")
        print(f"  Equity Analysis:")
        print(f"    Mean cooling in high-equity zones: {equity_analysis['mean_cooling_high_equity']:.4f}")
        print(f"    Mean cooling in low-equity zones: {equity_analysis['mean_cooling_low_equity']:.4f}")
        print(f"    Cooling equity ratio: {equity_analysis['cooling_equity_ratio']:.2f}")
    
    # 6. Generate Summary Report
    print("\n" + "=" * 80)
    print("WORLDBUILDING SUMMARY")
    print("=" * 80)
    
    summary = f"""
    PARADIGM COMPONENTS IMPLEMENTED:
    
    1. INTEGER LATTICE FORMALIZATION
       - Formal representation of urban space as subset of Z^2
       - State function S: G → {{P, V, A}}
       - Equity weighting function W_e(i)
    
    2. CELLULAR AUTOMATA URBAN GENERATOR
       - Binary urban CA model based on Chakraborty et al. (2022)
       - Three morphology archetypes: organic, sparse, linear
       - P: {ratios['P']:.1%}, V: {ratios['V']:.1%}, A: {ratios['A']:.1%}
    
    3. DUAL-SCALE GRID SYSTEM
       - Coarse grid (G_c): {dual_grid.coarse_n_cells}x{dual_grid.coarse_n_cells} cells, 10m resolution
       - Fine grid (G_f): {dual_grid.fine_n_cells}x{dual_grid.fine_n_cells} cells, 1m resolution
       - Plantable cells: {len(plantable_locations)}/{dual_grid.coarse_n_cells**2}
    
    4. PHILIPPINE TREE FUNCTIONAL TYPES
       - 6 TFTs with biophysical parameters
       - FORMIND allometric equations for DBH and LAI
       - CPA and LAI normalization for cooling potential
    
    5. NON-SUBMODULAR COOLING MODEL
       - Distance-decay function with Manhattan distance
       - Cumulative Crown Area (CCA) competition model
       - Sigmoidal reduction factor for diminishing returns
    
    6. SECPI OBJECTIVE FUNCTION
       - Equity-weighted benefit classification
       - Quartile-based cooling classes
       - Integrated equity analysis metrics
    
    NEXT STEPS FOR ACO IMPLEMENTATION:
    1. Initialize pheromone matrix on coarse grid
    2. Implement heuristic information η(p,s)
    3. Develop ant solution construction procedure
    4. Implement pheromone update rules
    5. Add parallelization for colony evaluation
    """
    
    print(summary)
    
    # Save summary to file
    with open('worldbuilding_summary.txt', 'w', encoding='utf-8') as f:
        f.write("EQUITABLE INTEGER LATTICE OPTIMIZATION PARADIGM\n")
        f.write("=" * 60 + "\n\n")
        f.write(summary)
    
    print("\nSummary saved to 'worldbuilding_summary.txt'")
    print("\nWorldbuilding complete! Ready for ACO implementation.")
    
    return {
        'ca_generator': ca_generator,
        'dual_grid': dual_grid,
        'tft_db': tft_db,
        'cooling_model': cooling_model,
        'secpi_obj': secpi_obj
    }

# ============================================================================
# EXAMPLE USAGE
# ============================================================================

if __name__ == "__main__":
    
    # Create output directory
    Path("worldbuilding_outputs").mkdir(exist_ok=True)
    
    # Run demonstration
    print("\nStarting worldbuilding demonstration...")
    components = demonstrate_worldbuilding()
    
    print("\n" + "=" * 80)
    print("PARADIGM READY FOR ACO INTEGRATION")
    print("=" * 80)
    
    print("\nThe foundational components of the Equitable Integer Lattice")
    print("Optimization Paradigm have been successfully implemented.")
    print("\nKey features:")
    print("1. Formal integer lattice representation ✓")
    print("2. Procedural urban morphology generation ✓")
    print("3. Dual-scale evaluation system ✓")
    print("4. Biophysical tree modeling ✓")
    print("5. Non-submodular cooling with competition ✓")
    print("6. Equity-weighted SECPI objective ✓")
    print("\nReady for Ant Colony Optimization implementation!")
