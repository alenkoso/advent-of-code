from collections import defaultdict
from itertools import product


def parse_input(filename="input.txt"):
    with open(filename) as f:
        lines = f.readlines()
    p1_start = int(lines[0].strip().split(": ")[1])
    p2_start = int(lines[1].strip().split(": ")[1])
    return p1_start, p2_start

# Pre-calculate all possible combinations of 3 rolls
ROLL_COMBINATIONS = list(product([1, 2, 3], repeat=3))
# Count frequency of each sum to avoid recalculating
ROLL_SUMS = defaultdict(int)
for rolls in ROLL_COMBINATIONS:
    ROLL_SUMS[sum(rolls)] += 1

def play_dirac_dice(p1_start, p2_start):
    # State: (p1_pos, p1_score, p2_pos, p2_score, p1_turn)
    # Value: number of universes in this state
    states = defaultdict(int)
    states[(p1_start, 0, p2_start, 0, True)] = 1
    
    p1_wins = 0
    p2_wins = 0
    
    while states:
        new_states = defaultdict(int)
        
        for state, universes in states.items():
            p1_pos, p1_score, p2_pos, p2_score, p1_turn = state
            
            # For each possible sum of three rolls
            for roll_sum, frequency in ROLL_SUMS.items():
                if p1_turn:
                    new_pos = ((p1_pos + roll_sum - 1) % 10) + 1
                    new_score = p1_score + new_pos
                    
                    # If player 1 wins in these universes
                    if new_score >= 21:
                        p1_wins += universes * frequency
                    else:
                        new_state = (new_pos, new_score, p2_pos, p2_score, False)
                        new_states[new_state] += universes * frequency
                else:
                    new_pos = ((p2_pos + roll_sum - 1) % 10) + 1
                    new_score = p2_score + new_pos
                    
                    # If player 2 wins in these universes
                    if new_score >= 21:
                        p2_wins += universes * frequency
                    else:
                        new_state = (p1_pos, p1_score, new_pos, new_score, True)
                        new_states[new_state] += universes * frequency
        
        states = new_states
    
    return max(p1_wins, p2_wins)

def main():
    p1_start, p2_start = parse_input()
    
    # Part 2
    result = play_dirac_dice(p1_start, p2_start)
    print(f"Part 2: {result}")

if __name__ == "__main__":
    main()

