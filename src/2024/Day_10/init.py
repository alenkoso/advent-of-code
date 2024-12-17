from collections import deque

def parse_input(file_path):
    with open(file_path) as file:
        return [line.strip() for line in file]

def explore(grid, r, c):
    rows, cols = len(grid), len(grid[0])
    q = deque([(r, c, 0)])
    seen = set()
    nines = set()
    
    while q:
        r, c, h = q.popleft()
        if (r, c) in seen:
            continue
            
        seen.add((r, c))
        curr = grid[r][c]
        
        if curr == 9:
            nines.add((r, c))
            continue
            
        if curr != h:
            continue
            
        for nr, nc in [(r-1,c), (r+1,c), (r,c-1), (r,c+1)]:
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == h + 1:
                q.append((nr, nc, h + 1))
                
    return nines

def dfs(grid, r, c, h, memo=None):
    if memo is None:
        memo = {}
        
    if (r, c, h) in memo:
        return memo[(r, c, h)]
        
    if not (0 <= r < len(grid) and 0 <= c < len(grid[0])):
        return 0
        
    if grid[r][c] != h:
        return 0
        
    if h == 9:
        return 1
        
    total = 0
    for nr, nc in [(r-1,c), (r+1,c), (r,c-1), (r,c+1)]:
        total += dfs(grid, nr, nc, h + 1, memo)
        
    memo[(r, c, h)] = total
    return total

def solve(data):
    grid = [[int(x) for x in row] for row in data]
    rows, cols = len(grid), len(grid[0])
    
    starts = [(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 0]
    p1 = sum(len(explore(grid, r, c)) for r, c in starts)
    
    memo = {}
    p2 = sum(dfs(grid, r, c, 0, memo) for r, c in starts)
    
    return p1, p2

def main():    
    data = parse_input("input.txt")
    p1, p2 = solve(data)
    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")

if __name__ == "__main__":
    main()