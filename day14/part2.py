import os
import time

from aoc.utils import read_lines


def parse_input(lines):
    robots = []
    velocity = []
    for line in lines:
        p_part, v_part = line.split(" ")
        p = tuple(map(int, p_part[2:].split(",")))
        v = tuple(map(int, v_part[2:].split(",")))
        robots.append(p)
        velocity.append(v)
    return robots, velocity


def simulate_robots(robots, volocity, width, height, seconds):
    final_positions = []
    for (px, py), (vx, vy) in zip(robots, volocity):
        final_px = (px + vx * seconds) % width
        final_py = (py + vy * seconds) % height
        final_positions.append((final_px, final_py))
    return final_positions


def print_grid(positions, width, height):
    os.system("clear" if os.name == "posix" else "cls")
    grid = [["." for _ in range(width)] for _ in range(height)]
    for x, y in positions:
        if grid[y][x] == ".":
            grid[y][x] = "1"
        else:
            grid[y][x] = str(int(grid[y][x]) + 1)
    for row in grid:
        print("".join(row))
    time.sleep(0.5)


def count_robots_in_quadrants(positions, width, height):
    mid_x = width // 2
    mid_y = height // 2
    quadrants = [0, 0, 0, 0]  # top-left, top-right, bottom-left, bottom-right

    for x, y in positions:
        if x == mid_x or y == mid_y:
            continue
        if x < mid_x and y < mid_y:
            quadrants[0] += 1
        elif x >= mid_x and y < mid_y:
            quadrants[1] += 1
        elif x < mid_x and y >= mid_y:
            quadrants[2] += 1
        elif x >= mid_x and y >= mid_y:
            quadrants[3] += 1

    return quadrants


def calculate_safety_factor(quadrants):
    factor = 1
    for count in quadrants:
        factor *= count
    return factor


def main(path: str, width: int, height: int, seconds: int, iterate: bool = True) -> int:
    lines = read_lines(path)
    # Parse input
    robots, velocity = parse_input(lines)

    # Print positions in the grid
    # print_grid([robot[0] for robot in robots], width, height)
    safety_factor = []
    # Simulate robots
    if iterate:
        for second in range(seconds):
            robots = simulate_robots(robots, velocity, width, height, 1)
            # print_grid(robots, width, height)

            # Count robots in quadrants
            quadrants = count_robots_in_quadrants(robots, width, height)

            # Calculate safety factor
            safety_factor.append(calculate_safety_factor(quadrants))
        min_safety_factor = min(safety_factor)
        min_index = safety_factor.index(min_safety_factor)
        return min_index + 1
    else:
        robots = simulate_robots(robots, velocity, width, height, seconds)
        print_grid(robots, width, height)

        # Count robots in quadrants
        quadrants = count_robots_in_quadrants(robots, width, height)

        # Calculate safety factor
        return calculate_safety_factor(quadrants)


if __name__ == "__main__":
    input_result = main(path="day14/input.txt", width=101, height=103, seconds=10000)

    main(path="day14/input.txt", width=101, height=103, seconds=input_result, iterate=False)
    print(input_result)
