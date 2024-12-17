from collections import deque

def parse_input(file_path):
    with open(file_path) as f:
        raw = f.read().strip()
    maze, path = raw.split('\n\n')
    return maze.split('\n'), [x for x in path if x in '^v<>']

def get_robot_pos(maze):
    for i, row in enumerate(maze):
        if '@' in row:
            return i, row.index('@')
    return 0, 0

def push_boxes(maze, pos_r, pos_c, dr, dc):
    next_r = pos_r + dr
    next_c = pos_c + dc
    
    if maze[next_r][next_c] == '#':
        return pos_r, pos_c, maze
        
    if maze[next_r][next_c] == '.':
        return next_r, next_c, maze
        
    q = deque([(pos_r, pos_c)])
    boxes = set()
    
    while q:
        r, c = q.popleft()
        if (r, c) in boxes:
            continue
        boxes.add((r, c))
        
        new_r = r + dr
        new_c = c + dc
        
        if maze[new_r][new_c] == '#':
            return pos_r, pos_c, maze
            
        if maze[new_r][new_c] in 'O[]':
            q.append((new_r, new_c))
            if maze[new_r][new_c] == '[':
                q.append((new_r, new_c + 1))
            elif maze[new_r][new_c] == ']':
                q.append((new_r, new_c - 1))
                    
    new_maze = [list(row) for row in maze]
    while boxes:
        for r, c in sorted(boxes):
            new_r = r + dr
            new_c = c + dc
            if (new_r, new_c) not in boxes and new_maze[new_r][new_c] == '.':
                new_maze[new_r][new_c] = new_maze[r][c]
                new_maze[r][c] = '.'
                boxes.remove((r, c))
                break
                    
    return next_r, next_c, [''.join(row) for row in new_maze]

if __name__ == '__main__':
    moves = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
    maze, path = parse_input("input.txt")
    rr, cc = get_robot_pos(maze)
    maze[rr] = maze[rr][:cc] + '.' + maze[rr][cc + 1:]
    
    for step in path:
        rr, cc, maze = push_boxes(maze, rr, cc, *moves[step])
    
    total = 0
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if maze[r][c] in 'O[':
                total += 100 * r + c
    print("Part 1: ", total)