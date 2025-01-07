from itertools import product


def next_secret_number(secret):
    # Step 1: Multiply by 64, mix, and prune
    secret = (secret ^ (secret * 64)) % 16777216
    # Step 2: Divide by 32, mix, and prune
    secret = (secret ^ (secret // 32)) % 16777216
    # Step 3: Multiply by 2048, mix, and prune
    secret = (secret ^ (secret * 2048)) % 16777216
    return secret


def generate_prices(initial_secret, iterations):
    prices = [initial_secret % 10]
    secret = initial_secret
    for _ in range(iterations):
        secret = next_secret_number(secret)
        prices.append(secret % 10)
    return prices


def find_best_sequence(initial_secret, iterations, result):
    prices = generate_prices(initial_secret, iterations)
    seen = set()
    for i in range(len(prices) - 4):
        seq = prices[i : i + 5]
        diff = [seq[i + 1] - seq[i] for i in range((len(seq) - 1))]
        diff_str = ",".join(map(str, diff))
        if diff_str in seen:
            continue
        seen.add(diff_str)
        if diff_str not in result:
            result[diff_str] = seq[-1]
        else:
            result[diff_str] += seq[-1]
    return result


result = {}
for line in open("day22/input.txt"):
    result = find_best_sequence(int(line), 2000, result)

print(max(result.values()))
