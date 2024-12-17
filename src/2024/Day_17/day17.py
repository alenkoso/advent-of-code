def run_program(register_a, register_b, register_c, program):
    registers = {'A': register_a, 'B': register_b, 'C': register_c}
    ip = 0 
    output = []

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

    while ip < len(program):
        opcode = program[ip]
        operand = program[ip + 1]
        ip += 2

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
        else:
            raise ValueError(f"Unknown opcode: {opcode}")
    
    return ",".join(map(str, output))

if __name__ == "__main__":
    with open("input.txt") as file:
        lines = file.read().splitlines()
    
    register_a = int(lines[0].split(": ")[1])
    register_b = int(lines[1].split(": ")[1])
    register_c = int(lines[2].split(": ")[1])

    program_line = next(line for line in lines if line.startswith("Program:"))
    program = list(map(int, program_line.split(": ")[1].split(",")))

    result = run_program(register_a, register_b, register_c, program)
    print("Part 1: ", result)
