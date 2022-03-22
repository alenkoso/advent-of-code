import re
import copy
from collections import defaultdict

step = {
    0: 5,
    13: 4,
    1: 3,
    16: 2,
    6: 1,
}

next_step = {
    0: 5,
    13: 4,
    1: 3,
    16: 2,
    6: 1,
    17: 0
}

myInput = [0, 13, 1, 16, 6, 17]
current_position_index = len(myInput)

last_added = None
while len(myInput) < 30000000:
    number = myInput[-1]
    if number not in step:
        next_step[number] = 0
        add = 0
    else:
        add = step[number]
        next_step[number] = 0

    myInput.append(add)
    for i in next_step:
        next_step[i] += 1
    step = copy.deepcopy(next_step)

print("The 30000000th number spoken will be: ", myInput[-1])

# TODO optimize this piece of junk.
