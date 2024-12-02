import numpy as np

from aoc.utils import parse


def is_safe(report: list[int]) -> bool:
    if len(report) < 2:
        return True
    previous = np.array(report[:-1])
    current = np.array(report[1:])
    diff = current - previous
    safe = np.all(abs(diff) <= 3) and (np.all(diff < 0) or np.all(diff > 0))
    return bool(safe)


def main(path: str) -> int:
    lines = parse(path)
    result = []
    for line in lines:
        report = [int(item) for item in line.split(" ")]
        result.append(is_safe(report))
    return sum(result)


if __name__ == "__main__":
    input_sum_example = main(path="day2/example.txt")
    assert input_sum_example == 2
    input_sum_input = main(path="day2/input.txt")
    print(input_sum_input)
