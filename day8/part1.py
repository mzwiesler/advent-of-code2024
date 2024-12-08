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


def create_antinodes(p1: Tuple[int, int], p2: Tuple[int, int]) -> set[Tuple[int, int]]:
    antinodes = set()
    dx, dy = calculate_distance(p1, p2)
    antinodes.add((p1[0] - dx, p1[1] - dy))
    antinodes.add((p2[0] + dx, p2[1] + dy))

    return antinodes


def calculate_antinodes(antennas: Dict[str, List[Tuple[int, int]]]) -> set[Tuple[int, int]]:
    antinodes = set()
    for _, positions in antennas.items():
        n = len(positions)
        for i in range(n):
            for j in range(i + 1, n):
                p1 = positions[i]
                p2 = positions[j]
                antinodes.update(create_antinodes(p1, p2))
    return antinodes


def count_unique_antinodes(input_map: List[str]) -> int:
    antennas = get_antennas(input_map)
    antinodes = calculate_antinodes(antennas)
    unique_antinodes = set()
    for x, y in antinodes:
        if 0 <= x < len(input_map[0]) and 0 <= y < len(input_map):
            unique_antinodes.add((x, y))
    return len(unique_antinodes)


def main(path: str) -> int:
    lines = read_lines(path)
    result = count_unique_antinodes(lines)
    return result


if __name__ == "__main__":
    example_result = main(path="day8/example.txt")
    print(example_result)
    assert example_result == 14
    input_result = main(path="day8/input.txt")
    print(input_result)
