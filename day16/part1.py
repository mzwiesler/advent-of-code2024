from typing import List

from aoc.utils import read_lines

# Directions: (dy, dx, cost to move forward)
DIRECTIONS = {"E": (0, 1, 1), "S": (1, 0, 1), "W": (0, -1, 1), "N": (-1, 0, 1)}

# Rotations: (current direction, new direction, cost to rotate)
ROTATIONS = {
    "E": {"S": 1000, "N": 1000},
    "S": {"E": 1000, "W": 1000},
    "W": {"S": 1000, "N": 1000},
    "N": {"E": 1000, "W": 1000},
}


def parse_map(maze):
    start = end = None
    grid = []
    for y, line in enumerate(maze):
        grid.append(list(line))
        if "S" in line:
            start = (y, line.index("S"))
        if "E" in line:
            end = (y, line.index("E"))
    return grid, start, end


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return not self.elements

    def put(self, item, priority):
        self.elements.append((priority, item))
        self.elements.sort(key=lambda x: x[0])

    def get(self):
        return self.elements.pop(0)[1]


def a_star_search(grid, start, end):
    # Priority queue for A* search
    pq = PriorityQueue()
    pq.put((start[0], start[1], "E", 0), 0)  # (y, x, direction, cost)
    visited = set()

    while not pq.is_empty():
        y, x, direction, cost = pq.get()

        if (y, x) == end:
            return cost

        if (y, x, direction) in visited:
            continue
        visited.add((y, x, direction))

        # Move forward
        dy, dx, move_cost = DIRECTIONS[direction]
        ny, nx = y + dy, x + dx
        if grid[ny][nx] != "#":
            pq.put((ny, nx, direction, cost + move_cost), cost + move_cost + heuristic((ny, nx), end))

        # Rotate
        for new_direction, rotate_cost in ROTATIONS[direction].items():
            dy, dx, _ = DIRECTIONS[new_direction]
            if grid[y + dy][x + dx] != "#":
                pq.put((y, x, new_direction, cost + rotate_cost), cost + rotate_cost + heuristic((y, x), end))

    raise ValueError("No path found")


def solve_maze(maze: List[str]) -> int:
    grid, start, end = parse_map(maze)
    return a_star_search(grid, start, end)


def main(path: str) -> int:
    lines = read_lines(path)
    result = solve_maze(lines)
    return result


if __name__ == "__main__":
    example_result = main(path="day16/example.txt")
    print(example_result)
    assert example_result == 7036
    example_result2 = main(path="day16/example2.txt")
    print(example_result2)
    assert example_result2 == 11048
    input_result = main(path="day16/input.txt")
    print(input_result)
