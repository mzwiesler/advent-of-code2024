from collections import deque

import matplotlib.pyplot as plt
import numpy as np

from aoc.utils import read_lines

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def parse_grid(grid):
    start = end = None
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val == "S":
                start = (r, c)
            elif val == "E":
                end = (r, c)
    return start, end


def bfs(grid, end):
    rows, cols = len(grid), len(grid[0])
    dists = [[-1] * cols for _ in range(rows)]
    dists[end[0]][end[1]] = 0

    queue = deque([(end[0], end[1])])  # (row, col)

    while queue:
        r, c = queue.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != "#" and dists[nr][nc] == -1:
                dists[nr][nc] = dists[r][c] + 1
                queue.append((nr, nc))

    return dists


def check_cheats(dists, pos, radius, rows, cols, diff):
    count = 0
    r, c = pos
    for rad in range(2, radius + 1):
        for dr in range(rad + 1):
            dc = rad - dr
            for nr, nc in {(r + dr, c + dc), (r + dr, c - dc), (r - dr, c + dc), (r - dr, c - dc)}:
                if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                    continue
                if dists[nr][nc] == -1:
                    continue
                if dists[r][c] >= dists[nr][nc] + rad + diff:
                    count += 1
    return count


def evaluate_cheats(dists, start, radius, diff):
    rows = len(dists)
    cols = len(dists[0])
    r, c = start
    count = 0
    while dists[r][c] > 0:
        count += check_cheats(dists, (r, c), radius, rows, cols, diff)
        for dir in directions:
            nr = r + dir[0]
            nc = c + dir[1]
            if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                continue
            if dists[nr][nc] == dists[r][c] - 1:
                r, c = nr, nc
                break
    return count


grid = read_lines("day20/input.txt")
start, end = parse_grid(grid)
dists = bfs(grid, end)
heatmap = np.array(dists)

plt.imshow(heatmap, cmap="hot", interpolation="nearest")
plt.colorbar()
plt.show()

count = evaluate_cheats(dists, start, 20, 100)
print(count)
