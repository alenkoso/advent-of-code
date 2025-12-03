def parse_input(file_path: str) -> list[str]:
    with open(file_path, 'r') as f:
        return [line.strip() for line in f if line.strip()]


def solve_part1(rotations: list[str]) -> int:
    position = 50
    zero_count = 0
    
    for rotation in rotations:
        direction = rotation[0]
        distance = int(rotation[1:])
        
        if direction == 'L':
            position = (position - distance) % 100
        else: # direction == 'R'
            position = (position + distance) % 100
        
        if position == 0:
            zero_count += 1
    
    return zero_count


def count_zero_crossings(position: int, direction: str, distance: int) -> int:
    """Count how many times we land on 0 during this rotation (including final position)."""
    # Find the first click number (1-indexed) that lands on 0
    if direction == 'L':
        first_hit = position if position > 0 else 100
    else: # direction == 'R'
        first_hit = (100 - position) % 100 or 100  # 0 becomes 100
    
    if first_hit > distance:
        return 0
    # Every 100 clicks after the first one, we hit 0 again
    return (distance - first_hit) // 100 + 1


def solve_part2(rotations: list[str]) -> int:
    position = 50
    zero_count = 0
    
    for rotation in rotations:
        direction = rotation[0]
        distance = int(rotation[1:])
        
        zero_count += count_zero_crossings(position, direction, distance)
        
        if direction == 'L':
            position = (position - distance) % 100
        else: # direction == 'R'
            position = (position + distance) % 100
    
    return zero_count


def main():
    rotations = parse_input('input.txt')
    
    print(f"Part 1: {solve_part1(rotations)}")
    print(f"Part 2: {solve_part2(rotations)}")


if __name__ == "__main__":
    main()