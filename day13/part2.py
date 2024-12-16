import re
from typing import List, Tuple

from aoc.utils import read_lines


def determinant(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def solve_with_cramers_rule(ax, ay, bx, by, px, py):
    A = [[ax, bx], [ay, by]]
    det_A = determinant(A)

    if det_A == 0:
        return None

    A_ca = [[px, bx], [py, by]]
    A_cb = [[ax, px], [ay, py]]

    det_A_ca = determinant(A_ca)
    det_A_cb = determinant(A_cb)

    ca = det_A_ca / det_A
    cb = det_A_cb / det_A

    if ca % 1 == 0 and cb % 1 == 0:
        return int(ca), int(cb)
    else:
        return None


def solve_claw_machines(machines):
    total_tokens = 0
    prizes_won = 0

    for machine in machines:
        ax, ay, bx, by, px, py = machine
        solution = solve_with_cramers_rule(ax, ay, bx, by, px, py)
        if solution:
            ca, cb = solution
            total_tokens += ca * 3 + cb
            prizes_won += 1

    return prizes_won, total_tokens


def parse_lines(lines: List[str]) -> List[Tuple[int, int, int, int, int, int]]:
    machines = []
    pattern_A = r"Button A: X\+(\d+), Y\+(\d+)"
    pattern_B = r"Button B: X\+(\d+), Y\+(\d+)"
    pattern_C = r"Prize: X=(\d+), Y=(\d+)"
    for i in range(0, len(lines) - 1, 4):
        A_x, A_y = map(int, re.match(pattern_A, lines[i]).groups())
        B_x, B_y = map(int, re.match(pattern_B, lines[i + 1]).groups())
        prize_x, prize_y = map(int, re.match(pattern_C, lines[i + 2]).groups())
        addition = 10000000000000
        machines.append((A_x, A_y, B_x, B_y, prize_x + addition, prize_y + addition))
    return machines


def main(path: str) -> int:
    lines = read_lines(path)
    machines = parse_lines(lines)

    _, tokens = solve_claw_machines(machines)
    return tokens


if __name__ == "__main__":
    example_result = main(path="day13/example.txt")
    print(example_result)
    input_result = main(path="day13/input.txt")
    print(input_result)
