# # with open("Inputs\InputDay22_Example.txt") as input_file:
# with open("Inputs\InputDay22.txt") as input_file:
#     raw = input_file.read()

# input_raw = [line for line in raw.split('\n') if line.strip()]

player1 = [
    41,
    33,
    20,
    32,
    7,
    45,
    2,
    12,
    14,
    29,
    49,
    37,
    6,
    11,
    39,
    46,
    47,
    38,
    23,
    22,
    28,
    10,
    36,
    35,
    24
]
player2 = [
    17,
    4,
    44,
    9,
    27,
    18,
    30,
    42,
    21,
    26,
    16,
    48,
    8,
    15,
    34,
    50,
    19,
    43,
    25,
    1,
    13,
    31,
    3,
    5,
    40
]

while player1 and player2:
    p1 = player1.pop(0)
    p2 = player2.pop(0)
    if p1 > p2:
        player1.append(p1)
        player1.append(p2)
    else:
        player2.append(p2)
        player2.append(p1)

if player1:
    part_one = 0
    for i, card in enumerate(player1):
        part_one += (len(player1) - i) * card

elif player2:
    part_one = 0
    for i, card in enumerate(player2):
        part_one += (len(player2) - i) * card

print("Play the small crab in a game of Combat using the two decks you just dealt.")
print("What is the winning player's score?", part_one)