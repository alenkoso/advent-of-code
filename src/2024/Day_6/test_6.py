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

@pytest.fixture
def parsed_example(example_input):
    return solution.parse_input(example_input)

def test_part1(parsed_example):
    grid, start_pos = parsed_example
    assert solution.solve_part1(grid, start_pos) == 41

def test_part2(parsed_example):
    grid, start_pos = parsed_example
    assert solution.solve_part2(grid, start_pos) == 6

def test_parse_input():
    test_input = [
        "..^..",
        ".....",
        "..#.."
    ]
    grid, start_pos = solution.parse_input(test_input)
    assert grid[0][2] == '.'  # Guard position replaced with '.'
    assert start_pos == (0, 2)  # Guard position correctly identified
    assert grid[2][2] == '#'  # Obstacle remains in place

def test_simple_path():
    test_input = [
        "..^..",
        ".....",
        "#...."
    ]
    grid, start_pos = solution.parse_input(test_input)
    # Guard starts facing up, hits top, turns right, hits right edge
    # Total unique positions: start + 2 up + 2 right = 6
    assert solution.solve_part1(grid, start_pos) == 6

def test_loop_detection():
    test_input = [
        "..^..",
        ".....",
        ".#..."
    ]
    grid, start_pos = solution.parse_input(test_input)
    # Adding obstacle at (1,1) should create a loop:
    # Guard starts up, hits top, turns right, hits obstacle, turns right, etc.
    assert solution.simulate_guard(grid, start_pos, (1, 1))

def test_no_loop():
    test_input = [
        "..^..",
        ".....",
        "....."
    ]
    grid, start_pos = solution.parse_input(test_input)
    # Adding obstacle at (2,4) shouldn't create a loop as guard will escape
    assert not solution.simulate_guard(grid, start_pos, (2, 4))

def test_edge_cases():
    # Test guard at edge
    edge_input = [
        "^....",
        ".....",
        "....."
    ]
    grid, start_pos = solution.parse_input(edge_input)
    # Guard should move right along top edge and then off map
    assert solution.solve_part1(grid, start_pos) == 5