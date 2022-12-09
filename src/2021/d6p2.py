from src.utils import run, ParsingConfig

example_answer = 26984457539

example_data = """
3,4,3,1,2
"""


parsing_config = ParsingConfig(
    # parser_class=None,
    # parser_func=None,
    field_separator=",",
    value_converter=int,
    # single_field=True,
    # multi_line=True,
    # strip=False,
)


def solve(data):
    state = [len([n for n in data[0] if i == n]) for i in range(7)] + [0, 0]
    n_days = 256
    for _ in range(n_days):
        zeros = state[0]
        for i in range(8):
            state[i] = state[i+1]
        state[8] = zeros
        state[6] += zeros
    return sum(state)


real_answer = None


if __name__ == "__main__":
    run(example_data, example_answer, parsing_config, solve, real_answer)
