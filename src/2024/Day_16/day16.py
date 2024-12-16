import heapq

def parse_maze(file_path):
    with open(file_path, 'r') as f:
        grid = [list(line.strip()) for line in f.readlines()]
    start = end = None
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == 'S':
                start = (r, c)
            elif cell == 'E':
                end = (r, c)
    return grid, start, end

def calculate_manhattan_distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def reindeer_maze_lowest_score(grid, start, end):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # N, E, S, W
    start_dir = 1  # Starting facing East
    queue = [(0, start[0], start[1], start_dir)]  # (cost, row, col, direction)
    visited = set()

    while queue:
        cost, r, c, d = heapq.heappop(queue)
        if (r, c, d) in visited:
            continue
        visited.add((r, c, d))

        if (r, c) == end:
            return cost

        for i, (dr, dc) in enumerate(directions):
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != '#':
                step_cost = 1
                turn_cost = 1000 if i != d else 0
                heapq.heappush(queue, (cost + step_cost + turn_cost, nr, nc, i))

    return float('inf')  # If no path is found

# Load and parse the input
maze, start, end = parse_maze("input.txt")

# Find the lowest score to navigate the maze
print(reindeer_maze_lowest_score(maze, start, end))
