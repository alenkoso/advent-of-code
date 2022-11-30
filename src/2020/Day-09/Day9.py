from itertools import combinations

numbers = []
with open('../Inputs/InputDay9.txt') as f:
    numbers = [int(line.strip()) for line in f]

# part 1
for i in range(25, len(numbers)):
    if not any([x != y and x + y == numbers[i] for x, y in combinations(numbers[i-25:i], 2)]):
        GOAL = numbers[i]
        break

print(GOAL)

# part 2
for i in range(len(numbers) - 1):
    _sum = numbers[i]
    _list = [numbers[i]]
    j = i + 1
    while _sum + numbers[j] <= GOAL:
        _sum += numbers[j]
        _list.append(numbers[j])
        j += 1
    if _sum == GOAL and len(_list) > 1:
        print(min(_list) + max(_list))