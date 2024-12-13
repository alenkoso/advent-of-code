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

def test_first_machine_solution():
    """Test the known solution for the first machine"""
    machine = {
        "a_x": 94, "a_y": 34,
        "b_x": 22, "b_y": 67,
        "prize_x": 8400, "prize_y": 5400
    }
    result = solution.find_button_presses(machine)
    assert result == (80, 40)

def test_impossible_machine():
    """Test a machine that has no solution"""
    machine = {
        "a_x": 26, "a_y": 66,
        "b_x": 67, "b_y": 21,
        "prize_x": 12748, "prize_y": 12176
    }
    result = solution.find_button_presses(machine)
    assert result is None

def test_third_machine_solution():
    """Test the known solution for the third machine"""
    machine = {
        "a_x": 17, "a_y": 86,
        "b_x": 84, "b_y": 37,
        "prize_x": 7870, "prize_y": 6450
    }
    result = solution.find_button_presses(machine)
    assert result == (38, 86)

def test_token_calculation():
    """Test token calculation for various button press combinations"""
    test_cases = [
        ((80, 40), 280),  # First machine example
        ((38, 86), 200),  # Third machine example
        ((0, 0), 0),      # Edge case - no presses
        ((1, 1), 4),      # Simple case
        ((100, 100), 400) # Maximum allowed presses
    ]
    
    for (a_presses, b_presses), expected in test_cases:
        assert solution.calculate_tokens(a_presses, b_presses) == expected

def test_full_solution(sample_input):
    """Test the complete solution with example input"""
    machines = solution.parse_input(sample_input)
    result = solution.solve_part1(machines)
    assert result == 480  # Known sum of tokens for winning machines

def test_over_limit_case():
    """Test machine requiring more than 100 button presses"""
    machine = {
        "a_x": 1, "a_y": 1,
        "b_x": 1, "b_y": 1,
        "prize_x": 101, "prize_y": 101
    }
    result = solution.find_button_presses(machine)
    assert result is None

def test_negative_coordinates():
    """Test machine with negative prize coordinates"""
    machine = {
        "a_x": 2, "a_y": 3,
        "b_x": 4, "b_y": 6,
        "prize_x": -10, "prize_y": -15
    }
    result = solution.find_button_presses(machine)
    assert result is None

def test_edge_cases():
    """Test various edge cases"""
    test_machines = [
        # Zero movement buttons
        {
            "a_x": 0, "a_y": 0,
            "b_x": 0, "b_y": 0,
            "prize_x": 1, "prize_y": 1
        },
        # Zero prize coordinates
        {
            "a_x": 1, "a_y": 1,
            "b_x": 1, "b_y": 1,
            "prize_x": 0, "prize_y": 0
        },
        # Parallel movements
        {
            "a_x": 2, "a_y": 4,
            "b_x": 1, "b_y": 2,
            "prize_x": 10, "prize_y": 20
        }
    ]
    
    for machine in test_machines:
        result = solution.find_button_presses(machine)
        assert result is None

def test_full_solution_with_file():
    """Test the solution with actual input file"""
    with open('input.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    machines = solution.parse_input(lines)
    result = solution.solve_part1(machines)
    assert result > 0  # Basic sanity check

if __name__ == "__main__":
    pytest.main([__file__])