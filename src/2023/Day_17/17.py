import heapq
import time

def solve(grid, min_dist, max_dist):
    R, C = len(grid), len(grid[0])
    DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

    q = [(0, 0, 0, -1, 0)]  # (cost, x, y, direction, distance in current direction)
    seen = set()
    costs = {}

    while q:
        cost, x, y, prev_dir, dist = heapq.heappop(q)
        if (x, y) == (R - 1, C - 1):  # Reached destination
            return cost
        if (x, y, prev_dir) in seen:
            continue
        seen.add((x, y, prev_dir))

        for new_dir, (dx, dy) in enumerate(DIRS):
            if new_dir == (prev_dir + 2) % 4:  # Prevent reversing direction
                continue
            if prev_dir != new_dir and dist < min_dist:  # Minimum distance check
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C:
                new_cost = cost + int(grid[nx][ny])
                new_dist = dist + 1 if new_dir == prev_dir else 1
                if new_dist > max_dist or costs.get((nx, ny, new_dir), float('inf')) <= new_cost:
                    continue
                costs[(nx, ny, new_dir)] = new_cost
                heapq.heappush(q, (new_cost, nx, ny, new_dir, new_dist))

    return float('inf')  # In case no path is found

def main():
    # Read input and process
    # ...

    # Part One
    start_time = time.time()
    min_heat_loss_normal = solve(grid, 1, 3)
    print(f"Part One Result: {min_heat_loss_normal}")
    end_time = time.time()
    print(f"Part One Execution Time: {end_time - start_time} seconds")

    # Part Two
    start_time = time.time()
    min_heat_loss_ultra = solve(grid, 4, 10)
    print(f"Part Two Result: {min_heat_loss_ultra}")
    end_time = time.time()
    print(f"Part Two Execution Time: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()
