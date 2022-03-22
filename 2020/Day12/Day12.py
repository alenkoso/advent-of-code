angle_direction_map = {
    0: 'N',
    90: 'E',
    180: 'S',
    270: 'W',
}


def rotate(angle, ins):
    amount = int(ins[1:])
    if ins[0] == 'L':
        amount = -1 * amount
    return (angle + amount) % 360


def move(pos, facing, ins):
    # Note: Part one uses screen coordinates
    # N is -y and S is +y
    x, y = pos
    amount = int(ins[1:])
    direction = ins[0]
    if direction == 'F':
        direction = angle_direction_map[facing]
    elif direction == 'R':
        facing = (facing + 180) % 360
        direction = angle_direction_map[facing]
    if direction == 'N':
        y -= amount
    elif direction == 'E':
        x += amount
    elif direction == 'S':
        y += amount
    elif direction == 'W':
        x -= amount

    return x, y


with open("../Inputs/InputDay12.txt") as input:
    raw = input.read()

# pofiltrira prazne vrstice
directions = [line for line in raw.split('\n') if line.strip()]

x = 0
y = 0
angle = 90

for d in directions:
    if d[0] in ["N", "S", "F", "W", "E"]:
        x, y = move((x, y), angle, d)
    else:
        angle = rotate(angle, d)
# print(d, x, y, angle)
# Manhattan distance
print("Part one: ", abs(x) + abs(y))
