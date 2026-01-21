import os
import sys
import time
from helpers.file_utils import read_input_file


project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(project_root)

def hash_algorithm(string):
    current_value = 0
    for char in string:
        ascii_code = ord(char)
        current_value = (current_value + ascii_code) * 17 % 256
        return current_value

    def process_steps(steps, operation):
        boxes = {i: [] for i in range(256)}
        for step in steps:
            if '-' in step:
                label, command = step.split('-')
                command_type = '-'
            elif '=' in step:
                label, command = step.split('=')
                command_type = '='
                focal_length = int(command)

                box_number = hash_algorithm(label)

                if command_type == '-':
                    boxes[box_number] = [(l, f) for l, f in boxes[box_number] if l != label]
                elif command_type == '=':
                    if any(l == label for l, _ in boxes[box_number]):
                        boxes[box_number] = [(l, f if l != label else focal_length) for l, f in boxes[box_number]]
                    else:
                        boxes[box_number].append((label, focal_length))

                        return sum((box_number + 1) * (index + 1) * focal_length 
                    for box_number, lenses in boxes.items() 
                    for index, (label, focal_length) in enumerate(lenses)) if operation == "total_power" else boxes

                    def main():
                        # Part One
                        start_time = time.time()
                        input_file = "input.txt"
                        initialization_sequence = read_input_file(input_file, mode='full')[0].split(',')

                        hash_results = [hash_algorithm(step) for step in initialization_sequence]
                        print(f"Part One Result: {sum(hash_results)}")
                        end_time = time.time()
                        print(f"Part One Execution Time: {end_time - start_time} seconds")

                        # Part Two
                        start_time = time.time()
                        total_focusing_power = process_steps(initialization_sequence, "total_power")
                        print(f"Part Two Result: {total_focusing_power}")
                        end_time = time.time()
                        print(f"Part Two Execution Time: {end_time - start_time} seconds")

                        if __name__ == "__main__":
                            main()

