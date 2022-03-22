import re
import collections

# https://www.youtube.com/watch?v=21OXFXOtGOU -> good to check


def part_one(data):
    points = collections.defaultdict(int)
    for line in data:
        x1, y1, x2, y2 = map(int, re.match(r'(\d+),(\d+) -> (\d+),(\d+)', line).groups())
        # here we are just looking for points who are either on horizontal or vertical lines
        if x1 == x2:  # horizontal
            for y in range(min(y1, y2), max(y1, y2) + 1):
                points[(x1, y)] += 1
        elif y1 == y2:  # vertical
            for x in range(min(x1, x2), max(x1, x2) + 1):
                points[(x, y1)] += 1
    return len([x for x in points.values() if x >= 2])


def part_two(data):
    points = collections.defaultdict(int)
    for line in data:
        x1, y1, x2, y2 = map(int, re.match(r'(\d+),(\d+) -> (\d+),(\d+)', line).groups())
        # here we need to check the diagonals as well
        if x1 == x2:  # horizontal
            for y in range(min(y1, y2), max(y1, y2) + 1):
                points[(x1, y)] += 1
        elif y1 == y2:  # vertical
            for x in range(min(x1, x2), max(x1, x2) + 1):
                points[(x, y1)] += 1
        else:  # for diagonals we need to add the direction (-1 down | +1 up | 0 same line)
            x_mod = -1 if x1 > x2 else 1
            y_mod = -1 if y1 > y2 else 1
            # points on the line are therefore x + the direction of the line
            for x, y in zip(range(x1, x2 + x_mod, x_mod), range(y1, y2 + y_mod, y_mod)):
                points[(x, y)] += 1

    return len([x for x in points.values() if x >= 2])


if __name__ == "__main__":
    test1_input = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2""".split('\n')

    test1_answer = 5
    if part_one(test1_input) == test1_answer:
        print("First Question Test Passed")
    else:
        print("First Question Test FAILED")

    test2_input = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2""".split('\n')
    test2_answer = 12
    if part_two(test2_input) == test2_answer:
        print("Second Question Test 1 Passed")
    else:
        print("Second Question Test 1 FAILED")

    with open("../inputs/day5.txt") as f:
        input_data = [line.rstrip() for line in f]

    import copy

    print("Answer 1: ", part_one(copy.copy(input_data)))
    print("Answer 2: ", part_two(copy.copy(input_data)))
