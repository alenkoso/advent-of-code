array = []

with open('../Inputs/InputDay1.txt') as f:
    for line in f:
        array.append(int(line))

left = 0
right = len(array) - 1
array.sort()

# Sum of two numbers
while left < right:
    sum = array[right] + array[left]
    if sum == 2020:
        print("Part one: ", array[right] * array[left])
        print("The pair that gives our ending sum is: ", array[right], array[left])
        print("=========================================================================")
        break

    if sum > 2020:
        right -= 1
    else:
        left += 1

# Sum of three numbers
for i in range(len(array) - 2):
    left = i + 1
    right = len(array) - 1
    while left < right:
        sum = array[i] + array[right] + array[left]
        if sum == 2020:
            print("Part two: ", array[i] * array[right] * array[left])
            print("Triplet that gives our ending sum is: ", array[i], array[right], array[left])
            print("=========================================================================")
            break

        if sum > 2020:
            right -= 1
        elif sum < 2020:
            left += 1
