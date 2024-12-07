import numpy as np

from aoc.utils import read_lines


def get_diff(report: list[int]) -> np.ndarray:
    previous = np.array(report[:-1])
    current = np.array(report[1:])
    return current - previous


def is_safe(diff: np.ndarray) -> bool:
    safe = np.all(abs(diff) <= 3) and (np.all(diff < 0) or np.all(diff > 0))
    return bool(safe)


def count_pos_neg_zero(diff: np.ndarray) -> tuple[int, int, int]:
    pos_count = np.sum(diff > 0)
    neg_count = np.sum(diff < 0)
    zero_count = np.sum(diff == 0)
    return int(pos_count), int(neg_count), int(zero_count)


def check_report(report: list[int]) -> bool:
    if len(report) == 1:
        return True
    diff = get_diff(report)
    if is_safe(diff):
        return True
    for i in range(len(report)):
        new_report = report[:i] + report[i + 1 :]
        if is_safe(get_diff(new_report)):
            return True
    return False


def main(path: str) -> int:
    lines = read_lines(path)
    result = []
    for line in lines:
        report = [int(item) for item in line.split(" ")]
        result.append(check_report(report))
    return sum(result)


if __name__ == "__main__":
    input_sum_example = main(path="day2/example.txt")
    assert input_sum_example == 4
    input_sum_input = main(path="day2/input.txt")
    print(input_sum_input)
