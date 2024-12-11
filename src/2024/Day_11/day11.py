import sys
import os
from collections import defaultdict
from functools import lru_cache
import time

project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(project_root)

from helpers.file_utils import read_input_file

@lru_cache
def transform_stone(stone):
    # Transform a single stone, cached for efficiency.
    # Rule 1: If stone is 0, it becomes 1
    if stone == 0:
        return [1]
        
    # Rule 2: If number has even number of digits, split in half
    stone_str = str(stone)
    if len(stone_str) % 2 == 0:
        mid = len(stone_str) // 2
        return [int(stone_str[:mid]), int(stone_str[mid:])]
        
    # Rule 3: Multiply by 2024
    return [2024 * stone]

def transform_all_stones(stone_counts):
    # Transform all stones, maintaining counts.
    new_counts = defaultdict(int)
    for stone, count in stone_counts.items():
        for new_stone in transform_stone(stone):
            new_counts[new_stone] += count
    return new_counts

def solve_stones(stone_counts, blinks):
    # Calculate total stones after given number of blinks.
    current_counts = stone_counts.copy()
    for _ in range(blinks):
        current_counts = transform_all_stones(current_counts)
    return sum(current_counts.values())

def count_stones(stones):
    # Convert stone list to count dictionary
    counts = defaultdict(int)
    for stone in stones:
        counts[stone] += 1
    return counts

def main():
    # Read and parse input
    lines = read_input_file('input.txt', mode='lines_stripped')
    initial_stones = [int(x) for x in lines[0].split()]
    stone_counts = count_stones(initial_stones)
    
    # Part 1: 25 blinks
    start_time = time.time()
    result1 = solve_stones(stone_counts, 25)
    end_time = time.time()
    print(f"Part 1: After 25 blinks there will be {result1} stones")
    print(f"Part 1 execution time: {end_time - start_time:.2f} seconds")
    
    # Part 2: 75 blinks
    start_time = time.time()
    result2 = solve_stones(stone_counts, 75)
    end_time = time.time()
    print(f"Part 2: After 75 blinks there will be {result2} stones")
    print(f"Part 2 execution time: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()