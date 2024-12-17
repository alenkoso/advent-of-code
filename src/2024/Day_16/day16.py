import time
import heapq
import sys
import os

project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(project_root)

from helpers.parsing_utils import read_input_file_to_grid

def find_start_end(maze):
    start_pos, end_pos = None, None
    for row_idx in range(len(maze)):
        for col_idx in range(len(maze[0])):
            if maze[row_idx][col_idx] == "S":
                start_pos = (row_idx, col_idx)
            elif maze[row_idx][col_idx] == "E":
                end_pos = (row_idx, col_idx)
    return start_pos, end_pos

def find_best_path(maze, starting_point, target_point):
    possible_moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    maze_height, maze_width = len(maze), len(maze[0])
    priority_queue = [(0, starting_point[0], starting_point[1], 1)]
    seen_states = set()
    lowest_score = None
    path_distances = {}
    
    while priority_queue:
        distance, current_row, current_col, facing = heapq.heappop(priority_queue)
        
        if (current_row, current_col, facing) in seen_states:
            continue
            
        seen_states.add((current_row, current_col, facing))
        path_distances[(current_row, current_col, facing)] = distance
        
        if (current_row, current_col) == target_point and lowest_score is None:
            lowest_score = distance
            break

        move_row, move_col = possible_moves[facing]
        next_row = current_row + move_row
        next_col = current_col + move_col
        
        if 0 <= next_row < maze_height and 0 <= next_col < maze_width and maze[next_row][next_col] != "#":
            heapq.heappush(priority_queue, (distance + 1, next_row, next_col, facing))
        
        turn_right = (facing + 1) % 4
        turn_left = (facing - 1) % 4
        heapq.heappush(priority_queue, (distance + 1000, current_row, current_col, turn_right))
        heapq.heappush(priority_queue, (distance + 1000, current_row, current_col, turn_left))
    
    return lowest_score, path_distances

def find_optimal_tiles(maze, target_point, best_path_score, forward_path_costs):
    possible_moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    maze_height, maze_width = len(maze), len(maze[0])
    priority_queue = [(0, target_point[0], target_point[1], direction) for direction in range(4)]
    seen_states = set()
    backward_path_costs = {}
    tiles_on_best_path = set()
    
    while priority_queue:
        distance, current_row, current_col, facing = heapq.heappop(priority_queue)
        
        if (current_row, current_col, facing) in seen_states:
            continue
            
        seen_states.add((current_row, current_col, facing))
        backward_path_costs[(current_row, current_col, facing)] = distance
        
        reverse_facing = (facing + 2) % 4
        move_row, move_col = possible_moves[reverse_facing]
        next_row = current_row + move_row
        next_col = current_col + move_col
        
        if 0 <= next_row < maze_height and 0 <= next_col < maze_width and maze[next_row][next_col] != "#":
            heapq.heappush(priority_queue, (distance + 1, next_row, next_col, facing))
            
        turn_right = (facing + 1) % 4
        turn_left = (facing - 1) % 4
        heapq.heappush(priority_queue, (distance + 1000, current_row, current_col, turn_right))
        heapq.heappush(priority_queue, (distance + 1000, current_row, current_col, turn_left))

    for row in range(maze_height):
        for col in range(maze_width):
            if maze[row][col] == "#":
                continue
            for facing in range(4):
                current_state = (row, col, facing)
                if current_state in forward_path_costs and current_state in backward_path_costs:
                    total_distance = forward_path_costs[current_state] + backward_path_costs[current_state]
                    if total_distance == best_path_score:
                        tiles_on_best_path.add((row, col))
                        break

    return len(tiles_on_best_path)

def main():
    maze = read_input_file_to_grid("input.txt")
    starting_point, target_point = find_start_end(maze)
    
    start_time = time.time()
    best_score, forward_path_costs = find_best_path(maze, starting_point, target_point)
    end_time = time.time()
    print("Part 1: ", best_score)
    print(f"Part 1 Execution Time: {end_time - start_time} seconds")
    
    start_time = time.time()
    optimal_tile_count = find_optimal_tiles(maze, target_point, best_score, forward_path_costs)
    end_time = time.time()
    print("Part 2: ", optimal_tile_count)
    print(f"Part 2 Execution Time: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()