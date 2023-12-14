from typing import List

from utils import run, ParsingConfig, Example, Example

examples = [
    Example(
        answer=374,
        data="""
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
"""
    )
]


parsing_config = ParsingConfig(
    field_separator="",
)


def solve(data: List[List[str]]) -> int:
    empty_columns = [x for x in range(len(data[0])) if all(row[x] == '.' for row in data)]
    empty_rows = [y for y in range(len(data)) if all(d == '.' for d in data[y])]

    total = 0
    galaxies = [(x, y) for y, row in enumerate(data) for x, c in enumerate(row) if c == '#']
    for i in range(len(galaxies) - 1):
        (x, y) = galaxies[i]
        for (xx, yy) in galaxies[i+1:]:
            min_x = min(x, xx)
            max_x = max(x, xx)
            distance = (yy - y) + (max_x - min_x) + len([col for col in empty_columns if min_x < col < max_x]) + len([row for row in empty_rows if y < row < yy])
            total += distance

    return total


if __name__ == "__main__":
    run(
        examples=examples,
        parsing_config=parsing_config,
        solve=solve,
        real_answer=9648398,
    )
