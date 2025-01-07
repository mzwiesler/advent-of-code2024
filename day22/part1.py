from aoc.utils import read_lines


def next_secret_number(secret):
    # Step 1: Multiply by 64, mix, and prune
    secret = (secret ^ (secret * 64)) % 16777216
    # Step 2: Divide by 32, mix, and prune
    secret = (secret ^ (secret // 32)) % 16777216
    # Step 3: Multiply by 2048, mix, and prune
    secret = (secret ^ (secret * 2048)) % 16777216
    return secret


def simulate_secret_numbers(initial_secrets, iterations):
    final_secrets = []
    for secret in initial_secrets:
        for _ in range(iterations):
            secret = next_secret_number(secret)
        final_secrets.append(secret)
    return final_secrets


# Example input

initial_secrets = read_lines("day21/input.txt")
initial_secrets = [int(secret) for secret in initial_secrets]

iterations = 2000

# Simulate the secret numbers
final_secrets = simulate_secret_numbers(initial_secrets, iterations)

# Calculate the sum of the 2000th secret number for each buyer
result = sum(final_secrets)

print(result)
