with open("input.txt") as f:
    DATA = [[int(calorieAmount) for calorieAmount in allCalorieAmounts.split("\n")] for
            allCalorieAmounts in (f.read().strip().split("\n\n"))]


def part_one(data=DATA):
    return max(sum(val) for val in DATA)


print(part_one())

# https://stackoverflow.com/questions/3766633/how-to-sort-with-lambda-in-python
# I now have all mid sums, if I reverse that list, sorted by the sums, I get top 3 elves
DATA.sort(key=lambda x: sum(x), reverse=True)


def part_two(data=DATA):
    return sum(sum(val) for val in DATA[:3])


print(part_two())
