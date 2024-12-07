import os
import time
from typing import Any, List, Tuple

from aoc.utils import read_lines

TIME_DELAY = 0.000001


def get_initial_position(map_lines: List[str], directions: dict[str, Any]) -> Tuple[Tuple[int, int], str]:
    # Find the initial position and direction of the guard
    for y in range(len(map_lines)):
        for x in range(len(map_lines[0])):
            if map_lines[y][x] in directions:
                guard_pos = (y, x)
                guard_dir = map_lines[y][x]
                return guard_pos, guard_dir
    raise ValueError("Guard not found in the map")


def simulate_guard_path(map_lines: List[str], visualize: bool = False):
    # Parse the map data
    height = len(map_lines)
    width = len(map_lines[0])

    # Directions: up, right, down, left
    turn_right = {"^": ">", ">": "v", "v": "<", "<": "^"}
    directions = {
        "^": (-1, 0),
        ">": (0, 1),
        "v": (1, 0),
        "<": (0, -1),
    }
    guard_pos, guard_dir = get_initial_position(map_lines, directions)
    visited_positions = set()
    visited_positions.add(guard_pos)
    dy, dx = directions[guard_dir]
    next_pos = (guard_pos[0] + dy, guard_pos[1] + dx)
    if visualize:
        vis_grid = visualize_grid(map_lines, visited_positions, guard_pos, guard_dir)
        print_grid(vis_grid)
    while 0 <= next_pos[0] < height and 0 <= next_pos[1] < width:
        if map_lines[next_pos[0]][next_pos[1]] == "#":
            guard_dir = turn_right[guard_dir]
        else:
            guard_pos = next_pos
            if visualize:
                vis_grid = visualize_grid(map_lines, visited_positions, guard_pos, guard_dir)
                print_grid(vis_grid)
            visited_positions.add(guard_pos)

        dy, dx = directions[guard_dir]
        next_pos = (guard_pos[0] + dy, guard_pos[1] + dx)

    return len(visited_positions)


def visualize_grid(grid, visited_positions, guard_pos, guard_dir) -> List[List[str]]:
    vis_grid = grid.copy()
    vis_grid = [list(row) for row in vis_grid]
    for r, c in visited_positions:
        vis_grid[r][c] = "X"
    vis_grid[guard_pos[0]][guard_pos[1]] = guard_dir
    return vis_grid


def print_grid(vis_grid: List[List[str]]) -> None:
    os.system("clear" if os.name == "posix" else "cls")
    for row in vis_grid:
        print("".join(row))
    time.sleep(TIME_DELAY)


def main(path: str, visualize: bool = False) -> int:
    grid = read_lines(path)
    return simulate_guard_path(grid, True)


if __name__ == "__main__":
    example_result = main(path="day6/example.txt")
    assert example_result == 41
    input_result = main(path="day6/input.txt")
    print(input_result)
