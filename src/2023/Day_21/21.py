from collections import deque
import os
import sys

project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(project_root)

from helpers.parsing_utils import read_input_file_to_grid

def find_start_position(grid):
    # Finds the start position marked as 'S' in the grid.
    for row_index, row in enumerate(grid):
        if 'S' in row:
            return row_index, row.index('S')  # (start_row, start_col)
    return None

def calculate_distances(grid, start_position):
    # Calculates the distances from the start position to all reachable positions.
    distance_map = {}
    queue = deque([(0, 0, start_position[0], start_position[1], 0)])  # (temp_row, temp_col, current_col, current_row, distance)
    row_count, col_count = len(grid), len(grid[0])

    while queue:
        temp_row, temp_col, current_col, current_row, distance = queue.popleft()
        # Adjust column and row with wrapping
        current_col, temp_row = (current_col + col_count) % col_count, temp_row + (current_col // col_count)
        current_row, temp_col = (current_row + row_count) % row_count, temp_col + (current_row // row_count)
        
        if (temp_row, temp_col, current_row, current_col) in distance_map or abs(temp_row) > 4 or abs(temp_col) > 4:
            continue
        
        if grid[current_row][current_col] != '#':  # Check if not a wall
            distance_map[(temp_row, temp_col, current_row, current_col)] = distance
            for delta_row, delta_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Check all four directions
                queue.append((temp_row, temp_col, current_col + delta_col, current_row + delta_row, distance + 1))
    return distance_map

def calculate_reachable_plots(distance_map, step_limit, row_count, col_count):
    # Calculates the number of reachable plots within a given step limit.
    def get_reach_count(distance, variant, step_limit, row_count, col_count):
        amount = (step_limit - distance) // max(row_count, col_count)
        return sum(((x + 1) if variant == 2 else 1) for x in range(1, amount + 1) if (distance + max(row_count, col_count) * x) <= step_limit and (distance + max(row_count, col_count) * x) % 2 == (step_limit % 2))

    reachable_plots = 0
    for (temp_row, temp_col, current_row, current_col), distance in distance_map.items():
        if distance % 2 == step_limit % 2 and distance <= step_limit:
            reachable_plots += 1
        if temp_row in [-3, -2, -1, 0, 1, 2, 3] and temp_col in [-3, -2, -1, 0, 1, 2, 3]:
            if temp_row in [-3, 3] and temp_col in [-3, 3]:
                reachable_plots += get_reach_count(distance, 2, step_limit, row_count, col_count)
            elif temp_row in [-3, 3] or temp_col in [-3, 3]:
                reachable_plots += get_reach_count(distance, 1, step_limit, row_count, col_count)

    return reachable_plots

def main():
    grid = read_input_file_to_grid("input.txt")
    start_position = find_start_position(grid)
    distances = calculate_distances(grid, start_position)
    row_count, col_count = len(grid), len(grid[0])

    # Part 1
    print(f"Part 1 - Reachable plots in 64 steps: {calculate_reachable_plots(distances, 64, row_count, col_count)}")

    # Part 2
    print(f"Part 2 - Reachable plots in 26501365 steps: {calculate_reachable_plots(distances, 26501365, row_count, col_count)}")

if __name__ == "__main__":
    main()