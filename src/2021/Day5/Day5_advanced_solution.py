from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Tuple, NamedTuple

FILE_DIR = Path(__file__).parent


class Coord(NamedTuple):
    x: int
    y: int


def parse_input(lines: str) -> List[Tuple[Coord, Coord]]:
    dual_coordinates = [line.split(" -> ") for line in lines.split("\n")]
    return [
        (
            Coord(int(first.split(",")[0]), int(first.split(",")[1])),
            Coord(int(second.split(",")[0]), int(second.split(",")[1])),
        )
        for first, second in dual_coordinates
    ]


def solve(coord_pairs: List[Tuple[Coord, Coord]]) -> Tuple[int, int]:
    visited_locations: Dict[Tuple[int, int], int] = defaultdict(int)
    diagonals: List[Tuple[Coord, Coord]] = []
    for first, second in coord_pairs:
        if first.x == second.x:
            points_on_line = ((first.x, y) for y in range(min(first.y, second.y), max(first.y, second.y) + 1))
        elif first.y == second.y:
            points_on_line = ((x, first.y) for x in range(min(first.x, second.x), max(first.x, second.x) + 1))
        else:
            diagonals.append((first, second))
            continue
        for point in points_on_line:
            visited_locations[point] += 1
    part1 = sum(v > 1 for v in visited_locations.values())

    for first, second in diagonals:
        x_down = 1 if first.x < second.x else -1
        y_down = 1 if first.y < second.y else -1
        for point in zip(range(first.x, second.x + x_down, x_down), range(first.y, second.y + y_down, y_down)):
            visited_locations[point] += 1
    return part1, sum(v > 1 for v in visited_locations.values())


if __name__ == "__main__":
    DATA = (FILE_DIR / "day5.input").read_text().strip()

    VENT_LINES = parse_input(DATA)

    print(solve(VENT_LINES))