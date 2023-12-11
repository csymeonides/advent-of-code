from utils import run, ParsingConfig, Example

example_answer = 24000

example_data = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""


parsing_config = ParsingConfig(
    parser_func=sum,
    value_converter=int,
    multi_line=True,
    single_field=True,
)


def solve(data):
    return max(data)


if __name__ == "__main__":
    run([Example(answer=example_answer, data=example_data)], parsing_config, solve)
