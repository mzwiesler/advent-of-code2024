from typing import List


def read_lines(file_path: str) -> List[str]:
    # Read in the input file as string
    with open(file_path, "r") as f:
        data = f.read()
    lines = data.split("\n")  # split by new line
    return lines
