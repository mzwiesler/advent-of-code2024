from collections import deque

import pandas as pd

from aoc.utils import read_lines


def parse_grid(grid):
    start = end = None
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val == "S":
                start = (r, c)
            elif val == "E":
                end = (r, c)
    return start, end


def bfs(grid, start, end, calculate_path=False):
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(start[0], start[1], 0)])  # (row, col, time)
    visited = set([(start[0], start[1])])
    parent = {}

    while queue:
        r, c, time = queue.popleft()

        if (r, c) == end:
            path = []
            if calculate_path:
                while (r, c) != start:
                    path.append((r, c))
                    r, c = parent[(r, c)]
                # print("Path:", path[::-1])
                # print("Time:", time)
            return time, path[::-1]

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != "#" and (nr, nc) not in visited:
                visited.add((nr, nc))
                if calculate_path:
                    parent[(nr, nc)] = (r, c)
                queue.append((nr, nc, time + 1))

    return float("inf"), []


def evaluate_cheats(grid, path, end):
    paths = set()
    cheats = []
    original_time = len(path)
    for i in range(len(path) - 1):
        r1, c1 = path[i]
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr1, nc1 = r1 + dr, c1 + dc
            # nr2, nc2 = nr1 + dr, nc1 + dc

            if 0 <= nr1 < len(grid) and 0 <= nc1 < len(
                grid[0]
            ):  # and 0 <= nr2 < len(grid) and 0 <= nc2 < len(grid[0]):
                if grid[nr1][nc1] == "#":
                    new_grid = grid.copy()
                    new_grid[nr1] = new_grid[nr1][:nc1] + "." + new_grid[nr1][nc1 + 1 :]
                    # if new_grid[nr2][nc2] == "#":
                    # new_grid[nr2] = new_grid[nr2][:nc2] + "." + new_grid[nr2][nc2 + 1 :]
                    new_time, this_path = bfs(new_grid, start, end, True)
                    path_string = "".join(f"{r}{c}" for r, c in this_path)
                    if new_time != float("inf"):
                        if path_string not in paths:
                            paths.add(path_string)
                            time_saved = original_time - new_time
                            cheats.append(time_saved)

    return cheats


def count_cheats_saving_at_least(grid, start, end, min_saving):
    time, path = bfs(grid, start, end, True)
    cheats = evaluate_cheats(grid, path, end)
    return cheats


grid = read_lines("day20/input.txt")
start, end = parse_grid(grid)
min_saving = 100
cheats_count = count_cheats_saving_at_least(grid, start, end, min_saving)
cheats_series = pd.Series(cheats_count)
cheats_grouped = cheats_series.groupby(cheats_series).count()
cheats_above_100 = cheats_grouped[cheats_grouped.index >= 100].sum()
print(f"Number of cheats saving more than 100 picoseconds: {cheats_above_100}")
print(cheats_grouped)
print(f"Number of cheats saving at least {min_saving} picoseconds: {cheats_series.count()}")
