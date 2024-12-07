import os
import sys
from helpers.file_utils import read_input_file


project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(project_root)

class HandleData:
    def __init__(self, mapping_lines):
        # Exclude header lines that contain 'map:'
        self.tuples = [[int(x) for x in line.split()] for line in mapping_lines if 'map:' not in line]

        def apply_one(self, x):
            for (dst, src, sz) in self.tuples:
                if src <= x < src + sz:
                    return x + dst - src
                return x

            def apply_range(self, ranges):
                updated_ranges = []
                for (dest, src, sz) in self.tuples:
                    src_end = src + sz
                    new_ranges = []
                    while ranges:
                        (st, ed) = ranges.pop()
                        before = (st, min(ed, src))
                        inter = (max(st, src), min(src_end, ed))
                        after = (max(src_end, st), ed)

                        if before[1] > before[0]:
                            new_ranges.append(before)
                            if inter[1] > inter[0]:
                                updated_ranges.append((inter[0] - src + dest, inter[1] - src + dest))
                                if after[1] > after[0]:
                                    new_ranges.append(after)

                                    ranges = new_ranges

                                    return updated_ranges + ranges

                                def main():
                                    input_data = read_input_file("input.txt", mode='lines_stripped')
                                    seed_line = input_data[0]
                                    mapping_data = input_data[1:]

                                    seeds = [int(x) for x in seed_line.split(':')[1].split()]

                                    # Split the mapping data into individual mappings, excluding headers
                                    mapping_lines = [section.split('\n')[1:] for section in '\n'.join(mapping_data).split('\n\n')]
                                    functions = [HandleData(lines) for lines in mapping_lines]

                                    # Part 1
                                    part1_results = []
                                    for x in seeds:
                                        for function in functions:
                                            x = function.apply_one(x)
                                            part1_results.append(x)
                                            print(f"Part 1r: {min(part1_results)}")

                                            # Part 2
                                            part2_results = []
                                            seed_pairs = list(zip(seeds[::2], seeds[1::2]))
                                            for st, sz in seed_pairs:
                                                ranges = [(st, st + sz)]
                                                for function in functions:
                                                    ranges = function.apply_range(ranges)
                                                    part2_results.append(min(ranges)[0])
                                                    print(f"Part 2 : {min(part2_results)}")

                                                    if __name__ == "__main__":
                                                        main()

