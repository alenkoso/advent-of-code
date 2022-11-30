def calculate_score(deck):
    answer = 0
    for i, card in enumerate(deck):
        answer += (len(deck) - i) * card
    return answer


starting_state_winners_map = {}


def recursive_combat(player1, player2, game_num=1):
    # print("Starting Game on stackframe", game_num)
    # print("Player1:", player1)
    # print("Player2:", player2)
    initial_state = (tuple(player1), tuple(player2))
    if initial_state in starting_state_winners_map:
        # print("Repeat game with state")
        # print("Player1:", player1)
        # print("Player2:", player2)
        winner = starting_state_winners_map[initial_state]
        # print(f"The winner in frame {game_num} is Player {winner}!")
        return winner
    previous_states = []
    winner = 1
    while player1 and player2:
        if (state := (tuple(player1), tuple(player2))) in previous_states:
            break

        previous_states.append(state)

        p1 = player1.pop(0)
        p2 = player2.pop(0)

        # print("Next round start")
        # print("Player1:", player1, p1)
        # print("Player2:", player2, p2)

        w = None
        if len(player1) >= p1 and len(player2) >= p2:
            new_deck1 = player1[:p1][:]
            new_deck2 = player2[:p2][:]
            w = recursive_combat(new_deck1, new_deck2, game_num + 1)
            # print("Back to ", game_num)
        else:
            w = 1 if p1 > p2 else 2
        if w == 1:
            player1.append(p1)
            player1.append(p2)
        else:
            player2.append(p2)
            player2.append(p1)

    if len(player1) == 0:
        winner = 2
    elif len(player2) == 0:
        winner = 1
    else:
        winner = 1
        # print("Player 1 wins by default")

    starting_state_winners_map[initial_state] = winner
    # print(f"The winner in frame {game_num} is Player {winner}!")

    return winner


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

# player1 = [9, 2, 6, 3, 1]
# player2 = [5, 8, 4, 7, 10]

w = recursive_combat(player1, player2)

if w == 1:
    part_two = calculate_score(player1)

else:
    part_two = calculate_score(player2)

print(
    "Defend your honor as Raft Captain by playing the small crab in a game of Recursive Combat using the same two decks as before.")
print("What is the winning player's score? ", part_two)
