g = [list(s.strip()) for s in open('input.txt') if s.strip()]
R, C = len(g), len(g[0])

# Find start
x = y = 0
for i in range(R):
    for j in range(C):
        if g[i][j] == '^':
            x, y = i, j
            g[i][j] = '.'
            break

def sim(gx, gy, ox=-1, oy=-1):
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    x,y,d = gx,gy,0
    
    if ox < 0:  # Part 1 - just track visited
        seen = {(x,y)}
        while True:
            nx,ny = x + dx[d], y + dy[d]
            if not (0 <= nx < R and 0 <= ny < C):
                return len(seen)
            if g[nx][ny] == '#':
                d = (d+1) % 4
            else:
                x,y = nx,ny
                seen.add((x,y))
    else:  # Part 2 - look for loops
        steps = 0
        states = {(x,y,d)}
        while steps < 10000:  # Limit total steps
            nx,ny = x + dx[d], y + dy[d]
            if not (0 <= nx < R and 0 <= ny < C):
                return False
            if nx == ox and ny == oy or g[nx][ny] == '#':
                d = (d+1) % 4
            else:
                x,y = nx,ny
                if (x,y,d) in states:
                    return True
                states.add((x,y,d))
            steps += 1
        return False  # Too many steps without loop

print(sim(x,y))

ans = 0
for i in range(R):
    for j in range(C):
        if g[i][j] == '.' and (i,j) != (x,y):
            if sim(x,y,i,j):
                ans += 1
print(ans)