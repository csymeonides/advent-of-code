from utils import run, ParsingConfig

example_answer = 198

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
    gamma = ""
    epsilon = ""
    half_count = len(data) // 2
    for i in range(len(data[0])):
        ones = len([1 for line in data if line[i] == "1"])
        if ones > half_count:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    return int(gamma, 2) * int(epsilon, 2)


if __name__ == "__main__":
    run(example_data, example_answer, parsing_config, solve)
