from operator import mul

with open("../inputs/day2.txt") as f:
    splitLine = lambda x: [x[: x.index(" ")], int(x[x.index(" ") + 1 :])]
    DATA = [splitLine(x.strip()) for x in f.readlines()]


def part_one():
    return mul(
        sum(x[1] if x[0] == "down" else -x[1] for x in DATA if x[0] in ("up, down")),
        sum(x[1] for x in DATA if x[0] == "forward"),
    )


def part_two():
    aim = depth = horizontal = 0
    for x in DATA:
        if x[0] == "up":
            aim -= x[1]
        elif x[0] == "down":
            aim += x[1]
        else:
            horizontal += x[1]
            depth += x[1] * aim
    return depth * horizontal


print(part_one())
print(part_two())