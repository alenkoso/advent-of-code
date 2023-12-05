import os
import sys

project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(project_root)
from helpers.file_utils import read_input_file

class DataMapper:
    def __init__(self, mapping_lines):
        # Parsing each mapping line into tuples and excluding header lines
        self.mapping_rules = [[int(x) for x in line.split()] for line in mapping_lines if 'map:' not in line]

    def map_single_number(self, number):
        # Apply mapping rules to a single number
        for (destination_start, source_start, range_size) in self.mapping_rules:
            if source_start <= number < source_start + range_size:
                return number + destination_start - source_start
        return number

    def map_number_range(self, number_ranges):
        # Apply mapping rules to a range of numbers
        updated_ranges = []
        for (destination_start, source_start, range_size) in self.mapping_rules:
            source_end = source_start + range_size
            temp_ranges = []
            while number_ranges:
                (range_start, range_end) = number_ranges.pop()
                # Splitting the range into before, intersecting, and after parts
                before_range = (range_start, min(range_end, source_start))
                intersecting_range = (max(range_start, source_start), min(source_end, range_end))
                after_range = (max(source_end, range_start), range_end)

                # Process each part separately
                if before_range[1] > before_range[0]:
                    temp_ranges.append(before_range)
                if intersecting_range[1] > intersecting_range[0]:
                    updated_ranges.append((intersecting_range[0] - source_start + destination_start, intersecting_range[1] - source_start + destination_start))
                if after_range[1] > after_range[0]:
                    temp_ranges.append(after_range)

            number_ranges = temp_ranges

        return updated_ranges + number_ranges

def main():
    # Reading input data using the helper function
    input_data = read_input_file("input.txt", mode='lines_stripped')
    seeds_line = input_data[0]
    mapping_sections = input_data[1:]

    # Extracting seed numbers from the seed line
    seeds = [int(x) for x in seeds_line.split(':')[1].split()]

    # Processing the mapping data into individual sections
    mapping_sections = [section.split('\n')[1:] for section in '\n'.join(mapping_sections).split('\n\n')]
    mappers = [DataMapper(section) for section in mapping_sections]

    # Part 1: Mapping individual seed numbers
    part1_min_number = min(mapper.map_single_number(seed) for seed in seeds for mapper in mappers)
    print(f"Part 1: {part1_min_number}")

    # Part 2: Processing seed ranges
    part2_min_number = float('inf')
    seed_pairs = list(zip(seeds[::2], seeds[1::2]))
    for start, size in seed_pairs:
        ranges = [(start, start + size)]
        for mapper in mappers:
            ranges = mapper.map_number_range(ranges)
        part2_min_number = min(part2_min_number, min(range_start for range_start, _ in ranges))

    print(f"Part 2: {part2_min_number}")

if __name__ == "__main__":
    main()
