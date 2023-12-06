import os
import sys

project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(project_root)
from helpers.file_utils import read_input_file

# Part 1
def calculate_winning_ways(race_times, record_distances):
    winning_ways = []
    for race_time, record_distance in zip(race_times, record_distances):
        ways_to_win = 0
        for hold_time in range(race_time):
            speed = hold_time
            travel_time = race_time - hold_time
            distance = speed * travel_time
            if distance > record_distance:
                ways_to_win += 1
        winning_ways.append(ways_to_win)
    return winning_ways

def parse_input(input_data):
    race_times = list(map(int, input_data[0].split()[1:]))
    record_distances = list(map(int, input_data[1].split()[1:]))
    return race_times, record_distances

# Part 2
def calculate_winning_ways_single_race(race_time, record_distance):
    optimal_hold_time = race_time // 2
    ways_to_win = 0

    # Start from the optimal hold time and decrease
    for hold_time in range(optimal_hold_time, -1, -1):
        distance = hold_time * (race_time - hold_time)
        if distance > record_distance:
            ways_to_win = race_time - hold_time
            break

    return ways_to_win

def parse_single_race_input(input_data):
    race_time = int(input_data[0].replace("Time:", "").replace(" ", ""))
    record_distance = int(input_data[1].replace("Distance:", "").replace(" ", ""))
    return race_time, record_distance

def main():
    # Part 1
    input_data_multiple = [
        "Time:      7  15   30",
        "Distance:  9  40  200"
    ]
    race_times, record_distances = parse_input(input_data_multiple)
    total_ways_multiple = 1
    for ways in calculate_winning_ways(race_times, record_distances):
        total_ways_multiple *= ways
    print(f"Total ways to win all races: {total_ways_multiple}")

    # Part 2
    input_data_single = [
        "Time:      71530",
        "Distance:  940200"
    ]
    race_time, record_distance = parse_single_race_input(input_data_single)
    total_ways_single = calculate_winning_ways_single_race(race_time, record_distance)
    print(f"Total ways to win the single race: {total_ways_single}")

if __name__ == "__main__":
    main()

