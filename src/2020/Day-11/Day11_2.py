import copy


def count_adjacent_occupied(seats, row, col):
    directions = ['N', 'E', 'S', 'W', 'NE', 'NW', 'SE', 'SW']

    count = 0
    for d in directions:
        if get_first_seen(seats, row, col, d):
            count += 1

    return count


def get_first_seen(seats, row, col, direction):
    diff_r = 0
    diff_c = 0
    if 'N' in direction:
        diff_r = -1
    if 'S' in direction:
        diff_r = 1
    if 'W' in direction:
        diff_c = -1
    if 'E' in direction:
        diff_c = 1

    row += diff_r
    col += diff_c
    while row >= 0 and row < len(seats) and col >= 0 and col < len(seats[0]):
        if seats[row][col] == '#':
            return True
        elif seats[row][col] == 'L':
            return False
        else:
            row += diff_r
            col += diff_c
    return False


def seats_next(seats):
    new_seats = copy.deepcopy(seats)
    for r in range(len(seats)):
        for c in range(len(seats[0])):
            if seats[r][c] == 'L':
                if count_adjacent_occupied(seats, r, c) == 0:
                    new_seats[r][c] = '#'
            elif seats[r][c] == '#':
                if count_adjacent_occupied(seats, r, c) >= 5:
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

seats = [list(line) for line in raw.split('\n') if line.strip()]

prev_seats = seats
next_seats = seats_next(seats)
while not seats_equal(prev_seats, next_seats):
    prev_seats = next_seats
    next_seats = seats_next(prev_seats)
count = count_occupied(next_seats)
print(count)
