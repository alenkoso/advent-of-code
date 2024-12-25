import sys
import os
import time

project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(project_root)

from helpers.parsing_utils import read_input_file_strip_lines

def separate_schematics(data):
    schematics = [[]]
    for line in data:
        if line:
            schematics[-1].append(line)
        elif schematics[-1]:
            schematics.append([])
    return schematics

def check_lock_key_compatibility(lock, key):
    for y in range(7):
        for x in range(5):
            if lock[y][x] == '#' and key[y][x] == '#':
                return False
    return True

def part1(schematics):
    locks = []
    keys = []
    
    for schematic in schematics:
        if not schematic:
            continue
        if schematic[0].startswith('#'):
            locks.append(schematic)
        else:
            keys.append(schematic)
            
    compatible_pairs = 0
    for lock in locks:
        for key in keys:
            if check_lock_key_compatibility(lock, key):
                compatible_pairs += 1
    
    return compatible_pairs

def main():
    data = read_input_file_strip_lines("input.txt")
    
    start_time = time.time()
    part_1 = part1(separate_schematics(data))
    end_time = time.time()
    
    print("Part 1:", part_1)
    print("Part 1 Execution Time:", end_time - start_time, "seconds")

if __name__ == "__main__":
    main()