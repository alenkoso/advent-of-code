import os
import sys
import time

project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(project_root)
from helpers.file_utils import read_input_file




def main():
    # Part One
    start_time = time.time()
    input_file = "input.txt"
    # parsed_input = read_input_file(.....)
    
    #part one logic
    print(f"Part One Result: {part1 result}")
    end_time = time.time()
    print(f"Part One Execution Time: {end_time - start_time} seconds")

    # Part Two
    start_time = time.time()

    # part two logic
    print(f"Part Two Result: {part2 result}")
    end_time = time.time()
    print(f"Part Two Execution Time: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()
