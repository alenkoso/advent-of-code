import networkx as nx
from itertools import product

def parse_input(file_path):
    data = [list(line.strip()) for line in open(file_path)]
    start = end = None
    for r, row in enumerate(data):
        for c, cell in enumerate(row):
            if cell == 'S':
                start = (r, c)
            elif cell == 'E':
                end = (r, c)
    return data, start, end

def make_graph(data, walls=False):
    g = nx.Graph()
    rows, cols = len(data), len(data[0])
    
    for r, c in product(range(rows), range(cols)):
        if not walls and data[r][c] == '#':
            continue
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if walls or data[nr][nc] in '.SE':
                    g.add_edge((r,c), (nr,nc))
    return g

def count_cheats(data, start, end, max_cheat=2):
    reg_graph = make_graph(data)
    wall_graph = make_graph(data, True)
    
    base_len = nx.shortest_path_length(reg_graph, start, end)
    start_dists = nx.single_source_shortest_path_length(reg_graph, start)
    end_dists = nx.single_source_shortest_path_length(reg_graph, end)
    
    cheats = 0
    for r, c in product(range(len(data)), range(len(data[0]))):
        if data[r][c] not in '.SE':
            continue
        
        cheat_from = (r, c)
        if cheat_from not in start_dists:
            continue
        
        start_len = start_dists[cheat_from]
        reachable = nx.single_source_shortest_path_length(wall_graph, cheat_from, cutoff=max_cheat)
        
        for cheat_to, cheat_len in reachable.items():
            if data[cheat_to[0]][cheat_to[1]] not in '.SE':
                continue
            if cheat_to not in end_dists:
                continue
            
            total = start_len + cheat_len + end_dists[cheat_to]
            if base_len - total >= 100:
                cheats += 1
    
    return cheats

if __name__ == "__main__":
    data, start, end = parse_input("input.txt")
    print("Part 1:", count_cheats(data, start, end))
    print("Part 2:", count_cheats(data, start, end, 20))