from ast import literal_eval
import numpy as np


def part_one():
    with open("input.txt") as input:
        instructions = [line.split() for line in input]

    lights = np.zeros(shape=(1000, 1000), dtype=np.int64)

    for instruction in instructions:
        x1, y1 = literal_eval(instruction[-3])
        x2, y2 = literal_eval(instruction[-1])

        if instruction[0] == 'toggle':
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    lights[x, y] = abs(lights[x, y] - 1)  # flip 1 <-> 0

        elif instruction[1] == 'on':
            lights[x1:x2 + 1:1, y1:y2 + 1:1] = 1

        elif instruction[1] == 'off':
            lights[x1:x2 + 1:1, y1:y2 + 1:1] = 0

    print("After following the instructions, how many lights are lit? ", (np.count_nonzero(lights)))


def part_two():
    with open("input.txt") as input:
        instructions = [line.split() for line in input]

    lights = np.zeros(shape=(1000, 1000), dtype=np.int64)

    for instruction in instructions:
        x1, y1 = literal_eval(instruction[-3])
        x2, y2 = literal_eval(instruction[-1])

        if instruction[0] == 'toggle':
            lights[x1:x2 + 1:1, y1:y2 + 1:1] += 2

        elif instruction[1] == 'on':
            lights[x1:x2 + 1:1, y1:y2 + 1:1] += 1

        elif instruction[1] == 'off':
            lights[x1:x2 + 1:1, y1:y2 + 1:1] -= 1
            lights[lights < 0] = 0  # stop at 0

    print("What is the total brightness of all lights combined after following Santa's instructions? ", lights.sum())


print("=============================== PART ONE ===============================")
part_one()
print("=============================== PART TWO ===============================")
part_two()
