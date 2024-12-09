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
    count = 0
    start_pos = -1
    
    for i in range(start):
        if blocks[i] == '.':
            if count == 0:
                start_pos = i
            count += 1
            if count >= size_needed:
                return start_pos
        else:
            count = 0
    return -1

def move_file(blocks, file_start, file_size, new_pos):
    file_id = blocks[file_start]
    # Clear old location and place at new location in one pass
    for i in range(file_size):
        blocks[new_pos + i] = file_id
        blocks[file_start + i] = '.'

def compact_disk_part1(blocks):
    # Track free spaces in a queue
    free_spaces = deque()
    
    # Initialize free spaces queue
    for i in range(len(blocks)):
        if blocks[i] == '.':
            free_spaces.append(i)
    
    # Process blocks right to left
    for i in range(len(blocks)-1, -1, -1):
        if blocks[i] != '.' and free_spaces and free_spaces[0] < i:
            # Move block to leftmost available space
            new_pos = free_spaces.popleft()
            blocks[new_pos] = blocks[i]
            blocks[i] = '.'
            free_spaces.append(i)
    
    return blocks

def compact_disk_part2(blocks, files):
    for file_id, start_pos, length in sorted(files, reverse=True):
        new_pos = find_free_space(blocks, start_pos, length)
        if new_pos != -1:
            move_file(blocks, start_pos, length, new_pos)
    return blocks

def calculate_checksum(blocks):
    return sum(pos * block for pos, block in enumerate(blocks) if block != '.')

def solve_part1(disk_map):
    if isinstance(disk_map, str):
        disk_map = [int(x) for x in disk_map]
    blocks, _ = expand_disk_map(disk_map)
    blocks = compact_disk_part1(blocks)
    return calculate_checksum(blocks)

def solve_part2(disk_map):
    if isinstance(disk_map, str):
        disk_map = [int(x) for x in disk_map]
    blocks, files = expand_disk_map(disk_map)
    blocks = compact_disk_part2(blocks, files)
    return calculate_checksum(blocks)

def main():
    disk_map = read_input_file('input.txt', mode='lines_stripped')[0]
    
    # Part 1
    start_time = time.time()
    part1_result = solve_part1(disk_map)
    end_time = time.time()
    print(f"Part 1: {part1_result}")
    print(f"Part 1 Execution Time: {end_time - start_time} seconds")
    
    # Part 2
    start_time = time.time()
    part2_result = solve_part2(disk_map)
    end_time = time.time()
    print(f"Part 2: {part2_result}")
    print(f"Part 2 Execution Time: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()