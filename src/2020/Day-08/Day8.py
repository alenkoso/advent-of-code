instructions = []

with open('../Inputs/InputDay8.txt') as file:
    for line in file:
        data = line.split()
        instructions.append(data)

# Part 1


def calcAcc(instructions):
    visited = set()
    acc = i = 0
    while i not in visited:
        visited.add(i)
        if i >= len(instructions):
            return acc, True
        instruction, value = instructions[i]
        if instruction == 'nop':
            i += 1
        elif instruction == 'jmp':
            i += int(value)
        else:
            i += 1
            acc += int(value)
    return acc, False


print(calcAcc(instructions)[0])

# Part 2

for pos, item in enumerate(instructions):
    operation, argument = item
    if operation == "acc":
        continue
    if operation == "nop":
        instructions[pos] = ("jmp", argument)
        acc, terminated = calcAcc(instructions)
    else:
        instructions[pos] = ("nop", argument)
        acc, terminated = calcAcc(instructions)
    instructions[pos] = [operation, argument]
    if terminated:
        print(acc)
        break