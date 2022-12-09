from typing import Dict

from src.utils import run, ParsingConfig

example_answer = 45000

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
    return sum(sorted(data)[-3:])


if __name__ == "__main__":
    run(example_data, example_answer, parsing_config, solve)
