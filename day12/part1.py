from typing import List

from aoc.utils import read_lines


def calculate_fence_price(garden_map: List[str]) -> int:
    rows = len(garden_map)
    cols = len(garden_map[0])
    visited = [[False] * cols for _ in range(rows)]

    def flood_fill(r, c, plant_type):
        stack = [(r, c)]
        area = 0
        perimeter = 0

        while stack:
            x, y = stack.pop()
            if visited[x][y]:
                continue
            visited[x][y] = True
            area += 1
            # Check all four directions
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and garden_map[nx][ny] == plant_type:
                    if not visited[nx][ny]:
                        stack.append((nx, ny))
                else:
                    perimeter += 1

        return area, perimeter

    total_price = 0

    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                plant_type = garden_map[r][c]
                area, perimeter = flood_fill(r, c, plant_type)
                total_price += area * perimeter

    return total_price


def main(path: str) -> int:
    garden_map = read_lines(path)
    return calculate_fence_price(garden_map)


if __name__ == "__main__":
    example_result = main(path="day12/example.txt")
    print(example_result)
    assert example_result == 1930
    input_result = main(path="day12/input.txt")
    print(input_result)
