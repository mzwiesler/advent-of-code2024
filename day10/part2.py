from collections import deque
from typing import List, Tuple

from aoc.utils import read_lines


def find_trailheads(map_data: List[List[int]]) -> List[Tuple[int, int]]:
    trailheads = []
    for r in range(len(map_data)):
        for c in range(len(map_data[0])):
            if map_data[r][c] == 0:
                trailheads.append((r, c))
    return trailheads


def bfs(map_data: List[List[int]], start: Tuple[int, int]) -> int:
    """Breadth-first search to find the score of a trailhead."""
    rows, cols = len(map_data), len(map_data[0])
    queue = deque([start])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    score = 0

    while queue:
        r, c = queue.popleft()
        if map_data[r][c] == 9:
            score += 1
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if map_data[nr][nc] == map_data[r][c] + 1:
                    queue.append((nr, nc))

    return score


def main(path: str) -> int:
    map_data = [list(map(int, line)) for line in read_lines(path)]
    trailheads = find_trailheads(map_data)
    total_score = 0

    for trailhead in trailheads:
        total_score += bfs(map_data, trailhead)

    return total_score


if __name__ == "__main__":
    example_result = main(path="day10/example.txt")
    print(example_result)
    assert example_result == 81
    input_result = main(path="day10/input.txt")
    print(input_result)
