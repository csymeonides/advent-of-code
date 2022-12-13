from src.utils import run, ParsingConfig

example_answer = 195

example_data = """
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
"""


parsing_config = ParsingConfig(
    # parser_class=None,
    # parser_func=None,
    field_separator="",
    value_converter=int,
    # single_field=True,
    # multi_line=True,
    # strip=False,
)


def find_neighbours(data, i, j):
    out = []
    if i > 0:
        out.append((i-1, j))
        if j > 0:
            out.append((i-1, j-1))
        if j+1 < len(data[0]):
            out.append((i-1, j+1))
    if i+1 < len(data):
        out.append((i+1, j))
        if j > 0:
            out.append((i+1, j-1))
        if j+1 < len(data[0]):
            out.append((i+1, j+1))
    if j > 0:
        out.append((i, j-1))
    if j+1 < len(data[0]):
        out.append((i, j+1))
    return out


def solve(data):
    total = 0
    for step in range(999):
        data = [[x + 1 for x in row] for row in data]
        flashed = set()
        while True:
            new_flashes = {
                (i, j) for i, row in enumerate(data) for j, x in enumerate(row)
                if (i, j) not in flashed and x > 9
            }
            if not new_flashes:
                break
            flashed = flashed.union(new_flashes)
            total += len(new_flashes)
            for i, j in new_flashes:
                for neighbour in find_neighbours(data, i, j):
                    data[neighbour[0]][neighbour[1]] += 1
        for (i, j) in flashed:
            data[i][j] = 0
        if len(flashed) == len(data) * len(data[0]):
            return step + 1
    return None


real_answer = 273


if __name__ == "__main__":
    run(example_data, example_answer, parsing_config, solve, real_answer)
