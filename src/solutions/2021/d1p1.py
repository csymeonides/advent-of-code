from utils import run, ParsingConfig, Example

example_answer = 7

example_data = """
199
200
208
210
200
207
240
269
260
263
"""


parsing_config = ParsingConfig(
    value_converter=int,
    single_field=True,
)


def solve(data):
    total = 0
    for i, d in enumerate(data[:-1]):
        if d < data[i+1]:
            total += 1
    return total


if __name__ == "__main__":
    run([Example(answer=example_answer, data=example_data)], parsing_config, solve)
