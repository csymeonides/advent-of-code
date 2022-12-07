from typing import Dict

from src.utils import check_example_and_get_actual_answer, ParsingConfig

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
    check_example_and_get_actual_answer(example_data, example_answer, parsing_config, solve)
