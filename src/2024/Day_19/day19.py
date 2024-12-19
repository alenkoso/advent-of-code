import os
import sys
import time

project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(project_root)

from helpers.parsing_utils import read_input_file_strip_lines

def parse_input(lines):
    combined_text = '\n'.join(lines)
    patterns_section, designs_section = combined_text.split('\n\n')
    patterns = patterns_section.split(', ')
    designs = designs_section.split('\n')
    return patterns, designs

def is_design_possible(patterns, design):
    dp = [False] * (len(design) + 1)
    dp[0] = True

    for i in range(1, len(design) + 1):
        for pattern in patterns:
            if i >= len(pattern) and design[i - len(pattern):i] == pattern:
                dp[i] = dp[i] or dp[i - len(pattern)]
                if dp[i]:
                    break
    return dp[-1]

def count_possible_constructions(patterns, design):
    dp = [0] * (len(design) + 1)
    dp[0] = 1

    for i in range(1, len(design) + 1):
        for pattern in patterns:
            if i >= len(pattern) and design[i - len(pattern):i] == pattern:
                dp[i] += dp[i - len(pattern)]
    return dp[-1]

def part1(patterns, designs):
    return sum(is_design_possible(patterns, design) for design in designs)

def part2(patterns, designs):
    return sum(count_possible_constructions(patterns, design) for design in designs)

def main():
    lines = read_input_file_strip_lines("input.txt")
    patterns, designs = parse_input(lines)
    
    start_time = time.time()
    part_1 = part1(patterns, designs)
    end_time = time.time()
    print("Part 1:", part_1)
    print("Part 1 Execution Time:", end_time - start_time, "seconds")
    
    start_time = time.time()
    part_2 = part2(patterns, designs)
    end_time = time.time()
    print("Part 2:", part_2)
    print("Part 2 Execution Time:", end_time - start_time, "seconds")

if __name__ == "__main__":
    main()