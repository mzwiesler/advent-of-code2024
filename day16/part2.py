# Directions: (dy, dx, cost to move forward)
from aoc.utils import read_lines

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


def a_star_search_all_paths(grid, start, end):
    # Priority queue for A* search
    pq = PriorityQueue()
    pq.put((start[0], start[1], "E", 0, []), 0)  # (y, x, direction, cost, path)
    visited = {}
    all_paths = []
    min_cost = float("inf")

    while not pq.is_empty():
        y, x, direction, cost, path = pq.get()

        if (y, x) == end:
            if cost < min_cost:
                min_cost = cost
                all_paths = [path + [(y, x)]]
            elif cost == min_cost:
                all_paths.append(path + [(y, x)])
            continue
        if cost > min_cost:
            continue
        if (y, x, direction) in visited and visited[(y, x, direction)] < cost:
            continue
        visited[(y, x, direction)] = cost

        # Move forward
        dy, dx, move_cost = DIRECTIONS[direction]
        ny, nx = y + dy, x + dx
        if grid[ny][nx] != "#":
            pq.put((ny, nx, direction, cost + move_cost, path + [(y, x)]), cost + move_cost + heuristic((ny, nx), end))

        # Rotate
        for new_direction, rotate_cost in ROTATIONS[direction].items():
            dy, dx, _ = DIRECTIONS[new_direction]
            if grid[y + dy][x + dx] != "#":
                pq.put(
                    (y, x, new_direction, cost + rotate_cost, path + [(y, x)]),
                    cost + rotate_cost + heuristic((y, x), end),
                )

    return min_cost, all_paths


def solve_maze(maze):
    grid, start, end = parse_map(maze)
    return a_star_search_all_paths(grid, start, end)


def print_maze_with_paths(maze, path_set):
    grid, start, end = parse_map(maze)

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if (y, x) in path_set:
                if (y, x) == start:
                    print("S", end="")
                elif (y, x) == end:
                    print("E", end="")
                else:
                    print("O", end="")
            else:
                print(grid[y][x], end="")
        print()


def main(path: str):
    lines = read_lines(path)
    _, all_paths = solve_maze(lines)
    path_set = set()
    for path in all_paths:
        path_set.update(path)
    print_maze_with_paths(lines, path_set)
    num_tiles = len(path_set)
    return num_tiles


if __name__ == "__main__":
    num_tiles_example = main(path="day16/example.txt")
    print(num_tiles_example)
    assert num_tiles_example == 45
    num_tiles_example2 = main(path="day16/example2.txt")
    print(num_tiles_example2)
    assert num_tiles_example2 == 64
    input_result = main(path="day16/input.txt")
    print(input_result)
