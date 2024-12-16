from typing import Dict, List

from aoc.utils import read_lines


def count_stones(stone: int, step: int, cache: Dict) -> int:
    """Recursively counts the number of stones after a given number of steps.

    This function uses memoization to cache results of previous computations
    to optimize performance. The behavior of the function changes based on
    the value of the stone and the step.

    Args:
        stone (int): The initial number of stones.
        step (int): The number of steps to simulate.
        cache (Dict): A dictionary used to store previously computed results.

    Returns:
        int: The total number of stones after the given number of steps.
    """
    if (stone, step) in cache:
        return cache[(stone, step)]
    # Termination after number of steps are executed
    if step == 0:
        result = 1
    else:
        if stone == 0:
            result = count_stones(1, step - 1, cache)
        elif len(str(stone)) % 2 == 0:
            half_len = len(str(stone)) // 2
            left = int(str(stone)[:half_len])
            right = int(str(stone)[half_len:])
            result = count_stones(left, step - 1, cache) + count_stones(right, step - 1, cache)
        else:
            result = count_stones(stone * 2024, step - 1, cache)

    cache[(stone, step)] = result
    return result


def simulate_blinks(initial_stones: List[int], blinks: int) -> int:
    cache = {}
    total_stones = 0

    for stone in initial_stones:
        total_stones += count_stones(stone, blinks, cache)

    return total_stones


def main(path: str) -> int:
    initial_stones = list(map(int, read_lines(path)[0].split(" ")))
    blinks = 75
    number_of_stones = simulate_blinks(initial_stones, blinks)
    return number_of_stones


if __name__ == "__main__":
    example_result = main(path="day11/example.txt")
    print(example_result)
    input_result = main(path="day11/input.txt")
    print(input_result)
