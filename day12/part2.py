import os
import time
from typing import List, Set, Tuple

from aoc.utils import read_lines

DIRECTION = [(0, 1), (1, 0), (0, -1), (-1, 0)]
TIME_DELAY = 0.1


def calculate_fence_price(garden_map: List[str], visualize: bool = False) -> int:
    rows = len(garden_map)
    cols = len(garden_map[0])
    visited = [[False] * cols for _ in range(rows)]

    def flood_fill(r, c, plant_type) -> Tuple[int, Set[Tuple[int, int]]]:
        stack = [(r, c)]
        area = 0
        region = {(r, c)}

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
                        region.add((nx, ny))

        return area, region

    def get_upper_points(region: Set[Tuple[int, int]]) -> Set[Tuple[int, int]]:
        upper_points = set()
        for upper_candidate in region:
            while upper_candidate in region:
                upper_candidate = (upper_candidate[0] - 1, upper_candidate[1])
            upper_points.add(upper_candidate)
        return upper_points

    def get_next_point(current: Tuple[int, int], direction: Tuple[int, int]) -> Tuple[int, int]:
        current_this = current
        return current_this[0] + direction[0], current_this[1] + direction[1]

    def print_region_and_current(region: Set[Tuple[int, int]], current: Tuple[int, int], plant_type: str):
        os.system("clear" if os.name == "posix" else "cls")
        rows = len(garden_map) + 1
        cols = len(garden_map[0]) + 1
        for r in range(-1, rows):
            for c in range(-1, cols):
                if (r, c) == current:
                    print("X", end="")
                elif (r, c) in region:
                    print(plant_type, end="")
                else:
                    print(".", end="")
            print()
        time.sleep(TIME_DELAY)

    def get_new_direction(
        current: Tuple[int, int],
        dir: int,
        buttom: int,
        region: Set[Tuple[int, int]],
    ) -> Tuple[int, int, int]:
        add_sides = 0
        # ground does not belong to region so we fall down and change dir to right
        if get_next_point(current, DIRECTION[buttom]) not in region:
            dir = (dir + 1) % 4
            buttom = (buttom + 1) % 4
            add_sides += 1
        # hit wall and turn left until we hit no wall
        turns = 0
        while get_next_point(current, DIRECTION[dir]) in region:
            if turns >= 4:
                break
            dir = (dir - 1) % 4
            buttom = (buttom - 1) % 4
            add_sides += 1
            turns += 1
        return dir, buttom, add_sides

    total_price = 0
    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                plant_type = garden_map[r][c]
                area, region = flood_fill(r, c, plant_type)
                upper_points = list(get_upper_points(region))
                sides = 0
                while upper_points:
                    upper_point = upper_points[0]
                    if visualize:
                        print_region_and_current(region, upper_point, plant_type)
                        print(plant_type)
                        print(sides)
                    upper_points.remove(upper_point)
                    dir = 0
                    buttom = 1
                    dir, buttom, _ = get_new_direction(upper_point, dir, buttom, region)
                    start = (upper_point, dir)
                    steps = 0
                    current = upper_point
                    while True:
                        dir, buttom, add_sides = get_new_direction(current, dir, buttom, region)
                        sides += add_sides
                        # This is special case for one point in region
                        if add_sides == 4:
                            break
                        if (current, dir) == start and steps > 0:
                            break
                        current = get_next_point(current, DIRECTION[dir])
                        if current in upper_points:
                            upper_points.remove(current)
                        if visualize:
                            print_region_and_current(region, current, plant_type)
                            print(sides)
                        steps += 1
                        if steps > 1000:
                            raise ValueError("Too many steps")
                    # print(plant_type)
                    # print(area)
                    # print(sides)

                total_price += area * sides
    return total_price


def main(path: str, visualize: bool = False) -> int:
    garden_map = read_lines(path)
    return calculate_fence_price(garden_map, visualize)


if __name__ == "__main__":
    example_result = main(path="day12/example.txt", visualize=False)
    print(example_result)
    assert example_result == 1206
    input_result = main(path="day12/input.txt")
    print(input_result)
