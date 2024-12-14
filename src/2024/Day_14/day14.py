import os
import sys
from collections import deque
import time

project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(project_root)

from helpers.parsing_utils import read_input_file_strip_lines

# WIDHT = 101
# 103 = 103

def parse_robots(lines):
    robots = []
    for line in lines:
        print(f"Debug: raw line = '{line}'")  # Debug print
        try:
            # Try different parsing approaches based on the format
            numbers = [int(x) for x in line.split() if x.isdigit()]
            if len(numbers) >= 4:
                x, y, dx, dy = numbers[:4]
                robots.append([x, y, dx, dy])
        except Exception as e:
            print(f"Error parsing line: {line}")
            print(f"Exception: {e}")
            raise
    return robots

def print_grid(grid):
    for row in grid:
        print(''.join(row))
    print()

def find_separate_components(robots):
    # Create grid representation
    grid = [['.' for _ in range(103)] for _ in range(101)]
    for x,y,_,_ in robots:
        x = x % 101
        y = y % 103
        grid[x][y] = '#'
    
    # Find connected components using BFS
    dirs = [(-1,0), (0,1), (1,0), (0,-1)]
    seen = set()
    components = 0
    
    for x in range(101):
        for y in range(103):
            if grid[x][y] == '#' and (x,y) not in seen:
                components += 1
                queue = deque([(x,y)])
                while queue:
                    cx, cy = queue.popleft()
                    if (cx,cy) in seen:
                        continue
                    seen.add((cx,cy))
                    for dx,dy in dirs:
                        nx, ny = cx+dx, cy+dy
                        if 0 <= nx < 101 and 0 <= ny < 103 and grid[nx][ny] == '#':
                            queue.append((nx,ny))
                            
    # Print the current grid state
    if components <= 400:
        print(f"\nGrid state at step with {components} components:")
        print_grid(grid)
    
    return components
            

if __name__ == "__main__":
    # Read and parse the input file
    lines = read_input_file_strip_lines("input.txt")

    robots = []
    for line in lines:
        p_part, v_part = line.split(' v=')
        px, py = map(int, p_part[2:].split(','))
        vx, vy = map(int, v_part.split(','))
        robots.append([px, py, vx, vy])


    start_time = time.time()

    for t in range(1, 10**6):
        # Create fresh grid for visualization
        G = [['.' for _ in range(103)] for _ in range(101)]

        for i, (px, py, vx, vy) in enumerate(robots):
            px += vx
            py += vy

            # Wrap coordinates around edges
            px %= 101
            py %= 103

            robots[i] = [px, py, vx, vy]
            G[px][py] = '#'

        # Count connected components
        components = 0
        SEEN = set()

        for x in range(101):
            for y in range(103):
                if G[x][y] == '#' and (x, y) not in SEEN:
                    components += 1
                    Q = deque([(x, y)])

                    while Q:
                        cx, cy = Q.popleft()
                        if (cx, cy) in SEEN:
                            continue
                        SEEN.add((cx, cy))

                        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                            nx, ny = (cx + dx) % 101, (cy + dy) % 103
                            if G[nx][ny] == '#' and (nx, ny) not in SEEN:
                                Q.append((nx, ny))

        # Detect Easter egg: Example threshold refinement
        if components <= 400:  # Adjust this value based on pattern
            print(f"Part 2: {t}")
            print(f"Part 2 Execution Time: {time.time() - start_time:.2f} seconds")
            print(f"Components: {components}")

            # Visualize grid
            print(f"\nGrid at step {t}:")
            for row in G:
                print(''.join(row))