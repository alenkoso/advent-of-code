import pytest
import importlib.util

# Import solution
spec = importlib.util.spec_from_file_location("solution", "day12.py")
day12 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(day12)

@pytest.fixture
def example1_grid():
    return [
        list("AAAA"),
        list("BBCD"),
        list("BBCC"),
        list("EEEC")
    ]

@pytest.fixture
def example2_grid():
    return [
        list("OOOOO"),
        list("OXOXO"),
        list("OOOOO"),
        list("OXOXO"),
        list("OOOOO")
    ]

@pytest.fixture
def example3_grid():
    return [
        list("EEEEE"),
        list("EXXXX"),
        list("EEEEE"),
        list("EXXXX"),
        list("EEEEE")
    ]

# Part 1 Tests
def test_part1_example1(example1_grid):
    assert day12.explore_landscape_part1(example1_grid) == 140

def test_part1_example2(example2_grid):
    assert day12.explore_landscape_part1(example2_grid) == 772

def test_part1_single_cell():
    grid = [['A']]
    assert day12.explore_landscape_part1(grid) == 4

def test_part1_two_cells_adjacent():
    grid = [
        ['A', 'A'],
        ['B', 'B']
    ]
    assert day12.explore_landscape_part1(grid) == 12

def test_part1_multiple_regions():
    grid = [
        ['A', 'B', 'C'],
        ['A', 'B', 'C'],
        ['D', 'E', 'F']
    ]
    assert day12.explore_landscape_part1(grid) > 0

def test_part1_large_region():
    grid = [['X' for _ in range(10)] for _ in range(10)]
    assert day12.explore_landscape_part1(grid) == 400

# Part 2 Tests
def test_part2_example1(example1_grid):
    assert day12.explore_landscape_part2(example1_grid) == 80

def test_part2_example2(example2_grid):
    assert day12.explore_landscape_part2(example2_grid) == 436

def test_part2_example3(example3_grid):
    assert day12.explore_landscape_part2(example3_grid) == 236

def test_part2_single_cell():
    grid = [['A']]
    assert day12.explore_landscape_part2(grid) == 4  # area=1 * sides=4

def test_part2_two_cells_adjacent():
    grid = [
        ['A', 'A'],
        ['B', 'B']
    ]
    assert day12.explore_landscape_part2(grid) == 4

def test_part2_complex_shape():
    grid = [
        list("AAAAA"),
        list("ABBBA"),
        list("ABBBA"),
        list("AAAAA")
    ]
    # Checks for regions with internal divisions
    assert day12.explore_landscape_part2(grid) > 0

def test_part2_different_char_regions():
    grid = [
        ['A', 'B', 'C'],
        ['D', 'E', 'F'],
        ['G', 'H', 'I']
    ]
    assert day12.explore_landscape_part2(grid) > 0

def test_part2_large_region():
    grid = [['X' for _ in range(10)] for _ in range(10)]
    assert day12.explore_landscape_part2(grid) == 40

def test_part2_irregular_shape():
    grid = [
        list("EEEEE"),
        list("EXEXE"),
        list("EEEEE")
    ]
    # Checks for regions with non-rectangular shapes
    assert day12.explore_landscape_part2(grid) > 0

# Edge Cases
def test_empty_grid():
    grid = []
    assert day12.explore_landscape_part1(grid) == 0
    assert day12.explore_landscape_part2(grid) == 0

def test_grid_with_single_type():
    grid = [['A', 'A', 'A'], ['A', 'A', 'A']]
    assert day12.explore_landscape_part1(grid) == len(grid) * len(grid[0]) * 2
    assert day12.explore_landscape_part2(grid) == 4

def test_grid_with_different_length_rows():
    grid = [
        list("ABCD"),
        list("EFGH"),
        list("IJK")
    ]
    # Ensures the code handles rows of different lengths
    assert day12.explore_landscape_part1(grid) > 0
    assert day12.explore_landscape_part2(grid) > 0