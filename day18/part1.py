from collections import deque

from aoc.utils import read_lines

# Define the grid size
# List of incoming byte positions (example input)
# Parse the input to get the list of byte positions


def get_grid(byte_positions, byte_length, grid_size):
    # Initialize the grid
    grid = [["." for _ in range(grid_size)] for _ in range(grid_size)]

    # Mark the corrupted positions
    for x, y in byte_positions[:byte_length]:  # Simulate the first 1024 bytes
        if x < grid_size and y < grid_size:
            grid[y][x] = "#"
    return grid


# Directions for moving in the grid (right, down, left, up)
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


# Function to print the grid
def print_grid(grid):
    for row in grid:
        print("".join(row))


# BFS to find the shortest path
def bfs(start, goal, grid, grid_size):
    queue = deque([start])
    visited = set()
    visited.add(start)
    steps = 0

    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            if (x, y) == goal:
                return steps
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < grid_size and 0 <= ny < grid_size and (nx, ny) not in visited and grid[ny][nx] == ".":
                    queue.append((nx, ny))
                    visited.add((nx, ny))
        steps += 1
    return -1  # If there's no path


def main(path: str, byte_length: int, grid_size: int) -> int:
    # Start and goal positions
    start = (0, 0)
    goal = (grid_size - 1, grid_size - 1)

    byte_positions = []
    lines = read_lines(path)
    for line in lines:
        x, y = map(int, line.split(","))
        byte_positions.append((x, y))
    grid = get_grid(byte_positions, byte_length, grid_size)
    print_grid(grid)
    result = bfs(start, goal, grid, grid_size)
    return result


if __name__ == "__main__":
    example_result = main(path="day18/example.txt", byte_length=12, grid_size=7)
    print(example_result)
    assert example_result == 22
    input_result = main(path="day18/input.txt", byte_length=1024, grid_size=71)
    print(input_result)
