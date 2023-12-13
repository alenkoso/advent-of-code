import os
import sys
import time

project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(project_root)
from helpers.file_utils import read_input_file

def count_arrangements(dots, blocks, i=0, bi=0, current=0, memo=None):
    if memo is None:
        memo = {}
    key = (i, bi, current)

    # Check if the current state is already computed
    if key in memo:
        return memo[key]

    # Base cases
    if i == len(dots):
        if bi == len(blocks) and current == 0:
            return 1
        elif bi == len(blocks) - 1 and blocks[bi] == current:
            return 1
        else:
            return 0

    # Recursive cases
    ans = 0
    for c in ['.', '#']:
        if dots[i] == c or dots[i] == '?':
            if c == '.':
                if current == 0:
                    ans += count_arrangements(dots, blocks, i + 1, bi, 0, memo)
                elif current > 0 and bi < len(blocks) and blocks[bi] == current:
                    ans += count_arrangements(dots, blocks, i + 1, bi + 1, 0, memo)
            elif c == '#':
                ans += count_arrangements(dots, blocks, i + 1, bi, current + 1, memo)

    memo[key] = ans
    return ans

def process_line(line, part_two=False):
    dots, blocks = line.split()
    if part_two:
        dots = '?'.join([dots] * 5)
        blocks = ','.join([blocks] * 5)
    blocks = [int(x) for x in blocks.split(',')]
    return count_arrangements(dots, blocks)

def main():
    input_file = "input.txt"
    lines = read_input_file(input_file, mode='lines_stripped')

    # Part 1
    start_time = time.time()
    part1_result = sum(process_line(line) for line in lines)
    end_time = time.time()
    print("Part 1 Result:", part1_result)
    print(f"Part 1 Execution Time: {end_time - start_time} seconds")

    # Part 2
    start_time = time.time()
    part2_result = sum(process_line(line, part_two=True) for line in lines)
    end_time = time.time()
    print("Part 2 Result:", part2_result)
    print(f"Part 2 Execution Time: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()
