from typing import List, Tuple

from aoc.utils import read_lines


def parse_disk_map(disk_map: str) -> List[int]:
    lengths = [int(digit) for digit in disk_map]
    return lengths


def create_disk_representation(lengths: List[int]) -> Tuple:
    data_blocks = []
    free_blocks = []
    file_id = 0
    for i in range(0, len(lengths), 2):
        file_length = lengths[i]
        free_space_length = lengths[i + 1] if i + 1 < len(lengths) else 0
        data_blocks.append((file_id, file_length))
        free_blocks.append(([], free_space_length))
        file_id += 1
    return data_blocks, free_blocks


def get_position(disk, id) -> int:
    for j in range(len(disk) - 1, -1, -1):
        if disk[j][0] == id:
            return j
    raise Exception("id not found")


def get_blocks_as_list(data_blocks: List[Tuple[int, int]], free_blocks: List):
    result = []
    for i in range(len(data_blocks)):
        result.extend([data_blocks[i][0]] * data_blocks[i][1])
        result.extend(free_blocks[i][0])
        result.extend(["."] * free_blocks[i][1])
    return result


def get_block_as_list(block: Tuple[int, int]) -> List[int]:
    return [block[0]] * block[1]


def compact_disk(data_blocks: List[Tuple[int, int]], free_blocks: List):
    max_file_length = len(data_blocks)
    for file_id in range(max_file_length - 1, 1, -1):
        for j in range(file_id):
            if free_blocks[j][1] < data_blocks[file_id][1]:
                continue
            current_data_block = data_blocks[file_id]
            current_free_block = free_blocks[j]
            free_blocks[j] = [
                current_free_block[0] + get_block_as_list(current_data_block),
                current_free_block[1] - current_data_block[1],
            ]
            data_blocks[file_id] = (0, data_blocks[file_id][1])
            break
    return data_blocks, free_blocks


def calculate_checksum(disk):
    checksum = 0
    for position, block in enumerate(disk):
        if block != ".":
            checksum += position * int(block)
    return checksum


def main(path: str) -> int:
    disk_map = read_lines(path)[0]
    # result = part2(list(map(int, disk_map)))
    lengths = parse_disk_map(disk_map)
    data_blocks, free_blocks = create_disk_representation(lengths)
    data_blocks_updated, free_blocks_updated = compact_disk(data_blocks, free_blocks)
    disk_combined = get_blocks_as_list(data_blocks_updated, free_blocks_updated)
    checksum = calculate_checksum(disk_combined)
    return checksum


if __name__ == "__main__":
    example_result = main(path="day9/example.txt")
    assert example_result == 2858
    input_result = main(path="day9/input.txt")
    print(input_result)
