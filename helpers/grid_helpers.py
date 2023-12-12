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


class Grid:
    def __init__(self, grid_data):
        self.grid = grid_data
        self.height = len(grid_data)
        self.width = len(grid_data[0]) if self.height > 0 else 0

    @classmethod
    def from_file(cls, file_path):
        with open(file_path, 'r') as file:
            grid_data = [list(line.strip()) for line in file.readlines()]
        return cls(grid_data)

    def get(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid[y][x]
        return None

    def set(self, x, y, value):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = value

    def expand(self):
        # Expands the rows and columns that are empty
        expanded_grid = [['.' for _ in range(self.width * 2)] for _ in range(self.height * 2)]

        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] != '.':
                    expanded_grid[y * 2][x * 2] = self.grid[y][x]
                    expanded_grid[y * 2 + 1][x * 2] = self.grid[y][x]
                    expanded_grid[y * 2][x * 2 + 1] = self.grid[y][x]
                    expanded_grid[y * 2 + 1][x * 2 + 1] = self.grid[y][x]

        self.grid = expanded_grid
        self.height *= 2
        self.width *= 2