import math


def move(position, directionPoint, instruction):
    # Za drugi del naloge bom uporabil kartezijski koordinatni sistem
    #  'N' is +y and 'S' is -y
    x, y = position
    x_w, y_w = directionPoint
    amount = int(instruction[1:])
    direction = instruction[0]

    if direction == 'F':
        x += x_w * amount
        y += y_w * amount
    if direction == 'N':
        y_w += amount
    elif direction == 'E':
        x_w += amount
    elif direction == 'S':
        y_w -= amount
    elif direction == 'W':
        x_w -= amount

    return (x, y), (x_w, y_w)


def rotate(position, instruction):
    x, y = position
    amount = int(instruction[1:])
    if instruction[0] == 'R':
        amount = -1 * amount

    length = math.sqrt(x * x + y * y)
    angle = math.degrees(math.atan2(y, x))

    new_x = length * math.cos(math.radians(angle + amount))
    new_y = length * math.sin(math.radians(angle + amount))

    return round(new_x), round(new_y)


with open("../Inputs/InputDay12.txt") as input:
    raw = input.read()

# pofiltrira prazne vrstice
directions = [line for line in raw.split('\n') if line.strip()]

position = 0, 0

directionPoint = 10, 1

for direction in directions:
    if direction[0] in ["N", "S", "F", "W", "E"]:
        position, directionPoint = move(position, directionPoint, direction)
    else:
        directionPoint = rotate(directionPoint, direction)

x, y = position
# Manhattan distance part 2
print("Part two:", abs(x) + abs(y))
