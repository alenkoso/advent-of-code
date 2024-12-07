import os
import sys
from collections import defaultdict

class SimpleDeque:
    def __init__(self):
        self.items = []

    def append(self, item):
        # Add an item to the right end of the deque.
        self.items.append(item)

    def popleft(self):
        # Remove and return an item from the left end of the deque.
        if self.is_empty():
            raise IndexError("pop from an empty deque")
        return self.items.pop(0)

    def is_empty(self):
        # Check if the deque is empty. 
        return len(self.items) == 0

# Adjusting the import path for parsing_utils
project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(project_root)
from helpers.parsing_utils import read_input_file_to_grid

grid = read_input_file_to_grid("input.txt")
row_count = len(grid)
col_count = len(grid[0])

sys.setrecursionlimit(10**6)

def solve_maze():
    vertex_set = set()
    edges = defaultdict(list)

    # Identify potential vertices
    for row in range(row_count):
        for col in range(col_count):
            neighbor_count = 0
            for delta_row, delta_col in [['^', -1, 0], ['v', 1, 0], ['<', 0, -1], ['>', 0, 1]]:
                if (0 <= row + delta_row < row_count and 0 <= col + delta_col < col_count and grid[row + delta_row][col + delta_col] != '#'):
                    neighbor_count += 1
            if neighbor_count > 2 and grid[row][col] != '#':
                vertex_set.add((row, col))

    # Identify start and end points
    for col in range(col_count):
        if grid[0][col] == '.':
            vertex_set.add((0, col))
            start_point = (0, col)
        if grid[row_count - 1][col] == '.':
            vertex_set.add((row_count - 1, col))

    # Build edges
    for (vertex_row, vertex_col) in vertex_set:
        queue = SimpleDeque()
        queue.append((vertex_row, vertex_col, 0))
        seen = set()
        while not queue.is_empty():
            current_row, current_col, distance = queue.popleft()
            if (current_row, current_col) in seen:
                continue
            seen.add((current_row, current_col))
            if (current_row, current_col) in vertex_set and (current_row, current_col) != (vertex_row, vertex_col):
                edges[(vertex_row, vertex_col)].append(((current_row, current_col), distance))
                continue
            for delta_row, delta_col in [['^', -1, 0], ['v', 1, 0], ['<', 0, -1], ['>', 0, 1]]:
                if (0 <= current_row + delta_row < row_count and 0 <= current_col + delta_col < col_count and grid[current_row + delta_row][current_col + delta_col] != '#'):
                    queue.append((current_row + delta_row, current_col + delta_col, distance + 1))

    # Depth-first search to find the longest path
    max_distance = 0
    visited = [[False for _ in range(col_count)] for _ in range(row_count)]
    def dfs(vertex, distance):
        nonlocal max_distance
        row, col = vertex
        if visited[row][col]:
            return
        visited[row][col] = True
        if row == row_count - 1:
            max_distance = max(max_distance, distance)
        for (next_vertex, edge_distance) in edges[vertex]:
            dfs(next_vertex, distance + edge_distance)
        visited[row][col] = False

    dfs(start_point, 0)
    return max_distance

print(f"Max Distance: {solve_maze()}")
