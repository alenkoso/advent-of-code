import os
import sys
import itertools
from math import lcm
from helpers.file_utils import read_input_file
import time

project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(project_root)

def parse_input(input_data):
    instructions = input_data[0]
    graph = {}
    for line in input_data[1:]:
        if '=' in line:
            parts = line.split(' = ')
            node, mapping = parts[0], parts[1]
            left, right = mapping.strip('()').split(', ')
            graph[node] = (left, right)
    return instructions, graph

def find_steps_to_ZZZ(instructions, graph, part2=False):
    if not part2:
        curr = 'AAA'
        for p1, rl in enumerate(itertools.cycle(instructions), 1):
            curr = graph[curr][rl == 'R']
            if curr == 'ZZZ':
                return p1
    else:
        currs = [n for n in graph if n.endswith('A')]
        cycles = [None] * len(currs)
        for step, rl in enumerate(itertools.cycle(instructions), 1):
            for c in range(len(currs)):
                currs[c] = graph[currs[c]][rl == 'R']
                if currs[c].endswith('Z'):
                    cycles[c] = step
            if all(cy for cy in cycles):
                return lcm(*cycles)

def main():
    input_data = read_input_file("input.txt", mode='lines_stripped')
    instructions, node_mappings = parse_input(input_data)

    # Part 1
    start_time = time.time()
    steps_part1 = find_steps_to_ZZZ(instructions, node_mappings)
    end_time = time.time()
    print(f"Steps to reach ZZZ (Part 1): {steps_part1}")
    print(f"Part 1 Execution Time: {end_time - start_time} seconds")

    # Part 2
    start_time = time.time()
    steps_part2 = find_steps_to_ZZZ(instructions, node_mappings, part2=True)
    end_time = time.time()
    print(f"Steps to reach ZZZ (Part 2): {steps_part2}")
    print(f"Part 2 Execution Time: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()

