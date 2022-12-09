from src.utils import run, ParsingConfig

example_answer = 21

example_data = """
30373
25512
65332
33549
35390
"""


parsing_config = ParsingConfig(
    field_separator="",
    value_converter=int,
)


def solve(data):
    n_rows = len(data)
    n_cols = len(data[0])
    visible = [[False for _ in range(n_cols)] for _ in range(n_rows)]

    for i, row in enumerate(data):
        for j, tree in enumerate(row):
            visible[i][j] = (
                all(data[ii][j] < tree for ii in range(i)) or
                all(data[ii][j] < tree for ii in range(i+1, n_rows)) or
                all(data[i][jj] < tree for jj in range(j)) or
                all(data[i][jj] < tree for jj in range(j+1, n_cols))
            )

    return len([v for row in visible for v in row if v])


if __name__ == "__main__":
    run(example_data, example_answer, parsing_config, solve)
