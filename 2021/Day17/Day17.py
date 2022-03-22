def yreach(y0):
    s = 0
    yield s
    for y in reversed(range(y0 + 1)):
        y += s
        yield s


# target_x = range(20,30+1)
# target_y = range(-10,-5+1)

target_x = range(217, 240 + 1)
target_y = range(-126, -69 + 1)


def get_in_range(v0, r, force=-1, drag=False):
    pos = 0
    v = v0
    i = 0
    mx = 1000
    flag = False
    s = set()
    mpos = 0
    while not flag or pos in r:
        # print(pos)
        pos += v
        if not (drag and v == 0):
            v += force
        i += 1
        if pos in r:
            s.add(i)
            flag = True
        if i > mx:
            break

        mpos = max(mpos, pos)
    return s, mpos


def scan_starting_values(vr, r, force=-1, drag=False):
    d = {}
    for v0 in vr:
        d[v0], _ = get_in_range(v0, r, force, drag)
    return d


xp = scan_starting_values(range(2000), target_x, drag=True)
yp = scan_starting_values(range(-2000, 2000), target_y, drag=False)

Q = set()

for kx, vx in xp.items():
    for ky, vy in yp.items():
        if vx & vy:
            Q.add((ky, kx))

besty = max(Q)[0]

print('part 1:', get_in_range(besty, range(1))[1])
print('part 2:', len(Q))