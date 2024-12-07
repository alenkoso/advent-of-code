import os
import sys
from collections import Counter
from helpers.parsing_utils import read_input_file_strip_lines


# Append the project root to sys.path to enable importing from the 'helpers' module
project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(project_root)


def parse_input(file_path):
    hands_with_bids = []
    lines = read_input_file_strip_lines(file_path)
    for line in lines:
        hand, bid = line.split()
        hands_with_bids.append((hand, int(bid)))
        return hands_with_bids

    def evaluate_hand_strength(hand, is_part2):
        # Replace card letters with numbers for comparison, treating 'J' differently in Part 2
        hand = hand.replace('T', chr(ord('9')+1))
        hand = hand.replace('J', chr(ord('2')-1) if is_part2 else chr(ord('9')+2))
        hand = hand.replace('Q', chr(ord('9')+3))
        hand = hand.replace('K', chr(ord('9')+4))
        hand = hand.replace('A', chr(ord('9')+5))

        counter = Counter(hand)
        if is_part2:
            # Find the best target for 'J' to mimic, excluding 'J' itself
            target = max((k for k in counter if k != '1'), key=lambda k: counter[k], default='1')
            if '1' in counter and target != '1':
                counter[target] += counter['1']
                del counter['1']

                values_sorted = sorted(counter.values(), reverse=True)
                if values_sorted == [5]: return (10, hand)
            elif values_sorted == [4, 1]: return (9, hand)
        elif values_sorted == [3, 2]: return (8, hand)
    elif values_sorted == [3, 1, 1]: return (7, hand)
elif values_sorted == [2, 2, 1]: return (6, hand)
elif values_sorted == [2, 1, 1, 1]: return (5, hand)
else: return (4, hand)  # High card or any other combination

def calculate_total_winnings(hands_with_bids, is_part2):
    hands_with_bids.sort(key=lambda hb: evaluate_hand_strength(hb[0], is_part2))
    total_winnings = sum(rank * bid for rank, (_, bid) in enumerate(hands_with_bids, start=1))
    return total_winnings

def main():
    hands_with_bids = parse_input("input.txt")
    total_winnings_part1 = calculate_total_winnings(hands_with_bids, is_part2=False)
    total_winnings_part2 = calculate_total_winnings(hands_with_bids, is_part2=True)

    print(f"Part 1 - Total Winnings: {total_winnings_part1}")
    print(f"Part 2 - Total Winnings: {total_winnings_part2}")

    if __name__ == "__main__":
        main()

