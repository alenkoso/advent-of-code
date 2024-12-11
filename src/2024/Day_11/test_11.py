import pytest
import importlib.util
from collections import defaultdict

# Import the solution module
spec = importlib.util.spec_from_file_location("solution", "day11.py")
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_transform_stone_zero():
    """Test that 0 transforms to 1"""
    assert solution.transform_stone(0) == [1]

def test_transform_stone_even_digits():
    """Test stones with even number of digits split correctly"""
    assert solution.transform_stone(1234) == [12, 34]
    assert solution.transform_stone(1000) == [10, 0]
    assert solution.transform_stone(5566) == [55, 66]

def test_transform_stone_odd_digits():
    """Test stones with odd number of digits multiply by 2024"""
    assert solution.transform_stone(123) == [123 * 2024]
    assert solution.transform_stone(7) == [7 * 2024]

def test_transform_all_stones():
    """Test transforming multiple stones with counts"""
    initial_counts = {0: 2, 123: 1}  # 2 zeros and 1 stone with value 123
    expected = defaultdict(int, {1: 2, 123 * 2024: 1})
    assert dict(solution.transform_all_stones(initial_counts)) == dict(expected)

def test_example_data_one_blink():
    """Test one blink with example data"""
    initial = {125: 1, 17: 1}
    after_one = solution.transform_all_stones(initial)
    expected = {253000: 1, 1: 1, 7: 1}
    assert dict(after_one) == expected

def test_full_solution_part1():
    # Test the known correct answer for part 1 (25 blinks)
    with open('input.txt') as f:
        stones = [int(num) for num in f.read().split()]
    initial_counts = {num: stones.count(num) for num in set(stones)}
    assert solution.solve_stones(initial_counts, 25) == 211306

def test_edge_cases():
    # Test edge cases
    # Empty input
    assert solution.solve_stones({}, 1) == 0
    
    # Single zero
    assert solution.solve_stones({0: 1}, 1) == 1
    
    # All zeros
    assert solution.solve_stones({0: 5}, 1) == 5

@pytest.fixture
def example_data():
    # Fixture providing example data from problem description"""
    return {125: 1, 17: 1}

def test_multi_step_transformation(example_data):
    # Test multiple transformation steps using example data"""
    counts = example_data
    
    # After 1 blink
    counts = solution.transform_all_stones(counts)
    assert sum(counts.values()) == 3
    
    # After 2 blinks
    counts = solution.transform_all_stones(counts)
    assert sum(counts.values()) == 4

# Test for cache effectiveness
def test_cache_hit():
    # Verify that caching is working by transforming the same stone twice
    solution.transform_stone.cache_clear()  # Clear cache first
    
    # First call
    result1 = solution.transform_stone(1234)
    
    # Second call (should use cache)
    result2 = solution.transform_stone(1234)
    
    assert result1 == result2
    assert solution.transform_stone.cache_info().hits >= 1

if __name__ == "__main__":
    pytest.main([__file__])