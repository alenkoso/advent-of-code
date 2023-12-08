import os
import sys

project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(project_root)
from helpers.file_utils import read_input_file

def parse_input(input_data):
    instructions = input_data[0]
    node_mappings = {}
    for line in input_data[1:]:
        if '=' in line:  # Ensure the line contains an equals sign
            node, mapping = line.split(' = ')
            left, right = mapping.strip('()').split(', ')
            node_mappings[node] = (left, right)
    return instructions, node_mappings

def navigate_network(instructions, node_mappings):
    current_node = 'AAA'
    steps = 0

    while current_node != 'ZZZ':
        direction = instructions[steps % len(instructions)]
        current_node = node_mappings[current_node][0 if direction == 'L' else 1]
        steps += 1

    return steps

def main():
    input_data = read_input_file('input.txt', mode='lines_stripped')
    instructions, node_mappings = parse_input(input_data)
    steps_to_reach_ZZZ = navigate_network(instructions, node_mappings)

    print(f"Steps required to reach ZZZ: {steps_to_reach_ZZZ}")

if __name__ == "__main__":
    main()
