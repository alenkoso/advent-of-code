def parse_input(file_path):
    with open(file_path) as file:
        return [list(line.strip()) for line in file]

def part1(grid, word):
    rows, cols = len(grid), len(grid[0])
    word_length = len(word)
    count = 0
    directions = [
        (0, 1), (1, 0), (1, 1), (1, -1), (0, -1), (-1, 0), (-1, -1), (-1, 1)
    ]
    for row in range(rows):
        for col in range(cols):
            for dr, dc in directions:
                if all(0 <= row + dr * i < rows and 0 <= col + dc * i < cols and grid[row + dr * i][col + dc * i] == word[i] for i in range(word_length)):
                    count += 1
    return count

def part2(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            if grid[row][col] != 'A':
                continue

            if ((grid[row - 1][col - 1] == 'M' and grid[row + 1][col + 1] == 'S') or
                (grid[row - 1][col - 1] == 'S' and grid[row + 1][col + 1] == 'M')) and \
               ((grid[row - 1][col + 1] == 'M' and grid[row + 1][col - 1] == 'S') or
                (grid[row - 1][col + 1] == 'S' and grid[row + 1][col - 1] == 'M')):
                count += 1

    return count


def main():
    grid = parse_input("input.txt")
    
    part_1 = part1(grid, "XMAS")
    print(part_1)
    
    part_2 = part2(grid)
    print(part_2)

if __name__ == "__main__":
    main()
