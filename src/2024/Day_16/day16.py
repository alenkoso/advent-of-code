import time
import heapq
import sys
import os

# Adjust the project path
project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(project_root)

from helpers.parsing_utils import read_input_file_to_grid


def locate_start_and_end(grid):
    start_position, end_position = None, None
    for row_index, row in enumerate(grid):
        for col_index, cell in enumerate(row):
            if cell == 'S':
                start_position = (row_index, col_index)
            elif cell == 'E':
                end_position = (row_index, col_index)
    return start_position, end_position


def execute_a_star_search(grid, start_position, movement_directions, reverse_search=False):
    num_rows, num_cols = len(grid), len(grid[0])
    priority_queue = []
    distance_map = {}
    visited_states = set()

    # Initialize queue for forward or reverse search
    if reverse_search:
        for direction in range(4):
            heapq.heappush(priority_queue, (0, *start_position, direction))
    else:
        heapq.heappush(priority_queue, (0, *start_position, 1))  # Start facing East

    while priority_queue:
        current_cost, row, col, current_direction = heapq.heappop(priority_queue)

        if (row, col, current_direction) not in distance_map:
            distance_map[(row, col, current_direction)] = current_cost

        if (row, col, current_direction) in visited_states:
            continue
        visited_states.add((row, col, current_direction))

        # Move forward
        row_delta, col_delta = movement_directions[current_direction]
        next_row, next_col = row + row_delta, col + col_delta
        if 0 <= next_row < num_rows and 0 <= next_col < num_cols and grid[next_row][next_col] != '#':
            heapq.heappush(priority_queue, (current_cost + 1, next_row, next_col, current_direction))

        # Rotate left or right
        heapq.heappush(priority_queue, (current_cost + 1000, row, col, (current_direction + 1) % 4))
        heapq.heappush(priority_queue, (current_cost + 1000, row, col, (current_direction + 3) % 4))

    return distance_map


if __name__ == "__main__":
    # Movement directions: Up, Right, Down, Left
    movement_directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    # Parse the input grid
    grid = read_input_file_to_grid("input.txt")
    start_position, end_position = locate_start_and_end(grid)

    # Part 1: Perform forward A* search to compute the best score
    start_time_part1 = time.time()
    priority_queue = []
    heapq.heappush(priority_queue, (0, *start_position, 1))  # Start facing East
    forward_distance_map = {}
    visited_states = set()
    best_score = None

    while priority_queue:
        current_cost, row, col, direction = heapq.heappop(priority_queue)
        if (row, col, direction) not in forward_distance_map:
            forward_distance_map[(row, col, direction)] = current_cost
        if (row, col, direction) in visited_states:
            continue
        visited_states.add((row, col, direction))
        if (row, col) == end_position and best_score is None:
            best_score = current_cost

        # Move forward
        row_delta, col_delta = movement_directions[direction]
        next_row, next_col = row + row_delta, col + col_delta
        if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]) and grid[next_row][next_col] != '#':
            heapq.heappush(priority_queue, (current_cost + 1, next_row, next_col, direction))

        # Rotate left and right
        heapq.heappush(priority_queue, (current_cost + 1000, row, col, (direction + 1) % 4))
        heapq.heappush(priority_queue, (current_cost + 1000, row, col, (direction + 3) % 4))

    execution_time_part1 = time.time() - start_time_part1
    
    print(f"Part 1: Best score is {best_score}")
    print(f"Part 1 execution time: {execution_time_part1:.5f} seconds")

    # Part 2: Perform backward A* search from end to compute optimal paths
    start_time_part2 = time.time()
    priority_queue = []
    backward_distance_map = {}
    visited_states = set()

    for direction in range(4):
        heapq.heappush(priority_queue, (0, *end_position, direction))

    while priority_queue:
        current_cost, row, col, direction = heapq.heappop(priority_queue)
        if (row, col, direction) not in backward_distance_map:
            backward_distance_map[(row, col, direction)] = current_cost
        if (row, col, direction) in visited_states:
            continue
        visited_states.add((row, col, direction))

        # Move backward
        row_delta, col_delta = movement_directions[(direction + 2) % 4]
        next_row, next_col = row + row_delta, col + col_delta
        if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]) and grid[next_row][next_col] != '#':
            heapq.heappush(priority_queue, (current_cost + 1, next_row, next_col, direction))

        # Rotate left and right
        heapq.heappush(priority_queue, (current_cost + 1000, row, col, (direction + 1) % 4))
        heapq.heappush(priority_queue, (current_cost + 1000, row, col, (direction + 3) % 4))

    # Identify all tiles that are part of any optimal path
    optimal_tiles = set()
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            for direction in range(4):
                if (row, col, direction) in forward_distance_map and (row, col, direction) in backward_distance_map:
                    total_cost = forward_distance_map[(row, col, direction)] + backward_distance_map[(row, col, direction)]
                    if total_cost == best_score:
                        optimal_tiles.add((row, col))

    optimal_tiles_count = len(optimal_tiles)
    execution_time_part2 = time.time() - start_time_part2

    print(f"Part 2: Number of optimal tiles is {optimal_tiles_count}")
    print(f"Part 2 execution time: {execution_time_part2:.5f} seconds")

