def part_one():
    res = []
    with open("../inputs/day7.txt") as f:
        res = f.read().split(",")
    res = [int(i) for i in res]
    ans = float("inf")
    for i in range(min(res), max(res)):
        diff = sum(abs(i - j) for j in res)
        ans = min(ans, diff)
    print(ans)


def part_two():
    res = []
    with open("../inputs/day7.txt") as f:
        res = f.read().split(",")
    res = [int(i) for i in res]
    ans = float("inf")
    for i in range(min(res), max(res)):
        diff = sum(abs(i - j) * (abs(i - j) + 1) // 2 for j in res)
        ans = min(ans, diff)
    print(ans)


part_one()
part_two()
