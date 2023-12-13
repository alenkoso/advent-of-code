#!/usr/bin/env python3

import sys
import time

def unfold_row(row, unfold_times=5):
    springs, block_sizes = row.split()
    unfolded_springs = '?'.join([springs] * unfold_times)
    unfolded_block_sizes = ','.join([block_sizes] * unfold_times)
    return unfolded_springs, [int(x) for x in unfolded_block_sizes.split(',')]

def count_arrangements(springs, groups, index=0, group_index=0, current=0, memo=None):
    key = (index, group_index, current)
    
    if memo is None:
        memo = {}

    # Check if the result is already computed
    if key in memo:
        return memo[key]

    # Base cases
    if index == len(springs):
        result = 1 if group_index == len(groups) and current == 0 else 0
        memo[key] = result
        print(f"Base case reached at end of springs: {key} -> {result}")
        return result

    if group_index == len(groups):
        result = 1 if springs[index:].count('#') == 0 else 0
        memo[key] = result
        print(f"Base case reached at end of groups: {key} -> {result}")
        return result

    if springs[index] != '?':
        if springs[index] == '#' and (group_index == 0 or groups[group_index - 1] == 0):
            result = count_arrangements(springs, groups, index + 1, group_index + 1, 0, memo)
            memo[key] = result
            print(f"Non '?' char encountered, incremented group_index: {key} -> {result}")
            return result
        result = count_arrangements(springs, groups, index + 1, group_index, memo)
        memo[key] = result
        print(f"Non '?' char encountered, no increment: {key} -> {result}")
        return result
    
    # Recursive case for '?'
    count = 0
    # Option 1: Current spring is operational
    count += count_arrangements(springs, groups, index + 1, group_index, memo)
    # Option 2: Current spring is damaged
    if group_index == 0 or groups[group_index - 1] == 0:
        count += count_arrangements(springs, [groups[0] - 1] + groups[1:], index + 1, group_index + 1, 0, memo)

    memo[key] = count
    print(f"Recursive case '?': {key} -> {count}")
    return count

def calculate_total_arrangements(filename, part2=False):
    with open(filename, 'r') as file:
        lines = file.readlines()

    total_arrangements = 0
    for line in lines:
        line = line.strip()
        if part2:
            springs, blocks = unfold_row(line)
        else:
            springs, block_sizes = line.split()
            blocks = [int(x) for x in block_sizes.split(',')]

        memo = {}
        arrangements = count_arrangements(springs, blocks, 0, 0, 0, memo)
        total_arrangements += arrangements

    return total_arrangements

def main():
    input_file = "input.txt"  # Replace with your input file

    start_time = time.time()
    part1_result = calculate_total_arrangements(input_file)
    end_time = time.time()
    print(f"Part 1: {part1_result}, Execution Time: {end_time - start_time:.2f} seconds")

    start_time = time.time()
    part2_result = calculate_total_arrangements(input_file, part2=True)
    end_time = time.time()
    print(f"Part 2: {part2_result}, Execution Time: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()
