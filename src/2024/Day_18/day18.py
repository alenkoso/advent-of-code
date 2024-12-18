from collections import deque

def parse_input(raw_input):
    return [tuple(map(int, line.split(','))) for line in raw_input.strip().split('\n')]

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

def part1(raw_input):
    byte_positions = parse_input(raw_input)
    grid = simulate_falling_bytes(71, byte_positions, 1024)
    return find_shortest_path(grid)

def part2(raw_input):
    byte_positions = parse_input(raw_input)
    grid_size = 71
    grid = [[False] * grid_size for _ in range(grid_size)]

    for i, (x, y) in enumerate(byte_positions):
        grid[y][x] = True
        if find_shortest_path(grid) == -1:
            return f"{x},{y}"

    return None

example_input = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0"""

if __name__ == "__main__":
    with open("input.txt") as f:
        puzzle_input = f.read()
    print("Part 1:", part1(puzzle_input))
    print("Part 2:", part2(puzzle_input))