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
        before = registers.copy()
        ip += 2

        if len(output) > len(program):
            if debug:
                print(f"Early termination: A={registers['A']}, output={output}")
            break

        if opcode == 0:
            registers['A'] //= 2 ** combo_value(operand)
        elif opcode == 1:
            registers['B'] ^= operand
        elif opcode == 2:
            registers['B'] = combo_value(operand) % 8
        elif opcode == 3:
            if registers['A'] != 0:
                if debug:
                    print(f"Jump triggered: ip={ip-2}, A={registers['A']}, target={operand}")
                ip = operand
        elif opcode == 4:
            registers['B'] ^= registers['C']
        elif opcode == 5:
            val = combo_value(operand) % 8
            if debug:
                print(f"Output {val} from value {combo_value(operand)}")
            output.append(val)
        elif opcode == 6:
            registers['B'] = registers['A'] // (2 ** combo_value(operand))
        elif opcode == 7:
            registers['C'] = registers['A'] // (2 ** combo_value(operand))
        else:
            raise ValueError(f"Unknown opcode: {opcode}")

        after = registers.copy()
        if debug:
            print(f"Op {opcode}: A={before['A']} -> {after['A']}, B={before['B']} -> {after['B']}, C={before['C']} -> {after['C']}")

        if steps == MAX_STEPS:
            if debug:
                print(f"Step limit reached: A={registers['A']}, B={registers['B']}, C={registers['C']}, Output={output}")

    return output, registers

def find_min_register_a(program):
    target_length = len(program)
    queue = [(program, target_length - 1, 0)]  # (current program, offset, value)

    while queue:
        prog, offset, value = queue.pop(0)

        for candidate in range(8):  # Try all possible outputs [0-7]
            next_value = (value << 3) + candidate
            result, _ = run_program(next_value, 0, 0, prog, debug=False)

            if result == prog[offset:]:
                if offset == 0:
                    return next_value  # Found the valid A
                queue.append((prog, offset - 1, next_value))
    
    return None


if __name__ == "__main__":
    with open("input.txt") as file:
        lines = file.read().splitlines()
    
    register_a = int(lines[0].split(": ")[1])
    register_b = int(lines[1].split(": ")[1])
    register_c = int(lines[2].split(": ")[1])

    program_line = next(line for line in lines if line.startswith("Program:"))
    program = list(map(int, program_line.split(": ")[1].split(",")))

    part_one_output, registers = run_program(register_a, register_b, register_c, program, debug=False)
    print("Part 1 Output:", ",".join(map(str, part_one_output)))
    print("Final Registers:", registers)

    lowest_a = find_min_register_a(program)
    print("Part 2:", lowest_a)
