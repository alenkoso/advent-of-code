import os
import sys
import time

project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(project_root)

from helpers.parsing_utils import read_input_file_to_ints

def calculate_next_secret(current_secret):
    modulo_value = 16777216
    
    current_secret ^= (current_secret * 64) % modulo_value
    current_secret %= modulo_value
    
    current_secret ^= (current_secret // 32) % modulo_value
    current_secret %= modulo_value
    
    current_secret ^= (current_secret * 2048) % modulo_value
    current_secret %= modulo_value
    
    return current_secret

def get_secret_after_steps(initial_secret, number_of_steps):
    evolving_secret = initial_secret
    for _ in range(number_of_steps):
        evolving_secret = calculate_next_secret(evolving_secret)
    return evolving_secret

def build_price_sequence(initial_secret, sequence_length):
    previous_price = initial_secret % 10
    current_secret = initial_secret
    price_sequence = []
    
    for _ in range(sequence_length):
        next_secret = calculate_next_secret(current_secret)
        current_price = next_secret % 10
        price_delta = current_price - previous_price
        price_sequence.append((price_delta, current_price))
        previous_price = current_price
        current_secret = next_secret
    
    return price_sequence

def find_optimal_pattern(price_sequences, target_pattern_length):
    pattern_totals = {}
    
    for buyer_sequence in price_sequences:
        seen_patterns = set()
        sequence_length = len(buyer_sequence)
        
        for start_pos in range(sequence_length - target_pattern_length + 1):
            end_pos = start_pos + target_pattern_length
            price_deltas = tuple(delta[0] for delta in buyer_sequence[start_pos:end_pos])
            final_price = buyer_sequence[end_pos - 1][1]
            
            if price_deltas not in seen_patterns:
                seen_patterns.add(price_deltas)
                pattern_totals[price_deltas] = pattern_totals.get(price_deltas, 0) + final_price
    
    best_pattern, highest_total = max(pattern_totals.items(), key=lambda x: x[1])
    return highest_total, best_pattern

def main():
    data = read_input_file_to_ints("input.txt")
    
    start_time = time.time()
    part_1 = sum(get_secret_after_steps(secret, 2000) for secret in data)
    end_time= time.time()
    print("Part 1: ", part_1)
    print("Part 1 Execution Time: ", end_time - start_time, "seconds")
    
    start_time = time.time()
    price_sequences = [build_price_sequence(secret, 2000) for secret in data]
    part_2, best_pattern = find_optimal_pattern(price_sequences, 4)
    end_time = time.time()
    print("Part 2: ", part_2)
    print("Best pattern: ", best_pattern)
    print("Part 2 Execution Time: ", end_time - start_time, "seconds")

if __name__ == "__main__":
    main()