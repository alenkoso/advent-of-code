import os
import sys
import time

project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(project_root)

from helpers.parsing_utils import read_input_file_strip_lines

def parse_input(lines):
    # Convert each line to list of numbers
    return [list(map(int, line.split())) for line in lines]

def is_sequence_valid(nums):
    # Check if sequence is valid (all increasing or decreasing with diffs 1-3)
    if len(nums) <= 1:
        return True
        
    is_increasing = nums[1] > nums[0]
    
    for i in range(len(nums)-1):
        diff = nums[i+1] - nums[i]
        
        # Check if direction matches and diff is in range
        if is_increasing and (diff <= 0 or diff > 3):
            return False
        if not is_increasing and (diff >= 0 or abs(diff) > 3):
            return False
            
    return True

def solve_part1(reports):
    return sum(1 for report in reports if is_sequence_valid(report))

def solve_part2(reports):
    valid_count = 0
    
    for report in reports:
        # Check if valid without removing any number
        if is_sequence_valid(report):
            valid_count += 1
            continue
            
        # Try removing each number
        for i in range(len(report)):
            modified = report[:i] + report[i+1:]
            if is_sequence_valid(modified):
                valid_count += 1
                break
                
    return valid_count

def main():
    # Read input
    lines = read_input_file_strip_lines("input.txt")
    reports = parse_input(lines)
    
    # Part 1
    start_time = time.time()
    part1_result = solve_part1(reports)
    end_time = time.time()
    print(f"Part 1: {part1_result}")
    print(f"Part 1 Execution Time: {end_time - start_time} seconds")
    
    # Part 2
    start_time = time.time()
    part2_result = solve_part2(reports)
    end_time = time.time()
    print(f"Part 2: {part2_result}")
    print(f"Part 2 Execution Time: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()