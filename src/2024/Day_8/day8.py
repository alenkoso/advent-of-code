import sys
import os
import time
from collections import defaultdict

project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(project_root)

from helpers.file_utils import read_input_file

def parse_input(lines):
    # Create grid and track antenna positions
    grid = []
    antennas = defaultdict(list)
    
    for i, line in enumerate(lines):
        grid.append(list(line.strip()))
        for j, c in enumerate(line.strip()):
            if c != '.':
                antennas[c].append((i, j))
                
    return grid, antennas

def is_collinear(p1, p2, p3=None):
    if p3 is None:
        x1, y1 = p1
        x2, y2 = p2
        dx = x2 - x1
        dy = y2 - y1
        
        if dx == 0 and dy == 0:
            return []
            
        # Calculate points at double distance
        points = [
            (x1 - dx, y1 - dy),
            (x2 + dx, y2 + dy)
        ]
        return points
    else:
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3
        return (y2 - y1) * (x3 - x1) == (y3 - y1) * (x2 - x1)

def find_antinodes(grid, antennas, part2=False):
    height = len(grid)
    width = len(grid[0])
    antinodes = set()

    for freq, points in antennas.items():
        if len(points) < 2:
            continue

        if part2:
            # Add antenna positions for same frequency
            if len(points) > 1:
                antinodes.update(points)

            # Check all grid points for collinearity
            for i, p1 in enumerate(points):
                for j, p2 in enumerate(points[i+1:], i+1):
                    for x in range(height):
                        for y in range(width):
                            if (x,y) != p1 and (x,y) != p2 and is_collinear(p1, p2, (x,y)):
                                antinodes.add((x,y))
        else:
            # Part 1: Check points at double distance
            for i, p1 in enumerate(points):
                for p2 in points[i+1:]:
                    potential_points = is_collinear(p1, p2)
                    for x, y in potential_points:
                        if 0 <= x < height and 0 <= y < width:
                            antinodes.add((x, y))

    return len(antinodes)

def main():
    # Read input
    lines = read_input_file('input.txt', mode='lines_stripped')
    grid, antennas = parse_input(lines)
    
    # Part 1
    start_time = time.time()
    part1_result = find_antinodes(grid, antennas)
    end_time = time.time()
    print(f"Part 1: {part1_result}")
    print(f"Part 1 Execution Time: {end_time - start_time} seconds")
    
    # Part 2
    start_time = time.time()
    part2_result = find_antinodes(grid, antennas, True)
    end_time = time.time()
    print(f"Part 2: {part2_result}")
    print(f"Part 2 Execution Time: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()