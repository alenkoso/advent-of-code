import os
import sys
import time
from helpers.file_utils import read_input_file


project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(project_root)

def read_input(file_path):
    with open(file_path, 'r') as file:
        return [list(line.strip()) for line in file.readlines()]

def rotate_grid(grid):
    ### Rotate the grid 90 degrees clockwise. ###
    num_rows = len(grid)
    num_cols = len(grid[0])
    new_grid = [['?' for _ in range(num_rows)] for _ in range(num_cols)]
    for row in range(num_rows):
        for col in range(num_cols):
            new_grid[col][num_rows - 1 - row] = grid[row][col]
    return new_grid

def roll_rocks(grid):
    ### Roll the rounded rocks down as far as possible. ###
    num_rows = len(grid)
    num_cols = len(grid[0])
    for col in range(num_cols):
        for _ in range(num_rows):
            for row in range(num_rows):
                if grid[row][col] == 'O' and row > 0 and grid[row - 1][col] == '.':
                    grid[row][col], grid[row - 1][col] = grid[row - 1][col], grid[row][col]
    return grid

def calculate_load(grid):
    ### Calculate the total load on the support beams. ###
    load = 0
    num_rows = len(grid)
    for row in range(num_rows):
        load += sum(1 for cell in grid[row] if cell == 'O') * (num_rows - row)
    return load

def calculate_load_after_cycles(grid, target_cycles):
    ### Calculate load after a given number of cycles. ###
    time_step = 0
    seen_grids = {}
    while time_step < target_cycles:
        time_step += 1
        for _ in range(4):
            roll_rocks(grid)
            grid = rotate_grid(grid)

        grid_hash = tuple(tuple(row) for row in grid)
        if grid_hash in seen_grids:
            cycle_length = time_step - seen_grids[grid_hash]
            steps_remaining = target_cycles - time_step
            skip_cycles = steps_remaining // cycle_length
            time_step += skip_cycles * cycle_length

        seen_grids[grid_hash] = time_step

    return calculate_load(grid)

def main():
    input_file = "input.txt"
    grid = [list(line) for line in read_input_file(input_file, mode='lines_stripped')]
    
    # Part 1
    start_time = time.time()
    roll_rocks(grid)  # Perform initial roll
    part1_load = calculate_load(grid)
    part1_time = time.time() - start_time
    print(f"Part 1 Load: {part1_load}, Execution Time: {part1_time:.2f} seconds")

    # Part 2
    start_time = time.time()
    part2_load = calculate_load_after_cycles(grid, 10**9)
    part2_time = time.time() - start_time
    print(f"Part 2 Load: {part2_load}, Execution Time: {part2_time:.2f} seconds")

if __name__ == "__main__":
    main()

