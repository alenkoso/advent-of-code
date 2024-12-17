import os
import sys
import time
from collections import deque

project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(project_root)

from helpers.parsing_utils import read_input_file_strip_lines

def parse_input(lines):
    # Split into layout and movement sequence
    content = '\n'.join(lines)
    layout, movements = content.split('\n\n')
    return layout.split('\n'), [move for move in movements if move in "^v<>"]

def find_robot_position(warehouse_layout):
    for row_index, row in enumerate(warehouse_layout):
        for col_index, cell in enumerate(row):
            if cell == '@':
                return row_index, col_index
    return 0, 0

def simulate_warehouse_movement(warehouse, robot_row, robot_col, direction_row, direction_col):
    target_row = robot_row + direction_row
    target_col = robot_col + direction_col
    
    if warehouse[target_row][target_col] == "#":
        return robot_row, robot_col, warehouse
        
    if warehouse[target_row][target_col] == ".":
        return target_row, target_col, warehouse
    
    movable_boxes = deque([(robot_row, robot_col)])
    affected_positions = set()
    movement_possible = True
    
    while movable_boxes:
        current_row, current_col = movable_boxes.popleft()
        if (current_row, current_col) in affected_positions:
            continue
            
        affected_positions.add((current_row, current_col))
        next_row = current_row + direction_row
        next_col = current_col + direction_col

        current_cell = warehouse[next_row][next_col]
        
        if current_cell == "#":
            movement_possible = False
            break
            
        if current_cell == "O":
            movable_boxes.append((next_row, next_col))
        elif current_cell == "[":
            movable_boxes.append((next_row, next_col))
            if warehouse[next_row][next_col + 1] != "]":
                movement_possible = False
                break
            movable_boxes.append((next_row, next_col + 1))
        elif current_cell == "]":
            movable_boxes.append((next_row, next_col))
            if warehouse[next_row][next_col - 1] != "[":
                movement_possible = False
                break
            movable_boxes.append((next_row, next_col - 1))
    
    if not movement_possible:
        return robot_row, robot_col, warehouse
    
    new_warehouse = [list(row) for row in warehouse]
    affected_positions.remove((robot_row, robot_col))
    
    while affected_positions:
        for pos_row, pos_col in sorted(affected_positions):
            next_row = pos_row + direction_row
            next_col = pos_col + direction_col
            if (next_row, next_col) not in affected_positions and new_warehouse[next_row][next_col] == ".":
                new_warehouse[next_row][next_col] = new_warehouse[pos_row][pos_col]
                new_warehouse[pos_row][pos_col] = "."
                affected_positions.remove((pos_row, pos_col))
                break
    
    return target_row, target_col, ["".join(row) for row in new_warehouse]

def calculate_score(warehouse):
    score = 0
    for row_index in range(len(warehouse)):
        for col_index in range(len(warehouse[0])):
            if warehouse[row_index][col_index] in "O[":
                score += 100 * row_index + col_index
    return score

def double_warehouse_width(warehouse):
    expanded = []
    for row in warehouse:
        new_row = []
        for cell in row:
            if cell == "#": new_row.extend(["#", "#"])
            elif cell == "O": new_row.extend(["[", "]"])
            elif cell == ".": new_row.extend([".", "."])
            elif cell == "@": new_row.extend(["@", "."])
        expanded.append("".join(new_row))
    return expanded

def part1(warehouse_layout, movement_sequence):
    movement_directions = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
    
    robot_row, robot_col = find_robot_position(warehouse_layout)
    warehouse = [list(row) for row in warehouse_layout]
    warehouse[robot_row][robot_col] = "."
    warehouse = ["".join(row) for row in warehouse]
    
    for movement in movement_sequence:
        direction_row, direction_col = movement_directions[movement]
        robot_row, robot_col, warehouse = simulate_warehouse_movement(
            warehouse, robot_row, robot_col, direction_row, direction_col
        )
    
    return calculate_score(warehouse)

def part2(warehouse_layout, movement_sequence):
    movement_directions = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
    
    warehouse = double_warehouse_width(warehouse_layout)
    robot_row, robot_col = find_robot_position(warehouse)
    warehouse = [list(row) for row in warehouse]
    warehouse[robot_row][robot_col] = "."
    warehouse = ["".join(row) for row in warehouse]
    
    for movement in movement_sequence:
        direction_row, direction_col = movement_directions[movement]
        robot_row, robot_col, warehouse = simulate_warehouse_movement(
            warehouse, robot_row, robot_col, direction_row, direction_col
        )
    
    return calculate_score(warehouse)

def main():
    # Read input
    lines = read_input_file_strip_lines("input.txt")
    warehouse_layout, movement_sequence = parse_input(lines)
    
    # Part 1
    start_time = time.time()
    part_1 = part1(warehouse_layout, movement_sequence)
    end_time = time.time()
    print(f"Part 1: {part_1}")
    print(f"Part 1 Execution Time: {end_time - start_time} seconds")
    
    # Part 2
    start_time = time.time()
    part_2 = part2(warehouse_layout, movement_sequence)
    end_time = time.time()
    print(f"Part 2: {part_2}")
    print(f"Part 2 Execution Time: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()