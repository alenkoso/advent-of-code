import json
import re


def sum_numbers(s):
    return sum(int(i) for i in re.findall(r"(-?\d+)", str(s)))


def sum_ignore_red(s):
    if isinstance(s, int):
        return s
    elif isinstance(s, list):
        return sum(sum_ignore_red(i) for i in s)
    elif isinstance(s, dict):
        if "red" in s.values():
            return 0
        else:
            return sum(sum_ignore_red(i) for i in s.values())

    return 0


def part_one():
    with open("input.txt") as input_file:
        print(sum_numbers(input_file.read()))


def part_two():
    with open("input.txt") as fin:
        print(sum_ignore_red(json.load(fin)))


if __name__ == "__main__":
    part_one()
    part_two()
