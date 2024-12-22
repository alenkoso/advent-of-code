def compute_next_secret(secret_number):
    MODULO = 16777216
    secret_number ^= (secret_number * 64) % MODULO
    secret_number %= MODULO
    secret_number ^= (secret_number // 32) % MODULO
    secret_number %= MODULO
    secret_number ^= (secret_number * 2048) % MODULO
    secret_number %= MODULO
    return secret_number

def simulate_sequence(secret, steps):
    for _ in range(steps):
        secret = compute_next_secret(secret)
    return secret

def generate_deltas_and_values(secret, steps):
    last_price = secret % 10
    deltas = []
    for _ in range(steps):
        next_secret = compute_next_secret(secret)
        current_price = next_secret % 10
        deltas.append((current_price - last_price, current_price))
        last_price = current_price
        secret = next_secret
    return deltas

def find_best_pattern(deltas, pattern_length):
    patterns = {}
    for buyer_deltas in deltas:
        seen = set()
        for i in range(len(buyer_deltas) - pattern_length + 1):
            pattern = tuple(delta[0] for delta in buyer_deltas[i:i + pattern_length])
            value = buyer_deltas[i + pattern_length - 1][1]
            if pattern not in seen:
                seen.add(pattern)
                patterns[pattern] = patterns.get(pattern, 0) + value
    best_pattern, part_2 = max(patterns.items(), key=lambda x: x[1])
    return part_2, best_pattern

with open("input.txt", 'r') as file:
    initial_secrets = [int(line.strip()) for line in file.readlines()]

part_1 = sum(simulate_sequence(secret, 2000) for secret in initial_secrets)
print("Part 1: ", part_1)

deltas = [generate_deltas_and_values(secret, 2000) for secret in initial_secrets]
part_2, best_pattern = find_best_pattern(deltas, 4)
print("Part 2: ", part_2)
print("Best pattern: ", best_pattern)
