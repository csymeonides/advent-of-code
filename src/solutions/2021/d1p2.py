from utils import run, ParsingConfig, Example

example_answer = 5

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
    for i in range(len(data) - 3):
        if sum(data[i:i+3]) < sum(data[i+1:i+4]):
            total += 1
    return total


if __name__ == "__main__":
    run([Example(answer=example_answer, data=example_data)], parsing_config, solve)
