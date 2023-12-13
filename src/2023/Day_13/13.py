import time
import os
import sys

project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(project_root)
from helpers.file_utils import read_input_file

def find_symmetry_line(pattern):
    rows = len(pattern)
    cols = len(pattern[0])

    for col in range(cols - 1):
        mismatches = 0
        for delta_col in range(cols):
            left_col = col - delta_col
            right_col = col + 1 + delta_col
            if 0 <= left_col < right_col < cols:
                for row in range(rows):
                    if pattern[row][left_col] != pattern[row][right_col]:
                        mismatches += 1
        if mismatches == 0:
            return col + 1

    for row in range(rows - 1):
        mismatches = 0
        for delta_row in range(rows):
            upper_row = row - delta_row
            lower_row = row + 1 + delta_row
            if 0 <= upper_row < lower_row < rows:
                for col in range(cols):
                    if pattern[upper_row][col] != pattern[lower_row][col]:
                        mismatches += 1
        if mismatches == 0:
            return 100 * (row + 1)

    return 0

def process_file(filename):
    content = read_input_file(filename)
    pattern_blocks = content.split('\n\n')
    total_sum = 0

    for block in pattern_blocks:
        pattern = [list(row) for row in block.split('\n')]
        total_sum += find_symmetry_line(pattern)

    return total_sum

def main():
    start_time = time.time()
    filename = "input.txt"
    result = process_file(filename)
    execution_time = time.time() - start_time
    print(f"Result: {result}, Execution Time: {execution_time:.2f} seconds")

if __name__ == "__main__":
    main()
