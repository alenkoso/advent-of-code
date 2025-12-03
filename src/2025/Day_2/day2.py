def parse_input(file_path: str) -> list[tuple[int, int]]:
    with open(file_path, 'r') as f:
        content = f.read().strip()
    
    ranges = []
    for part in content.split(','):
        part = part.strip()
        if not part:
            continue
        start, end = part.split('-')
        ranges.append((int(start), int(end)))
    return ranges


def generate_doubles(max_val: int) -> list[int]:
    def parse_input(file_path: str) -> list[tuple[int, int]]:
        with open(file_path, 'r') as f:
            content = f.read().strip()
        
        ranges = []
        for part in content.split(','):
            part = part.strip()
            if not part:
                continue
            start, end = part.split('-')
            ranges.append((int(start), int(end)))
        return ranges


    def generate_doubles(max_val: int) -> list[int]:
        # Generate all numbers of form XX (sequence repeated twice).
        doubles = []
        base = 1
        while True:
            double = int(str(base) + str(base))
            if double > max_val:
                break
            doubles.append(double)
            base += 1
        return doubles


    def solve_part1(ranges: list[tuple[int, int]]) -> int:
        max_val = max(end for _, end in ranges)
        doubles = generate_doubles(max_val)
        
        total = 0
        for d in doubles:
            for start, end in ranges:
                if start <= d <= end:
                    total += d
                    break  # Don't double count if in multiple ranges
        
        return total


    def main():
        ranges = parse_input('input.txt')
        print(f"Part 1: {solve_part1(ranges)}")


    if __name__ == "__main__":
        main()
    doubles = []
    base = 1
    while True:
        double = int(str(base) + str(base))
        if double > max_val:
            break
        doubles.append(double)
        base += 1
    return doubles


def solve_part1(ranges: list[tuple[int, int]]) -> int:
    max_val = max(end for _, end in ranges)
    doubles = generate_doubles(max_val)
    
    total = 0
    for d in doubles:
        for start, end in ranges:
            if start <= d <= end:
                total += d
                break  # Don't double count if in multiple ranges
    
    return total


def main():
    ranges = parse_input('input.txt')
    print(f"Part 1: {solve_part1(ranges)}")


if __name__ == "__main__":
    main()