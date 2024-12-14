import pytest
import time
import importlib.util
from typing import Dict, Tuple

# Import solution
spec = importlib.util.spec_from_file_location("solution", "day14.py")
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

@pytest.fixture
def tree_pattern() -> Dict[Tuple[int, int], int]:
    """Create a simple Christmas tree pattern for testing.
    Note: Pattern is more tree-like than previous version."""
    positions = {
        # Single top point
        (5, 0): 1,
        # Upper branches
        (4, 1): 1,
        (6, 1): 1,
        # Middle branches
        (3, 2): 1,
        (5, 2): 1,
        (7, 2): 1,
        # Lower branches
        (2, 3): 1,
        (4, 3): 1,
        (6, 3): 1,
        (8, 3): 1,
        # Trunk
        (5, 4): 1,
        (5, 5): 1,
        (5, 6): 1,
    }
    return positions

def test_bounding_box():
    """Test bounding box calculation."""
    positions = {
        (1, 1): 1,
        (4, 5): 1,
        (2, 3): 1
    }
    min_x, min_y, max_x, max_y = solution.calculate_bounding_box(positions)
    assert min_x == 1
    assert min_y == 1
    assert max_x == 4
    assert max_y == 5

def test_tree_pattern_detection(tree_pattern):
    """Test detection of a valid tree pattern."""
    total_robots = sum(tree_pattern.values())
    assert solution.is_tree_pattern(tree_pattern, total_robots)

def test_not_tree_pattern():
    """Test rejection of non-tree patterns."""
    # Random scattered pattern
    positions = {
        (1, 1): 1,
        (5, 5): 1,
        (9, 9): 1,
        (2, 8): 1,
    }
    assert not solution.is_tree_pattern(positions, total_robots=4)

def test_visualization():
    """Test position visualization."""
    positions = {
        (1, 1): 1,
        (2, 2): 2,
        (3, 3): 10,
    }
    vis = solution.visualize_positions(positions, width=5, height=5)
    expected = (
        ".....\n"
        ".1...\n"
        "..2..\n"
        "...#.\n"
        ".....\n"
    ).strip()
    assert vis == expected

def test_step_simulation():
    """Test single step simulation."""
    robots = [
        solution.Robot(0, 0, 1, 1),
        solution.Robot(1, 1, -1, -1)
    ]
    positions = solution.simulate_step(robots, width=5, height=5)
    assert positions[(1, 1)] == 1  # First robot moved right and down
    assert positions[(0, 0)] == 1  # Second robot moved left and up

def test_periodic_movement():
    """Test that robots eventually repeat their positions."""
    robot = solution.Robot(0, 0, 2, 3)
    width, height = 4, 6
    
    # Record initial position
    initial_pos = (robot.pos_x, robot.pos_y)
    
    # Move robot until it returns to initial position
    steps = 0
    max_steps = width * height  # Maximum possible unique positions
    
    while steps < max_steps:
        robot.move(width, height)
        steps += 1
        if (robot.pos_x, robot.pos_y) == initial_pos:
            break
    
    assert steps < max_steps, "Robot should eventually return to initial position"

def test_pattern_detection_timing():
    """Test that pattern detection runs within reasonable time."""
    lines = [
        "p=0,0 v=1,1",
        "p=1,1 v=1,1",
        "p=2,2 v=1,1",
        "p=3,3 v=1,1",
    ]
    robots = [solution.parse_robot(line) for line in lines]
    start_time = time.time()
    solution.find_tree_pattern(robots, width=10, height=10, max_steps=100)
    duration = time.time() - start_time
    assert duration < 1.0  # Should complete within 1 second

if __name__ == "__main__":
    pytest.main([__file__])