from collections import defaultdict
import sys
import os

project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(project_root)
from helpers.file_utils import read_input_file

def process_grid(grid):
    num_rows = len(grid)
    num_columns = len(grid[0]) if grid else 0
    part1_total = 0
    numbers_adjacent_to_gears = defaultdict(list)

    for row_index in range(num_rows):
        adjacent_gear_positions = set()
        current_number = 0
        is_adjacent_to_symbol = False

        for column_index in range(len(grid[row_index]) + 1):
            if column_index < num_columns and grid[row_index][column_index].isdigit():
                current_number = current_number * 10 + int(grid[row_index][column_index])
                for delta_row in [-1, 0, 1]:
                    for delta_column in [-1, 0, 1]:
                        adjacent_row = row_index + delta_row
                        adjacent_column = column_index + delta_column
                        if 0 <= adjacent_row < num_rows and 0 <= adjacent_column < num_columns:
                            adjacent_char = grid[adjacent_row][adjacent_column]
                            if not adjacent_char.isdigit() and adjacent_char != '.':
                                is_adjacent_to_symbol = True
                            if adjacent_char == '*':
                                adjacent_gear_positions.add((adjacent_row, adjacent_column))
            elif current_number > 0:
                for gear_position in adjacent_gear_positions:
                    numbers_adjacent_to_gears[gear_position].append(current_number)
                if is_adjacent_to_symbol:
                    part1_total += current_number
                current_number = 0
                is_adjacent_to_symbol = False
                adjacent_gear_positions = set()

    # Part 2
    part2_total = 0
    for adjacent_numbers in numbers_adjacent_to_gears.values():
        if len(adjacent_numbers) == 2:
            part2_total += adjacent_numbers[0] * adjacent_numbers[1]

    return part1_total, part2_total

def main():
    lines = read_input_file("input.txt", mode='lines_stripped')
    grid = [[char for char in line] for line in lines]

    part1_total, part2_total = process_grid(grid)
    print(f"Part 1: {part1_total}")
    print(f"Part 2: {part2_total}")

if __name__ == "__main__":
    main()
