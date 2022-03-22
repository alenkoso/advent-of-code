result = 0
arr = []
visited = set()


def syncd(arr):
    for row in arr:
        for el in row:
            if el != 0:
                return False
    return True


def illuminate(arr, row, col):
    global visited
    visited.add((row, col))
    for i in filter((lambda x: x >= 0 and x < len(arr)), range(row - 1, row + 2)):
        for j in filter((lambda x: x >= 0 and x < len(arr[row])), range(col-1, col+2)):
            try:
                if i != row or j != col:
                    arr[i][j] += 1
                if ((i, j) not in visited) and arr[i][j] > 9:
                    illuminate(arr, i, j)
            except IndexError:
                continue


def solve1day(arr: list(list())) -> None:
    global result, visited
    for row in range(0, len(arr)):
        for col in range(0, len(arr[row])):
            arr[row][col] += 1
            if arr[row][col] == 10:
                illuminate(arr, row, col)
    visited = set()
    for row in range(0, len(arr)):
        for col in range(0, len(arr[row])):
            if arr[row][col] >= 10:
                arr[row][col] = 0
                result += 1


with open("input.in", "r") as f:
    for line in f.readlines():
        arr.append([int(n) for n in line.strip()])
    arr2 = arr.copy()
    for i in range(0, len(arr)):
        arr2[i] = arr[i].copy()
    step = 0
    for i in range(0, 100):
        solve1day(arr)
    print(result)
    while syncd(arr2) == False:
        solve1day(arr2)
        step += 1
    print(step)