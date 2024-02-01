import os
import sys
from dataclasses import dataclass

# this doesn't work, fix it + find the temp solution you had.
# Append the project root to sys.path to enable importing from the 'helpers' module
project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(project_root)

from helpers.parsing_utils import read_input_file_strip_lines

@dataclass
class Instruction:
    direction: str
    distance: int

def parse_instructions(lines, part2):
    instructions = []
    for line in lines:
        if not line.strip():
            continue  # Skip empty lines
        _, _, hex_code = line.split()
        if part2:
            hex_value = hex_code.strip('#')
            direction = {0: 'R', 1: 'D', 2: 'L', 3: 'U'}[int(hex_value[-1], 16)]
            distance = int(hex_value[:-1], 16)
        else:
            direction_code, distance_str, _ = line.split()
            direction = direction_code
            distance = int(distance_str)
        instructions.append(Instruction(direction, distance))
    return instructions

def calculate_area(instructions):
    x, y = 0, 0
    vertices = [(x, y)]

    for instruction in instructions:
        dx, dy = {'R': (1, 0), 'D': (0, -1), 'L': (-1, 0), 'U': (0, 1)}[instruction.direction]
        x += dx * instruction.distance
        y += dy * instruction.distance
        vertices.append((x, y))

    # Shoelace formula for area calculation
    area = 0
    for i in range(len(vertices) - 1):
        area += vertices[i][0] * vertices[i + 1][1] - vertices[i + 1][0] * vertices[i][1]
    area += vertices[-1][0] * vertices[0][1] - vertices[0][0] * vertices[-1][1]
    area = abs(area) / 2

    # Perimeter calculation
    perimeter = sum(instruction.distance for instruction in instructions)
    # Total area calculation based on Pick's Theorem: A = I + B/2 - 1
    total_area = area + (perimeter / 2) + 1
    return total_area

def main(input_file):
    lines = read_input_file_strip_lines(input_file)

    for part2 in [False, True]:
        instructions = parse_instructions(lines, part2)
        total_area = calculate_area(instructions)
        print(f"Total area ({'Part 2' if part2 else 'Part 1'}): {total_area}")

if __name__ == "__main__":
    input_file = "input.txt"
    main(input_file)
