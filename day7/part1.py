from itertools import product
from typing import List, Tuple

from aoc.utils import read_lines


def evaluate_expression(numbers: List[int], operators: Tuple[str, ...]) -> int:
    """Evaluate the expression formed by numbers and operators."""
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == "+":
            result += numbers[i + 1]
        elif operators[i] == "*":
            result *= numbers[i + 1]
    return result


def lines_to_equations(lines: List[str]) -> List[Tuple[int, List[int]]]:
    """Parse the input data into a list of (test_value, numbers) tuples."""
    equations = []
    for line in lines:
        test_value_str, numbers_str = line.split(":")
        test_value = int(test_value_str.strip())
        numbers = list(map(int, numbers_str.strip().split()))
        equations.append((test_value, numbers))
    return equations


def find_valid_equations(equations: List[Tuple[int, List[int]]]):
    """Find valid equations and calculate the total calibration result."""
    total_calibration_result = 0

    for test_value, numbers in equations:
        num_operators = len(numbers) - 1
        possible_operators = product("+*", repeat=num_operators)

        for operators in possible_operators:
            if evaluate_expression(numbers, operators) == test_value:
                total_calibration_result += test_value
                break

    return total_calibration_result


def main(path: str) -> int:
    lines = read_lines(path)
    equations = lines_to_equations(lines)
    result = find_valid_equations(equations)
    return result


if __name__ == "__main__":
    example_result = main(path="day7/example.txt")
    assert example_result == 3749
    input_result = main(path="day7/input.txt")
    print(input_result)
