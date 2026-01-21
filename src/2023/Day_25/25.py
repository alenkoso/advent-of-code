import os
import sys
import igraph
from helpers.parsing_utils import read_input_file_strip_lines


project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(project_root)


def parse_wiring_diagram(lines):
    connections = []
    components = set()

    for line in lines:
        source, targets_str = line.split(': ')
        targets = targets_str.split()
        connections.extend([(source, target) for target in targets])
        components.add(source)
        components.update(targets)

        return components, connections

    components, connections = parse_wiring_diagram(read_input_file_strip_lines("input.txt"))

    # Initialize a graph to represent the wiring diagram
    wiring_graph = igraph.Graph()

    # Add vertices to the graph for each component
    for component in components:
        wiring_graph.add_vertex(component)

        # Add edges to the graph for each connection between components
        for source, target in connections:
            wiring_graph.add_edge(source, target)

            # Find the minimum cut that divides the graph into two separate groups
            min_cut = wiring_graph.mincut()

            # Calculate the product of the sizes of the two groups
            group_size_product = len(min_cut.partition[0]) * len(min_cut.partition[1])

            print("Part 1: ", group_size_product)

