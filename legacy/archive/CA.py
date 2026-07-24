"""
PARADIGM: Cellular Automata for Synthetic Urban Testbed Generation (Pre-ACO Stage)

Complete implementation with enhanced clustering and visualization.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from scipy.ndimage import label, center_of_mass
import os
import imageio
import matplotlib as mpl

# Set professional font
mpl.rcParams['font.family'] = 'DejaVu Sans'
mpl.rcParams['font.size'] = 10

# --- 1. INITIALIZATION ---
def initialize_grid(m, n, params):
    """
    Creates the initial coarse grid G_c with random P-cell seeds.
    
    Args:
        m, n: Grid dimensions
        params: Dictionary with CA parameters including 'p_init' and optional 'bias_axis'
    
    Returns:
        Initial grid with 0 (empty) and 1 (P cells)
    """
    grid = np.zeros((m, n), dtype=np.int8)
    
    # Apply spatial bias for linear corridor morphology
    if 'bias_axis' in params:
        if params['bias_axis'] == 'y':
            # Concentrate initial seeds along vertical center
            center_col = n // 2
            for i in range(m):
                for j in range(n):
                    # Higher probability near center column
                    distance_from_center = abs(j - center_col) / (n / 2)
                    adjusted_p = params['p_init'] * (1 - 0.7 * distance_from_center)
                    if np.random.random() < adjusted_p:
                        grid[i, j] = 1
        elif params['bias_axis'] == 'x':
            # Concentrate along horizontal center
            center_row = m // 2
            for i in range(m):
                for j in range(n):
                    distance_from_center = abs(i - center_row) / (m / 2)
                    adjusted_p = params['p_init'] * (1 - 0.7 * distance_from_center)
                    if np.random.random() < adjusted_p:
                        grid[i, j] = 1
    else:
        # Uniform random seeding
        initial_seeds = np.random.random((m, n)) < params['p_init']
        grid[initial_seeds] = 1
    
    return grid


# --- 2. CORE CA TRANSITION FUNCTION ---
def apply_ca_rule(grid, params):
    """
    Applies one iteration of the CA transition rule.
    
    Rule: A non-P cell becomes P with probability:
          p_transition = alpha + beta * (N_P / 8)
          if N_P >= theta (threshold number of P neighbors)
    
    Args:
        grid: Current grid state
        params: Dictionary with 'theta', 'alpha', 'beta'
    
    Returns:
        Updated grid after one iteration
    """
    m, n = grid.shape
    new_grid = grid.copy()
    
    # Moore neighborhood offsets (8 neighbors)
    neighbors_offsets = [(-1, -1), (-1, 0), (-1, 1),
                         (0, -1),           (0, 1),
                         (1, -1),  (1, 0),  (1, 1)]
    
    for i in range(1, m - 1):  # Avoid edge cells
        for j in range(1, n - 1):
            # Only consider non-P cells for transition
            if grid[i, j] != 1:
                # Count P neighbors
                neighbor_count = 0
                for di, dj in neighbors_offsets:
                    if grid[i + di, j + dj] == 1:
                        neighbor_count += 1
                
                # Apply probabilistic transition rule
                if neighbor_count >= params['theta']:
                    p_transition = params['alpha'] + params['beta'] * (neighbor_count / 8.0)
                    if np.random.random() < p_transition:
                        new_grid[i, j] = 1
    
    return new_grid


# --- 3. POST-PROCESSING: ASSIGN VULNERABLE ZONES ---
def assign_vulnerable_zones(grid, num_zones=3, radius=1):
    """
    Assigns Vulnerable (V) zones based on urban cluster centroids.
    
    Strategy: Find connected components of P cells, identify largest clusters,
    place V zones at their centroids representing high-priority areas.
    
    Args:
        grid: Final CA grid with P cells
        num_zones: Number of V zones to create
        radius: Radius of influence for each V zone
    
    Returns:
        Grid with V cells (value=2) added
    """
    m, n = grid.shape
    v_grid = grid.copy()
    
    # Find connected components (clusters) of P cells
    binary_p = (grid == 1).astype(int)
    labeled_array, num_features = label(binary_p)
    
    # Calculate cluster sizes and centroids
    cluster_info = []
    for cluster_id in range(1, num_features + 1):
        cluster_mask = (labeled_array == cluster_id)
        cluster_size = np.sum(cluster_mask)
        if cluster_size > 5:  # Only consider substantial clusters
            centroid = center_of_mass(cluster_mask)
            cluster_info.append((cluster_size, centroid, cluster_id))
    
    # Sort by size (largest first) and select top clusters
    cluster_info.sort(reverse=True, key=lambda x: x[0])
    
    zones_placed = 0
    for _, (cy, cx), _ in cluster_info[:num_zones]:
        cy, cx = int(cy), int(cx)
        
        # Create circular V zone around centroid
        for i in range(max(0, cy - radius), min(m, cy + radius + 1)):
            for j in range(max(0, cx - radius), min(n, cx + radius + 1)):
                distance = np.sqrt((i - cy)**2 + (j - cx)**2)
                if distance <= radius and v_grid[i, j] == 0:  # Only on plantable cells
                    v_grid[i, j] = 2
        
        zones_placed += 1
        if zones_placed >= num_zones:
            break
    
    # If not enough large clusters, place remaining zones strategically
    while zones_placed < num_zones:
        # Find areas far from existing P cells
        max_distance = 0
        best_pos = None
        for _ in range(50):  # Sample 50 random positions
            y, x = np.random.randint(radius, m - radius), np.random.randint(radius, n - radius)
            if v_grid[y, x] == 0:
                # Calculate minimum distance to nearest P cell
                min_dist_to_p = float('inf')
                for i in range(max(0, y - 2), min(m, y + 2)):
                    for j in range(max(0, x - 2), min(n, x + 2)):
                        if v_grid[i, j] == 1:
                            dist = np.sqrt((i - y)**2 + (j - x)**2)
                            min_dist_to_p = min(min_dist_to_p, dist)
                
                if min_dist_to_p > max_distance:
                    max_distance = min_dist_to_p
                    best_pos = (y, x)
        
        if best_pos:
            cy, cx = best_pos
            for i in range(max(0, cy - radius), min(m, cy + radius + 1)):
                for j in range(max(0, cx - radius), min(n, cx + radius + 1)):
                    distance = np.sqrt((i - cy)**2 + (j - cx)**2)
                    if distance <= radius and v_grid[i, j] == 0:
                        v_grid[i, j] = 2
            zones_placed += 1
        else:
            break
    
    return v_grid


# --- 4. VISUALIZATION FUNCTION ---
def visualize_grid(ax, grid, iteration, title_suffix=""):
    """
    Plots a single grid state with appropriate colormap.
    
    Color scheme:
    - A (Plantable): Light Green #90EE90
    - P (Prohibited): Dark Gray #4D4D4D  
    - V (Vulnerable): Red #E74C3C
    """
    cmap = colors.ListedColormap(['#90EE90', '#4D4D4D', '#E74C3C'])
    bounds = [-0.5, 0.5, 1.5, 2.5]
    norm = colors.BoundaryNorm(bounds, cmap.N)
    
    ax.imshow(grid, cmap=cmap, norm=norm, interpolation='none', origin='lower')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(f"Iteration {iteration} {title_suffix}", fontsize=11, fontweight='bold')
    ax.set_aspect('equal')
    
    # Add subtle grid lines
    ax.grid(False)


# --- 5. SAVE INDIVIDUAL FRAMES ---
def save_frame(grid, iteration, morphology, output_dir='frames'):
    """
    Saves individual frame as PNG for potential video creation.
    """
    os.makedirs(output_dir, exist_ok=True)
    
    fig, ax = plt.subplots(1, 1, figsize=(6, 6))
    visualize_grid(ax, grid, iteration)
    plt.tight_layout()
    plt.savefig(f'{output_dir}/{morphology}_iter_{iteration:04d}.png', 
                dpi=150, bbox_inches='tight')
    plt.close(fig)


# --- 6. MAIN EXECUTION ---
def main():
    """
    Main execution: Generate CA urban morphology with visualization.
    """
    # Removed fixed seed for procedural generation
    # np.random.seed(42)
    
    # Choose morphology archetype
    morphology = 'organic_cluster'  # Options: 'organic_cluster', 'sparse_suburban', 'linear_corridor'
    
    # Adjusted parameters for desired ratios
    params = {
        'm': 10, 'n': 10,
        'p_init': 0.05,  # Lower for more spread out initial P cells
        'theta': 3,      # Threshold for growth
        'alpha': 0.03,   # Base probability
        'beta': 0.15,    # Neighbor influence
        'num_v_zones': 2, # Zones for V cells
        'radius': 2      # Larger radius for V zones
    }
    
    print(f"Generating '{morphology.replace('_', ' ').title()}' morphology...")
    print(f"Grid: {params['m']}x{params['n']}, Target Ratios: P 55-65%, V 5-10%, A 25-50%")
    
    # Initialize grid
    G_c = initialize_grid(params['m'], params['n'], params)
    
    iteration = 0
    max_iterations = 200  # Safety limit
    total_cells = params['m'] * params['n']
    
    while iteration < max_iterations:
        iteration += 1
        G_c = apply_ca_rule(G_c, params)
        
        # Save frame for gif
        save_frame(G_c, iteration, morphology)
        
        # Calculate P percentage
        p_count = np.sum(G_c == 1)
        p_percent = p_count / total_cells * 100
        
        print(f"Iteration {iteration}: P={p_percent:.1f}%")
        
        # Check if P is within range
        if 55 <= p_percent <= 65:
            print("P ratio achieved, assigning V zones...")
            break
    
    # Assign vulnerable zones once at the end
    G_c_with_v = assign_vulnerable_zones(G_c, num_zones=params['num_v_zones'], radius=params['radius'])
    
    # Calculate final percentages
    total_cells = G_c_with_v.size
    p_count = np.sum(G_c_with_v == 1)
    v_count = np.sum(G_c_with_v == 2)
    a_count = np.sum(G_c_with_v == 0)
    p_percent = p_count / total_cells * 100
    v_percent = v_count / total_cells * 100
    a_percent = a_count / total_cells * 100
    
    print(f"Final: P={p_percent:.1f}%, V={v_percent:.1f}%, A={a_percent:.1f}%")
    
    # Check if all ratios are satisfied
    ratios_ok = (55 <= p_percent <= 65 and 
                 5 <= v_percent <= 10 and 
                 25 <= a_percent <= 50)
    if ratios_ok:
        print("All target ratios achieved!")
    else:
        print("Ratios not fully achieved, but proceeding...")
    
    # Create gif from saved frames
    print("Creating evolution gif...")
    try:
        images = []
        for i in range(1, iteration + 1):
            frame_path = f'frames/{morphology}_iter_{i:04d}.png'
            if os.path.exists(frame_path):
                images.append(imageio.v2.imread(frame_path))
        gif_path = f'{morphology}_evolution.gif'
        if os.path.exists(gif_path):
            os.remove(gif_path)
        imageio.mimsave(gif_path, images, fps=5)
        print(f"Saved gif: {gif_path}")
    except Exception as e:
        print(f"Error creating gif: {e}")
        print("Continuing without gif...")
    
    # Create final visualization
    fig, ax = plt.subplots(1, 1, figsize=(6, 6))
    visualize_grid(ax, G_c_with_v, iteration, "Final with Target Ratios")
    plt.suptitle(f"CA Urban Morphology: {morphology.replace('_', ' ').title()}", 
                 fontsize=16, fontweight='bold', y=1.02)
    plt.tight_layout()
    output_filename = f'ca_generation_{morphology}.png'
    plt.savefig(output_filename, dpi=200, bbox_inches='tight')
    print(f"Saved visualization: {output_filename}")
    # plt.show()  # Removed to avoid blocking in terminal
    
    # Final statistics
    print("\n" + "="*60)
    print("FINAL GRID STATISTICS")
    print("="*60)
    print(f"Grid Shape: {G_c_with_v.shape}")
    print(f"Total Cells: {G_c_with_v.size}")
    print(f"  A (Plantable):  {a_count:4d} cells ({a_percent:.1f}%)")
    print(f"  P (Prohibited): {p_count:4d} cells ({p_percent:.1f}%)")
    print(f"  V (Vulnerable): {v_count:4d} cells ({v_percent:.1f}%)")
    print("="*60)
    print(f"\n✓ Grid ready for ACO-based tree planting optimization!")
    
    return G_c_with_v


if __name__ == "__main__":
    final_grid = main()