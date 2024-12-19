def parse_input(file_path):
    with open(file_path, 'r') as f:
        raw_data = f.read()
    patterns, designs = raw_data.strip().split("\n\n")
    patterns = patterns.split(", ")
    designs = designs.split("\n")
    return patterns, designs

def is_design_possible(patterns, design):
    dp = [False] * (len(design) + 1)
    dp[0] = True

    for i in range(1, len(design) + 1):
        for pattern in patterns:
            if i >= len(pattern) and design[i - len(pattern):i] == pattern:
                dp[i] = dp[i] or dp[i - len(pattern)]
                if dp[i]:
                    break
    return dp[-1]

def part1(patterns, designs):
    return sum(is_design_possible(patterns, design) for design in designs)

def count(patterns, design):
    dp = [0] * (len(design) + 1)
    dp[0] = 1

    for i in range(1, len(design) + 1):
        for pattern in patterns:
            if i >= len(pattern) and design[i - len(pattern):i] == pattern:
                dp[i] += dp[i - len(pattern)]
    return dp[-1]

def part2(patterns, designs):
    return sum(count(patterns, design) for design in designs)

def main():
    patterns, designs = parse_input("input.txt")
    part_1 = part1(patterns, designs)
    print("Part 1: ", part_1)
    
    part_2 = part2(patterns, designs)
    print("Part 2: ", part_2)

if __name__ == "__main__":
    main()
