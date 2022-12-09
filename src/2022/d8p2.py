from src.utils import run, ParsingConfig

example_answer = 8

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
    scores = [[0 for _ in range(n_cols)] for _ in range(n_rows)]

    for i, row in enumerate(data):
        for j, tree in enumerate(row):
            score = compute_score(tree, [data[ii][j] for ii in reversed(range(i))])
            if score != 0:
                score *= compute_score(tree, [data[ii][j] for ii in range(i+1, n_rows)])
            if score != 0:
                score *= compute_score(tree, [data[i][jj] for jj in reversed(range(j))])
            if score != 0:
                score *= compute_score(tree, [data[i][jj] for jj in range(j+1, n_cols)])
            scores[i][j] = score

    return max([v for row in scores for v in row])


def compute_score(tree, others):
    score = 0
    for other in others:
        score += 1
        if other >= tree:
            break
    return score


if __name__ == "__main__":
    run(example_data, example_answer, parsing_config, solve)
