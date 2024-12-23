import os
import sys
import time
from itertools import combinations

project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(project_root)

from helpers.parsing_utils import read_input_file_strip_lines

def build_network_map(lines):
    network_map = {}
    for line in lines:
        computer1, computer2 = line.strip().split('-')
        network_map.setdefault(computer1, []).append(computer2)
        network_map.setdefault(computer2, []).append(computer1)
    return network_map

def find_triangles(network):
    triangle_sets = set()
    for computer in network:
        for computer1, computer2 in combinations(network[computer], 2):
            if computer1 in network[computer2]:
                triangle = tuple(sorted([computer, computer1, computer2]))
                triangle_sets.add(triangle)
    return triangle_sets

def bron_kerbosch(current_nodes, potential_nodes, excluded_nodes, network, cliques):
    if not potential_nodes and not excluded_nodes:
        cliques.append(current_nodes)
        return
    
    for node in list(potential_nodes):
        neighbors = set(network[node])
        bron_kerbosch(
            current_nodes.union([node]),
            potential_nodes.intersection(neighbors),
            excluded_nodes.intersection(neighbors),
            network,
            cliques
        )
        potential_nodes.remove(node)
        excluded_nodes.add(node)

def main():
    lines = read_input_file_strip_lines("input.txt")
    network = build_network_map(lines)
    
    start_time = time.time()
    triangles = find_triangles(network)
    triangles_with_t = [triangle for triangle in triangles 
                       if any(node.startswith('t') for node in triangle)]
    part_1 = len(triangles_with_t)
    end_time = time.time()
    print("Part 1:", part_1)
    print("Part 1 Execution Time: ", end_time - start_time, "seconds")
    
    start_time = time.time()
    cliques = []
    bron_kerbosch(set(), set(network.keys()), set(), network, cliques)
    largest_clique = max(cliques, key=len)
    part_2 = ",".join(sorted(largest_clique))
    end_time = time.time()
    print("Part 2:", part_2) 
    print("Part 2 Execution Time: ", end_time - start_time, "seconds")

if __name__ == '__main__':
    main()