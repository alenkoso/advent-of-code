import os
import sys
import time

project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(project_root)
from helpers.file_utils import read_input_file

def main():
    input_data = read_input_file("input.txt", mode='lines_stripped')
    
    # Preprocess the input
    width = len(input_data[0])
    data = ''.join(input_data)

    direction_map = {
        'S': [],
        '|': [width, -width],
        '-': [-1, 1],
        '.': [],
        '7': [-1, width],
        'L': [1, -width],
        'J': [-1, -width],
        'F': [1, width]
    }

    start_position = data.find('S')
    path = {start_position}
    data = [direction_map[c] for c in data]

    # Find the starting direction for 'S'
    for i, offsets in enumerate(data):
        if start_position in (i + o for o in offsets):
            direction_map['S'].append(i - start_position)

    # Part 1: Find the longest distance
    start_time = time.time()
    distance = 0
    new_positions = None
    while True:
        new_positions_temp = new_positions
        new_positions = set()
        for p in (new_positions_temp or path):
            for offset in data[p]:
                if p + offset not in path:
                    new_positions.add(p + offset)
        
        if new_positions:
            path |= new_positions
            distance += 1
        else:
            break
    end_time = time.time()
    print('Part 1:', distance)
    print(f"Part 1 Execution Time: {end_time - start_time} seconds")

    # Part 2: Find the area inside the loop
    start_time = time.time()
    inside = 0
    for i in range(len(data)):
        if i in path:
            continue
        outside_right = outside_left = True
        j = i
        while j > 0:
            if j in path and 1 in data[j]:
                outside_right = not outside_right
            if j in path and -1 in data[j]:
                outside_left = not outside_left
            j -= width

        if not (outside_right or outside_left):
            inside += 1
    end_time = time.time()
    print('Part 2:', inside)
    print(f"Part 2 Execution Time: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()