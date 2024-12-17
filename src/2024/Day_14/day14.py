from collections import deque, defaultdict

def parse_input(filename):
    robots = []
    with open(filename) as f:
        for line in f:
            pos, vel = line.strip().split()
            x, y = map(int, pos.replace('p=','').split(','))
            dx, dy = map(int, vel.replace('v=','').split(','))
            robots.append([x, y, dx, dy])
    return robots

def simulate_step(robots):
    for i, (x, y, dx, dy) in enumerate(robots):
        x = (x + dx) % 101  # Width
        y = (y + dy) % 103  # Height
        robots[i] = [x, y, dx, dy]
    return robots

def calculate_safety_factor(robots):
    # Count robots at each position
    pos = defaultdict(int)
    for r in robots:
        pos[(r[0], r[1])] += 1
    
    # Calculate quadrant counts
    mx, my = 101//2, 103//2
    quadrants = [0] * 4
    
    for (x, y), count in pos.items():
        if x == mx or y == my:
            continue
        idx = (1 if x > mx else 0) + (2 if y > my else 0)
        quadrants[idx] += count
    
    # Calculate safety factor
    safety_factor = 1
    for n in quadrants:
        safety_factor *= n
    return safety_factor

def count_components(robots):
    # Create grid
    grid = [['.' for _ in range(103)] for _ in range(101)]
    for x, y, _, _ in robots:
        grid[x][y] = '#'
    
    # Count components using BFS
    components = 0
    seen = set()
    dirs = [(-1,0), (1,0), (0,-1), (0,1)]
    
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
                    for dx, dy in dirs:
                        nx, ny = (cx + dx) % 101, (cy + dy) % 103
                        if grid[nx][ny] == '#' and (nx,ny) not in seen:
                            queue.append((nx,ny))
    return components

def solve():
    robots = parse_input('input.txt')
    
    # Part 1: Calculate safety factor at t=100
    for t in range(100):
        robots = simulate_step(robots)
    
    safety_factor = calculate_safety_factor(robots)
    print("Part 1: ", safety_factor)
    
    # Part 2: Find Easter egg pattern
    step = 100
    while True:
        step += 1
        robots = simulate_step(robots)
        components = count_components(robots)
        
        if components <= 200:
            print("Part 2: ", step)
            break

if __name__ == "__main__":
    solve()