import sys
import copy
from collections import defaultdict


def get_min_max(tiles):
    coordinates = list(tiles.keys())
    min_row, min_column, max_row, max_column = 1e99, 1e99, -1e99, -1e99
    for row, column in coordinates:
        if row < min_row:
            min_row = row
        if row > max_row:
            max_row = row
        if column < min_column:
            min_column = column
        if column > max_column:
            max_column = column
    return min_row, min_column, max_row, max_column


def count_neighbours(tiles, row, col):
    north_east = row - 1, col
    north_west = row - 1, col - 1
    west = row, col - 1
    east = row, col + 1
    south_west = row + 1, col
    south_east = row + 1, col + 1

    return tiles[north_east] + tiles[north_west] + tiles[west] + tiles[east] + tiles[south_west] + tiles[south_east]


# # with open("Inputs\InputDay24_Example.txt") as infile:
with open("../Inputs/InputDay24.txt") as input_file:
    raw = input_file.read()

input_raw = [line for line in raw.split('\n') if line.strip()]

tile_refs = []

for line in input_raw:
    tile = []
    i = 0
    while i < len(line):
        if line[i] in ['n', 's']:
            tile.append(line[i:i + 2])
            i += 2
        else:
            tile.append(line[i])
            i += 1

    tile_refs.append(tile)

tile_board = defaultdict(bool)

for tile in tile_refs:
    r, c = 0, 0
    for ref in tile:
        if ref == 'ne':
            r -= 1
        elif ref == 'nw':
            r -= 1
            c -= 1
        elif ref == 'w':
            c -= 1
        elif ref == 'e':
            c += 1
        elif ref == 'sw':
            r += 1
        elif ref == 'se':
            r += 1
            c += 1

    current = tile_board[(r, c)]

    tile_board[(r, c)] = not current

part_one = 0
for c in tile_board:
    part_one += tile_board[c]

# Sanity check parser
# for ref in tile_refs:
#     print(ref)

print(
    "=========================================================== PART ONE ===========================================================")
print("Go through the renovation crew's list and determine which tiles they need to flip.")
print("After all of the instructions have been followed, how many tiles are left with the black side up? ", part_one)

min_row, min_column, max_row, max_column = get_min_max(tile_board)

print(
    "=========================================================== PART TWO ===========================================================")

sys.stdout.flush()

# Part 2
for i in range(100):
    min_row -= 1
    min_column -= 1
    max_row += 1
    max_column += 1
    new_board = copy.deepcopy(tile_board)
    for row in range(min_row, max_row + 1):
        for column in range(min_column, max_column + 1):
            n = count_neighbours(tile_board, row, column)
            if tile_board[(row, column)]:
                if n == 0 or n > 2:
                    new_board[(row, column)] = False
            else:
                if n == 2:
                    new_board[(row, column)] = True

    tile_board = new_board

part_two = 0
for c in tile_board:
    part_two += tile_board[c]

print("How many tiles will be black after 100 days? ", part_two)
