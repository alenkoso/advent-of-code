import pytest
from day1 import parse_input, solve_part1, solve_part2


@pytest.fixture
def example_input():
    # Example input from problem description
    return [
        "3   4",
        "4   3",
        "2   5",
        "1   3",
        "3   9",
        "3   3"
    ]

@pytest.fixture
def parsed_example(example_input):
    # Parse example input into lists
    return parse_input(example_input)

def test_part1(parsed_example):
    # Test part 1 with example data
    left_list, right_list = parsed_example
    assert solve_part1(left_list, right_list) == 11

def test_part2(parsed_example):
    # Test part 2 with example data
    left_list, right_list = parsed_example
    assert solve_part2(left_list, right_list) == 31

def test_parse_input(example_input):
    # Test input parsing
    left_list, right_list = parse_input(example_input)
    assert left_list == [3, 4, 2, 1, 3, 3]
    assert right_list == [4, 3, 5, 3, 9, 3]

def test_empty_input():
    # Test with empty input
    left_list, right_list = parse_input([])
    assert left_list == []
    assert right_list == []

def test_single_pair():
    # Test with single pair of numbers
    left_list, right_list = parse_input(["1   2"])
    assert solve_part1(left_list, right_list) == 1
    assert solve_part2(left_list, right_list) == 0

