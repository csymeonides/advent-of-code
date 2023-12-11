import math

from utils import run, ParsingConfig, Example

example_answer = 1134

example_data = """
2199943210
3987894921
9856789892
8767896789
9899965678
"""


parsing_config = ParsingConfig(
    field_separator="",
    value_converter=int,
)


def solve(data):
    max_i = len(data)
    max_j = len(data[0])

    def _find_neighbours(ii, jj):
        ns = set()
        if ii > 0:
            ns.add((ii-1, jj))
        if jj > 0:
            ns.add((ii, jj-1))
        if ii+1 < max_i:
            ns.add((ii+1, jj))
        if jj+1 < max_j:
            ns.add((ii, jj+1))
        return ns

    basins = []
    for i, row in enumerate(data):
        for j, n in enumerate(row):
            if n < 9:
                new_basin = {(i, j)}
                neighbours = _find_neighbours(i, j)
                for basin in basins.copy():
                    if basin.intersection(neighbours):
                        basins.remove(basin)
                        new_basin = basin.union(new_basin)
                basins.append(new_basin)

    return math.prod(sorted([len(b) for b in basins])[-3:])


real_answer = 891684


if __name__ == "__main__":
    run([Example(answer=example_answer, data=example_data)], parsing_config, solve, real_answer)
