import sys
import os
import time
from collections import deque

project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(project_root)

from helpers.file_utils import read_input_file

def expand_disk_map(disk_map):
    blocks = []
    file_id = 0
    files = []  # Track file info: (id, start_pos, length)
    pos = 0
    
    for i, length in enumerate(disk_map):
        length = int(length)
        if i % 2 == 0:  # File
            blocks.extend([file_id] * length)
            files.append((file_id, pos, length))
            file_id += 1
        else:  # Space
            blocks.extend(['.'] * length)
        pos += length
            
    return blocks, files

def find_free_space(blocks, start, size_needed):
    # Find continuous free space of required size
    spaces = 0
    for i in range(start):
        if blocks[i] == '.':
            spaces += 1
            if spaces >= size_needed:
                return i - size_needed + 1
        else:
            spaces = 0
    return -1

def move_file(blocks, file_start, file_size, new_pos):
    # Move entire file to new position
    file_id = blocks[file_start]
    # Clear old location
    for i in range(file_size):
        blocks[file_start + i] = '.'
    # Place at new location
    for i in range(file_size):
        blocks[new_pos + i] = file_id

def compact_disk_part2(blocks, files):
    # Process files in reverse ID order
    for file_id, start_pos, length in sorted(files, reverse=True):
        # Find leftmost suitable free space
        new_pos = find_free_space(blocks, start_pos, length)
        if new_pos != -1:
            move_file(blocks, start_pos, length, new_pos)
    return blocks

def calculate_checksum(blocks):
    return sum(pos * block for pos, block in enumerate(blocks) if block != '.')

def solve_part2(disk_map):
    disk_map = [int(x) for x in disk_map]
    blocks, files = expand_disk_map(disk_map)
    blocks = compact_disk_part2(blocks, files)
    return calculate_checksum(blocks)

def main():
    # Read input
    disk_map = read_input_file('input.txt', mode='lines_stripped')[0]
    
    # Test with example
    test_input = "2333133121414131402"
    test_result = solve_part2(test_input)
    print(f"Test Result: {test_result}")  # Should be 2858
    
    # Part 2
    start_time = time.time()
    result = solve_part2(disk_map)
    end_time = time.time()
    
    print(f"Part 2: {result}")
    print(f"Part 2 Execution Time: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()