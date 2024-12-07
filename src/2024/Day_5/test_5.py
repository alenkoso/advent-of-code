import pytest
import importlib.util


# Import solution
spec = importlib.util.spec_from_file_location("solution", "day5.py")
solution = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution)

@pytest.fixture
def example_input():
    return [
        "47|53",
        "97|13",
        "97|61",
        "97|47",
        "75|29",
        "61|13",
        "75|53",
        "29|13",
        "97|29",
        "53|29",
        "61|53",
        "97|53",
        "61|29",
        "47|13",
        "75|47",
        "97|75",
        "47|61",
        "75|61",
        "47|29",
        "75|13",
        "53|13",
        "",
        "75,47,61,53,29",
        "97,61,53,29,13",
        "75,29,13",
        "75,97,47,61,53",
        "61,13,29",
        "97,13,75,29,47"
    ]

@pytest.fixture
def parsed_example(example_input):
    return solution.parse_input(example_input)

def test_part1(parsed_example):
    rules, updates = parsed_example
    assert solution.solve_part1(rules, updates) == 143

def test_part2(parsed_example):
    rules, updates = parsed_example
    assert solution.solve_part2(rules, updates) == 123

def test_parse_input():
    test_input = [
        "1|2",
        "3|4",
        "",
        "1,2,3",
        "3,4,5"
    ]
    rules, updates = solution.parse_input(test_input)
    assert rules == [(1, 2), (3, 4)]
    assert updates == [[1, 2, 3], [3, 4, 5]]

def test_is_valid_order():
    rules = [(1, 2), (2, 3)]
    assert solution.is_valid_order([1, 2, 3], rules)
    assert not solution.is_valid_order([2, 1, 3], rules)
    assert solution.is_valid_order([1, 3], rules)  # Missing 2 is fine

def test_get_middle_page():
    assert solution.get_middle_page([1, 2, 3]) == 2  # Odd length
    assert solution.get_middle_page([1, 2, 3, 4, 5]) == 3  # Odd length
    assert solution.get_middle_page([1, 2, 3, 4]) == 3  # Even length - returns upper middle

def test_build_dependency_graph():
    pages = [1, 2, 3]
    rules = [(1, 2), (2, 3)]
    graph, indegree = solution.build_dependency_graph(pages, rules)
    assert graph[1] == {2}
    assert graph[2] == {3}
    assert indegree[1] == 0
    assert indegree[2] == 1
    assert indegree[3] == 1

def test_topological_sort():
    pages = [2, 1, 3]
    rules = [(1, 2), (2, 3)]
    assert solution.topological_sort(pages, rules) == [1, 2, 3]

def test_example_updates_validity(parsed_example):
    rules, _ = parsed_example
    # Test first three updates (should be valid)
    assert solution.is_valid_order([75, 47, 61, 53, 29], rules)
    assert solution.is_valid_order([97, 61, 53, 29, 13], rules)
    assert solution.is_valid_order([75, 29, 13], rules)
    # Test last three updates (should be invalid)
    assert not solution.is_valid_order([75, 97, 47, 61, 53], rules)
    assert not solution.is_valid_order([61, 13, 29], rules)
    assert not solution.is_valid_order([97, 13, 75, 29, 47], rules)

def test_example_reorderings(parsed_example):
    rules, _ = parsed_example
    # Test reordering of invalid updates
    assert solution.topological_sort([75, 97, 47, 61, 53], rules) == [97, 75, 47, 61, 53]
    assert solution.topological_sort([61, 13, 29], rules) == [61, 29, 13]
    assert solution.topological_sort([97, 13, 75, 29, 47], rules) == [97, 75, 47, 29, 13]

