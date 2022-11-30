import time


class Cup:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

    def __repr__(self):
        return "Cup " + str(self.val)


map_number_of_cups = {}


def pick_up(current):
    first = current.next
    last = first.next.next

    current.next = last.next
    last.next.prev = first

    first.prev = None
    last.next = None

    contents = []
    current = first
    while current != None:
        contents.append(current.val)
        current = current.next

    return first, contents


def insert_after(dest, lst):
    d = map_number_of_cups[dest]
    last = lst.next.next

    lst.prev = d
    last.next = d.next
    d.next.prev = last
    d.next = lst


# # with open("InputDay23_Example.txt") as input_file:
# with open("InputDay23.txt") as input_file:
#     raw = input_file.read()

# input_raw = [line for line in raw.split('\n') if line.strip()]

# example_input = "389125467"

my_input = "158937462"

num = int(my_input[0])
first_object = Cup(num)
map_number_of_cups[num] = first_object
previous_object = first_object
for n in my_input[1:]:
    num = int(n)
    number_of_objects = Cup(num)
    number_of_objects.prev = previous_object
    previous_object.next = number_of_objects
    map_number_of_cups[num] = number_of_objects
    previous_object = number_of_objects

for num in range(10, 1000001):
    number_of_objects = Cup(num)
    number_of_objects.prev = previous_object
    previous_object.next = number_of_objects
    map_number_of_cups[num] = number_of_objects
    previous_object = number_of_objects

previous_object.next = first_object
first_object.prev = previous_object

start_time = time.time()
print("Sanity Check: # Cups", len(map_number_of_cups))

max_cup = 1000000
min_cup = 1
number_of_cups = 1000000

current_cup = first_object
for i in range(10000000):
    if (i + 1) % 1000000 == 0:
        print("Iteration", i + 1)
    last, picked_up = pick_up(current_cup)
    # select destination
    destination = current_cup.val - 1
    if destination < min_cup:
        destination = max_cup
    while destination in picked_up:
        destination -= 1
        if destination < min_cup:
            destination = max_cup

    insert_after(destination, last)

    current_cup = current_cup.next

cup_1 = map_number_of_cups[1]

part_two = cup_1.next.val * cup_1.next.next.val

print("Determine which two cups will end up immediately clockwise of cup 1.")
print("What do you get if you multiply their labels together? ", part_two)
print()
print(f"Code run time: {time.time() - start_time} sec")
