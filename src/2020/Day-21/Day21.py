import re
import math
import itertools
import numpy as np
from collections import defaultdict


class Food:
    def __init__(self, ingredients, allergens):
        self.ing = set(ingredients)
        self.allergens = set(allergens)

    def __repr__(self):
        ingr = ' '.join(self.ing)
        allerg = ', '.join(self.allergens)
        return f"{ingr} ({allerg})"


# with open("Inputs\InputDay21_Example.txt") as input:
with open("../Inputs/InputDay21.txt") as input:
    raw = input.read()

input_raw = [line for line in raw.split('\n') if line.strip()]

foods = []
ingredients = set()
allergens = set()

allergen_probable_map = defaultdict(list)
for line in input_raw:
    ingredients_regex = re.match(r"(.*?)\(contains (.*?)\)", line)
    ingredients_split = [x for x in ingredients_regex.group(1).split(' ') if x]
    allergens_split = [x for x in ingredients_regex.group(2).split(', ') if x]
    ingredients.update(ingredients_split)
    allergens.update(allergens_split)
    food = Food(ingredients_split, allergens_split)
    foods.append(food)

could_allergens = set()
for a in allergens:
    ingredient_sets = []
    for f in foods:
        if a in f.allergens:
            ingredient_sets.append(f.ing)
    if len(ingredient_sets) > 1:
        could_allergens.update(ingredient_sets[0].intersection(*ingredient_sets[1:]))
    else:
        could_allergens.update(ingredient_sets[0])

not_allergens = ingredients - could_allergens
print(not_allergens)

ingredients_occur_map = defaultdict(int)
for f in foods:
    for ing in not_allergens:
        if ing in f.ing:
            ingredients_occur_map[ing] += 1

part_one = sum(list(ingredients_occur_map.values()))

print(
    "=========================================================== PART ONE ===========================================================")
print("Determine which ingredients cannot possibly contain any of the allergens in your list.")
print("How many times do any of those ingredients appear?", part_one)

for f in foods:
    f.ing -= not_allergens

eng_candidate_map = {a: None for a in allergens}

for a in allergens:
    ingredient_sets = []
    for f in foods:
        if a in f.allergens:
            ingredient_sets.append(f.ing)
    if len(ingredient_sets) > 1:
        intersection = ingredient_sets[0].intersection(*ingredient_sets[1:])
    else:
        intersection = ingredient_sets[0]

    eng_candidate_map[a] = intersection

eng_gib_map = {a: None for a in allergens}
not_processed = set(allergens)
while eng_candidate_map:
    for a, gibs in eng_candidate_map.items():
        if len(gibs) == 1:
            break
    eng_gib_map[a] = list(gibs)[0]
    del eng_candidate_map[a]
    for a in eng_candidate_map:
        eng_candidate_map[a] -= gibs

print(eng_gib_map)

gib_eng_map = {
    gib: eng for eng, gib in eng_gib_map.items()
}
dang_list = list(eng_gib_map.values())
dang_list.sort(key=lambda x: gib_eng_map[x])

print(
    "=========================================================== PART TWO ===========================================================")
print("Part two solution:", ','.join(dang_list))
