# Read grid and find all antenna positions by frequency
from collections import defaultdict

grid = [list(l.strip()) for l in open('input.txt') if l.strip()]
R, C = len(grid), len(grid[0])

# Group antennas by frequency
antennas = defaultdict(list)
for i in range(R):
    for j in range(C):
        if grid[i][j] not in '.':
            antennas[grid[i][j]].append((i,j))

def get_antinode(p1, p2):
    # Get both antinode positions given two antenna positions
    x1,y1 = p1
    x2,y2 = p2
    
    # Vector from p1 to p2
    dx = x2 - x1
    dy = y2 - y1
    
    # Get both antinodes (1/2 and 2x distance)
    results = []
    
    # Half distance point
    x3 = x1 + dx/2
    y3 = y1 + dy/2
    # Double distance point
    x4 = x2 + dx
    y4 = y2 + dy
    # And other side
    x5 = x1 - dx
    y5 = y1 - dy
    
    for x,y in [(x3,y3), (x4,y4), (x5,y5)]:
        # Check if in bounds and is integer position
        if (0 <= x < R and 0 <= y < C and 
            abs(x - round(x)) < 1e-10 and 
            abs(y - round(y)) < 1e-10):
            results.append((round(x),round(y)))
    
    return results

antinodes = set()

# For each frequency, check all pairs
for freq in antennas:
    points = antennas[freq]
    for i,p1 in enumerate(points):
        for j,p2 in enumerate(points[i+1:], i+1):
            for antinode in get_antinode(p1, p2):
                antinodes.add(antinode)

print(len(antinodes))