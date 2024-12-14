import pytest
import importlib.util

# Import solution
spec = importlib.util.spec_from_file_location("solution", "day12.py")
day12 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(day12)

def test_count_region_sides_part1():
    region_cells = {(0, 0), (0, 1), (1, 0), (1, 1)}
    assert day12.count_region_sides_part1(region_cells) == 8

    region_cells = {(0, 0), (0, 1), (1, 0), (1, 1), (1, 2)}
    assert day12.count_region_sides_part1(region_cells) == 10

def test_count_region_sides_part2():
    region_cells = {(0, 0), (0, 1), (1, 0), (1, 1)}
    assert day12.count_region_sides_part2(region_cells) == 4

    region_cells = {(0, 0), (0, 1), (1, 0), (1, 1), (1, 2)}
    assert day12.count_region_sides_part2(region_cells) == 8

def test_solve_landscape_part1():
    terrain_grid = [
        ['A', 'A', 'A', 'A'],
        ['B', 'B', 'C', 'D'],
        ['B', 'B', 'C', 'C'],
        ['E', 'E', 'E', 'C']
    ]
    result = day12.solve_landscape(terrain_grid, is_part2=False)
    assert result == 140

def test_solve_landscape_part2():
    terrain_grid = [
        ['A', 'A', 'A', 'A'],
        ['B', 'B', 'C', 'D'],
        ['B', 'B', 'C', 'C'],
        ['E', 'E', 'E', 'C']
    ]
    result = day12.solve_landscape(terrain_grid, is_part2=True)
    assert result == 80

def test_solve_landscape_edge_case():
    terrain_grid = [['A']]
    result = day12.solve_landscape(terrain_grid, is_part2=False)
    assert result == 4

    terrain_grid = [['A', 'B', 'C']]
    result = day12.solve_landscape(terrain_grid, is_part2=False)
    assert result == 12

    terrain_grid = [['A'], ['B'], ['C']]
    result = day12.solve_landscape(terrain_grid, is_part2=False)
    assert result == 12

def test_solve_landscape_complex_case():
    terrain_grid = [
        ['R', 'R', 'R', 'R', 'I', 'C', 'C', 'F', 'F'],
        ['R', 'R', 'R', 'I', 'C', 'C', 'C', 'F', 'F'],
        ['V', 'V', 'R', 'R', 'C', 'C', 'F', 'F', 'F'],
        ['V', 'V', 'R', 'C', 'C', 'J', 'F', 'F', 'F'],
        ['V', 'V', 'V', 'C', 'J', 'J', 'C', 'E', 'E'],
        ['V', 'V', 'I', 'C', 'C', 'J', 'J', 'E', 'E'],
        ['V', 'V', 'I', 'I', 'C', 'J', 'J', 'E', 'E'],
        ['M', 'I', 'I', 'I', 'I', 'J', 'J', 'E', 'E'],
        ['M', 'M', 'I', 'S', 'I', 'J', 'J', 'E', 'E'],
        ['M', 'M', 'I', 'S', 'J', 'J', 'J', 'E', 'E']
    ]
    result = day12.solve_landscape(terrain_grid, is_part2=False)
    assert result == 1930

def test_solve_landscape_bulk_discount_case():
    terrain_grid = [
        ['E', 'E', 'E', 'E', 'E'],
        ['E', 'X', 'X', 'X', 'E'],
        ['E', 'X', 'O', 'X', 'E'],
        ['E', 'X', 'X', 'X', 'E'],
        ['E', 'E', 'E', 'E', 'E']
    ]
    result = day12.solve_landscape(terrain_grid, is_part2=True)
    assert result == 236

@pytest.mark.parametrize("terrain_grid, expected_result", [
    ([
        ['A', 'A', 'A', 'A'],
        ['B', 'B', 'C', 'D'],
        ['B', 'B', 'C', 'C'],
        ['E', 'E', 'E', 'C']
    ], 140),
    ([
        ['A', 'A', 'A', 'A'],
        ['B', 'B', 'C', 'D'],
        ['B', 'B', 'C', 'C'],
        ['E', 'E', 'E', 'C']
    ], 80),
])
def test_solve_landscape_parametrized(terrain_grid, expected_result):
    result = day12.solve_landscape(terrain_grid, is_part2=True)
    assert result == expected_result

if __name__ == "__main__":
    pytest.main()
