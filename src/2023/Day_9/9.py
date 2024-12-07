import os
import sys
import time
from helpers.file_utils import read_input_file


project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(project_root)

def calculate_next_value(history):
    if sum(item != 0 for item in history) == 0:
        return 0
    differences = [history[i + 1] - history[i] for i in range(len(history) - 1)]
    return history[-1] + calculate_next_value(differences)

def calculate_previous_value(history):
    reversed_history = history[::-1]
    return calculate_next_value(reversed_history)

def main():
    input_data = read_input_file("input.txt", mode='lines_stripped')
    histories = [[int(number) for number in line.split()] for line in input_data]

    # Part 1
    start_time = time.time()  # Start time
    total_next_values = sum(calculate_next_value(history) for history in histories)
    print(f"Part 1: {total_next_values}")
    end_time = time.time()  # End time
    print(f"Part 1 Execution Time: {end_time - start_time} seconds")

    # Part 2
    start_time = time.time()  # Start time
    total_previous_values = sum(calculate_previous_value(history) for history in histories)
    print(f"Part 2: {total_previous_values}")
    end_time = time.time()  # End time
    print(f"Part 2 Execution Time: {end_time - start_time} seconds")

    if __name__ == '__main__':
        main()

