# Re-implementing the necessary functions to read and parse the example input
# and solve the puzzle for the example case.

from collections import deque

def read_and_parse_input(file_path):
    with open(file_path, 'r') as file:
        garden_map = [list(line.strip()) for line in file.readlines()]
    start = None
    for y, row in enumerate(garden_map):
        for x, cell in enumerate(row):
            if cell == 'S':
                start = (x, y)
                break
        if start:
            break
    return garden_map, start

def valid_move(x, y, garden_map):
    return 0 <= y < len(garden_map) and 0 <= x < len(garden_map[0]) and garden_map[y][x] == '.'

def bfs(garden_map, start, steps):
    visited = set()
    queue = deque([(start, 0)])
    final_positions = set()

    while queue:
        (x, y), step = queue.popleft()
        if step == steps:
            final_positions.add((x, y))
        elif step < steps:
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if valid_move(nx, ny, garden_map) and (nx, ny, step + 1) not in visited:
                    visited.add((nx, ny, step + 1))
                    queue.append(((nx, ny), step + 1))

    return len(final_positions)

# Test the script with the example input
example_input_path = 'input.txt'
garden_map, start = read_and_parse_input(example_input_path)
result = bfs(garden_map, start, 64)  # Using 6 steps as per the example
print(f"Number of garden plots the Elf can reach in exactly 64 steps: {result+1}") #figured I don't count S position.
