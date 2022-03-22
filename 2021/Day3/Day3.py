from collections import Counter
from pathlib import Path
from typing import List, Tuple

FILE_DIR = Path(__file__).parent


def part1(lines: List[str]) -> Tuple[str, str]:
    counters = [Counter(line[i] for line in lines) for i in range(len(lines[0]))]

    most = "".join(count.most_common()[0][0] for count in counters)
    least = "".join(count.most_common()[-1][0] for count in counters)
    return most, least


def part2(lines: List[str]) -> Tuple[str, str]:
    oxygen_values_pool = lines
    co2_values_pool = lines
    for i in range(len(lines[0])):
        if len(oxygen_values_pool) > 1:
            oxygen_most_common = Counter(l[i] for l in oxygen_values_pool).most_common()
            oxygen_digit = "1" if oxygen_most_common[0][1] == oxygen_most_common[1][1] else oxygen_most_common[0][0]
            oxygen_values_pool = [l for l in oxygen_values_pool if l[i] == oxygen_digit]
        if len(co2_values_pool) > 1:
            co2_most_common = Counter(l[i] for l in co2_values_pool).most_common()
            co2_digit = "0" if co2_most_common[0][1] == co2_most_common[1][1] else co2_most_common[-1][0]
            co2_values_pool = [l for l in co2_values_pool if l[i] == co2_digit]
    return oxygen_values_pool[0], co2_values_pool[0]


if __name__ == "__main__":
    DATA = (FILE_DIR / "day3.input").read_text().strip()
    INPUT = [i for i in DATA.split("\n")]

    MOST_COMMON, LEAST_COMMON = part1(INPUT)

    print(int(MOST_COMMON, base=2) * int(LEAST_COMMON, base=2))

    OXY_RATING, CO2_RATING = part2(INPUT)
    print(int(OXY_RATING, base=2) * int(CO2_RATING, base=2))