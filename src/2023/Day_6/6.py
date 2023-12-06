import os
import sys
import time

project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(project_root)
from helpers.file_utils import read_input_file

def calculate_ways_to_win(race_time, record_distance):
    ways_to_win = 0
    for hold_time in range(race_time + 1):
        distance_travelled = hold_time * (race_time - hold_time)
        if distance_travelled >= record_distance:
            ways_to_win += 1
    return ways_to_win

def parse_input(input_data):
    race_times = [int(x) for x in input_data[0].split(':')[1].split()]
    record_distances = [int(x) for x in input_data[1].split(':')[1].split()]
    combined_race_time = int(''.join(map(str, race_times)))
    combined_record_distance = int(''.join(map(str, record_distances)))
    return race_times, record_distances, combined_race_time, combined_record_distance

def main():
    input_data = read_input_file('input.txt', mode='lines_stripped')

    race_times, record_distances, combined_race_time, combined_record_distance = parse_input(input_data)

    # Part 1
    start_time = time.time()
    total_ways_multiple = 1
    for each_race_time, each_record_distance in zip(race_times, record_distances):
        total_ways_multiple *= calculate_ways_to_win(each_race_time, each_record_distance)
    end_time = time.time()
    print(f"Part 1: {total_ways_multiple}")
    print(f"Part 1 Execution Time: {end_time - start_time} seconds")

    # Part 2
    start_time = time.time()
    total_ways_single = calculate_ways_to_win(combined_race_time, combined_record_distance)
    end_time = time.time()
    print(f"Part 2: {total_ways_single}")
    print(f"Part 2 Execution Time: {end_time - start_time} seconds")

if __name__ == '__main__':
    main()
