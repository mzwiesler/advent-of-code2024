def can_form_design(design, patterns):
    n = len(design)
    dp = [False] * (n + 1)
    dp[0] = True  # An empty design can always be formed

    for i in range(1, n + 1):
        for pattern in patterns:
            if i >= len(pattern) and design[i - len(pattern) : i] == pattern:
                dp[i] = dp[i] or dp[i - len(pattern)]

    return dp[n]


def count_possible_designs(input_data):
    # Split the input data into patterns and designs
    parts = input_data.strip().split("\n\n")
    patterns = parts[0].split(", ")
    designs = parts[1].split("\n")

    count = 0
    for design in designs:
        if can_form_design(design, patterns):
            count += 1
    return count


def main(path: str) -> int:
    ## Count how many designs are possible
    input_data = open(path).read()
    possible_designs_count = count_possible_designs(input_data)
    return possible_designs_count


if __name__ == "__main__":
    example_result = main(path="day19/example.txt")
    print(example_result)
    assert example_result == 6
    input_result = main(path="day19/input.txt")
    print(input_result)
