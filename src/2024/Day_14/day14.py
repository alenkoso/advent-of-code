import os,sys
from collections import defaultdict,deque

project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(project_root)

from helpers.parsing_utils import read_input_file_strip_lines

def parse_robots(lines):
    robots = []
    for line in lines:
        position, velocity = line.split()
        robot_x, robot_y = map(int, position.replace('p=','').split(','))
        velocity_x, velocity_y = map(int, velocity.replace('v=','').split(','))
        robots.append([robot_x, robot_y, velocity_x, velocity_y])
    return robots

def simulate_step(robots, grid_width, grid_height):
    for robot in robots:
        robot[0] = (robot[0] + robot[2]) % grid_width
        robot[1] = (robot[1] + robot[3]) % grid_height

def calculate_safety_factor(robots, grid_width, grid_height):
    middle_x, middle_y = grid_width//2, grid_height//2
    robot_positions = defaultdict(int)
    quadrant_counts = [0]*4

    for robot in robots:
        robot_positions[(robot[0], robot[1])] += 1

    for (position_x, position_y), robot_count in robot_positions.items():
        if position_x != middle_x and position_y != middle_y:
            quadrant_index = (1 if position_x > middle_x else 0) + (2 if position_y > middle_y else 0)
            quadrant_counts[quadrant_index] += robot_count

    return quadrant_counts[0] * quadrant_counts[1] * quadrant_counts[2] * quadrant_counts[3]

def count_components(robots, grid_width, grid_height):
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    visited_positions = set()
    component_count = 0
    occupied_positions = defaultdict(bool)
    
    for robot in robots:
        occupied_positions[(robot[0], robot[1])] = True
    
    for x_coord in range(grid_width):
        for y_coord in range(grid_height):
            if occupied_positions[(x_coord, y_coord)] and (x_coord, y_coord) not in visited_positions:
                component_count += 1
                position_queue = deque([(x_coord, y_coord)])
                
                while position_queue:
                    current_x, current_y = position_queue.popleft()
                    if (current_x, current_y) in visited_positions:
                        continue
                    
                    visited_positions.add((current_x, current_y))
                    
                    for delta_x, delta_y in directions:
                        next_x = (current_x + delta_x) % grid_width
                        next_y = (current_y + delta_y) % grid_height
                        if occupied_positions[(next_x, next_y)] and (next_x, next_y) not in visited_positions:
                            position_queue.append((next_x, next_y))
    
    return component_count

def part1(robots, grid_width, grid_height):
    for _ in range(100):
        simulate_step(robots, grid_width, grid_height)
    return calculate_safety_factor(robots, grid_width, grid_height)

def part2(robots, grid_width, grid_height, start_time=100):
    current_time = start_time
    while True:
        current_time += 1
        simulate_step(robots, grid_width, grid_height)
        if count_components(robots, grid_width, grid_height) <= 200:
            return current_time

def main():
    grid_width, grid_height = 101, 103
    input_lines = read_input_file_strip_lines("input.txt")
    robots = parse_robots(input_lines)
    
    part_1 = part1(robots.copy(), grid_width, grid_height)
    print("Part 1: ", part_1)
    
    part_2 = part2(robots, grid_width, grid_height)
    print("Part 2: ", part_2)

if __name__ == "__main__":
    main()