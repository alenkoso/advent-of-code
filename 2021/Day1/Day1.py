with open("../inputs/day1.txt") as f:
    DATA = [int(x) for x in f.readlines()]


def part_one(data=DATA):
    return sum(1 if data[x] > data[x - 1] else 0 for x in range(1, len(data)))


def part_two():
    return part_one(
        [DATA[x] + DATA[x - 1] + DATA[x - 2] for x in range(len(DATA)) if x >= 2]
    )


print(part_one())
print(part_two())