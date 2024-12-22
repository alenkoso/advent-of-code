def compute_next_secret(secret_number):
    MODULO = 16777216

    secret_number ^= (secret_number * 64) % MODULO
    secret_number %= MODULO

    secret_number ^= (secret_number // 32) % MODULO
    secret_number %= MODULO

    secret_number ^= (secret_number * 2048) % MODULO
    secret_number %= MODULO

    return secret_number

def simulate_secret_sequence(initial_secret, steps=2000):
    secret = initial_secret
    for _ in range(steps):
        secret = compute_next_secret(secret)
    return secret

input_file_path = 'input.txt'

with open(input_file_path, 'r') as file:
    initial_secrets = [int(line.strip()) for line in file.readlines()]

results = [simulate_secret_sequence(secret) for secret in initial_secrets]
total_sum = sum(results)

print(total_sum)