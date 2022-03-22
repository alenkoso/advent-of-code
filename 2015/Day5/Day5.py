# part one
def is_nice(word):
    bad_word_substrings = ("ab", "cd", "pq", "xy")
    vowels = "aeiou"
    number_of_vowels = 0
    duplicates_found = False

    for i in range(len(word) - 1):
        if word[i] in vowels:
            number_of_vowels += 1

        if word[i] + word[i + 1] in bad_word_substrings:
            return False

        if word[i] == word[i + 1]:
            duplicates_found = True
        if word[-1] in vowels:
            number_of_vowels += 1

    return number_of_vowels >= 3 and duplicates_found


# part two
# Now, a nice string is one with all of the following properties:
#
# It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
# It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.

def is_nice_part_two(word):
    pairs = {}
    duplicates_found = False
    repeating_letters = False

    for i in range(len(word) - 1):
        previous_position = pairs.setdefault(word[i] + word[i + 1], i)
        if previous_position != i and previous_position != i - 1:
            duplicates_found = True

        # repeating letters

# ZMERAJ pazi na indentatione, sploh continue mora biti nujno znotraj for ali while zanke, drugače ne dela
        try:
            if word[i] == word[i + 2]:
                repeating_letters = True
        except IndexError:
            continue  # continue is only allowed within a for or while loop

    return duplicates_found and repeating_letters


# Main

with open("input.txt") as input:
    number_of_nice_words1 = 0
    number_of_nice_words2 = 0

    for word in input:
        if is_nice(word):  # part one
            number_of_nice_words1 += 1
        if is_nice_part_two(word):  # part two
            number_of_nice_words2 += 1
print("============== PART ONE ==============")
print("How many strings are nice? ", number_of_nice_words1)
print("============== PART TWO ==============")
print("How many strings are nice under these new rules? ", number_of_nice_words2)
