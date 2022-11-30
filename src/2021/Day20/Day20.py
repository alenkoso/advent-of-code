import time
from functools import lru_cache


start = time.time()


@lru_cache(maxsize=32)
def process_image(algorithm, light_pixels, step):
    rows = []
    cols = []
    for pixel in light_pixels:
        rows.append(pixel[0])
        cols.append(pixel[1])

    min_row = min(rows)
    max_row = max(rows)
    min_col = min(cols)
    max_col = max(cols)

    processed_lights = set()  # speedy
    for i in range(min_row - 3, max_row + 4):
        for j in range(min_col - 3, max_col + 4):
            binary = ''
            for i1 in [i - 1, i, i + 1]:
                for j1 in [j - 1, j, j + 1]:
                    if min_row <= i1 <= max_row and min_col <= j1 <= max_col:
                        if (i1, j1) in light_pixels:
                            binary += '1'
                        else:
                            binary += '0'
                    else:
                        binary += str(step % 2)
            algo_value = algorithm[int(binary, 2)]
            # print(binary, algo_value)
            if algo_value == '#':
                processed_lights.add((i, j))
    return frozenset(processed_lights)


with open("input.in") as file:
    lines = file.read().strip().splitlines()

    algorithm = lines[0]
    lines = lines[2:]
    board = [[ch for ch in line] for line in lines]

    light_pixels = set()
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col == '#':
                light_pixels.add((i, j))

    processed_pixels = frozenset(light_pixels)
    end1 = None
    for i in range(50):
        if i == 2:
            print("1: " + str(len(processed_pixels)))
            end1 = time.time()
        processed_pixels = frozenset(process_image(algorithm, processed_pixels, i))
    print("2: " + str(len(processed_pixels)))
    end = time.time()
    print()
    print("Execution time")
    print("1:     " + str(end1-start) + "s")
    print("2:     " + str(end-end1) + "s")
    print("Total: " + str(end-start) + "s")
