import pytest
import importlib.util


# Import solution
spec = importlib.util.spec_from_file_location("solution", "day3.py")
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

@pytest.fixture
def example_input():
    # Example input from problem description
    return ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)do()?mul(8,5))"]

@pytest.fixture
def parsed_example(example_input):
    # Parse example input
    return solution.parse_input(example_input)

def test_part1(parsed_example):
    # Part 1 example should give 161
    assert solution.solve_part1(parsed_example) == 161

def test_part2(parsed_example):
    # Part 2 example should give 48
    assert solution.solve_part2(parsed_example) == 48

def test_find_instructions():
    # Test basic multiplication
    memory = "mul(2,4)"
    instructions = solution.find_all_instructions(memory)
    assert len(instructions) == 1
    assert instructions[0][0] == 'mul'
    assert instructions[0][2] == 8

    # Test do/don't instructions
    memory = "do()mul(2,4)don't()mul(3,3)"
    instructions = solution.find_all_instructions(memory)
    assert len(instructions) == 4
    assert [i[0] for i in instructions] == ['do', 'mul', 'dont', 'mul']

def test_edge_cases():
    # Test invalid instructions are ignored
    assert solution.solve_part2("mul(4*") == 0
    assert solution.solve_part2("mul(6,9!") == 0
    assert solution.solve_part2("?(12,34)") == 0
    assert solution.solve_part2("mul ( 2 , 4 )") == 0

    # Test conditional states
    assert solution.solve_part2("don't()mul(2,2)do()mul(3,3)") == 9
    assert solution.solve_part2("mul(2,2)don't()mul(3,3)") == 4

