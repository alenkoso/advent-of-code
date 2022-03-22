with open('../Inputs/InputDay6.txt') as file:
    lines = file.read().strip()

partOneGroup = lines.split('\n\n')
partOneNumber = sum([len(set(group.replace('\n', ''))) for group in partOneGroup])
print(partOneNumber)

partTwoGroup = lines.split('\n\n')
nums = []
for group in partTwoGroup:
    temp = group.split('\n')
    num = len(set.intersection(*[set(t) for t in temp]))
    nums.append(num)
print(sum(nums))
