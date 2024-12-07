import sys
import os
from helpers.file_utils import read_input_file

project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(project_root)

def calculate_points(scratchcards):
    total_points = 0
    for card in scratchcards:
        parts = card.split(" | ")
        winning_numbers = set(parts[0].split())
        your_numbers = parts[1].split()
        matches = 0
        for number in your_numbers:
            if number in winning_numbers:
                matches += 1
        if matches > 0:
            total_points += 2 ** (matches - 1)
    return total_points

def calculate_total_scratchcards(scratchcards):
    total_cards = len(scratchcards)
    card_copies = [1] * total_cards

    for i in range(total_cards):
        winning_numbers, your_numbers = scratchcards[i].split(" | ")
        winning_numbers = set(winning_numbers.split())
        your_numbers = your_numbers.split()
        matches = sum(num in winning_numbers for num in your_numbers)
        
        for j in range(i + 1, min(i + 1 + matches, total_cards)):
            card_copies[j] += card_copies[i]

    return sum(card_copies)

def main():
    input_file = 'input.txt'
    scratchcards = read_input_file(input_file)
    total_points = calculate_points(scratchcards)
    print(f"Part 1: {total_points}")
    total_scratchcards = calculate_total_scratchcards(scratchcards)
    print(f"Part 2: {total_scratchcards}")

if __name__ == "__main__":
    main()
