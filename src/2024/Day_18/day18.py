import os
import sys
import time
from collections import deque

project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(project_root)

from helpers.parsing_utils import read_input_file_strip_lines

def parse_input(lines):
    return [tuple(map(int, line.split(','))) for line in lines]

def simulate_falling_bytes(grid_size, byte_positions, limit):
    grid = [[False] * grid_size for _ in range(grid_size)]
    for x, y in byte_positions[:limit]:
        grid[y][x] = True
    return grid

def find_shortest_path(grid):
    grid_size = len(grid)
    start, end = (0, 0), (grid_size - 1, grid_size - 1)
    queue = deque([(start, 0)])
    visited = set()

    while queue:
        (x, y), steps = queue.popleft()

        if (x, y) == end:
            return steps

        if (x, y) in visited:
            continue

        visited.add((x, y))

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < grid_size and 0 <= ny < grid_size and not grid[ny][nx]:
                queue.append(((nx, ny), steps + 1))

    return -1

def part1(byte_positions):
    grid = simulate_falling_bytes(71, byte_positions, 1024)
    return find_shortest_path(grid)

def part2(byte_positions):
    grid_size = 71
    grid = [[False] * grid_size for _ in range(grid_size)]

    for i, (x, y) in enumerate(byte_positions):
        grid[y][x] = True
        if find_shortest_path(grid) == -1:
            return f"{x},{y}"

    return None

def main():
    lines = read_input_file_strip_lines("input.txt")
    byte_positions = parse_input(lines)
    
    # Part 1
    start_time = time.time()
    part1_result = part1(byte_positions)
    end_time = time.time()
    print(f"Part 1: {part1_result}")
    print(f"Part 1 Execution Time: {end_time - start_time} seconds")
    
    # Part 2
    start_time = time.time()
    part2_result = part2(byte_positions)
    end_time = time.time()
    print(f"Part 2: {part2_result}")
    print(f"Part 2 Execution Time: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()