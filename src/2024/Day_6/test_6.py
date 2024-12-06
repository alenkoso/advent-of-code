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

def test_guard_movement():
    test_input = [
        "..^..",  # Guard starts here facing up
        ".....",
        "....#"   # Obstacle at bottom right
    ]
    grid, start_pos = solution.parse_input(test_input)
    # Let's verify each step manually
    steps = solution.simulate_guard_steps(grid, start_pos)  # New helper function
    expected_steps = [
        (0, 2, 0),  # Start position, facing up
        (0, 2, 1),  # Hit top wall, turn right
        (0, 3, 1),  # Move right
        (0, 4, 1),  # Move right
        (0, 4, 2),  # Hit right wall, turn down
        (1, 4, 2),  # Move down
        (2, 4, 2),  # Move down until hit obstacle
    ]
    assert steps == expected_steps

def test_simple_path():
    test_input = [
        "..^..",
        ".....",
        "....#"
    ]
    grid, start_pos = solution.parse_input(test_input)
    # Guard should visit: (0,2), (0,3), (0,4), (1,4), (2,4)
    assert solution.solve_part1(grid, start_pos) == 5

def test_loop_detection():
    test_input = [
        "..^..",
        ".....",
        "....."
    ]
    grid, start_pos = solution.parse_input(test_input)
    # Create a simple 2x2 loop with obstacle at (1,2)
    # Guard will go up, right, down, left, up, repeating
    assert solution.simulate_guard(grid, start_pos, (1, 2))

def test_no_loop():
    test_input = [
        "..^..",
        ".....",
        "....."
    ]
    grid, start_pos = solution.parse_input(test_input)
    assert not solution.simulate_guard(grid, start_pos, (2, 4))