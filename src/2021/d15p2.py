import math

from src.utils import run, ParsingConfig

example_answer = 315

example_data = """
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
"""


parsing_config = ParsingConfig(
    field_separator="",
    value_converter=int,
)


def _find_neighbours(data, i, j):
    out = []
    if i > 0:
        out.append((i-1, j))
    if i+1 < len(data):
        out.append((i+1, j))
    if j > 0:
        out.append((i, j-1))
    if j+1 < len(data[0]):
        out.append((i, j+1))
    return out


def solve(data):
    for row in data:
        vals = row.copy()
        for i in range(1, 5):
            row += [((val - 1 + i) % 9) + 1 for val in vals]

    first_rows = data.copy()
    for j in range(1, 5):
        for row in first_rows:
            data.append([((val - 1 + j) % 9) + 1 for val in row])

    neighbours = {}
    for i, row in enumerate(data):
        for j in range(len(row)):
            neighbours[(i, j)] = _find_neighbours(data, i, j)

    costs = {(i, j): math.inf for i in range(len(data)) for j in range(len(data[0]))}
    costs[(0, 0)] = 0
    queue = [(0, 0)]
    while queue:
        current = queue.pop(0)
        for i, j in neighbours[current]:
            cost = costs[current] + data[i][j]
            if cost < costs[(i, j)]:
                costs[(i, j)] = cost
                queue.append((i, j))

    return costs[(len(data) - 1, len(data[0]) - 1)]


real_answer = 2922


if __name__ == "__main__":
    run(example_data, example_answer, parsing_config, solve, real_answer)
