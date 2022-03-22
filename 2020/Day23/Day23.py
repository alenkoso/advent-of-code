# # with open("InputDay23_Example.txt") as input_file:
# with open("InputDay23.txt") as input_file:
#     raw = input_file.read()

# input_raw = [line for line in raw.split('\n') if line.strip()]

# example_input = "389125467"
my_input = "158937462"

cups = [int(x) for x in my_input]

max_cup = max(cups)
min_cup = min(cups)
number_of_cups = len(cups)

current_index = 0
for i in range(100):
    print("cups: ", cups)
    current = cups[current_index]
    print("current: ", current)
    picked_up = []
    for i in range(3):
        next_cup = (current_index + i + 1) % number_of_cups
        # print(next_cup)
        picked_up.append(cups[next_cup])
    for c in picked_up:
        cups.remove(c)

    print("Pick up: ", picked_up)

    destination = current - 1
    if destination < min_cup:
        destination = max_cup
    while destination in picked_up:
        destination = destination - 1
        if destination < min_cup:
            destination = max_cup
    print("destination: ", destination)
    index = cups.index(destination)
    for cup in picked_up[::-1]:
        cups.insert(index + 1, cup)
    current_index = (cups.index(current) + 1) % number_of_cups

cup_1_i = cups.index(1)
print("Using your labeling, simulate 100 moves.")
print("What are the labels on the cups after cup 1? ", cups)
print()
print("What are the labels on the cups after cup 1? [in order for the answer] ")
for i in range(number_of_cups - 1):
    index = (cup_1_i + i + 1) % number_of_cups
    print(cups[index], end='')