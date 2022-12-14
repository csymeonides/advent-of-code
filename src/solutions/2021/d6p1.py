from utils import run, ParsingConfig

example_answer = 5934

example_data = """
3,4,3,1,2
"""


parsing_config = ParsingConfig(
    field_separator=",",
    value_converter=int,
)


def solve(data):
    state = data[0]
    n_days = 80
    for _ in range(n_days):
        for i in range(len(state)):
            if state[i] == 0:
                state[i] = 6
                state.append(8)
            else:
                state[i] -= 1
    return len(state)


real_answer = None


if __name__ == "__main__":
    run(example_data, example_answer, parsing_config, solve, real_answer)
