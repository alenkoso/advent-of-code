from collections import deque

def parse_input(file_path):
    with open(file_path) as f:
        raw = f.read().strip()
    maze, path = raw.split("\n\n")
    return maze.split("\n"), [x for x in path if x in "^v<>"]

def get_robot_pos(maze):
    for i, row in enumerate(maze):
        if "@" in row:
            return i, row.index("@")
    return 0, 0

def move_robot(maze, pos_r, pos_c, dr, dc):
    next_r = pos_r + dr
    next_c = pos_c + dc
    
    # Hit wall
    if maze[next_r][next_c] == "#":
        return pos_r, pos_c, maze
        
    # Empty space
    if maze[next_r][next_c] == ".":
        return next_r, next_c, maze
    
    # Find boxes to move
    q = deque([(pos_r, pos_c)])
    seen = set()
    ok = True
    
    while q:
        rr, cc = q.popleft()
        if (rr, cc) in seen:
            continue
        seen.add((rr, cc))
        
        rrr, ccc = rr + dr, cc + dc
        if maze[rrr][ccc] == "#":
            ok = False
            break
            
        if maze[rrr][ccc] == "O":
            q.append((rrr, ccc))
        elif maze[rrr][ccc] == "[":
            q.append((rrr, ccc))
            if maze[rrr][ccc+1] != "]":
                ok = False
                break
            q.append((rrr, ccc+1))
        elif maze[rrr][ccc] == "]":
            q.append((rrr, ccc))
            if maze[rrr][ccc-1] != "[":
                ok = False
                break
            q.append((rrr, ccc-1))
    
    if not ok:
        return pos_r, pos_c, maze
    
    # Move boxes
    new_maze = [list(row) for row in maze]
    seen.remove((pos_r, pos_c))
    
    while seen:
        for rr, cc in sorted(seen):
            rrr, ccc = rr + dr, cc + dc
            if (rrr, ccc) not in seen and new_maze[rrr][ccc] == ".":
                new_maze[rrr][ccc] = new_maze[rr][cc]
                new_maze[rr][cc] = "."
                seen.remove((rr, cc))
                break
    
    return next_r, next_c, ["".join(row) for row in new_maze]

def part1(maze, path):
    moves = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
    rr, cc = get_robot_pos(maze)
    maze = [list(row) for row in maze]
    maze[rr][cc] = "."
    maze = ["".join(row) for row in maze]
    
    for step in path:
        rr, cc, maze = move_robot(maze, rr, cc, *moves[step])
    
    total = 0
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if maze[r][c] == "O":
                total += 100 * r + c
    return total

def expand_maze(maze):
    new_maze = []
    for row in maze:
        expanded_row = []
        for char in row:
            if char == "#":
                expanded_row.append("##")
            elif char == "O":
                expanded_row.append("[]")
            elif char == ".":
                expanded_row.append("..")
            elif char == "@":
                expanded_row.append("@.")
        new_maze.append("".join(expanded_row))
    return new_maze

def part2(maze, path):
    moves = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
    maze = expand_maze(maze)
    rr, cc = get_robot_pos(maze)
    maze = [list(row) for row in maze]
    maze[rr][cc] = "."
    maze = ["".join(row) for row in maze]
    
    for step in path:
        rr, cc, maze = move_robot(maze, rr, cc, *moves[step])
    
    total = 0
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if maze[r][c] == "[":
                total += 100 * r + c
    return total

if __name__ == "__main__":
    maze, path = parse_input("input.txt")
    print("Part 1:", part1(maze, path))
    print("Part 2:", part2(maze, path))