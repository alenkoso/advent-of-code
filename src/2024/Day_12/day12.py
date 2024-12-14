import sys
import os
import time
from collections import deque

project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(project_root)

from helpers.parsing_utils import read_input_file_to_grid

def count_region_sides_part1(region_cells):
    # Perimeter counting for Part 1
    perimeter = 0
    for cell_row, cell_column in region_cells:
        boundary_directions = [
            (cell_row+1, cell_column),  # down
            (cell_row-1, cell_column),  # up
            (cell_row, cell_column+1),  # right
            (cell_row, cell_column-1)   # left
        ]
        
        for boundary_row, boundary_column in boundary_directions:
            if (boundary_row, boundary_column) not in region_cells:
                perimeter += 1
    
    return perimeter

def count_region_sides_part2(region_cells):
    # Side counting for Part 2
    unique_sides = set()
    min_row = min(r for r, _ in region_cells)
    max_row = max(r for r, _ in region_cells)
    min_col = min(c for _, c in region_cells)
    max_col = max(c for _, c in region_cells)

    # Track side points for each direction
    side_points = {
        'top': set(),
        'bottom': set(),
        'left': set(),
        'right': set()
    }

    for cell_row, cell_column in region_cells:
        # Check boundary conditions
        if cell_row == min_row:
            side_points['top'].add(cell_column)
        if cell_row == max_row:
            side_points['bottom'].add(cell_column)
        if cell_column == min_col:
            side_points['left'].add(cell_row)
        if cell_column == max_col:
            side_points['right'].add(cell_row)

    # Count unique sides
    side_count = (len(side_points['top']) > 0) + \
                 (len(side_points['bottom']) > 0) + \
                 (len(side_points['left']) > 0) + \
                 (len(side_points['right']) > 0)

    return side_count

def solve_landscape(terrain_grid, is_part2=False):
    terrain_height = len(terrain_grid)
    terrain_width = len(terrain_grid[0])
    explored_cells = set()
    total_landscape_value = 0

    def explore_terrain_region(start_row, start_column, terrain_type):
        # Flood fill to find connected region
        terrain_region = set()
        cell_exploration_queue = deque([(start_row, start_column)])
        
        while cell_exploration_queue:
            current_row, current_column = cell_exploration_queue.popleft()
            
            if ((current_row, current_column) in explored_cells or 
                current_row < 0 or current_row >= terrain_height or 
                current_column < 0 or current_column >= terrain_width or 
                terrain_grid[current_row][current_column] != terrain_type):
                continue
            
            explored_cells.add((current_row, current_column))
            terrain_region.add((current_row, current_column))
            
            # Explore adjacent cells in four directions
            adjacent_directions = [
                (current_row+1, current_column), 
                (current_row-1, current_column), 
                (current_row, current_column+1), 
                (current_row, current_column-1)
            ]
            cell_exploration_queue.extend(adjacent_directions)
        
        return terrain_region

    for terrain_row in range(terrain_height):
        for terrain_column in range(terrain_width):
            if (terrain_row, terrain_column) not in explored_cells:
                current_terrain_type = terrain_grid[terrain_row][terrain_column]
                terrain_region = explore_terrain_region(terrain_row, terrain_column, current_terrain_type)
                
                region_area = len(terrain_region)
                
                # Different side counting for Part 1 and Part 2
                if is_part2:
                    region_sides = count_region_sides_part2(terrain_region)
                else:
                    region_sides = count_region_sides_part1(terrain_region)
                
                total_landscape_value += region_area * region_sides

    return total_landscape_value

def main():
    # Part 1
    start_time = time.time()
    terrain_grid = read_input_file_to_grid("input.txt")
    part1_result = solve_landscape(terrain_grid, is_part2=False)
    end_time = time.time()
    print(f"Part 1: {part1_result}")
    print(f"Part 1 Execution Time: {end_time - start_time} seconds")

    # Part 2
    start_time = time.time()
    part2_result = solve_landscape(terrain_grid, is_part2=True)
    end_time = time.time()
    print(f"Part 2: {part2_result}")
    print(f"Part 2 Execution Time: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()