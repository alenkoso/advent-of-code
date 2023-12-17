import heapq

def read_input_file(file_path):
    with open(file_path, 'r') as file:
        return [[int(cell) for cell in line.strip()] for line in file]

def calculate_min_heat_loss(grid):
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    heap = [(0, 0, 0, -1)]  # Heat loss, row, col, last direction index
    visited = set()

    while heap:
        heat_loss, row, col, last_dir_idx = heapq.heappop(heap)
        if (row, col) == (rows - 1, cols - 1):
            return heat_loss
        if (row, col, last_dir_idx) in visited:
            continue
        visited.add((row, col, last_dir_idx))

        for d_idx, (dr, dc) in enumerate(directions):
            if d_idx == (last_dir_idx + 2) % 4:  # Skip reverse direction
                continue

            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < rows and 0 <= new_col < cols:
                new_heat_loss = heat_loss + grid[new_row][new_col]
                heapq.heappush(heap, (new_heat_loss, new_row, new_col, d_idx))

def main():
    input_file = "example.txt"
    grid = read_input_file(input_file)
    min_heat_loss = calculate_min_heat_loss(grid)
    print(f"Minimum Heat Loss: {min_heat_loss}")

if __name__ == "__main__":
    main()
