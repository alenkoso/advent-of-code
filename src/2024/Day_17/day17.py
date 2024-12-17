import sys
import os

project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(project_root)

from helpers.file_utils import read_input_file

def run_program(register_a, register_b, register_c, program, debug=False):
    registers = {'A': register_a, 'B': register_b, 'C': register_c}
    ip = 0
    output = []
    MAX_STEPS = len(program) * 100
    steps = 0

    def combo_value(operand):
        if operand <= 3:
            return operand
        elif operand == 4:
            return registers['A']
        elif operand == 5:
            return registers['B']
        elif operand == 6:
            return registers['C']
        raise ValueError("Invalid combo operand")

    while ip < len(program) and steps < MAX_STEPS:
        steps += 1
        opcode = program[ip]
        operand = program[ip + 1]
        ip += 2

        if len(output) > len(program):
            break

        if opcode == 0:
            registers['A'] //= 2 ** combo_value(operand)
        elif opcode == 1:
            registers['B'] ^= operand
        elif opcode == 2:
            registers['B'] = combo_value(operand) % 8
        elif opcode == 3:
            if registers['A'] != 0:
                ip = operand
        elif opcode == 4:
            registers['B'] ^= registers['C']
        elif opcode == 5:
            output.append(combo_value(operand) % 8)
        elif opcode == 6:
            registers['B'] = registers['A'] // (2 ** combo_value(operand))
        elif opcode == 7:
            registers['C'] = registers['A'] // (2 ** combo_value(operand))

    return output, registers

def find_min_register_a(program):
    target_length = len(program)
    queue = [(program, target_length - 1, 0)]

    while queue:
        prog, offset, value = queue.pop(0)
        for candidate in range(8):
            next_value = (value << 3) + candidate
            result, _ = run_program(next_value, 0, 0, prog)
            
            if result == prog[offset:]:
                if offset == 0:
                    return next_value
                queue.append((prog, offset - 1, next_value))
    return None

def main():
    # Read input
    lines = read_input_file("input.txt", mode='lines')
    
    # Parse registers
    register_a = int(lines[0].split(": ")[1])
    register_b = int(lines[1].split(": ")[1])
    register_c = int(lines[2].split(": ")[1])

    # Parse program
    program_line = next(line for line in lines if line.startswith("Program:"))
    program = list(map(int, program_line.split(": ")[1].split(",")))

    # Part 1
    part_one_output, registers = run_program(register_a, register_b, register_c, program)
    print(f"Part 1: {','.join(map(str, part_one_output))}")

    # Part 2
    lowest_a = find_min_register_a(program)
    print(f"Part 2: {lowest_a}")

if __name__ == "__main__":
    main()