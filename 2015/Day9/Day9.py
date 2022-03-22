from collections import defaultdict

import itertools
import sys
import time

razdalje = defaultdict(lambda: defaultdict(int))

with open("input.txt") as input:
    for row in input:
        left, right = row.strip().split(" = ")
        first_coordinate, second_coordinate = left.split(" to ")
        razdalje[first_coordinate][second_coordinate] = int(right)
        razdalje[second_coordinate][first_coordinate] = int(right)

    best_path_solution = sys.maxsize  # In python3, sys.maxint changed to sys.maxsize
    worst_path_solution = 0

    start_timer = time.time()
    for permutation in itertools.permutations(razdalje.keys(), len(razdalje)):
        razdalja = 0
        start = permutation[0]
        for mesto in permutation[1:]:
            razdalja += razdalje[start][mesto]
            start = mesto
        if razdalja < best_path_solution:
            best_path_solution = razdalja
        if razdalja > worst_path_solution:
            worst_path_solution = razdalja

print("=============================== PART ONE ===============================")
print("What is the distance of the shortest route? ", best_path_solution)
print("\n")
print("=============================== PART TWO ===============================")
print("What is the distance of the longest route? ", worst_path_solution)
print("\n")
print("Code run time: ", (time.time() - start_timer) * 1000, "ms")