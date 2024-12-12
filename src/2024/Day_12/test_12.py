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

def test_part1_example1(example1_grid):
    assert day12.solve_part1(example1_grid) == 140

def test_part1_example2(example2_grid):
    assert day12.solve_part1(example2_grid) == 772

def test_part2_example1(example1_grid):
    assert day12.solve_part2(example1_grid) == 80

def test_part2_example2(example2_grid):
    assert day12.solve_part2(example2_grid) == 436

def test_part2_example3(example3_grid):
    assert day12.solve_part2(example3_grid) == 236

def test_count_sides():
    # Test a simple square region
    region = {(0,0), (0,1), (1,0), (1,1)}
    grid = [['A', 'A'], ['A', 'A']]
    assert day12.count_sides(region, grid) == 4

def test_count_sides_complex():
    # Test E-shaped region from example
    grid = [list("EEEEE"), list("EXXXX"), list("EEEEE"), list("EXXXX"), list("EEEEE")]
    regions = day12.find_regions(grid)
    e_region = next(r for r in regions if r[0] == 'E')[1]
    assert day12.count_sides(e_region, grid) == 12

def test_single_cell():
    grid = [['A']]
    assert day12.solve_part2(grid) == 4  # area=1 * sides=4