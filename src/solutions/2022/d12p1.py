import math

from utils import run, ParsingConfig, Example

example_answer = 31

example_data = """
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""


START = -1
END = 999


def parse_height(val):
    if val == "S":
        return START
    elif val == "E":
        return END
    else:
        return ord(val) - ord("a")


parsing_config = ParsingConfig(
    field_separator="",
    value_converter=parse_height,
)


def _find_neighbours(data, i, j):
    out = []
    val = data[i][j]
    if i > 0 and data[i-1][j] <= val+1:
        out.append((i-1, j))
    if i+1 < len(data) and data[i+1][j] <= val+1:
        out.append((i+1, j))
    if j > 0 and data[i][j-1] <= val+1:
        out.append((i, j-1))
    if j+1 < len(data[0]) and data[i][j+1] <= val+1:
        out.append((i, j+1))
    return out


def solve(data):
    start = next((i, j) for i, row in enumerate(data) for j, val in enumerate(row) if val == START)
    end = next((i, j) for i, row in enumerate(data) for j, val in enumerate(row) if val == END)
    data[start[0]][start[1]] = 0
    data[end[0]][end[1]] = ord("z") - ord("a")

    neighbours = {}
    for i, row in enumerate(data):
        for j in range(len(row)):
            neighbours[(i, j)] = _find_neighbours(data, i, j)

    costs = {(i, j): math.inf for i in range(len(data)) for j in range(len(data[0]))}
    costs[start] = 0

    queue = [start]
    while queue:
        current = queue.pop(0)
        for i, j in neighbours[current]:
            cost = costs[current] + 1
            if cost < costs[(i, j)]:
                costs[(i, j)] = cost
                queue.append((i, j))

    return costs[end]


real_answer = 380


if __name__ == "__main__":
    run([Example(answer=example_answer, data=example_data)], parsing_config, solve, real_answer)
