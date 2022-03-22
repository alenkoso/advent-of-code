numbers = [0]

with open("../Inputs/InputDay10.txt") as input:
    for line in input:
        numbers.append(int(line))

numbers.sort()
numbers.append(numbers[-1] + 3)

ones, threes = 0, 0

for i, j in zip(numbers, numbers[1:]):
    if i + 1 == j:
        ones += 1
    elif i + 3 == j:
        threes += 1

partOne = ones * threes

partTwo, x = 1, 0
length = []

while x < len(numbers):
    if numbers[x] + 1 in numbers:
        length.append(numbers[x])
    elif numbers[x] + 1 not in numbers:
        if len(length) > 1:
            partTwo = partTwo * (pow(2, len(length) - 1) - max((len(length) - 3), 0))
        length = []
    x += 1

print("Part one: ", partOne)
print("Part two: ", partTwo)
