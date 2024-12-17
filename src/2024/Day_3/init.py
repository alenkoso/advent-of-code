import os
import re

def parse_input(file_path):
    with open(file_path) as file:
        return file.read()

def extract(memory):
    instructions = []
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"

    for match in re.finditer(mul_pattern, memory):
        x, y = map(int, match.groups())
        instructions.append(("mul", match.start(), x * y))

    for match in re.finditer(do_pattern, memory):
        instructions.append(("do", match.start(), None))

    for match in re.finditer(dont_pattern, memory):
        instructions.append(("don't", match.start(), None))

    return sorted(instructions, key=lambda x: x[1])

def part1(memory):
    instructions = extract(memory)
    return sum(result for instr, _, result in instructions if instr == "mul")

def part2(memory):
    instructions = extract(memory)
    is_enabled = True
    total = 0

    for instr, _, result in instructions:
        if instr == "do":
            is_enabled = True
        elif instr == "don't":
            is_enabled = False
        elif instr == "mul" and is_enabled:
            total += result

    return total

def main():
    memory = parse_input("input.txt")

    part_1 = part1(memory)
    print(part_1)

    part_2 = part2(memory)
    print(part_2)

if __name__ == "__main__":
    main()
