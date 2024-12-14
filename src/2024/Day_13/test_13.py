import pytest
import importlib.util

# Import the solution module
spec = importlib.util.spec_from_file_location("solution", "day13.py")
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

@pytest.fixture
def sample_input():
    """Fixture providing example data from problem description"""
    return [
        "Button A: X+94, Y+34",
        "Button B: X+22, Y+67",
        "Prize: X=8400, Y=5400",
        "",
        "Button A: X+26, Y+66",
        "Button B: X+67, Y+21",
        "Prize: X=12748, Y=12176",
        "",
        "Button A: X+17, Y+86",
        "Button B: X+84, Y+37",
        "Prize: X=7870, Y=6450",
        "",
        "Button A: X+69, Y+23",
        "Button B: X+27, Y+71",
        "Prize: X=18641, Y=10279"
    ]

def test_parse_input(sample_input):
    """Test that input parsing works correctly"""
    machines = solution.parse_input(sample_input)
    assert len(machines) == 4
    
    # Test first machine values
    first_machine = machines[0]
    assert first_machine["a_x"] == 94
    assert first_machine["a_y"] == 34
    assert first_machine["b_x"] == 22
    assert first_machine["b_y"] == 67
    assert first_machine["prize_x"] == 8400
    assert first_machine["prize_y"] == 5400

def test_part2_second_machine():
    """Test the second machine which should be winnable in Part 2"""
    offset = 10000000000000
    machine = {
        "a_x": 26, "a_y": 66,
        "b_x": 67, "b_y": 21,
        "prize_x": offset + 12748,
        "prize_y": offset + 12176
    }
    result = solution.find_minimal_solution(machine)
    assert result is not None
    a_presses, b_presses = result
    # Verify the solution reaches the target
    assert machine["a_x"] * a_presses + machine["b_x"] * b_presses == machine["prize_x"]
    assert machine["a_y"] * a_presses + machine["b_y"] * b_presses == machine["prize_y"]

def test_part2_fourth_machine():
    """Test the fourth machine which should be winnable in Part 2"""
    offset = 10000000000000
    machine = {
        "a_x": 69, "a_y": 23,
        "b_x": 27, "b_y": 71,
        "prize_x": offset + 18641,
        "prize_y": offset + 10279
    }
    result = solution.find_minimal_solution(machine)
    assert result is not None
    a_presses, b_presses = result
    # Verify the solution reaches the target
    assert machine["a_x"] * a_presses + machine["b_x"] * b_presses == machine["prize_x"]
    assert machine["a_y"] * a_presses + machine["b_y"] * b_presses == machine["prize_y"]

def test_part2_full_solution(sample_input):
    """Test complete Part 2 solution with example data"""
    machines = solution.parse_input(sample_input)
    result = solution.solve_part2(machines)
    assert result > 0

def test_part1_vs_part2_results():
    """Test that Part 1 and Part 2 give different results"""
    with open('input.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    machines = solution.parse_input(lines)
    
    part1 = solution.solve_part1(machines)
    part2 = solution.solve_part2(machines)
    
    assert part1 != part2
    assert part1 > 0
    assert part2 > 0

def test_solution_verification():
    """Test that solutions actually reach the prizes"""
    offset = 10000000000000
    machine = {
        "a_x": 26, "a_y": 66,
        "b_x": 67, "b_y": 21,
        "prize_x": offset + 12748,
        "prize_y": offset + 12176
    }
    result = solution.find_minimal_solution(machine)
    assert result is not None
    a_presses, b_presses = result
    
    # Verify both coordinates are reached
    assert machine["a_x"] * a_presses + machine["b_x"] * b_presses == machine["prize_x"]
    assert machine["a_y"] * a_presses + machine["b_y"] * b_presses == machine["prize_y"]
    
    # Verify token calculation
    tokens = solution.calculate_tokens(a_presses, b_presses)
    assert tokens > 0

def test_token_calculation():
    """Test token calculation for known cases"""
    assert solution.calculate_tokens(80, 40) == 280  # First machine from example
    assert solution.calculate_tokens(38, 86) == 200  # Third machine from example

def test_impossible_solutions():
    """Test cases that should have no solution"""
    machine = {
        "a_x": 1, "a_y": 1,
        "b_x": 1, "b_y": 1,
        "prize_x": -5, "prize_y": -5
    }
    assert solution.find_minimal_solution(machine) is None

if __name__ == "__main__":
    pytest.main([__file__])