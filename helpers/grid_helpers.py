# grid_helpers.py

def create_grid(rows, cols, default_value=0):
    ### Create a grid (2D list) initialized with a default value. ###
    return [[default_value for _ in range(cols)] for _ in range(rows)]

def print_grid(grid):
    ### Print the grid in a readable format. ###
    for row in grid:
        print(' '.join(str(cell) for cell in row))

def get_neighbors(r, c, grid):
    ### Get valid neighbors for a cell in the grid. ###
    neighbors = []
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Up, Down, Left, Right
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
            neighbors.append((nr, nc))
    return neighbors

