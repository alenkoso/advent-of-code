import os
import sys
import time
import networkx as nx
from itertools import product

project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(project_root)

from helpers.parsing_utils import read_input_file_to_grid

def parse_input(data):
    start_pos = end_pos = None
    for row, line in enumerate(data):
        for col, char in enumerate(line):
            if char == 'S':
                start_pos = (row, col)
            elif char == 'E':
                end_pos = (row, col)
    return start_pos, end_pos

def build_graph(data, allow_walls=False):
    graph = nx.Graph()
    row_count, col_count = len(data), len(data[0])
    
    for row, col in product(range(row_count), range(col_count)):
        if not allow_walls and data[row][col] == '#':
            continue
            
        for next_row, next_col in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
            if 0 <= next_row < row_count and 0 <= next_col < col_count:
                if allow_walls or data[next_row][next_col] in '.SE':
                    graph.add_edge((row, col), (next_row, next_col))
                    
    return graph

def count_cheats(data, start_pos, end_pos, max_shortcut_length=2):
    regular_graph = build_graph(data)
    wall_graph = build_graph(data, True)
    
    normal_path_length = nx.shortest_path_length(regular_graph, start_pos, end_pos)
    distances_from_start = nx.single_source_shortest_path_length(regular_graph, start_pos)
    distances_to_end = nx.single_source_shortest_path_length(regular_graph, end_pos)
    
    shortcut_count = 0
    
    for row, col in product(range(len(data)), range(len(data[0]))):
        if data[row][col] not in '.SE':
            continue
            
        shortcut_start = (row, col)
        if shortcut_start not in distances_from_start:
            continue
        
        path_to_shortcut = distances_from_start[shortcut_start]
        reachable_positions = nx.single_source_shortest_path_length(wall_graph, shortcut_start, cutoff=max_shortcut_length)
        
        for shortcut_end, shortcut_length in reachable_positions.items():
            if data[shortcut_end[0]][shortcut_end[1]] not in '.SE':
                continue
            if shortcut_end not in distances_to_end:
                continue
            
            total_path_length = path_to_shortcut + shortcut_length + distances_to_end[shortcut_end]
            if normal_path_length - total_path_length >= 100:
                shortcut_count += 1
    
    return shortcut_count

def main():
    data = read_input_file_to_grid("input.txt")
    start_pos, end_pos = parse_input(data)
    
    start_time = time.time()
    part_1 = count_cheats(data, start_pos, end_pos)
    end_time = time.time()
    print(f"Part 1: {part_1}")
    print(f"Part 1 Execution Time: {end_time - start_time} seconds")
    
    start_time = time.time()
    part_2 = count_cheats(data, start_pos, end_pos, 20)
    end_time = time.time()
    print(f"Part 2: {part_2}")
    print(f"Part 2 Execution Time: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()