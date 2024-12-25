def part1(data):
    locks = []
    keys = []
    schematic = []
    
    for line in data:
        if line:
            schematic.append(line)
            if len(schematic) == 7:
                if schematic[0][0] == '#':
                    locks.append(schematic)
                else:
                    keys.append(schematic)
                schematic = []
    
    result = 0
    for lock in locks:
        for key in keys:
            valid = True
            for y in range(7):
                for x in range(5):
                    if lock[y][x] == '#' and key[y][x] == '#':
                        valid = False
                        break
                if not valid:
                    break
            result += valid
    
    return result

def main():
    data = [line.strip() for line in open("input.txt")]
    
    print("Part 1:", part1(data))

if __name__ == "__main__":
    main()