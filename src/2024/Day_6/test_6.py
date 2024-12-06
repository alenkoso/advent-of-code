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
        ".....",
        "..^..",  # Guard in middle facing up
        "..#.."   # Obstacle below guard
    ]
    grid, start_pos = solution.parse_input(test_input)
    # Guard starts at (1,2), counts starting position
    # Then moves up to (0,2) before hitting wall and escaping
    assert solution.solve_part1(grid, start_pos) == 2

def test_loop_detection():
    test_input = [
        "#....",
        ".^...",  # Guard with walls creating a loop
        "#...."
    ]
    grid, start_pos = solution.parse_input(test_input)
    # Adding obstacle at (1,2) creates a loop
    assert solution.simulate_guard(grid, start_pos, (1, 2))

def test_no_loop():
    test_input = [
        "..^..",
        ".....",
        "....."
    ]
    grid, start_pos = solution.parse_input(test_input)
    # Obstacle near edge won't create loop
    assert not solution.simulate_guard(grid, start_pos, (2, 4))

def test_edge_cases():
    # Test guard at edge
    edge_input = [
        "^....",  # Guard at top-left corner
        ".....",
        "....."
    ]
    grid, start_pos = solution.parse_input(edge_input)
    # Guard starts at (0,0), moves right hitting positions:
    # (0,0), (0,1), (0,2), (0,3), (0,4)
    assert solution.solve_part1(grid, start_pos) == 5