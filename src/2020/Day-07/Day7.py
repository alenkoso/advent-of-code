from collections import defaultdict, deque
import re

with open("../../../curr/2020/Inputs/InputDay7.txt") as file:
    lines = [x.strip() for x in file.readlines()]


class Child:
    def __init__(self, colour, count):
        self.colour = colour
        self.count = count


contained_in = defaultdict(list)
contains = defaultdict(list)

for line in lines:
    children = re.findall(r"(\d) (\w+ \w+)", line)
    parent = " ".join(line.split()[:2])
    for count, color in children:
        contained_in[color].append(parent)
        contains[parent].append(Child(color, int(count)))


# BFS - Breadth - First Search
def part_one(colour):
    contains_colour = set()
    dequeued_colour = deque([colour])
    while dequeued_colour:
        i = dequeued_colour.popleft()
        for j in contained_in[i]:
            if j not in contains_colour:
                contains_colour.add(j)
                dequeued_colour.append(j)
    return len(contains_colour) #lahko daš samo contains_colour pa potem v printu kličeš len(contains_colour)


# Recursion
def part_two(colour):
    counter = 0
    for child in contains[colour]:
        counter += child.count * (1 + part_two(child.colour))
    return counter



print("Part one: ", part_one("shiny gold"))
print("Part two: ", part_two("shiny gold"))
