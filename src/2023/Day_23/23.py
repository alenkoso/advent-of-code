import sys

def parse_input(file_path):
     with open(file_path, 'r') as file:
        return [list(line.strip()) for line in file.readlines()]

def is_valid_move(x, y, grid, visited):
    if 0 <= y < len(grid) and 0 <= x < len(grid[0]) and (x, y) not in visited:
        return grid[y][x] != '#'
    return False

def get_next_position(x, y, direction):
    if direction == '>': return x + 1, y
    if direction == '<': return x - 1, y
    if direction == '^': return x, y - 1
    if direction == 'v': return x, y + 1
    return x, y

def dfs(x, y, grid, visited):
    if grid[y][x] in '^>v<':
        nx, ny = get_next_position(x, y, grid[y][x])
        if is_valid_move(nx, ny, grid, visited):
            return dfs(nx, ny, grid, visited | {(nx, ny)})
        else:
            return len(visited)
    
    longest = len(visited)
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if is_valid_move(nx, ny, grid, visited):
            longest = max(longest, dfs(nx, ny, grid, visited | {(nx, ny)}))
    return longest


def find_longest_hike(input_text):
    grid = parse_input(input_text)
    start_x = grid[0].index('.')
    return dfs(start_x, 0, grid, {(start_x, 0)})

# Example usage:
sys.setrecursionlimit(1000000)
input_path = "input.txt"
result = find_longest_hike(input_path)
print(f"Length of the longest hike: {result-1}") # i fd smthing up here, fix it
