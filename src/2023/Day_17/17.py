import os
import sys
import heapq

# Append the project root to sys.path to enable importing from the 'helpers' module
project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(project_root)

from helpers.parsing_utils import read_input_file_to_grid

def solve(grid, part2):
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    queue = [(0, 0, 0, -1, -1)]  # heat_loss, row, col, direction, in_direction
    visited = {}

    while queue:
        heat_loss, row, col, dir_, in_dir = heapq.heappop(queue)
        if (row, col, dir_, in_dir) in visited:
            continue
        visited[(row, col, dir_, in_dir)] = heat_loss

        for i, (dr, dc) in enumerate(directions):
            rr, cc = row + dr, col + dc
            new_dir, new_in_dir = i, 1 if i != dir_ else in_dir + 1
            isnt_reverse = (new_dir + 2) % 4 != dir_
            valid_part1 = new_in_dir <= 3
            valid_part2 = new_in_dir <= 10 and (new_dir == dir_ or in_dir >= 4 or in_dir == -1)
            valid = valid_part2 if part2 else valid_part1

            if 0 <= rr < rows and 0 <= cc < cols and isnt_reverse and valid:
                cost = int(grid[rr][cc])
                if (rr, cc, new_dir, new_in_dir) not in visited:
                    heapq.heappush(queue, (heat_loss + cost, rr, cc, new_dir, new_in_dir))

    # Find the minimum heat loss to the destination
    return min(value for (r, c, _, in_dir), value in visited.items() if r == rows - 1 and c == cols - 1 and (in_dir >= 4 or not part2))

def main():
    grid = read_input_file_to_grid("input.txt")
    min_heat_loss_part1 = solve(grid, part2=False)
    min_heat_loss_part2 = solve(grid, part2=True)

    print(f"Part 1 - Minimum Heat Loss: {min_heat_loss_part1}")
    print(f"Part 2 - Minimum Heat Loss: {min_heat_loss_part2}")

if __name__ == "__main__":
    main()
