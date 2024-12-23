import os
import sys
import time
from itertools import permutations
import numpy as np

project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(project_root)

from helpers.parsing_utils import read_input_file_strip_lines

door_keypad_positions = {
    '7': np.array([0, 0]), '8': np.array([0, 1]), '9': np.array([0, 2]),
    '4': np.array([1, 0]), '5': np.array([1, 1]), '6': np.array([1, 2]),
    '1': np.array([2, 0]), '2': np.array([2, 1]), '3': np.array([2, 2]),
    '0': np.array([3, 1]), 'A': np.array([3, 2])
}

control_keypad_positions = {
    '^': np.array([0, 1]), 'A': np.array([0, 2]),
    '<': np.array([1, 0]), 'v': np.array([1, 1]), '>': np.array([1, 2])
}

directional_moves = {
    '^': np.array([-1, 0]), 'v': np.array([1, 0]),
    '<': np.array([0, -1]), '>': np.array([0, 1])
}

movement_memory = {}

def find_valid_movement_paths(start_position, end_position, robot_level):
    invalid_pos = np.array([3, 0]) if robot_level == 0 else np.array([0, 0])
    position_delta = end_position - start_position
    needed_moves = []
    
    if position_delta[0] < 0:
        needed_moves.extend(['^'] * abs(position_delta[0]))
    else:
        needed_moves.extend(['v'] * position_delta[0])
        
    if position_delta[1] < 0:
        needed_moves.extend(['<'] * abs(position_delta[1]))
    else:
        needed_moves.extend(['>'] * position_delta[1])

    valid_paths = []
    for move_sequence in set(permutations(needed_moves)):
        current_pos = start_position.copy()
        path_valid = True
        
        for move in move_sequence:
            next_pos = current_pos + directional_moves[move]
            if np.array_equal(next_pos, invalid_pos) or (next_pos < 0).any():
                path_valid = False
                break
            current_pos = next_pos
            
        if path_valid:
            valid_paths.append(''.join(move_sequence) + 'A')
            
    return valid_paths if valid_paths else ['A']

def calculate_minimum_moves(door_code, robot_count, current_depth=0):
    memory_key = (door_code, current_depth, robot_count)
    if memory_key in movement_memory:
        return movement_memory[memory_key]

    current_position = (door_keypad_positions if current_depth == 0 else control_keypad_positions)['A']
    total_moves = 0

    for digit in door_code:
        active_keypad = door_keypad_positions if current_depth == 0 else control_keypad_positions
        if digit in active_keypad:
            target_position = active_keypad[digit]
            possible_paths = find_valid_movement_paths(current_position, target_position, current_depth)
            
            if current_depth >= robot_count:
                path_moves = len(min(possible_paths, key=len))
            else:
                shortest_path = float('inf')
                for path in possible_paths:
                    path_moves = calculate_minimum_moves(path, robot_count, current_depth + 1)
                    shortest_path = min(shortest_path, path_moves)
                path_moves = shortest_path
            
            total_moves += path_moves
            current_position = target_position

    movement_memory[memory_key] = total_moves
    return total_moves

def solve_keypad_sequence(keypad_sequences, robot_count):
    total_complexity = 0
    movement_memory.clear()
    
    for sequence in keypad_sequences:
        moves = calculate_minimum_moves(sequence, robot_count)
        sequence_value = int(''.join(filter(str.isdigit, sequence)))
        total_complexity += moves * sequence_value
        
    return total_complexity

def main():
    data = read_input_file_strip_lines("input.txt")
    
    start_time = time.time()
    part_1 = solve_keypad_sequence(data, 2)
    end_time = time.time()
    print("Part 1:", part_1)
    print("Part 1 Execution Time: ", end_time - start_time, "seconds")
    
    start_time = time.time()
    part_2 = solve_keypad_sequence(data, 25)
    end_time = time.time()
    print("Part 2:", part_2)
    print("Part 2 Execution Time: ", end_time - start_time, "seconds")

if __name__ == "__main__":
    main()