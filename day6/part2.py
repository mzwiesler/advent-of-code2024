from typing import Any, List, Set, Tuple

from aoc.utils import read_lines

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
DIRECTION_SYMBOLS = {"^": 0, ">": 1, "v": 2, "<": 3}


def get_initial_position(map_lines: List[str]) -> Tuple[Tuple[int, int], int]:
    # Find the initial position and direction of the guard
    for y in range(len(map_lines)):
        for x in range(len(map_lines[0])):
            if map_lines[y][x] in DIRECTION_SYMBOLS:
                guard_pos = (y, x)
                guard_dir = DIRECTION_SYMBOLS[map_lines[y][x]]
                return guard_pos, guard_dir
    raise ValueError("Guard not found in the map")


def get_next_pos(pos: Tuple[int, int], dir: int) -> Tuple[int, int]:
    dy, dx = DIRECTIONS[dir]
    return (pos[0] + dy, pos[1] + dx)


def get_guard_path(
    obstacles: Set[Tuple[int, int]], guard_pos: Tuple[int, int], guard_dir: int, width: int, height: int
) -> Set[Tuple[int, int]]:
    visited_positions = set()
    visited_positions.add((guard_dir, guard_pos))
    next_pos = get_next_pos(guard_pos, guard_dir)
    while 0 <= next_pos[0] < height and 0 <= next_pos[1] < width:
        if next_pos in obstacles:
            guard_dir = (guard_dir + 1) % 4
        else:
            guard_pos = next_pos
            visited_positions.add(guard_pos)

        next_pos = get_next_pos(guard_pos, guard_dir)

    return visited_positions


def simulate_guard_path_with_obstacle(
    obstacles: Set[Tuple[int, int]], guard_pos: Tuple[int, int], guard_dir: int, width: int, height: int
) -> int:
    visited_positions = set()
    while True:
        next_pos = get_next_pos(guard_pos, guard_dir)
        if pos_out_of_grid(height, width, next_pos):
            return False
        elif next_pos in obstacles:
            if (guard_dir, guard_pos) in visited_positions:
                return True
            visited_positions.add((guard_dir, guard_pos))
            guard_dir = (guard_dir + 1) % 4
        else:
            guard_pos = next_pos


def pos_out_of_grid(height: int, width: int, pos: Tuple[int, int]) -> bool:
    if 0 <= pos[0] < height and 0 <= pos[1] < width:
        return False
    return True


def main(path: str) -> int:
    grid = read_lines(path)
    intial_guard_pos, intial_guard_dir = get_initial_position(grid)
    height = len(grid)
    width = len(grid[0])
    obstacles = {(y, x) for y in range(height) for x in range(width) if grid[y][x] == "#"}

    guard_path = get_guard_path(obstacles, intial_guard_pos, intial_guard_dir, width, height)

    count = 0
    for pos in guard_path:
        new_obstacles = obstacles.copy()
        new_obstacles.add(pos)
        if simulate_guard_path_with_obstacle(new_obstacles, intial_guard_pos, intial_guard_dir, width, height):
            count += 1
    return count


if __name__ == "__main__":
    example_result = main(path="day6/example.txt")
    print(example_result)
    assert example_result == 6
    input_result = main(path="day6/input.txt")
    print(input_result)
