from aoc.utils import read_lines


def main(path: str) -> int:
    lines = read_lines(path)
    splitted_lines = [line.split("   ") for line in lines]
    left_list = sorted([int(line[0]) for line in splitted_lines])
    right_list = sorted([int(line[1]) for line in splitted_lines])
    sum_dict = {}
    final_count = 0
    for i in left_list:
        if i in sum_dict:
            final_count += i * sum_dict[i]
            continue
        count_right = right_list.count(i)
        sum_dict[i] = count_right
        final_count += i * count_right
    return final_count


if __name__ == "__main__":
    input_sum_example = main(path="day1/example.txt")
    assert input_sum_example == 31
    input_sum_input = main(path="day1/input.txt")
    print(input_sum_input)
