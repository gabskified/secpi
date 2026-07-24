import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from scipy.signal import convolve2d
import random

# ==========================================
# 1. CONFIGURATION & PARAMETERS
# ==========================================

# Grid Definitions
GRID_H, GRID_W = 100, 100  # Size of G_c (m x n)

# State Definitions
STATE_A = 0  # Available (Plantable) - Light Gray
STATE_P = 1  # Prohibited (Buildings) - Dark Gray
STATE_V = 2  # Vulnerable (Schools/Hospitals) - Red

# Morphological Archetypes
ARCHETYPES = {
    'organic_cluster': {
        'p_init': 0.05, 'theta': 3, 'alpha': 0.01, 
        'beta': 0.2, 't_max': 30, 'bias_axis': None
    },
    'sparse_suburban': {
        'p_init': 0.02, 'theta': 5, 'alpha': 0.005, 
        'beta': 0.1, 't_max': 40, 'bias_axis': None
    },
    'linear_corridor': {
        'p_init': 0.03, 'theta': 4, 'alpha': 0.02, 
        'beta': 0.15, 't_max': 35, 'bias_axis': 'y' # Biased along Y-axis (vertical strip)
    }
}

# Select Archetype here
CURRENT_ARCHETYPE = 'organic_cluster' 
PARAMS = ARCHETYPES[CURRENT_ARCHETYPE]

# ==========================================
# 2. CORE FUNCTIONS
# ==========================================

def initialize_grid(rows, cols, params):
    """
    Initializes the grid with seed 'P' cells based on density.
    Handles spatial biasing for specific archetypes.
    """
    grid = np.zeros((rows, cols), dtype=int)
    
    # Generate random mask
    random_mask = np.random.random((rows, cols))
    
    # Apply Biasing if required (e.g., Linear Corridor)
    if params.get('bias_axis') == 'y':
        # Create a probability gradient or hard mask centered on the vertical axis
        center_col = cols // 2
        width = cols // 5
        # Only allow seeds in the central strip
        spatial_mask = np.zeros((rows, cols), dtype=bool)
        spatial_mask[:, center_col-width : center_col+width] = True
        
        # Combine random chance with spatial restriction
        seeds = (random_mask < params['p_init']) & spatial_mask
    else:
        # Uniform random seeding
        seeds = random_mask < params['p_init']
        
    grid[seeds] = STATE_P
    return grid

def count_neighbors(grid):
    """
    Counts 'P' neighbors using convolution (Moore Neighborhood).
    """
    # Kernel for 8 neighbors (Moore)
    kernel = np.array([[1, 1, 1],
                       [1, 0, 1],
                       [1, 1, 1]])
    
    # Create a binary mask where P exists (1 if P, 0 otherwise)
    p_mask = (grid == STATE_P).astype(int)
    
    # Convolve to count neighbors
    neighbor_counts = convolve2d(p_mask, kernel, mode='same', boundary='fill', fillvalue=0)
    return neighbor_counts

def ca_step(grid, params):
    """
    Executes one iteration of the CA Transition Rule.
    """
    new_grid = grid.copy()
    rows, cols = grid.shape
    
    # Get neighbor counts
    n_p = count_neighbors(grid)
    
    # Calculate transition probabilities
    # Formula: alpha + beta * (N_P / 8)
    prob_transition = params['alpha'] + params['beta'] * (n_p / 8.0)
    
    # Generate random rolls
    rolls = np.random.random((rows, cols))
    
    # Determine which cells define the criteria:
    # 1. Must currently be empty (State A / 0)
    # 2. Neighbors >= Theta
    # 3. Random roll < Probability
    
    candidates = (grid == STATE_A) & (n_p >= params['theta'])
    transitions = candidates & (rolls < prob_transition)
    
    # Apply transitions
    new_grid[transitions] = STATE_P
    
    return new_grid

def assign_vulnerable_zones(grid, num_zones=3, radius=3):
    """
    Post-process: Places 'V' zones.
    Strategy: Places V zones near the centroid of dense urban clusters,
    overwriting existing P or A cells.
    """
    final_grid = grid.copy()
    rows, cols = grid.shape
    
    # Simple logic: Pick random 'P' cells to serve as "anchors" for V zones
    # (Simulating finding a dense neighborhood)
    p_indices = np.argwhere(final_grid == STATE_P)
    
    if len(p_indices) > 0:
        # Pick 'num_zones' random anchors from existing buildings
        anchors = p_indices[np.random.choice(len(p_indices), size=min(len(p_indices), num_zones), replace=False)]
        
        for r_c, c_c in anchors:
            # Create a circular blob around the anchor
            y, x = np.ogrid[-r_c:rows-r_c, -c_c:cols-c_c]
            mask = x*x + y*y <= radius*radius
            
            # Apply V state within radius (can overwrite P or A)
            final_grid[mask] = STATE_V
            
    return final_grid

# ==========================================
# 3. SIMULATION LOOP & VISUALIZATION
# ==========================================

def run_simulation():
    # 1. Init
    G_c = initialize_grid(GRID_H, GRID_W, PARAMS)
    t_max = PARAMS['t_max']
    
    # Checkpoints for visualization
    checkpoints = {
        0: None, 
        t_max // 4: None, 
        t_max // 2: None, 
        (3 * t_max) // 4: None, 
        t_max: None
    }
    
    # Store Initial State
    checkpoints[0] = G_c.copy()
    
    # 2. Iterate
    print(f"Starting Simulation: {CURRENT_ARCHETYPE} (T={t_max})")
    for t in range(1, t_max + 1):
        G_c = ca_step(G_c, PARAMS)
        
        if t in checkpoints:
            checkpoints[t] = G_c.copy()
            
    # 3. Post-Process (Assign V)
    # Apply only to the final frame
    final_grid = assign_vulnerable_zones(checkpoints[t_max], num_zones=5, radius=4)
    checkpoints[t_max] = final_grid # Update final frame with V zones
    
    # 4. Visualization
    plot_results(checkpoints)

def plot_results(checkpoints):
    """
    Plots the grid at specific time steps.
    """
    # Color Map Definition
    # 0: A (Light Gray), 1: P (Dark Gray), 2: V (Red)
    cmap = colors.ListedColormap(['#E6E6E6', '#333333', '#E74C3C'])
    bounds = [-0.5, 0.5, 1.5, 2.5]
    norm = colors.BoundaryNorm(bounds, cmap.N)
    
    sorted_keys = sorted(checkpoints.keys())
    fig, axes = plt.subplots(1, 5, figsize=(20, 5))
    
    for i, t in enumerate(sorted_keys):
        ax = axes[i]
        grid = checkpoints[t]
        
        # Plot matrix
        ax.imshow(grid, cmap=cmap, norm=norm, interpolation='nearest')
        
        # Styling
        title = f"Iteration: {t}"
        if i == len(sorted_keys) - 1:
            title += "\n(Post-Processed)"
        
        ax.set_title(title, fontsize=12, fontweight='bold')
        ax.axis('off') # Hide axis ticks
        
        # Save individual frames (Optional)
        # plt.imsave(f'frame_{t}.png', grid, cmap=cmap)

    plt.suptitle(f"Morphological Archetype: {CURRENT_ARCHETYPE.replace('_', ' ').upper()}", fontsize=16)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    run_simulation()

