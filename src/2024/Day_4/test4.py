import pytest
import importlib.util


# Import solution
spec = importlib.util.spec_from_file_location("solution", "day4.py")
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

@pytest.fixture
def example_input():
    # Example input from problem description
    return [
"MMMSXXMASM",
"MSAMXMSMSA",
"AMXSXMAAMM",
"MSAMASMSMX",
"XMASAMXAMM",
"XXAMMXXAMA",
"SMSMSASXSS",
"SAXAMASAAA",
"MAMMMXMMMM",
"MXMXAXMASX"
]

@pytest.fixture
def parsed_example(example_input):
    # Parse example input
    return solution.parse_input(example_input)

def test_part1(parsed_example):
    # Example should find 18 instances of XMAS
    assert solution.solve_part1(parsed_example) == 18

    def test_part2(parsed_example):
        # Example should find 9 X-MAS patterns
        assert solution.solve_part2(parsed_example) == 9

        def test_simple_xmas():
            # Test simple X-MAS pattern
            grid = [
            "M.S",
            ".A.",
            "M.S"
            ]
            assert solution.solve_part2(solution.parse_input(grid)) == 1

            def test_overlapping_xmas():
                # Test overlapping X-MAS patterns
                grid = [
                "MSMS",  # Changed to remove extra dots
                ".AA.",
                "MSMS"
                ]
                # Should find two X-MAS patterns
                assert solution.solve_part2(solution.parse_input(grid)) == 2

                def test_backwards_xmas():
                    # Test backwards MAS/SAM combinations
                    grid = [
                    "S.M",
                    ".A.",
                    "S.M"
                    ]
                    assert solution.solve_part2(solution.parse_input(grid)) == 1

                    def test_directions():
                        # Test horizontal XMAS
                        horizontal = ["XMAS"]
                        assert solution.solve_part1(solution.parse_input(horizontal)) == 1

