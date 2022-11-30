import copy


def count_neighbours(state, x, y, z):
    neighbours_count = 0
    for i in range(-1, 2):
        current_x = x + i
        if current_x < 0 or current_x >= len(state[0][0]):
            continue
        for j in range(-1, 2):
            current_y = y + j
            if current_y < 0 or current_y >= len(state[0]):
                continue
            for k in range(-1, 2):
                current_z = z + k
                if current_z < 0 or current_z >= len(state):
                    continue
                if current_x == x and current_y == y and current_z == z:
                    continue

                # print(current_z,current_y,current_x)

                neighbours_count += state[current_z][current_y][current_x]

    return neighbours_count


def expand_state(state):
    old_x, old_y, old_z = (len(state[0][0]), len(state[0]), len(state))
    new_dimensions = old_x + 2, old_y + 2, old_z + 2
    for z in range(old_z):
        for y in range(old_y):
            state[z][y].insert(0, False)
            state[z][y].append(False)

    for z in range(old_z):
        state[z].insert(0, [False for _ in range(new_dimensions[1])])
        state[z].append([False for _ in range(new_dimensions[1])])

    state.insert(0, [[False for _ in range(new_dimensions[0])] for _ in range(new_dimensions[1])])
    state.append([[False for _ in range(new_dimensions[0])] for _ in range(new_dimensions[1])])


def next_state(state):
    expand_state(state)
    # pad the state with two new arrays
    new_state = copy.deepcopy(state)

    dimension = len(state[0][0]), len(state[0]), len(state)

    for x in range(dimension[0]):
        for y in range(dimension[1]):
            for z in range(dimension[2]):
                count = count_neighbours(state, x, y, z)
                if state[z][y][x]:
                    new_state[z][y][x] = (count == 2 or count == 3)
                else:
                    new_state[z][y][x] = (count == 3)

    return new_state


def print_layer(state, layer):
    local_layer = state[layer]
    for row in local_layer:
        print(['#' if character else '.' for character in row])


def count_cubes(state):
    count = 0
    for row in state:
        for col in row:
            for it in col:
                count += it

    return count


with open("../Inputs/InputDay17.txt") as input:
    raw = input.read()

    state = [[[character == '#' for character in line] for line in raw.split('\n') if line.strip()]]
    # TESTNI IZPISI
    # print(state)

    # print(count_neighbours(state, 0, 0, 0))
    # print(count_neighbours(state, 1, 0, 0))
    #

    for i in range(6):  # vseh 6 iteracij
        state = next_state(state)

    print(count_cubes(state))
