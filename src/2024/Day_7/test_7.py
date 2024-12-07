import pytest
import importlib.util


# Import solution
spec = importlib.util.spec_from_file_location("solution", "day7.py")
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

@pytest.fixture
def example_input():
    return [
        "190: 10 19",
        "3267: 81 40 27",
        "83: 17 5",
        "156: 15 6",
        "7290: 6 8 6 15",
        "161011: 16 10 13",
        "192: 17 8 14",
        "21037: 9 7 18 13",
        "292: 11 6 16 20",
    ]

def test_eval_expr():
    # Basic operator combinations
    assert solution.eval_expr([10, 19], ['*']) == 190
    assert solution.eval_expr([81, 40, 27], ['+', '*']) == 3267
    assert solution.eval_expr([11, 6, 16, 20], ['+', '*', '+']) == 292
    assert solution.eval_expr([15, 6], ['||']) == 156

def test_solve_part1(example_input):
    result = solution.solve_part1(example_input)
    assert result == 3749  # Sum of 190 + 3267 + 292

def test_solve_part2(example_input):
    result = solution.solve_part2(example_input)
    assert result == 11387  # Sum of part1 values plus 156 + 7290 + 192

def test_solve_equation_part1():
    # Test cases that should work in part 1
    assert solution.solve_equation([10, 19], 190) == True
    assert solution.solve_equation([81, 40, 27], 3267) == True
    assert solution.solve_equation([11, 6, 16, 20], 292) == True

    # Test cases that shouldn't work in part 1
    assert solution.solve_equation([17, 5], 83) == False
    assert solution.solve_equation([15, 6], 156) == False

def test_solve_equation_part2():
    # Test additional cases that work in part 2
    assert solution.solve_equation([15, 6], 156, True) == True
    assert solution.solve_equation([6, 8, 6, 15], 7290, True) == True
    assert solution.solve_equation([17, 8, 14], 192, True) == True

    # Part 1 cases should still work
    assert solution.solve_equation([10, 19], 190, True) == True
    assert solution.solve_equation([81, 40, 27], 3267, True) == True

