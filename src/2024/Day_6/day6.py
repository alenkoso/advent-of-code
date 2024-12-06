import os
import sys
import time

project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(project_root)

from helpers.parsing_utils import read_input_file_strip_lines

def parse_input(lines):
    lab_grid = [list(line) for line in lines]
    row_count = len(lab_grid)
    col_count = len(lab_grid[0])
    
    # Find guard's starting position
    guard_start_row = guard_start_col = 0
    for row in range(row_count):
        for col in range(col_count):
            if lab_grid[row][col] == '^':
                guard_start_row, guard_start_col = row, col
                lab_grid[row][col] = '.'  # Replace guard with empty space
                return lab_grid, (guard_start_row, guard_start_col)
    
    return lab_grid, (guard_start_row, guard_start_col)

def simulate_guard(lab_grid, guard_start, obstacle_position=(-1, -1)):
    row_count = len(lab_grid)
    col_count = len(lab_grid[0])
    direction_row = [-1, 0, 1, 0]  # Up, Right, Down, Left
    direction_col = [0, 1, 0, -1]
    current_row, current_col = guard_start
    current_direction = 0  # Initial direction (up)
    
    if obstacle_position[0] < 0:  # Part 1 - count visited positions
        visited_positions = {(current_row, current_col)}
        while True:
            next_row = current_row + direction_row[current_direction]
            next_col = current_col + direction_col[current_direction]
            
            # Check if guard leaves mapped area
            if not (0 <= next_row < row_count and 0 <= next_col < col_count):
                return len(visited_positions)
                
            # Check if there's an obstacle ahead
            if lab_grid[next_row][next_col] == '#':
                current_direction = (current_direction + 1) % 4  # Turn right
            else:
                current_row, current_col = next_row, next_col
                visited_positions.add((current_row, current_col))
    else:  # Part 2 - look for loops with added obstacle
        obstacle_row, obstacle_col = obstacle_position
        steps_taken = 0
        visited_states = {(current_row, current_col, current_direction)}
        
        while steps_taken < 10000:  # Limit to prevent infinite loops
            next_row = current_row + direction_row[current_direction]
            next_col = current_col + direction_col[current_direction]
            
            # Check if guard leaves mapped area
            if not (0 <= next_row < row_count and 0 <= next_col < col_count):
                return False
                
            # Check if there's an obstacle (including new one) ahead
            if (next_row == obstacle_row and next_col == obstacle_col) or lab_grid[next_row][next_col] == '#':
                current_direction = (current_direction + 1) % 4  # Turn right
            else:
                current_row, current_col = next_row, next_col
                current_state = (current_row, current_col, current_direction)
                if current_state in visited_states:
                    return True  # Found a loop
                visited_states.add(current_state)
            steps_taken += 1
        return False  # Too many steps without finding a loop

def solve_part1(lab_grid, guard_start):
    return simulate_guard(lab_grid, guard_start)

def solve_part2(lab_grid, guard_start):
    row_count = len(lab_grid)
    col_count = len(lab_grid[0])
    loop_positions_count = 0
    
    for row in range(row_count):
        for col in range(col_count):
            # Check each empty space that isn't the guard's starting position
            if lab_grid[row][col] == '.' and (row, col) != guard_start:
                if simulate_guard(lab_grid, guard_start, (row, col)):
                    loop_positions_count += 1
                    
    return loop_positions_count

def main():
    # Read input
    lines = read_input_file_strip_lines("input.txt")
    lab_grid, guard_start = parse_input(lines)
    
    # Part 1
    start_time = time.time()
    part1_result = solve_part1(lab_grid, guard_start)
    end_time = time.time()
    print(f"Part 1: {part1_result}")
    print(f"Part 1 Execution Time: {end_time - start_time} seconds")
    
    # Part 2
    start_time = time.time()
    part2_result = solve_part2(lab_grid, guard_start)
    end_time = time.time()
    print(f"Part 2: {part2_result}")
    print(f"Part 2 Execution Time: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()