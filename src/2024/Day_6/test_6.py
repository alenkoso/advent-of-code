import pytest
import importlib.util

# Import solution
spec = importlib.util.spec_from_file_location("solution", "day6.py")
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

@pytest.fixture
def example_input():
    return [
        "....#.....",
        ".........#",
        "..........",
        "..#.......",
        ".......#..",
        "..........",
        ".#..^.....",
        "........#.",
        "#.........",
        "......#..."
    ]

def test_parse_input(example_input):
    """Test that the input is parsed correctly and guard position is found"""
    lab_grid, guard_start = solution.parse_input(example_input)
    assert len(lab_grid) == 10  # 10 rows
    assert len(lab_grid[0]) == 10  # 10 columns
    assert guard_start == (6, 4)  # Guard starts at row 6, col 4
    assert lab_grid[6][4] == '.'  # Guard position should be replaced with '.'

def test_part1_example(example_input):
    """Test Part 1 with the example from instructions"""
    lab_grid, guard_start = solution.parse_input(example_input)
    result = solution.solve_part1(lab_grid, guard_start)
    assert result == 41  # Example should visit 41 distinct positions

def test_part2_example(example_input):
    """Test Part 2 with the example from instructions"""
    lab_grid, guard_start = solution.parse_input(example_input)
    result = solution.solve_part2(lab_grid, guard_start)
    assert result == 6  # Example should have 6 possible obstruction positions

def test_empty_map():
    """Test behavior with an empty map"""
    empty_input = [
        ".........",
        "....^....",
        "........."
    ]
    lab_grid, guard_start = solution.parse_input(empty_input)
    result = solution.solve_part1(lab_grid, guard_start)
    assert result > 0  # Should visit at least one position

def test_guard_at_edge():
    """Test behavior when guard starts at edge of map"""
    edge_input = [
        "^........",
        ".........",
        "........."
    ]
    lab_grid, guard_start = solution.parse_input(edge_input)
    result = solution.solve_part1(lab_grid, guard_start)
    assert result > 0  # Should visit at least one position

def test_constrained_movement():
    """Test when guard has limited but valid movement options"""
    constrained_input = [
        "...#....",
        "...^....",
        "...#...."
    ]
    lab_grid, guard_start = solution.parse_input(constrained_input)
    result = solution.solve_part1(lab_grid, guard_start)
    # Guard should be able to move right and then leave the map
    assert result > 1  # Should visit at least starting position and one more