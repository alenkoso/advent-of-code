import importlib.util

# Import solution
spec = importlib.util.spec_from_file_location("solution", "day8.py")
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

# Test data
example_input = [
    "............",
    "........0...",
    ".....0......",
    ".......0....",
    "....0.......",
    "......A.....",
    "............",
    "............",
    "........A...",
    ".........A..",
    "............",
    "............"
]

def test_parse_input():
    grid, antennas = solution.parse_input(example_input)
    
    # Test grid dimensions
    assert len(grid) == 12
    assert len(grid[0]) == 12
    
    # Test antenna positions
    assert len(antennas['0']) == 4  # Should be 4 '0' antennas
    assert len(antennas['A']) == 3  # Should be 3 'A' antennas
    
    # Test specific antenna positions
    assert (1, 8) in antennas['0']  # Check one '0' position
    assert (8, 8) in antennas['A']  # Check one 'A' position

def test_is_collinear_part1():
    # Test double distance points calculation
    p1 = (0, 0)
    p2 = (1, 1)
    points = solution.is_collinear(p1, p2)
    
    assert len(points) == 2
    assert (-1, -1) in points  # Point at double distance in one direction
    assert (2, 2) in points    # Point at double distance in other direction
    
    # Test same point case
    points = solution.is_collinear((1, 1), (1, 1))
    assert len(points) == 0

def test_is_collinear_part2():
    # Test three points that are collinear
    assert solution.is_collinear((0, 0), (1, 1), (2, 2))
    
    # Test three points that are not collinear
    assert not solution.is_collinear((0, 0), (1, 1), (2, 0))
    
    # Test vertical line
    assert solution.is_collinear((0, 1), (1, 1), (2, 1))
    
    # Test horizontal line
    assert solution.is_collinear((1, 0), (1, 1), (1, 2))

def test_find_antinodes_part1():
    grid, antennas = solution.parse_input(example_input)
    result = solution.find_antinodes(grid, antennas, part2=False)
    assert result == 14  # Known result from puzzle description

def test_find_antinodes_part2():
    grid, antennas = solution.parse_input(example_input)
    result = solution.find_antinodes(grid, antennas, part2=True)
    assert result == 34  # Known result from puzzle description

def test_edge_cases():
    # Test empty grid
    empty_input = [".....", "....."]
    grid, antennas = solution.parse_input(empty_input)
    assert solution.find_antinodes(grid, antennas) == 0
    
    # Test single antenna
    single_input = [".....", "..A.."]
    grid, antennas = solution.parse_input(single_input)
    assert solution.find_antinodes(grid, antennas) == 0
    
    # Test two different frequencies
    diff_freq_input = ["..A..", "..B.."]
    grid, antennas = solution.parse_input(diff_freq_input)
    assert solution.find_antinodes(grid, antennas) == 0

def test_boundary_conditions():
    # Test antennas at grid edges
    edge_input = ["A...A", ".....", "A...."]
    grid, antennas = solution.parse_input(edge_input)
    
    # Test part 1
    result1 = solution.find_antinodes(grid, antennas, part2=False)
    assert result1 >= 0  # Should handle edge cases without errors
    
    # Test part 2
    result2 = solution.find_antinodes(grid, antennas, part2=True)
    assert result2 >= 3  # Should include antenna positions in part 2