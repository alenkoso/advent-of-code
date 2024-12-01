import os
import sys
import time
from collections import Counter

project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(project_root)

from helpers.parsing_utils import read_input_file_strip_lines

def parse_input(lines):
    # Parse input lines into left and right lists
    left_list = []
    right_list = []
    
    for line in lines:
        if line:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
    
    return left_list, right_list

def solve_part1(left_list, right_list):
    # Calculate total distance between sorted lists
    return sum(abs(l - r) for l, r in zip(sorted(left_list), sorted(right_list)))

def solve_part2(left_list, right_list):
    # Calculate similarity score based on number occurrences
    right_counts = Counter(right_list)
    return sum(num * right_counts[num] for num in left_list)

def main():
    # Read input
    lines = read_input_file_strip_lines("input.txt")
    left_list, right_list = parse_input(lines)
    
    # Part 1
    start_time = time.time()
    part1_result = solve_part1(left_list, right_list)
    end_time = time.time()
    print(f"Part 1: {part1_result}")
    print(f"Part 1 Execution Time: {end_time - start_time} seconds")
    
    # Part 2
    start_time = time.time()
    part2_result = solve_part2(left_list, right_list)
    end_time = time.time()
    print(f"Part 2: {part2_result}")
    print(f"Part 2 Execution Time: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()