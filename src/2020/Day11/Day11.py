import copy

def count_adjacent_occupied(seats, row, col):
    rows = [row - 1, row, row + 1]
    cols = [col - 1, col, col + 1]

    rows = [r for r in rows if 0 <= r < len(seats)]
    cols = [c for c in cols if 0 <= c < len(seats[0])]
    count = 0
    for r in rows:
        for c in cols:
            if r == row and c == col:
                continue
            if seats[r][c] == '#':
                count += 1

    return count


def find_next_seats(seats):
    new_seats = copy.deepcopy(seats)
    for r in range(len(seats)):
        for c in range(len(seats[0])):
            if seats[r][c] == 'L':
                if count_adjacent_occupied(seats, r, c) == 0:
                    new_seats[r][c] = '#'
            elif seats[r][c] == '#':
                if count_adjacent_occupied(seats, r, c) >= 4:
                    new_seats[r][c] = 'L'
    return new_seats


def count_occupied(seats):
    count = 0
    for r in seats:
        for c in r:
            if c == '#':
                count += 1
    return count


def seats_equal(seats1, seats2):
    for r in range(len(seats1)):
        for c in range(len(seats2)):
            if seats1[r][c] != seats2[r][c]:
                return False
    return True


with open("../Inputs/InputDay11.txt") as infile:
    raw = infile.read()
currentSeats = [list(line) for line in raw.split('\n') if line.strip()]

previousSeats = currentSeats
nextSeats = find_next_seats(currentSeats)
while not seats_equal(previousSeats, nextSeats):
    previousSeats = nextSeats
    nextSeats = find_next_seats(previousSeats)
count = count_occupied(nextSeats)
print("Part one: ", count)
