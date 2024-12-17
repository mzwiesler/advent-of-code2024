import os
import time
from typing import Set, Tuple


def parse_warehouse(layout):
    walls = set()
    robot_pos = None
    boxes = set()
    for r, line in enumerate(layout.strip().split("\n")):
        for c, char in enumerate(line):
            if char == "@":
                robot_pos = (r, c)
            elif char == "O":
                boxes.add((r, c))
            elif char == "#":
                walls.add((r, c))
    return walls, robot_pos, boxes


def can_move(walls, boxes, start_pos, direction):
    dr, dc = direction
    r, c = start_pos
    while (r, c) in boxes:
        r += dr
        c += dc
        if (r, c) in walls:
            return False
    return True


def move_boxes(boxes: Set[Tuple[int, int]], start_pos, direction):
    dr, dc = direction
    r, c = start_pos
    if (r, c) in boxes:
        boxes.remove((r, c))
    else:
        return None
    nr, nc = r + dr, c + dc
    while (nr, nc) in boxes:
        nr, nc = nr + dr, nc + dc
    boxes.add((nr, nc))


def move_robot(walls, robot_pos, boxes, move):
    directions = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
    dr, dc = directions[move]
    r, c = robot_pos
    nr, nc = r + dr, c + dc

    if (nr, nc) in walls:
        return robot_pos, boxes  # Hit a wall, no movement

    if (nr, nc) in boxes:
        if can_move(walls, boxes, (nr, nc), (dr, dc)):
            move_boxes(boxes, (nr, nc), (dr, dc))
        else:
            return robot_pos, boxes  # Box can't be pushed

    return (nr, nc), boxes


def calculate_gps_sum(boxes):
    return sum(100 * r + c for r, c in boxes)


def print_warehouse(walls, robot_pos, boxes, max_r, max_c):
    os.system("clear" if os.name == "posix" else "cls")
    for r in range(max_r):
        row_str = ""
        for c in range(max_c):
            if (r, c) == robot_pos:
                row_str += "@"
            elif (r, c) in boxes:
                row_str += "O"
            elif (r, c) in walls:
                row_str += "#"
            else:
                row_str += "."
        print(row_str)
    print()
    time.sleep(0.001)


def simulate_warehouse(layout, moves, visualize: bool = False):
    walls, robot_pos, boxes = parse_warehouse(layout)
    max_r = len(layout)
    max_c = len(layout[0])
    if visualize:
        print_warehouse(walls, robot_pos, boxes, max_r, max_c)
    for move in moves:
        robot_pos, boxes = move_robot(walls, robot_pos, boxes, move)
        if visualize:
            print_warehouse(walls, robot_pos, boxes, max_r, max_c)
    return calculate_gps_sum(boxes)


def main(path: str, visualize: bool = False) -> int:
    layout, moves = open(path).read().split("\n\n")
    moves = moves.replace("\n", "")
    result = simulate_warehouse(layout, moves, visualize)
    return result


if __name__ == "__main__":
    example_result = main(path="day15/example.txt")
    print(example_result)
    assert example_result == 2028
    input_result = main(path="day15/input.txt", visualize=False)
    print(input_result)
