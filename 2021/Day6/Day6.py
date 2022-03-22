from collections import defaultdict

with open("../inputs/day6.txt") as f:
    input_fish = [int(x) for x in f.read().strip().split(",")]


def solve(number_of_days):
    fish_age_to_count = defaultdict(int)
    for fish in input_fish:
        fish_age_to_count[fish] += 1

    for day in range(number_of_days):
        n = defaultdict(int)
        for age, count in fish_age_to_count.items():
            if age > 0:
                n[age - 1] += count
            else:
                n[6] += count
                n[8] += count
        fish_age_to_count = n

    return sum(fish_age_to_count.values())


print(solve(80))
print(solve(256))
