from utils import run, ParsingConfig, Example

example_answer = 230

example_data = """
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""


parsing_config = ParsingConfig(
    single_field=True,
)


def solve(data):
    return find_value(data, True) * find_value(data, False)


def find_value(data, most_common):
    i = 0
    while len(data) > 1:
        data = filter_values(data, i, most_common)
        i += 1
    return int(data[0], 2)


def filter_values(data, i, most_common):
    half_count = len(data) // 2
    ones = [line for line in data if line[i] == "1"]
    zeros = [line for line in data if line[i] == "0"]
    if len(zeros) > half_count:
        return zeros if most_common else ones
    else:
        return ones if most_common else zeros


if __name__ == "__main__":
    run([Example(answer=example_answer, data=example_data)], parsing_config, solve)
