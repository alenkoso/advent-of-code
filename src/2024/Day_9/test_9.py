import pytest
import importlib.util

# Import solution
spec = importlib.util.spec_from_file_location("solution", "day9.py")
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

def test_expand_disk_map():
    # Test with simple input
    blocks, files = solution.expand_disk_map([1, 2, 3])
    assert len(blocks) == 6  # 1 (file) + 2 (space) + 3 (file)
    assert blocks[:1] == [0]  # First file
    assert blocks[1:3] == ['.', '.']  # Space
    assert blocks[3:] == [1, 1, 1]  # Second file
    assert len(files) == 2  # Two files
    assert files[0] == (0, 0, 1)  # First file: id 0, start at 0, length 1
    assert files[1] == (1, 3, 3)  # Second file: id 1, start at 3, length 3

def test_find_free_space():
    blocks = ['.', '.', '.', 1, 1, '.', '.', 2]
    # Find space for size 2
    assert solution.find_free_space(blocks, 8, 2) == 0  # Should find first available space
    # Find space for size 3
    assert solution.find_free_space(blocks, 8, 3) == 0  # Should find first available space
    # No space available for size 4
    assert solution.find_free_space(blocks, 8, 4) == -1

def test_move_file():
    blocks = ['.', '.', 1, 1, '.', '.']
    solution.move_file(blocks, 2, 2, 0)
    assert blocks == [1, 1, '.', '.', '.', '.']

def test_calculate_checksum():
    blocks = [0, 0, '.', 1, 1, 1]
    # Each position contributes: 0*0 + 1*0 + skip(.) + 3*1 + 4*1 + 5*1 = 12
    assert solution.calculate_checksum(blocks) == 12

# Example test cases from problem description
def test_example_part2():
    input_map = "2333133121414131402"
    result = solution.solve_part2(input_map)  # Using example from problem
    assert result == 2858

def test_small_example():
    input_map = "12345"
    blocks, files = solution.expand_disk_map([int(x) for x in input_map])
    expected_blocks = [0] + ['.'] * 2 + [1] * 3 + ['.'] * 4 + [2] * 5
    assert blocks == expected_blocks

def test_no_spaces():
    input_map = "90909"  # Three 9-block files with no spaces
    blocks, files = solution.expand_disk_map([int(x) for x in input_map])
    assert len(blocks) == 27  # 9 + 0 + 9 + 0 + 9
    assert blocks.count('.') == 0  # No spaces
    assert len(files) == 3  # Three files

def test_edge_cases():
    # Single file
    blocks, files = solution.expand_disk_map([1])
    assert blocks == [0]
    assert files == [(0, 0, 1)]
    
    # Single space
    blocks, files = solution.expand_disk_map([1, 1])
    assert blocks == [0, '.']
    assert files == [(0, 0, 1)]
    
    # Empty input
    blocks, files = solution.expand_disk_map([])
    assert blocks == []
    assert files == []

def test_checksum_calculation():
    # Test with basic case
    blocks = [0, 1, '.', 2]
    assert solution.calculate_checksum(blocks) == 7  # 0*0 + 1*1 + skip + 3*2 = 0 + 1 + 0 + 6 = 7
    
    # Test with multiple spaces
    blocks = [0, '.', '.', 1]
    assert solution.calculate_checksum(blocks) == 3  # 0*0 + skip + skip + 3*1 = 3
    
    # Test empty blocks
    blocks = ['.', '.', '.']
    assert solution.calculate_checksum(blocks) == 0  # All spaces, should be 0

def test_full_process_part2():
    # Focus on example case from problem
    test_input = "2333133121414131402"
    assert solution.solve_part2(test_input) == 2858

def test_input_validation():
    # Test non-numeric input (remove if validation not required)
    pass