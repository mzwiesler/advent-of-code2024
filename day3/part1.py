import re

from aoc.utils import read_lines


def extract_and_multiply(input_string: str) -> int:
    # Define a regex pattern to match valid mul(X,Y) instructions
    pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")

    # Find all matches in the memory string
    matches = pattern.findall(input_string)

    # Initialize the sum of results
    total_sum = 0

    # Iterate over all matches and compute the results
    for match in matches:
        x, y = map(int, match)
        total_sum += x * y

    return total_sum


def main(path: str) -> int:
    lines = read_lines(path)
    print(f"Number of lines: {len(lines)}")
    result = []
    for line in lines:
        result.append(extract_and_multiply(line))
    return sum(result)


if __name__ == "__main__":
    input_sum_example = main(path="day3/example1.txt")
    assert input_sum_example == 161
    input_sum_input = main(path="day3/input.txt")
    print(str(input_sum_input))
