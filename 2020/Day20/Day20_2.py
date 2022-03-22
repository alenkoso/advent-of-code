import re
import math
import itertools
import numpy as np
from collections import defaultdict


class Tile:
    def __init__(self, tile_id):
        self.tile_id = tile_id
        self.raw_data = []
        self.data = None
        self.edge_matches_other = [None, None, None, None]

    def __repr__(self):
        return f"Tile {self.tile_id}"

    def rotate(self):
        # only rotates left
        self.data = np.rot90(self.data)  # , times)

    def undo_transformation(self):
        pass

    def flip(self, axis):
        if axis == 'x':
            self.data = np.fliplr(self.data)
            return True
        elif axis == 'y':
            self.data = np.flipud(self.data)
            return True
        else:
            print(axis)
            return False

    def get_edges(self):
        top_row = self.data[0, :]
        bottom_row = self.data[-1, :]
        left_row = self.data[:, 0]
        right_row = self.data[:, -1]
        return top_row, bottom_row, left_row, right_row

    def edge_matches(self, other, direction):
        m_edges = self.get_edges()
        o_edges = other.get_edges()

        if direction == 'up':
            return (m_edges[0] == o_edges[1]).all()
        elif direction == 'down':
            return (m_edges[1] == o_edges[0]).all()
        elif direction == 'left':
            return (m_edges[2] == o_edges[3]).all()
        elif direction == 'right':
            return (m_edges[3] == o_edges[2]).all()

        raise ValueError(direction1)

    def edge_matches_any_side(self, other):
        m_edges = self.get_edges()
        o_edges = other.get_edges()

        for i, m in enumerate(m_edges):
            for j, o in enumerate(o_edges):
                if (m == o).all():
                    self.edge_matches_other[i] = self, i
                    other.edge_matches_other[j] = other, j
                    return True
                if (m == o[::-1]).all():
                    self.edge_matches_other[i] = self, i
                    other.edge_matches_other[j] = other, -j
                    return True
        return False


def get_empty_tile(array):
    for row in range(array.shape[0]):
        for col in range(array.shape[1]):
            if array[row, col] == 0:
                return row, col
    return None


def check_neighbours(array, rowcol):
    row, col = rowcol
    tile = array[row, col]

    # up
    if row - 1 >= 0:
        other = array[row - 1, col]
        if other and not tile.edge_matches(other, 'up'):
            return False
    # down
    if row + 1 < array.shape[0]:
        other = array[row + 1, col]
        if other and not tile.edge_matches(other, 'down'):
            return False
    # left
    if col - 1 >= 0:
        other = array[row, col - 1]
        if other and not tile.edge_matches(other, 'left'):
            return False
    # right
    if col + 1 < array.shape[1]:
        other = array[row, col + 1]
        if other and not tile.edge_matches(other, 'right'):
            return False

    return True


def find_solution(unplaced_tiles, array, corner_tiles):
    rowcol = get_empty_tile(array)
    # print(rowcol)
    if not rowcol:
        return True
    row, col = rowcol
    # square array
    rowsize = array.shape[0]
    if rowcol in [(0, 0), (0, rowsize - 1), (rowsize - 1, 0), (rowsize - 1, rowsize - 1)]:
        for tile in corner_tiles:
            array[row, col] = tile
            # No flips
            for i in range(4):
                is_valid = check_neighbours(array, (row, col))
                if is_valid:
                    if find_solution(unplaced_tiles, array, corner_tiles - {tile}):
                        return True
                tile.rotate()
            # Flip x
            tile.flip('x')
            for i in range(4):
                is_valid = check_neighbours(array, (row, col))
                if is_valid:
                    if find_solution(unplaced_tiles, array, corner_tiles - {tile}):
                        return True
                tile.rotate()
            # Flip x&y
            tile.flip('y')
            for i in range(4):
                is_valid = check_neighbours(array, (row, col))
                if is_valid:
                    if find_solution(unplaced_tiles, array, corner_tiles - {tile}):
                        return True
                tile.rotate()
            # Flip y
            tile.flip('x')
            for i in range(4):
                is_valid = check_neighbours(array, (row, col))
                if is_valid:
                    if find_solution(unplaced_tiles, array, corner_tiles - {tile}):
                        return True
                tile.rotate()
            tile.flip('y')

            array[row, col] = 0
    else:
        for tile in unplaced_tiles:
            array[row, col] = tile
            # No flips
            for i in range(4):
                is_valid = check_neighbours(array, (row, col))
                if is_valid:
                    if find_solution(unplaced_tiles - {tile}, array, corner_tiles):
                        return True
                tile.rotate()
            # Flip x
            tile.flip('x')
            for i in range(4):
                is_valid = check_neighbours(array, (row, col))
                if is_valid:
                    if find_solution(unplaced_tiles - {tile}, array, corner_tiles):
                        return True
                tile.rotate()
            # Flip x&y
            tile.flip('y')
            for i in range(4):
                is_valid = check_neighbours(array, (row, col))
                if is_valid:
                    if find_solution(unplaced_tiles - {tile}, array, corner_tiles):
                        return True
                tile.rotate()
            # Flip y
            tile.flip('x')
            for i in range(4):
                is_valid = check_neighbours(array, (row, col))
                if is_valid:
                    if find_solution(unplaced_tiles - {tile}, array, corner_tiles):
                        return True
                tile.rotate()
            tile.flip('y')

            array[row, col] = 0

    print("Backtrack", rowcol)
    return False


def render_array(array):
    array_dim = array.shape[0]
    tile_dim = array[0, 0].data.shape[0]
    noborder_dim = tile_dim - 2

    dim = array.shape[0] * noborder_dim
    print("Pic dimensions:", dim)
    pic = np.zeros((dim, dim), dtype=object)

    for r in range(array_dim):
        for c in range(array_dim):
            r_idx, c_idx = noborder_dim * r, noborder_dim * c
            tile_data = array[r, c].data
            noborder = tile_data[1:-1, 1:-1]
            pic[r_idx: r_idx + noborder_dim, c_idx: c_idx + noborder_dim] = noborder

    return pic


def find_seamonsters(pic, sm):
    sm_r, sm_c = sm.shape
    dim = pic.shape[0]

    sm_care = (sm == '#')

    found_start = []

    for r in range(dim - sm_r):
        for c in range(dim - sm_c):
            pic_window = pic[r: r + sm_r, c:c + sm_c]
            check_window = (pic_window == sm)
            found = True
            for sr in range(sm_r):
                for sc in range(sm_c):
                    if sm_care[sr, sc] and not check_window[sr, sc]:
                        found = False
                        break
                if not found:
                    break
            if found:
                found_start.append((r, c))

    return found_start


def find_seamonsters_with_transform(pic, sm):
    for i in range(4):
        sm_starts = find_seamonsters(pic, sm)
        if sm_starts:
            return pic, sm_starts
        pic = np.rot90(pic)
    # Flip x
    pic = np.fliplr(pic)
    for i in range(4):
        sm_starts = find_seamonsters(pic, sm)
        if sm_starts:
            if sm_starts:
                return pic, sm_starts
        pic = np.rot90(pic)
    # Flip x&y
    pic = np.flipud(pic)
    for i in range(4):
        sm_starts = find_seamonsters(pic, sm)
        if sm_starts:
            return pic, sm_starts
        pic = np.rot90(pic)
    # Flip y
    pic = np.fliplr(pic)
    for i in range(4):
        sm_starts = find_seamonsters(pic, sm)
        if sm_starts:
            return pic, sm_starts
        pic = np.rot90(pic)
    pic = np.flipud(pic)
    return pic, None


def censor_seamonsters(pic, sm):
    pic, sm_starts = find_seamonsters_with_transform(pic, sm)
    sm_r, sm_c = sm.shape
    sm_care = (sm == '#')
    for row, col in sm_starts:
        pic_slice = pic[row: row + sm_r, col: col + sm_c]
        for r in range(sm_r):
            for c in range(sm_c):
                if sm_care[r, c]:
                    pic_slice[r][c] = '.'


if __name__ == "__main__":
    # with open("input_small.txt") as infile:
    with open("../Inputs/InputDay20.txt") as infile:
        raw = infile.read()

    input_raw = [line for line in raw.split('\n') if line.strip()]

    tiles = []
    current_tile = None
    for line in input_raw:
        if line.startswith("Tile"):
            if current_tile:
                tiles.append(current_tile)
                current_tile = None
            id_match = re.match(r"Tile (\d+):", line)
            tile_id = int(id_match.group(1))
            current_tile = Tile(tile_id)
        else:
            current_tile.raw_data.append(list(line))

    if current_tile:
        tiles.append(current_tile)

    for tile in tiles:
        tile.data = np.array(tile.raw_data)

    print(len(tiles))

    dim = int(math.sqrt(len(tiles)))

    #   # Part 1
    tile_matches_map = defaultdict(int)
    for i, t1 in enumerate(tiles):
        for j, t2 in enumerate(tiles[i + 1:]):
            part_one = t1.edge_matches_any_side(t2)
            if part_one:
                tile_matches_map[t1] += 1
                tile_matches_map[t2] += 1
    # print(tile_matches_map)
    part_one = 1
    corner_tiles = set()
    for t, val in tile_matches_map.items():
        if val == 2:
            corner_tiles.add(t)
            part_one *= t.tile_id

    print(
        "=========================================================== PART ONE ===========================================================")
    print("What do you get if you multiply together the IDs of the four corner tiles?", part_one)

    # Part 2
    unplaced_tiles = set(tiles) - corner_tiles
    array = np.zeros(shape=(dim, dim), dtype=object)

    # Not sure why running this in non-debug mode results in suboptimal perf...
    solution_found = find_solution(unplaced_tiles, array, corner_tiles)

    with open("../Inputs/InputDay20_SeaMonster.txt") as sm_file:
        sm_raw = sm_file.read()

    sm_l = [list(line) for line in sm_raw.split('\n') if line.strip()]

    sm = np.array(sm_l)

    pic = render_array(array)

    # Debug: print out the full combined and transformed pic
    # pic_t, sm_starts = find_seamonsters_with_transform(pic, sm)

    # with open("full_pic.txt", 'w') as outfile:
    #     for row in range(pic.shape[0]):
    #         for col in range(pic.shape[0]):
    #             outfile.write(pic_t[row, col])
    #         outfile.write('\n')

    censor_seamonsters(pic, sm)

    part_two = np.count_nonzero(pic == '#')
    # 2743 is too high, but 2366 is correct

    print(
        "=========================================================== PART TWO ===========================================================")
    print("How many # are not part of a sea monster? ", part_two)
