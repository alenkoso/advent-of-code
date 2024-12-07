import os
import sys
import time
from helpers.file_utils import read_input_file


project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(project_root)

def check_vertical_symmetry(pattern, part_two):
    ### Checks for vertical symmetry in the pattern. ###
    rows, cols = len(pattern), len(pattern[0])
    total_sum = 0
    for col in range(cols - 1):
        mismatches = 0
        for delta_col in range(cols):
            left_col, right_col = col - delta_col, col + 1 + delta_col
            if 0 <= left_col < right_col < cols:
                for row in range(rows):
                    if pattern[row][left_col] != pattern[row][right_col]:
                        mismatches += 1
                        if mismatches == (1 if part_two else 0):
                            total_sum += col + 1
                            return total_sum

                        def check_horizontal_symmetry(pattern, part_two):
                            ### Checks for horizontal symmetry in the pattern. ###
                            rows, cols = len(pattern), len(pattern[0])
                            total_sum = 0
                            for row in range(rows - 1):
                                mismatches = 0
                                for delta_row in range(rows):
                                    upper_row, lower_row = row - delta_row, row + 1 + delta_row
                                    if 0 <= upper_row < lower_row < rows:
                                        for col in range(cols):
                                            if pattern[upper_row][col] != pattern[lower_row][col]:
                                                mismatches += 1
                                                if mismatches == (1 if part_two else 0):
                                                    total_sum += 100 * (row + 1)
                                                    return total_sum

                                                def process_patterns(input_file, part_two=False):
                                                    ### Processes each pattern in the input file and calculates the sum of symmetry lines. ###
                                                    pattern_blocks = read_input_file(input_file, mode='full')
                                                    total_sum = 0
                                                    for grid in pattern_blocks:
                                                        pattern = [list(row) for row in grid.split('\n')]
                                                        total_sum += check_vertical_symmetry(pattern, part_two)
                                                        total_sum += check_horizontal_symmetry(pattern, part_two)
                                                        return total_sum

                                                    def main():
                                                        input_file = "input.txt"

                                                        # Part 1
                                                        start_time = time.time()  # Start time
                                                        part1_result = process_patterns(input_file, part_two=False)
                                                        end_time = time.time()  # End time
                                                        print("Part 1 Result:", part1_result)
                                                        print(f"Part 1 Execution Time: {end_time - start_time} seconds")

                                                        # Part 2
                                                        start_time = time.time()  # Start time
                                                        part2_result = process_patterns(input_file, part_two=True)
                                                        end_time = time.time()  # End time
                                                        print("Part 2 Result:", part2_result)
                                                        print(f"Part 2 Execution Time: {end_time - start_time} seconds")

                                                        if __name__ == "__main__":
                                                            main()

