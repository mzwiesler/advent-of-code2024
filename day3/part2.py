import re
from typing import Tuple

from aoc.utils import parse


def extract_and_multiply(input_string: str, enabled: bool = True) -> Tuple[int, bool]:
    # Define a regex pattern to match valid mul(X,Y) instructions

    combined_pattern = re.compile(r"(mul\((\d+),(\d+)\))|(do\(\))|(don\'t\(\))")
    mul_pattern = re.compile(r"mul\((\d+),(\d+)\)")
    # Find all matches for the combined pattern
    matches = re.finditer(combined_pattern, input_string)
    result = 0
    for match in matches:
        if match.group(5):
            enabled = False
        elif match.group(4):
            enabled = True
        else:
            if enabled:
                result += int(match.group(2)) * int(match.group(3))
    return result, enabled


def main(path: str) -> int:
    lines = parse(path)
    print(f"Number of lines: {len(lines)}")
    result = []
    enabled = True
    for line in lines:
        line_result, enabled = extract_and_multiply(line, enabled)
        result.append(line_result)
    return sum(result)


if __name__ == "__main__":
    input_sum_example = main(path="day3/example2.txt")
    assert input_sum_example == 48
    input_sum_input = main(path="day3/input.txt")
    print(str(input_sum_input))
