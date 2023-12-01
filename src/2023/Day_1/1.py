import sys
import os

project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(project_root)

from helpers.parsing_utils import read_input_file

def extract_digit_part1(line):
    first_digit = next((char for char in line if char.isdigit()), None)
    last_digit = next((char for char in reversed(line) if char.isdigit()), None)
    return int(first_digit + last_digit) if first_digit and last_digit else 0

def extract_digit_part2(line):
    ### Extract the real first and last digit (numerical or spelled out) for Part 2. ###
    convert = {
        "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
        "six": 6, "seven": 7, "eight": 8, "nine": 9
    }
    
    n = []
    cur = list(line)
    for i in range(len(line)):
        if line[i].isdigit():
            n.append(int(line[i]))
            continue

        for word, num in convert.items():
            if list(word) == cur[i:i+len(word)]:
                n.append(num)

    if n:
        a, b = n[0], n[-1]
        return a * 10 + b
    return 0


def sum_calibration_values(extract_function, file_path):
    lines = read_input_file(file_path)
    return sum(extract_function(line.strip()) for line in lines)

input_file = 'input.txt'
total_sum_part1 = sum_calibration_values(extract_digit_part1, input_file)
total_sum_part2 = sum_calibration_values(extract_digit_part2, input_file)

print(f"Part 1 - Sum of all calibration values: {total_sum_part1}")
print(f"Part 2 - Sum of all calibration values: {total_sum_part2}")

