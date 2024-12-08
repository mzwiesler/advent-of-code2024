from typing import Dict, List, Tuple

from aoc.utils import read_lines


def get_antennas(input_map: List[str]) -> Dict[str, List[Tuple[int, int]]]:
    antennas = {}
    for y, row in enumerate(input_map):
        for x, char in enumerate(row):
            if char != ".":
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append((x, y))
    return antennas


def calculate_distance(p1: Tuple[int, int], p2: Tuple[int, int]) -> Tuple[int, int]:
    return (p2[0] - p1[0], p2[1] - p1[1])


def create_antinodes(p1: Tuple[int, int], p2: Tuple[int, int], height: int, width: int) -> set[Tuple[int, int]]:
    antinodes = set()
    dx, dy = calculate_distance(p1, p2)
    new_p1 = (p1[0] - dx, p1[1] - dy)
    while 0 <= new_p1[0] < width and 0 <= new_p1[1] < height:
        antinodes.add(new_p1)
        new_p1 = (new_p1[0] - dx, new_p1[1] - dy)
    new_p2 = (p2[0] + dx, p2[1] + dy)
    while 0 <= new_p2[0] < width and 0 <= new_p2[1] < height:
        antinodes.add(new_p2)
        new_p2 = (new_p2[0] + dx, new_p2[1] + dy)

    return antinodes


def calculate_antinodes(antennas: Dict[str, List[Tuple[int, int]]], width: int, height: int) -> set[Tuple[int, int]]:
    antinodes = set()
    for _, positions in antennas.items():
        n = len(positions)
        for i in range(n):
            for j in range(i + 1, n):
                p1 = positions[i]
                p2 = positions[j]
                antinodes.update(create_antinodes(p1, p2, height, width))
    return antinodes


def count_unique_antinodes(input_map: List[str]) -> int:
    antennas = get_antennas(input_map)
    height = len(input_map)
    width = len(input_map[0])
    antinodes = calculate_antinodes(antennas, width, height)
    for antenna in antennas.values():
        antinodes.update(set(antenna))
    for antinode in antinodes:
        input_map[antinode[1]] = input_map[antinode[1]][: antinode[0]] + "X" + input_map[antinode[1]][antinode[0] + 1 :]
    return len(antinodes)


def print_gid(grid: List[str]):
    for row in grid:
        print(row)


def main(path: str) -> int:
    lines = read_lines(path)
    result = count_unique_antinodes(lines)
    return result


if __name__ == "__main__":
    example_result = main(path="day8/example.txt")
    assert example_result == 34
    input_result = main(path="day8/input.txt")
    print(input_result)
