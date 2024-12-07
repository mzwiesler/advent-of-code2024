from aoc.utils import read_lines


def count_xmas_occurrences(grid):
    word = "XMAS"
    word_len = len(word)
    rows = len(grid)
    cols = len(grid[0])
    directions = [
        (0, 1),  # right
        (1, 0),  # down
        (1, 1),  # down-right
        (1, -1),  # down-left
        (0, -1),  # left
        (-1, 0),  # up
        (-1, -1),  # up-left
        (-1, 1),  # up-right
    ]

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def search_from(x, y, dx, dy):
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
            if not is_valid(nx, ny) or grid[nx][ny] != word[i]:
                return False
        return True

    count = 0
    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                if search_from(x, y, dx, dy):
                    count += 1

    return count


def main(path: str) -> int:
    grid = read_lines(path)
    return count_xmas_occurrences(grid)


if __name__ == "__main__":
    example_result = main(path="day4/example1.txt")
    assert example_result == 18
    input_result = main(path="day4/input.txt")
    print(input_result)
