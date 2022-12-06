with open('input.txt') as f:
    DATA = f.read()


def solve(number_of_chars):
    for index in range(number_of_chars, len(DATA)):
        packet = DATA[index - number_of_chars:index]  # sliding window
        if len(set(packet)) == number_of_chars:
            return index


print("Part 1: ", solve(4))
print("Part 2: ", solve(14))
