import os
import sys
import time
from helpers.parsing_utils import read_input_file_strip_lines


project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(project_root)


def parse_input(lines):
    # Convert input into 2D grid
    return [list(line) for line in lines]

def count_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    
    # Only check XMAS in forward directions
    forward_directions = [
        (0,1),   # right
        (1,0),   # down
        (1,1),   # diagonal right-down
        (1,-1),  # diagonal left-down
    ]
    
    for row in range(rows):
        for col in range(cols):
            # Check each direction
            for dr, dc in forward_directions:
                # Check if XMAS pattern fits in bounds
                if (0 <= row + 3*dr < rows and 
                    0 <= col + 3*dc < cols):
                    # Check XMAS forwards
                    if (grid[row][col] == 'X' and
                        grid[row+dr][col+dc] == 'M' and
                        grid[row+2*dr][col+2*dc] == 'A' and
                        grid[row+3*dr][col+3*dc] == 'S'):
                        count += 1
                    # Check SAMX backwards from the end point
                    if (grid[row+3*dr][col+3*dc] == 'X' and
                        grid[row+2*dr][col+2*dc] == 'M' and
                        grid[row+dr][col+dc] == 'A' and
                        grid[row][col] == 'S'):
                        count += 1
    
    return count

def count_xmas_patterns(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    
    # For each possible center
    for row in range(1, rows-1):
        for col in range(1, cols-1):
            # Must be centered on 'A'
            if grid[row][col] != 'A':
                continue
                
            # Check both diagonals
            valid = True
            
            # Need an M and S in each diagonal
            if not ((grid[row-1][col-1] == 'M' and grid[row+1][col+1] == 'S') or
                    (grid[row-1][col-1] == 'S' and grid[row+1][col+1] == 'M')):
                valid = False
                
            if not ((grid[row-1][col+1] == 'M' and grid[row+1][col-1] == 'S') or
                    (grid[row-1][col+1] == 'S' and grid[row+1][col-1] == 'M')):
                valid = False
                
            if valid:
                count += 1
                
    return count

def solve_part1(grid):
    return count_xmas(grid)

def solve_part2(grid):
    return count_xmas_patterns(grid)

def main():
    # Read input
    lines = read_input_file_strip_lines("input.txt")
    grid = parse_input(lines)
    
    # Part 1
    start_time = time.time()
    part1_result = solve_part1(grid)
    end_time = time.time()
    print(f"Part 1: {part1_result}")
    print(f"Part 1 Execution Time: {end_time - start_time} seconds")
    
    # Part 2
    start_time = time.time()
    part2_result = solve_part2(grid)
    end_time = time.time()
    print(f"Part 2: {part2_result}")
    print(f"Part 2 Execution Time: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()

