import math
from dataclasses import dataclass
from typing import List, Tuple

from utils import run, ParsingConfig

example_answer = 467835

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


@dataclass
class Star:
    x: int
    y: int
    adjacent_numbers: List[int]

    @property
    def value(self) -> int:
        if len(self.adjacent_numbers) == 2:
            return self.adjacent_numbers[0] * self.adjacent_numbers[1]
        return 0

    def is_adjacent_to(self, y: int, min_x: int, max_x: int) -> bool:
        return min_x - 1 <= self.x <= max_x + 1 and y - 1 <= self.y <= y + 1


def _find_all_stars(data: List[List[str]]) -> List[Star]:
    stars = []
    for y, row in enumerate(data):
        for x, char in enumerate(row):
            if char == "*":
                stars.append(Star(x=x, y=y, adjacent_numbers=[]))
    return stars


def solve(data):
    stars = _find_all_stars(data)
    for y, row in enumerate(data):
        start_index = 0
        while start_index < len(row):
            char = row[start_index]
            if _is_digit(char):
                number, end_index = _get_number(row=row, start_index=start_index)
                for star in stars:
                    if star.is_adjacent_to(y=y, min_x=start_index, max_x=end_index):
                        star.adjacent_numbers.append(number)
                start_index = end_index
            start_index += 1
    return sum(star.value for star in stars)


if __name__ == "__main__":
    run(
        example_data=example_data,
        example_answer=example_answer,
        parsing_config=parsing_config,
        solve=solve,
        real_answer=79613331,
    )
