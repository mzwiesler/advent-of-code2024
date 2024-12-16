from aoc.utils import read_lines


def blink(stones):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            half_len = len(str(stone)) // 2
            left = int(str(stone)[:half_len])
            right = int(str(stone)[half_len:])
            new_stones.extend([left, right])
        else:
            new_stones.append(stone * 2024)
    return new_stones


def simulate_blinks(initial_stones, blinks):
    stones = initial_stones
    for _ in range(blinks):
        stones = blink(stones)
    return len(stones)


def main(path: str) -> int:
    initial_stones = list(map(int, read_lines(path)[0].split(" ")))
    blinks = 25
    number_of_stones = simulate_blinks(initial_stones, blinks)
    return number_of_stones


if __name__ == "__main__":
    example_result = main(path="day11/example.txt")
    print(example_result)
    assert example_result == 55312
    input_result = main(path="day11/input.txt")
    print(input_result)
