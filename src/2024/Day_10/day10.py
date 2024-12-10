import sys
import os
from collections import deque

project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(project_root)

from helpers.file_utils import read_input_file

def find_trails(grid, start):
    rows, cols = len(grid), len(grid[0])
    reachable_nines = set()
    visited = set()
    queue = deque([(start[0], start[1], 0)])  # row, col, current_height
    
    while queue:
        r, c, height = queue.popleft()
        
        if (r, c) in visited:
            continue
            
        visited.add((r, c))
        
        # Found a reachable 9
        if grid[r][c] == 9:
            reachable_nines.add((r, c))
            continue
            
        # Try all four directions
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols and 
                grid[nr][nc] == height + 1 and 
                (nr, nc) not in visited):
                queue.append((nr, nc, height + 1))
                
    return len(reachable_nines)

def count_trails(grid, start, cache):
    rows, cols = len(grid), len(grid[0])
    
    def dfs(r, c, height):
        # Cache key for current position and height
        state = (r, c, height)
        if state in cache:
            return cache[state]
            
        # Found valid endpoint
        if grid[r][c] == 9:
            cache[state] = 1
            return 1
            
        # Count paths from current position
        paths = 0
        # Try all four directions
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols and 
                grid[nr][nc] != -1 and      # Not impassable
                grid[nr][nc] == height + 1):
                paths += dfs(nr, nc, height + 1)
        
        cache[state] = paths
        return paths
    
    return dfs(start[0], start[1], 0)

def solve_part1(lines):
    # Parse grid
    grid = [[int(c) for c in line] for line in lines]
    rows, cols = len(grid), len(grid[0])
    
    # Find all trailheads (height 0)
    total_score = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                score = find_trails(grid, (r, c))
                total_score += score
                
    return total_score

def solve_part2(lines):
    # Parse grid
    grid = [[int(c) for c in line] for line in lines]
    rows, cols = len(grid), len(grid[0])
    
    # Find all trailheads (height 0) and count distinct paths
    total_rating = 0
    cache = {}  # Shared cache for all trailheads
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                rating = count_trails(grid, (r, c), cache)
                total_rating += rating
                
    return total_rating

def main():
    # Read input
    lines = read_input_file('input.txt', mode='lines_stripped')
    
    # Test with example from part 1
    test_input = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732""".splitlines()
    
    # Solve Part 1
    test_result_1 = solve_part1(test_input)
    print(f"Test Part 1: {test_result_1}")  # Should be 36
    result_1 = solve_part1(lines)
    print(f"Part 1: {result_1}")
    
    # Solve Part 2
    test_result_2 = solve_part2(test_input)
    print(f"Test Part 2: {test_result_2}")  # Should be 81
    result_2 = solve_part2(lines)
    print(f"Part 2: {result_2}")

if __name__ == "__main__":
    main()