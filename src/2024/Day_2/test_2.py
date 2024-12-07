import pytest
import importlib.util

# Import solution
spec = importlib.util.spec_from_file_location("solution", "day2.py")
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

@pytest.fixture
def example_input():
    # Example input from problem description
    return [
        "7 6 4 2 1",
        "1 2 7 8 9",
        "9 7 6 2 1",
        "1 3 2 4 5",
        "8 6 4 4 1",
        "1 3 6 7 9"
    ]

@pytest.fixture
def parsed_example(example_input):
    # Parse example input
    return solution.parse_input(example_input)

def test_part1(parsed_example):
    # Part 1 example should give 2
    assert solution.solve_part1(parsed_example) == 2

def test_part2(parsed_example):
    # Part 2 example should give 4
    assert solution.solve_part2(parsed_example) == 4

def test_sequence_validation():
    # Test individual cases
    assert solution.is_sequence_valid([7, 6, 4, 2, 1])  # Valid decreasing
    assert solution.is_sequence_valid([1, 3, 6, 7, 9])  # Valid increasing
    assert not solution.is_sequence_valid([1, 2, 7, 8, 9])  # Invalid jump
    assert not solution.is_sequence_valid([1, 3, 2, 4, 5])  # Mixed direction
    assert not solution.is_sequence_valid([8, 6, 4, 4, 1])  # No change