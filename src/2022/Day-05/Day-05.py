#!/usr/bin/python3
from copy import deepcopy
import time

# DATA = open("test.txt").read()
DATA = open("input.txt").read()
lines = [x for x in DATA.split('\n')]


solution = []
for line in lines:
    if line != '':
        sz = (len(line)+1)//4
        while len(solution) < sz:
            solution.append([])
        for i in range(len(solution)):
            ch = line[1 + 4 * i]
            if 'A' <= ch <= 'Z' and ch != ' ':
                solution[i].append(ch)
        continue
    break

part_one = deepcopy(solution)
part_two = deepcopy(solution)
found = False
for command in lines:
    if command == '':
        found = True
        continue
    if not found:
        continue

    # Command: move 3 from 5 to 2
    words = command.split()
    quantity = int(words[1])
    from_ = int(words[3]) - 1
    to_ = int(words[5]) - 1
    for (ST, do_rev) in [(part_one, True), (part_two, False)]:
        MOVE = ST[from_][:quantity]
        ST[from_] = ST[from_][quantity:]
        ST[to_] = (list(reversed(MOVE)) if do_rev else MOVE) + ST[to_]


def main():
    print('Part 1: ' + ''.join([s[0] for s in part_one if len(s) > 0]))
    print('Part 2: ' + ''.join([s[0] for s in part_two if len(s) > 0]))


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
