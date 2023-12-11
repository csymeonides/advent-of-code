import math
from typing import List, Tuple

from utils import run, ParsingConfig, Example

example_answer = 4361

example_data = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""


parsing_config = ParsingConfig(
    field_separator="",
)


def _is_digit(char: str) -> bool:
    try:
        int(char)
        return True
    except:
        return False


def _get_number(row: List[str], start_index: int) -> Tuple[int, int]:
    num_str = row[start_index]
    i = start_index + 1
    while i < len(row) and _is_digit(row[i]):
        num_str += row[i]
        i += 1
    return int(num_str), i-1


def _is_symbol(char: str) -> bool:
    return char not in ".0123456789"


def _has_adjacent_symbol(data: List[List[str]], y: int, start_index: int, end_index: int) -> bool:
    min_x = max(start_index - 1, 0)
    max_x = min(end_index + 1, len(data[0]) - 1)
    if _is_symbol(data[y][min_x]) or _is_symbol(data[y][max_x]):
        return True
    if y > 0 and any(_is_symbol(char) for char in data[y-1][min_x:max_x + 1]):
        return True
    if y < len(data) - 1 and any(_is_symbol(char) for char in data[y+1][min_x:max_x + 1]):
        return True


def solve(data):
    total = 0
    for y, row in enumerate(data):
        start_index = 0
        while start_index < len(row):
            char = row[start_index]
            if _is_digit(char):
                number, end_index = _get_number(row=row, start_index=start_index)
                if _has_adjacent_symbol(data=data, y=y, start_index=start_index, end_index=end_index):
                    total += number
                start_index = end_index
            start_index += 1
    return total


if __name__ == "__main__":
    run(
        examples=[Example(answer=example_answer, data=example_data)],
        parsing_config=parsing_config,
        solve=solve,
        real_answer=543867,
    )
