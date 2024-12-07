DATA = [line.strip() for line in open("input.txt")]

PART_ONE_PAIRING_SUMS = {
    ('A', 'X'): 3,
    ('A', 'Y'): 6,
    ('A', 'Z'): 0,
    ('B', 'X'): 0,
    ('B', 'Y'): 3,
    ('B', 'Z'): 6,
    ('C', 'X'): 6,
    ('C', 'Y'): 0,
    ('C', 'Z'): 3,
}
PART_TWO_PAIRING_SUMS = {
    ('A', 'X'): 3,
    ('A', 'Y'): 1,
    ('A', 'Z'): 2,
    ('B', 'X'): 1,
    ('B', 'Y'): 2,
    ('B', 'Z'): 3,
    ('C', 'X'): 2,
    ('C', 'Y'): 3,
    ('C', 'Z'): 1,
}

# The score for a single round is the score for the shape you selected:
#   1 for Rock (X),
#   2 for Paper (Y),
#   3 for Scissors(Z)
PART_ONE_SCORE_DICT = dict(X=1, Y=2, Z=3)

# plus the score for the outcome of the round:
#   0 if you lost (X),
#   3 if the round was a draw (Y),
#   and 6 if you won (Z)
PART_TWO_SCORE_DICT = dict(X=0, Y=3, Z=6)


def solve(pairing_sums, score_dict):
    result = 0

    for pairing in DATA:
        elf, myself = pairing.split()
        result += score_dict[myself]
        result += pairing_sums[(elf, myself)]
    return result


print(solve(PART_ONE_PAIRING_SUMS, PART_ONE_SCORE_DICT))
print(solve(PART_TWO_PAIRING_SUMS, PART_TWO_SCORE_DICT))

