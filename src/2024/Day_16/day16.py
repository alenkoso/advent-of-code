import heapq

def parse_input(file_path):
    grid = []
    with open(file_path, 'r') as file:
        for line in file:
            grid.append(list(line.strip()))
    return grid

def parse_positions(grid):
    start, end = None, None
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "S":
                start = (r, c)
            elif grid[r][c] == "E":
                end = (r, c)
    return start, end

def part1(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    q = [(0, start[0], start[1], 1)]
    visited = set()
    best_score = None
    path_costs = {}

    while q:
        cost, r, c, d = heapq.heappop(q)
        if (r, c, d) in visited:
            continue
        visited.add((r, c, d))
        path_costs[(r, c, d)] = cost
        if (r, c) == end:
            if best_score is None:
                best_score = cost
                break
        dr, dc = directions[d]
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != "#":
            heapq.heappush(q, (cost + 1, nr, nc, d))
        heapq.heappush(q, (cost + 1000, r, c, (d + 1) % 4))
        heapq.heappush(q, (cost + 1000, r, c, (d - 1) % 4))

    return best_score, path_costs

def part2(grid, start, end, best_score, forward_costs):
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    q = [(0, end[0], end[1], d) for d in range(4)]
    visited = set()
    backward_costs = {}
    optimal_tiles = set()

    while q:
        cost, r, c, d = heapq.heappop(q)
        if (r, c, d) in visited:
            continue
        visited.add((r, c, d))
        backward_costs[(r, c, d)] = cost
        dr, dc = directions[(d + 2) % 4]
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != "#":
            heapq.heappush(q, (cost + 1, nr, nc, d))
        heapq.heappush(q, (cost + 1000, r, c, (d + 1) % 4))
        heapq.heappush(q, (cost + 1000, r, c, (d - 1) % 4))

    for r in range(rows):
        for c in range(cols):
            for d in range(4):
                if (r, c, d) in forward_costs and (r, c, d) in backward_costs:
                    total_cost = forward_costs[(r, c, d)] + backward_costs[(r, c, d)]
                    if total_cost == best_score:
                        optimal_tiles.add((r, c))

    return len(optimal_tiles)

if __name__ == "__main__":
    grid = parse_input("input.txt")
    start, end = parse_positions(grid)
    
    score, forward_costs = part1(grid, start, end)
    print(f"Part 1: {score}")
    optimal_count = part2(grid, start, end, score, forward_costs)
    print(f"Part 2: {optimal_count}")
