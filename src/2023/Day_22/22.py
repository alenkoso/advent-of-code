import re
from collections import defaultdict
import os
import sys
from helpers.parsing_utils import read_input_file_strip_lines


project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(project_root)

# Extracts integers from a string
def extract_integers(s):
    return list(map(int, re.findall(r'\d+', s)))

# Moves a brick one unit down
def move_brick_down(brick):
    return (brick[0], brick[1], brick[2] - 1, brick[3], brick[4], brick[5] - 1, brick[6])

# Generates all positions occupied by a brick
def get_occupied_positions(brick):
    for x in range(brick[0], brick[3] + 1):
        for y in range(brick[1], brick[4] + 1):
            for z in range(brick[2], brick[5] + 1):
                yield (x, y, z)

# Main logic to process bricks
def process_bricks(brick_data):
    occupied_positions = {}
    fallen_bricks = []
    
    for brick in sorted(brick_data, key=lambda brick: brick[2]):
        while True:
            next_brick_position = move_brick_down(brick)
            if not any(pos in occupied_positions for pos in get_occupied_positions(next_brick_position)) and next_brick_position[2] > 0:
                brick = next_brick_position
            else:
                for pos in get_occupied_positions(brick):
                    occupied_positions[pos] = brick
                fallen_bricks.append(brick)
                break

    return occupied_positions, fallen_bricks

# Calculate the potential impact of removing a brick
def calculate_impact_of_removal(fallen_bricks, brick_relations_above, brick_relations_below, disintegrated_brick):
    falling_bricks = set()

    def check_if_falls(brick):
        if brick in falling_bricks:
            return
        falling_bricks.add(brick)
        for parent_brick in brick_relations_above[brick]:
            if not len(brick_relations_below[parent_brick] - falling_bricks):
                check_if_falls(parent_brick)

    check_if_falls(disintegrated_brick)
    return len(falling_bricks)

# Main function to run the simulation
def main():
    brick_data = [tuple(extract_integers(line) + [index]) for index, line in enumerate(read_input_file_strip_lines("input.txt"))]
    occupied_positions, fallen_bricks = process_bricks(brick_data)

    brick_relations_above = defaultdict(set)
    brick_relations_below = defaultdict(set)

    for brick in fallen_bricks:
        current_brick_positions = set(get_occupied_positions(brick))
        for pos in get_occupied_positions(move_brick_down(brick)):
            if pos in occupied_positions and pos not in current_brick_positions:
                above_brick = occupied_positions[pos]
                brick_relations_above[above_brick].add(brick)
                brick_relations_below[brick].add(above_brick)

    part1, part2 = 0, 0
    for brick in fallen_bricks:
        would_fall_count = calculate_impact_of_removal(fallen_bricks, brick_relations_above, brick_relations_below, brick)
        part1 += would_fall_count == 1
        part2 += would_fall_count - 1

    print("Part 1: ", part1)
    print("Part 2: ", part2)

# Example usage
if __name__ == "__main__":
    main()

