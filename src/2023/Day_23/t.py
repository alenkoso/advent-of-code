def parse_input(file_path):
    with open(file_path, 'r') as file:
        return [list(line.strip()) for line in file.readlines()]

def get_next_positions(x, y, grid):
    directions = []
    if grid[y][x] in '^>v<':
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] if grid[y][x] == '.' else []
        if grid[y][x] == '>': 
            directions.append((1, 0))
        if grid[y][x] == '<': 
            directions.append((-1, 0))
        if grid[y][x] == '^': 
            directions.append((0, -1))
        if grid[y][x] == 'v': 
            directions.append((0, 1))
    else:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    next_positions = []
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]) and grid[ny][nx] != '#':
            next_positions.append((nx, ny))
    return next_positions

def find_longest_hike(grid):
    dp = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    start_x = grid[0].index('.')
    dp[0][start_x] = 1  # starting position

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if dp[y][x] != -1:  # if the current position is reachable
                for nx, ny in get_next_positions(x, y, grid):
                    if grid[ny][nx] != '.' or (nx, ny) == (x, y):
                        continue
                    dp[ny][nx] = max(dp[ny][nx], dp[y][x] + 1)

    return max(max(row) for row in dp)

# Test with the example input
example_input = [
    "#.#####################",
    "#.......#########...###",
    "#######.#########.#.###",
    "###.....#.>.>.###.#.###",
    "###v#####.#v#.###.#.###",
    "###.>...#.#.#.....#...#",
    "###v###.#.#.#########.#",
    "###...#.#.#.......#...#",
    "#####.#.#.#######.#.###",
    "#.....#.#.#.......#...#",
    "#.#####.#.#.#########v#",
    "#.#...#...#...###...>.#",
    "#.#.#v#######v###.###v#",
    "#...#.>.#...>.>.#.###.#",
    "#####v#.#.###v#.#.###.#",
    "#.....#...#...#.#.#...#",
    "#.#########.###.#.#.###",
    "#...###...#...#...#.###",
    "###.###.#.###v#####v###",
    "#...#...#.#.>.>.#.>.###",
    "#.###.###.#.###.#.#v###",
    "#.....###...###...#...#",
    "#####################.#"
]

grid = [list(line) for line in example_input]
print(find_longest_hike(grid))

