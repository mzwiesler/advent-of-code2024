from aoc.utils import read_lines


def parse_input(lines):
    robots = []
    for line in lines:
        p_part, v_part = line.split(" ")
        p = tuple(map(int, p_part[2:].split(",")))
        v = tuple(map(int, v_part[2:].split(",")))
        robots.append((p, v))
    return robots


def simulate_robots(robots, width, height, seconds):
    final_positions = []
    for (px, py), (vx, vy) in robots:
        final_px = (px + vx * seconds) % width
        final_py = (py + vy * seconds) % height
        final_positions.append((final_px, final_py))
    return final_positions


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


def print_grid(positions, width, height):
    print("-------------")
    grid = [["." for _ in range(width)] for _ in range(height)]
    for x, y in positions:
        if grid[y][x] == ".":
            grid[y][x] = "1"
        else:
            grid[y][x] = str(int(grid[y][x]) + 1)
    for row in grid:
        print("".join(row))


def main(path: str, width: int, height: int, seconds: int) -> int:
    lines = read_lines(path)
    # Parse input
    robots = parse_input(lines)

    # Print positions in the grid
    # print_grid([robot[0] for robot in robots], width, height)

    # Simulate robots
    final_positions = simulate_robots(robots, width, height, seconds)

    print_grid(final_positions, width, height)

    # Count robots in quadrants
    quadrants = count_robots_in_quadrants(final_positions, width, height)

    # Calculate safety factor
    safety_factor = calculate_safety_factor(quadrants)

    print("Safety Factor:", safety_factor)
    return safety_factor


if __name__ == "__main__":
    example_result = main(path="day14/example.txt", width=11, height=7, seconds=100)
    print(example_result)
    # assert example_result == 480
    input_result = main(path="day14/input.txt", width=101, height=103, seconds=7132)
    print(input_result)
