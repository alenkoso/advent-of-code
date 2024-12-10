# test_10.py
from collections import deque
import pytest
import importlib.util

# Import solution module
spec = importlib.util.spec_from_file_location("solution", "day10.py")
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def create_grid_from_str(grid_str):
    grid = []
    for line in grid_str.splitlines():
        line = line.strip()
        if not line:
            continue
        # Handle -1 as a special case
        row = []
        i = 0
        while i < len(line):
            if line[i:i+2] == '-1':
                row.append(-1)
                i += 2
            else:
                row.append(int(line[i]))
                i += 1
        grid.append(row)
    return grid

def validate_path_possible(grid, start_pos, end_pos):
    """Helper function to validate if a path is possible between positions"""
    rows, cols = len(grid), len(grid[0])
    visited = set()
    queue = deque([(start_pos[0], start_pos[1], grid[start_pos[0]][start_pos[1]])])
    
    while queue:
        r, c, height = queue.popleft()
        if (r, c) == end_pos:
            return True
            
        if (r, c) in visited:
            continue
            
        visited.add((r, c))
        
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols and 
                grid[nr][nc] == height + 1 and
                (nr, nc) not in visited):
                queue.append((nr, nc, grid[nr][nc]))
                
    return False

@pytest.fixture
def large_example_grid():
    return [
        "89010123",
        "78121874",
        "87430965",
        "96549874",
        "45678903",
        "32019012",
        "01329801",
        "10456732"
    ]

def test_basic_square_grid():
    grid = create_grid_from_str("""
    0123
    1234
    8765
    9876
    """)
    assert grid[0][0] == 0  # Validate start position
    assert solution.find_trails(grid, (0,0)) == 1

def test_simple_vertical_grid():
    grid = create_grid_from_str("""
    ...0...
    ...1...
    ...2...
    6543456
    7.....7
    8.....8
    9.....9
    """.replace('.', '-1'))
    assert grid[0][3] == 0  # Validate start position
    assert solution.find_trails(grid, (0,3)) == 2

def test_complex_grid_with_multiple_paths():
    grid = create_grid_from_str("""
    ..90..9
    ...1.98
    ...2..7
    6543456
    765.987
    876....
    987....
    """.replace('.', '-1'))
    assert grid[0][3] == 0  # Start position
    assert solution.find_trails(grid, (0,3)) == 4

def test_part1_large_example(large_example_grid):
    assert solution.solve_part1(large_example_grid) == 36

def test_part2_simple_path_count():
    grid = create_grid_from_str("""
    .....0.
    ..4321.
    ..5..2.
    ..6543.
    ..7..4.
    ..8765.
    ..9....
    """.replace('.', '-1'))
    assert grid[0][5] == 0  # Start position
    cache = {}
    assert solution.count_trails(grid, (0,5), cache) == 3

def test_part2_complex_path_count():
    grid = create_grid_from_str("""
    ..90..9
    ...1.98
    ...2..7
    6543456
    765.987
    876....
    987....
    """.replace('.', '-1'))
    assert grid[0][3] == 0  # Start position
    cache = {}
    assert solution.count_trails(grid, (0,3), cache) == 13

def test_part2_227_paths():
    grid = create_grid_from_str("""
    012345
    123456
    234567
    345678
    4.6789
    56789.
    """.replace('.', '-1'))
    assert grid[0][0] == 0  # Start position
    cache = {}
    assert solution.count_trails(grid, (0,0), cache) == 227

def test_part2_large_example(large_example_grid):
    assert solution.solve_part2(large_example_grid) == 81

def test_grid_creation():
    """Test the grid creation function itself"""
    grid = create_grid_from_str("""
    ..1
    .2.
    3..
    """.replace('.', '-1'))
    assert grid == [
        [-1, -1, 1],
        [-1, 2, -1],
        [3, -1, -1]
    ]

def test_no_invalid_paths():
    """Test that paths cannot move diagonally or decrease in height"""
    grid = create_grid_from_str("""
    0123
    2198
    3987
    4567
    """)
    # Should not be able to reach 9 moving diagonally
    assert solution.find_trails(grid, (0,0)) == 0