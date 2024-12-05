import re
from typing import List, Tuple

from aoc.utils import parse


def search_pattern(x: int, y: int, grid: List[str], pattern: List[Tuple[int, int]]) -> bool:
    pos_letters = ["M", "S"]
    for dx, dy in pattern:
        nx, ny = x + dx, y + dy
        letter = grid[nx][ny]
        if (dx, dy) == (0, 0):
            if letter != "A":
                return False
        else:
            if letter not in pos_letters:
                return False
            pos_letters.remove(letter)
    return True


def count_xmas_patterns(grid: List[str]) -> int:
    rows = len(grid)
    cols = len(grid[0])

    # Define the X-MAS pattern and its variations
    diagonal_patters = [[(0, 0), (1, 1), (-1, -1)], [(0, 0), (-1, 1), (1, -1)]]

    count = 0
    for x in range(1, rows - 1):
        for y in range(1, cols - 1):
            if not (
                search_pattern(x, y, grid, diagonal_patters[0]) and search_pattern(x, y, grid, diagonal_patters[1])
            ):
                continue
            count += 1

    return count


def main(path: str) -> int:
    grid = parse(path)
    return count_xmas_patterns(grid)


if __name__ == "__main__":
    example_result = main(path="day4/example1.txt")
    assert example_result == 9
    input_result = main(path="day4/input.txt")
    print(input_result)
