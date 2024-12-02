from aoc.utils import parse


def main(path: str) -> int:
    lines = parse(path)
    splitted_lines = [line.split("   ") for line in lines]
    left_list = [int(line[0]) for line in splitted_lines]
    right_list = [int(line[1]) for line in splitted_lines]
    sorted_lists = zip(sorted(left_list), sorted(right_list))
    return sum([abs(right - left) for left, right in sorted_lists])


if __name__ == "__main__":
    input_sum_example = main(path="day1/example.txt")
    assert input_sum_example == 11
    input_sum_input = main(path="day1/input.txt")
    print(input_sum_input)
