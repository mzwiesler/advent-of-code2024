import os
import time
from typing import List, Set, Tuple


def parse_warehouse(layout):
    walls = set()
    robot_pos = None
    left = set()
    right = set()
    for r, line in enumerate(layout):
        for c, char in enumerate(line):
            if char == "@":
                robot_pos = (r, c)
            elif char == "[":
                left.add((r, c))
            elif char == "]":
                right.add((r, c))
            elif char == "#":
                walls.add((r, c))
    return walls, robot_pos, left, right


def can_move(walls, left, right, start_pos, direction) -> List[Tuple[int, int]] | None:
    dr, dc = direction
    r, c = start_pos
    targets = [(r, c)]
    for r, c in targets:
        nr = r + dr
        nc = c + dc
        if (nr, nc) in targets:
            continue
        if (nr, nc) in walls:
            return None
        if (nr, nc) in left:
            targets.append((nr, nc))
            targets.append((nr, nc + 1))
        if (nr, nc) in right:
            targets.append((nr, nc))
            targets.append((nr, nc - 1))
    return targets[1:]


def move_boxes(targets: List[Tuple[int, int]], direction, left, right):
    new_left = left.copy()
    new_right = right.copy()
    dr, dc = direction
    for r, c in targets:
        if (r, c) in left:
            new_left.remove((r, c))
        elif (r, c) in right:
            new_right.remove((r, c))
    for r, c in targets:
        if (r, c) in left:
            new_left.add((r + dr, c + dc))
        elif (r, c) in right:
            new_right.add((r + dr, c + dc))
    return new_left, new_right


def move_robot(walls, robot_pos, left, right, move):
    directions = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
    dr, dc = directions[move]
    r, c = robot_pos
    nr, nc = r + dr, c + dc

    if (nr, nc) in walls:
        return robot_pos, left, right  # Hit a wall, no movement

    if (nr, nc) in left or (nr, nc) in right:
        targets = can_move(walls, left, right, (r, c), (dr, dc))
        if targets:
            left, right = move_boxes(targets, (dr, dc), left, right)
        else:
            return robot_pos, left, right  # Box can't be pushed

    return (nr, nc), left, right


def calculate_gps_sum(left):
    return sum(100 * r + c for r, c in left)


def print_warehouse(walls, robot_pos, left, right, max_r, max_c):
    os.system("clear" if os.name == "posix" else "cls")
    for r in range(max_r):
        row_str = ""
        for c in range(max_c):
            if (r, c) == robot_pos:
                row_str += "@"
            elif (r, c) in left:
                row_str += "["
            elif (r, c) in right:
                row_str += "]"
            elif (r, c) in walls:
                row_str += "#"
            else:
                row_str += "."
        print(row_str)
    print()
    time.sleep(0.1)


def simulate_warehouse(layout, moves, visualize: bool = False):
    walls, robot_pos, left, right = parse_warehouse(layout)
    max_r = len(layout)
    max_c = len(layout[0])
    if visualize:
        print_warehouse(walls, robot_pos, left, right, max_r, max_c)
    for move in moves:
        robot_pos, left, right = move_robot(walls, robot_pos, left, right, move)
        if visualize:
            print_warehouse(walls, robot_pos, left, right, max_r, max_c)
    return calculate_gps_sum(left)


def main(path: str, visualize: bool = False) -> int:
    layout, moves = open(path).read().split("\n\n")
    expansion = {"#": "##", "O": "[]", ".": "..", "@": "@."}
    layout = [list("".join(expansion[char] for char in line)) for line in layout.splitlines()]
    moves = moves.replace("\n", "")
    result = simulate_warehouse(layout, moves, visualize)
    return result


if __name__ == "__main__":
    example_result = main(path="day15/example2.txt", visualize=True)
    print(example_result)
    input_result = main(path="day15/input2.txt", visualize=False)
    print(input_result)
