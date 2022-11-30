from itertools import groupby
import time

def elf_game(number, count=1):
    for _ in range(count):
        number = "".join(str(len(list(generated))) + str(previous) for previous, generated in groupby(number))
    return number

def part_one():
    with open("input.txt") as input:
        number = input.readline().strip()
        print("Starting with the digits in your puzzle input, apply this process 40 times.")
        print("What is the length of the result? ", len(elf_game(number, 40)))


def part_two():
    with open("input.txt") as input:
        number = input.readline().strip()
        print("Now, starting again with the digits in your puzzle input, apply this process 50 times.")
        print("What is the length of the new result? ", len(elf_game(number, 50)))


code_run_time = time.time()
print("=============================== PART ONE ===============================")
part_one()
print("=============================== PART TWO ===============================")
part_two()
print("Code run time: ", (time.time() - code_run_time) * 1000, "ms")