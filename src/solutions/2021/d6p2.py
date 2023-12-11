from utils import run, ParsingConfig, Example

example_answer = 26984457539

example_data = """
3,4,3,1,2
"""


parsing_config = ParsingConfig(
    field_separator=",",
    value_converter=int,
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
    run([Example(answer=example_answer, data=example_data)], parsing_config, solve, real_answer)
