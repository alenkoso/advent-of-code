import os
import sys
import re
import time
from helpers.parsing_utils import read_input_file_strip_lines


project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(project_root)


def parse_input(lines):
    # Join all lines into single string
    return " ".join(lines)

def find_all_instructions(memory):
    # Find all valid instructions (mul, do, don't) with their positions
    mul_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    do_pattern = r'do\(\)'
    dont_pattern = r"don't\(\)"

    instructions = []

    # Find all multiplications
    for match in re.finditer(mul_pattern, memory):
        x, y = map(int, match.groups())
        instructions.append(('mul', match.start(), x * y))

        # Find all do() instructions
        for match in re.finditer(do_pattern, memory):
            instructions.append(('do', match.start(), None))

            # Find all don't() instructions
            for match in re.finditer(dont_pattern, memory):
                instructions.append(('dont', match.start(), None))

                # Sort by position in string
                return sorted(instructions, key=lambda x: x[1])

            def solve_part1(memory):
                # Find and sum all valid multiplication results (ignoring do/don't)
                muls = [result for type, _, result in find_all_instructions(memory) if type == 'mul']
                return sum(muls)

            def solve_part2(memory):
                instructions = find_all_instructions(memory)
                enabled = True
                total = 0

                for type, _, result in instructions:
                    if type == 'do':
                        enabled = True
                    elif type == 'dont':
                        enabled = False
                    elif type == 'mul' and enabled:
                        total += result

                        return total

                    def main():
                        # Read input
                        lines = read_input_file_strip_lines("input.txt")
                        memory = parse_input(lines)

                        # Part 1
                        start_time = time.time()
                        part1_result = solve_part1(memory)
                        end_time = time.time()
                        print(f"Part 1: {part1_result}")
                        print(f"Part 1 Execution Time: {end_time - start_time} seconds")

                        # Part 2
                        start_time = time.time()
                        part2_result = solve_part2(memory)
                        end_time = time.time()
                        print(f"Part 2: {part2_result}")
                        print(f"Part 2 Execution Time: {end_time - start_time} seconds")

                        if __name__ == "__main__":
                            main()

