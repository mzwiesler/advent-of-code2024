from typing import List

from aoc.utils import read_lines


def parse_disk_map(disk_map: str) -> List[int]:
    lengths = [int(digit) for digit in disk_map]
    return lengths


def create_disk_representation(lengths: List[int]) -> List:
    disk = []
    file_id = 0
    for i in range(0, len(lengths), 2):
        file_length = lengths[i]
        free_space_length = lengths[i + 1] if i + 1 < len(lengths) else 0
        disk.extend([file_id] * file_length)
        disk.extend([None] * free_space_length)
        file_id += 1
    return disk


def compact_disk(disk):
    compacted_disk = []
    for _, block in enumerate(disk):
        if block is not None:
            compacted_disk.append(block)
        else:
            while disk and disk[-1] is None:
                disk.pop()
            compacted_disk.append(disk[-1])
            disk.pop()
            while disk and disk[-1] is None:
                disk.pop()
    # compacted_disk.extend(["."] * (len(disk) - len(compacted_disk)))
    return compacted_disk


def calculate_checksum(disk):
    checksum = 0
    for position, block in enumerate(disk):
        if block != ".":
            checksum += position * block
    return checksum


def main(path: str) -> int:
    disk_map = read_lines(path)[0]
    lengths = parse_disk_map(disk_map)
    disk = create_disk_representation(lengths)
    compacted_disk = compact_disk(disk)
    checksum = calculate_checksum(compacted_disk)
    return checksum


if __name__ == "__main__":
    example_result = main(path="day9/example.txt")
    print(example_result)
    assert example_result == 1928
    input_result = main(path="day9/input.txt")
    print(input_result)
