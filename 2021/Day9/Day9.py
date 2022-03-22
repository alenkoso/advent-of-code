from collections import Counter

ll = [[int(y) for y in x] for x in open('../inputs/day9.txt').read().strip().split('\n')]


def basin(i, j):
    downhill = None
    for (di, dj) in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
        if di in range(len(ll)) and dj in range(len(ll[0])):
            if ll[i][j] > ll[di][dj]:
                downhill = (di, dj)
    if downhill is None:
        return i, j
    result = basin(*downhill)
    return result


basins = []
for i in range(len(ll)):
    for j in range(len(ll[0])):
        if ll[i][j] != 9:
            basins.append(basin(i, j))

basins_result = 1
for basin, common in Counter(basins).most_common(3):
    basins_result *= common
print(basins_result)
