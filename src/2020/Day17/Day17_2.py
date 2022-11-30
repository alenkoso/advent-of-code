import copy


def count_neighbours(state, x, y, z, w):
    neighbours_count = 0
    for i in range(-1, 2):
        current_x = x + i
        if current_x < 0 or current_x >= len(state[0][0][0]):
            continue
        for j in range(-1, 2):
            current_y = y + j
            if current_y < 0 or current_y >= len(state[0][0]):
                continue
            for k in range(-1, 2):
                current_z = z + k
                if current_z < 0 or current_z >= len(state[0]):
                    continue
                for l in range(-1, 2):
                    current_w = w + l  # četrta dimenzija
                    if current_w < 0 or current_w >= len(state):
                        continue
                    if current_x == x and current_y == y and current_z == z and current_w == w:
                        continue

                    # print(current_z,current_y,current_x)
                    neighbours_count += state[current_w][current_z][current_y][current_x]
    return neighbours_count


def expand_state(state):
    old_x, old_y, old_z, old_w = (len(state[0][0][0]), len(state[0][0]), len(state[0]), len(state))
    new_dimensions = old_x + 2, old_y + 2, old_z + 2, old_w + 2

    for w in range(old_w):
        for z in range(old_z):
            for y in range(old_y):
                state[w][z][y].insert(0, False)
                state[w][z][y].append(False)

    for w in range(old_w):
        for z in range(old_z):
            state[w][z].insert(0, [False for x in range(new_dimensions[0])])
            state[w][z].append([False for x in range(new_dimensions[0])])

    for w in range(old_w):
        state[w].insert(0, [[False for x in range(new_dimensions[0])] for y in range(new_dimensions[1])])
        state[w].append([[False for x in range(new_dimensions[0])] for y in range(new_dimensions[1])])

    state.insert(0, [[[False for x in range(new_dimensions[0])] for y in range(new_dimensions[1])] for z in
                     range(new_dimensions[2])])
    state.append([[[False for x in range(new_dimensions[0])] for y in range(new_dimensions[1])] for z in
                  range(new_dimensions[2])])


def next_state(state):
    global max_count
    expand_state(state)
    # pad the state with two new arrays
    new_state = copy.deepcopy(state)

    dimensions = len(state[0][0][0]), len(state[0][0]), len(state[0]), len(state)

    for x in range(dimensions[0]):
        for y in range(dimensions[1]):
            for z in range(dimensions[2]):
                for w in range(dimensions[3]):
                    count = count_neighbours(state, x, y, z, w)
                    if state[w][z][y][x]:
                        new_state[w][z][y][x] = (count == 2 or count == 3)
                    else:
                        new_state[w][z][y][x] = (count == 3)

    return new_state


def count_cubes(state):
    count = 0
    for w in state:
        for z in w:
            for y in z:
                for x in y:
                    count += x
    return count


with open("../Inputs/InputDay17.txt") as input:
    raw = input.read()

    state = [[[[c == '#' for c in line] for line in raw.split('\n') if line.strip()]]]

    # TESTNI IZPISI
    # print(state)

    # print(count_neighbours(state, 0, 0, 0))
    # print(count_neighbours(state, 1, 0, 0))
    #

    for i in range(6):  # vseh 6 iteracij
        state = next_state(state)

    print(count_cubes(state))
