import sys
import os
from collections import defaultdict

project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(project_root)

from helpers.parsing_utils import read_input_file_to_grid

def find_regions(grid):
    seen = set()
    regions = []
    
    def flood_fill(x, y, char):
        if (x, y) in seen or x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] != char:
            return set()
        
        region = {(x, y)}
        seen.add((x, y))
        
        # Check all 4 directions
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                region.update(flood_fill(nx, ny, char))
            
        return region
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i,j) not in seen:
                region = flood_fill(i, j, grid[i][j])
                if region:
                    regions.append((grid[i][j], region))
    
    return regions

def calc_perimeter(region, grid):
    perimeter = 0
    for x, y in region:
        # Count each exposed side
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in region:  # Side is exposed if adjacent cell isn't in region
                perimeter += 1
                
    return perimeter

def solve(grid):
    total = 0
    regions = find_regions(grid)
    
    for char, region in regions:
        area = len(region)
        perimeter = calc_perimeter(region, grid)
        total += area * perimeter
        
    return total

def main():
    grid = read_input_file_to_grid("input.txt")
    result = solve(grid)
    print(f"Part 1: {result}")

if __name__ == "__main__":
    main()