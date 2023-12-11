from utils import run, ParsingConfig, Example

example_answer = 15

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


def _is_low_point(data, i, j):
    me = data[i][j]
    if i > 0 and data[i-1][j] <= me:
        return False
    if j > 0 and data[i][j-1] <= me:
        return False
    if i+1 < len(data) and data[i+1][j] <= me:
        return False
    if j+1 < len(data[i]) and data[i][j+1] <= me:
        return False
    return True


def solve(data):
    total = 0
    for i, row in enumerate(data):
        for j, n in enumerate(row):
            if _is_low_point(data, i, j):
                total += data[i][j] + 1
    return total


real_answer = 566


if __name__ == "__main__":
    run([Example(answer=example_answer, data=example_data)], parsing_config, solve, real_answer)
