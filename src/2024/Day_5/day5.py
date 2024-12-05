import os
import sys
import time
from collections import defaultdict

project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(project_root)

from helpers.parsing_utils import read_input_file_strip_lines

def parse_input(lines):
    rules = []
    updates = []
    parsing_rules = True
    
    for line in lines:
        if not line:
            parsing_rules = False
            continue
            
        if parsing_rules:
            before, after = line.split('|')
            rules.append((int(before), int(after)))
        else:
            updates.append([int(x) for x in line.split(',')])
    
    return rules, updates

def is_valid_order(pages, rules):
    for before, after in rules:
        if before not in pages or after not in pages:
            continue
        before_pos = pages.index(before)
        after_pos = pages.index(after)
        if before_pos > after_pos:
            return False
    return True

def get_middle_page(pages):
    return pages[len(pages) // 2]

def build_dependency_graph(pages, rules):
    # Create adjacency lists for dependencies
    graph = defaultdict(set)
    indegree = defaultdict(int)
    for before, after in rules:
        if before in pages and after in pages:
            graph[before].add(after)
            indegree[after] += 1
            if before not in indegree:
                indegree[before] = 0
    
    return graph, indegree

def topological_sort(pages, rules):
    graph, indegree = build_dependency_graph(pages, rules)
    ordered = []
    
    # Initialize queue with nodes that have no dependencies
    queue = [page for page in pages if indegree[page] == 0]
    
    while queue:
        # Get a node with no dependencies
        current = queue.pop(0)
        ordered.append(current)
        
        # Remove edges from this node
        for neighbor in graph[current]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    # If we haven't ordered all pages, there's a cycle
    return ordered if len(ordered) == len(pages) else None

def solve_part1(rules, updates):
    total = 0
    for update in updates:
        if is_valid_order(update, rules):
            total += get_middle_page(update)
    return total

def solve_part2(rules, updates):
    total = 0
    for update in updates:
        if not is_valid_order(update, rules):
            ordered_update = topological_sort(update, rules)
            if ordered_update:  # Only count if we found a valid ordering
                total += get_middle_page(ordered_update)
    return total

def main():
    # Read input
    lines = read_input_file_strip_lines("input.txt")
    rules, updates = parse_input(lines)
    
    # Part 1
    start_time = time.time()
    part1_result = solve_part1(rules, updates)
    end_time = time.time()
    print(f"Part 1: {part1_result}")
    print(f"Part 1 Execution Time: {end_time - start_time} seconds")
    
    # Part 2
    start_time = time.time()
    part2_result = solve_part2(rules, updates)
    end_time = time.time()
    print(f"Part 2: {part2_result}")
    print(f"Part 2 Execution Time: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()