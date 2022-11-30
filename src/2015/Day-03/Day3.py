def move(step, coordinates):
    moves = {
        ">": [1, 0],
        "<": [-1, 0],
        "^": [0, 1],
        "v": [0, -1],
    }

    return coordinates[0] + moves[step][0], coordinates[1] + moves[step][1]


def visits(steps, number_of_movers=1):
    visited = {(0, 0)}

    coordinates = [(0, 0)] * number_of_movers
    for number_of_steps, step in enumerate(steps):
        position = number_of_steps % number_of_movers
        coordinates[position] = move(step, coordinates[position])
        visited.add(coordinates[position])
    return len(visited)


with open("input.txt") as input:
    raw = input.read()

    print("How many houses receive at least one present? ", visits(raw))
    print("This year, how many houses receive at least one present? ", visits(raw, number_of_movers=2))