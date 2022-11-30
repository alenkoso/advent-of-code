print("=============================== PART TWO ===============================")
print(
    "Find the total number of characters to represent the newly encoded strings minus the number of characters of code in each original string literal: \n")
print("The answer is: ", sum(2 + string.count('\\') + string.count('"') for string in open('input.txt')))
