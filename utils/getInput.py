#!/usr/bin/env python3

import os
import requests
from datetime import datetime
from sys import argv

BASE_DIR = os.path.dirname(__file__)
URL = "https://adventofcode.com/{year}/day/{day}/input"


def print_usage():
    print("Usage:", argv[0], "[[YEAR] DAY]")
    exit(1)


def arg_to_int(i, name):
    try:
        return int(argv[i])
    except ValueError:
        print("Error:", name, "is not a number")
        print_usage()


def get_single_input(input_year, input_day):
    dir_name = os.path.join(BASE_DIR, "aoc", str(input_year), f"Day{input_day:02}")
    cookies = {}

    try:
        with open(os.path.join(BASE_DIR, "cookie")) as f:
            cookies["session"] = f.read().strip()
    except FileNotFoundError:
        print("No cookie file found.")
        print("Please paste the value of the 'session' cookie on the AoC website into a file named 'cookie'.")
        exit(2)

    os.makedirs(dir_name, exist_ok=True)
    target_file = os.path.join(dir_name, "input.txt")

    url = URL.format(year=input_year, day=input_day)
    req = requests.get(url, cookies=cookies)

    if req.status_code != 200:
        print("Error. Got status:", req.status_code)
        print(req.text)
        exit(3)
    else:
        with open(target_file, "w") as f:
            f.write(req.text)
        print("Input for", dir_name, "written to", target_file)


def get_all_inputs(input_year):
    for inputDay in range(1, 26):
        dir_name = os.path.join(BASE_DIR, "aoc", str(input_year), f"Day{inputDay:02}")
        cookies = {}

        try:
            with open(os.path.join(BASE_DIR, "cookie")) as f:
                cookies["session"] = f.read().strip()
        except FileNotFoundError:
            print("No cookie file found.")
            print("Please paste the value of the 'session' cookie on the AoC website into a file named 'cookie'.")
            exit(2)

        os.makedirs(dir_name, exist_ok=True)
        target_file = os.path.join(dir_name, "input.txt")

        url = URL.format(year=input_year, day=inputDay)
        req = requests.get(url, cookies=cookies)

        if req.status_code != 200:
            print("Error. Got status:", req.status_code)
            print(req.text)
            exit(3)
        else:
            with open(target_file, "w") as f:
                f.write(req.text)
            print("Input for", dir_name, "written to", target_file)


if len(argv) == 1:
    now = datetime.now()
    if now.month != 12 or now.day > 25:
        print("Failed to deduce day: There is no new AoC puzzle today.")
        print_usage()
    year = now.year
    day = now.day
    get_single_input(year, day)
elif "-h" in argv[1:] or "--help" in argv[1:]:
    print_usage()
elif len(argv) == 2:
    year = arg_to_int(1, "YEAR")
    get_all_inputs(year)
elif len(argv) == 3:
    year = arg_to_int(1, "YEAR")
    day = arg_to_int(2, "DAY")
    get_single_input(year, day)
else:
    print_usage()
