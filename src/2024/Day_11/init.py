from collections import defaultdict

def transform_stone(stone):
    if stone == 0:
        return [1]
    stone_str = str(stone)
    if len(stone_str) % 2 == 0:
        mid = len(stone_str) // 2
        return [int(stone_str[:mid]), int(stone_str[mid:])]
    return [2024 * stone]

def simulate_blinks(stone_counts, blinks):
    for _ in range(blinks):
        new_counts = defaultdict(int)
        for stone, count in stone_counts.items():
            for new_stone in transform_stone(stone):
                new_counts[new_stone] += count
        stone_counts = new_counts
    return sum(stone_counts.values())

def main():
    initial_stones = [4022724, 951333, 0, 21633, 5857, 97, 702, 6]
    stone_counts = defaultdict(int)
    for stone in initial_stones:
        stone_counts[stone] += 1

    print(f"Part 1: {simulate_blinks(stone_counts, 25)}")
    print(f"Part 2: {simulate_blinks(stone_counts, 75)}")

if __name__ == "__main__":
    main()
