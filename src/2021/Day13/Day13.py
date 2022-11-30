import itertools

# file = open("test.txt")
file = open("input.txt")

lines = file.readlines()

first = -1
sizeX = 0
sizeY = 0

dotLocations = []
matrix = []

for line in lines:
    line = line.strip()
    if "fold" in line:
        parts = line.split(" ")
        axis = parts[2].split('=')
        xOrY = axis[0]
        pos = int(axis[1])
        if xOrY == 'x':
            dotLocations[:] = [x for x in dotLocations if x[0] != pos]
            for x in dotLocations:
                if x[0] > pos:
                    x[0] = pos - (x[0] - pos)
        else:
            dotLocations[:] = [x for x in dotLocations if x[1] != pos]
            for x in dotLocations:
                if x[1] > pos:
                    x[1] = pos - (x[1] - pos)
        dotLocations.sort()
        dotLocations = list(dotLocations for dotLocations, _ in itertools.groupby(dotLocations))
        if first == -1:
            # print(dotLocations)
            first = len(dotLocations)
            print('part 1:', first)

    elif "," in line:
        parts = line.split(',')
        parts[:] = [int(part) for part in parts if part != '']
        dotLocations.append(parts)

for x in dotLocations:
    sizeX = max(sizeX, x[0])
    sizeY = max(sizeY, x[1])

sizeX += 1
sizeY += 1

for _ in range(sizeY):
    inp = []
    for _ in range(sizeX):
        inp.append(' ')
    matrix.append(inp)

for x in dotLocations:
    matrix[x[1]][x[0]] = '#'

print('Part 2 (please resize window if needed):')
for x in matrix:
    print(x)