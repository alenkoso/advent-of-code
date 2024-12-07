import os
import sys
import time
from helpers.parsing_utils import read_input_file_strip_lines


# limit for deep recursion
sys.setrecursionlimit(1000000)

project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(project_root)

# Directions and Mirrors behavior mapping
DIRECTIONS = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}
MIRROR_EFFECTS = {
'.': {'R': 'R', 'L': 'L', 'D': 'D', 'U': 'U'},
'-': {'R': 'R', 'L': 'L', 'D': 'LR', 'U': 'LR'},
'|': {'R': 'DU', 'L': 'DU', 'D': 'D', 'U': 'U'},
'/': {'R': 'U', 'L': 'D', 'D': 'L', 'U': 'R'},
'\\': {'R': 'D', 'L': 'U', 'D': 'R', 'U': 'L'},
}

def energized_tile_count(grid_layout, start_pos):
    energized_set = set()

    def trace_beam(x_coord, y_coord, beam_dir):
        if (x_coord, y_coord, beam_dir) in energized_set:
            return
        energized_set.add((x_coord, y_coord, beam_dir))
        current_mirror = grid_layout[x_coord][y_coord]
        for next_dir in MIRROR_EFFECTS[current_mirror][beam_dir]:
            next_move = DIRECTIONS[next_dir]
            next_x, next_y = x_coord + next_move[0], y_coord + next_move[1]
            if 0 <= next_x < len(grid_layout) and 0 <= next_y < len(grid_layout[0]):
                trace_beam(next_x, next_y, next_dir)

                trace_beam(start_pos[0], start_pos[1], start_pos[2])
                return len({(x, y) for x, y, _ in energized_set})

            def main():
                start_time = time.time()
                grid_data = read_input_file_strip_lines("input.txt")

                # Calculate energized tiles
                part_one_result = energized_tile_count(grid_data, (0, 0, 'R'))
                print(f"Part One Result: {part_one_result}")
                end_time = time.time()
                print(f"Part One Execution Time: {end_time - start_time} seconds")

                # Evaluate different entry points for Part Two
                start_time = time.time()
                entry_tests = [(x, 0, 'R') for x in range(len(grid_data))] + \
                [(x, len(grid_data[0]) - 1, 'L') for x in range(len(grid_data))] + \
                [(0, y, 'D') for y in range(len(grid_data[0]))] + \
                [(len(grid_data) - 1, y, 'U') for y in range(len(grid_data[0]))]

                part_two_result = max(energized_tile_count(grid_data, test) for test in entry_tests)
                print(f"Part Two Result: {part_two_result}")
                end_time = time.time()
                print(f"Part Two Execution Time: {end_time - start_time} seconds")

                if __name__ == "__main__":
                    main()

