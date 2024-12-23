from itertools import combinations

with open('input.txt', 'r') as file:
    network_connections = file.read().splitlines()

network_map = {}
for connection in network_connections:
    pc1, pc2 = connection.split('-')
    network_map.setdefault(pc1, []).append(pc2)
    network_map.setdefault(pc2, []).append(pc1)

tri_sets = set()
for pc in network_map:
    for pc1, pc2 in combinations(network_map[pc], 2):
        if pc1 in network_map[pc2]:
            triangle = tuple(sorted([pc, pc1, pc2]))
            tri_sets.add(triangle)

triangles_with_t = [triangle for triangle in tri_sets if any(pc.startswith('t') for pc in triangle)]

print("Part 1: ", len(triangles_with_t))

def bron_kerbosch(Rec, Potential, Exc, graph, cliques):
    if not Potential and not Exc:
        cliques.append(Rec)
        return
    for vertex in list(Potential):
        neighbors = set(graph[vertex])
        bron_kerbosch(
            Rec.union([vertex]),
            Potential.intersection(neighbors),
            Exc.intersection(neighbors),
            graph,
            cliques,
        )
        Potential.remove(vertex)
        Exc.add(vertex)

all_cliques = []
bron_kerbosch(set(), set(network_map.keys()), set(), network_map, all_cliques)

print("Part 2: ", ",".join(sorted(max(all_cliques, key=len))))