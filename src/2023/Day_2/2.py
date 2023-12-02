import re
import sys
import os

project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(project_root)
from helpers.parsing_utils import read_input_file

def parse_data(line):
    game_id = int(re.search(r'Game (\d+):', line).group(1))
    cube_counts = re.findall(r'(\d+) red|(\d+) green|(\d+) blue', line)
    subsets = [{'red': int(r or 0), 'green': int(g or 0), 'blue': int(b or 0)} for r, g, b in cube_counts]
    return game_id, subsets

def calculate_game_stats(lines):
    total_sum, total_power_sum = 0, 0

    for line in lines:
        game_id, subsets = parse_data(line.strip())

        # Part 1
        if all(subset['red'] <= 12 and subset['green'] <= 13 and subset['blue'] <= 14 for subset in subsets):
            total_sum += game_id

        # Part 2
        min_cubes = {color: max(subset[color] for subset in subsets) for color in ['red', 'green', 'blue']}
        total_power_sum += min_cubes['red'] * min_cubes['green'] * min_cubes['blue']

    return total_sum, total_power_sum

def main():
    input_file = 'input.txt'
    lines = read_input_file(input_file)
    total_sum, total_power_sum = calculate_game_stats(lines)
    
    print(f"Part 1: {total_sum}")
    print(f"Part 2: {total_power_sum}")

if __name__ == "__main__":
    main()
