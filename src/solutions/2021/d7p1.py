from utils import run, ParsingConfig

example_answer = 37

example_data = """
16,1,2,0,4,2,7,1,2,14
"""


parsing_config = ParsingConfig(
    field_separator=",",
    value_converter=int,
)


def _get_cost(i, pos):
    return sum(abs(p - i) for p in pos)


def solve(data):
    pos = data[0]
    costs = [_get_cost(i, pos) for i in range(min(pos), max(pos) + 1)]
    return min(costs)


real_answer = None


if __name__ == "__main__":
    run(example_data, example_answer, parsing_config, solve, real_answer)
