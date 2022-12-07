from src.utils import check_example_and_get_actual_answer, ParsingConfig

example_answer = None

example_data = """
"""


parsing_config = ParsingConfig(
    # parser_class=None,
    # parser_func=None,
    # field_separator=",",
    # value_converter=int,
    # single_field=True,
    # multi_line=True,
    # strip=False,
)


def solve(data):
    return len(data)


if __name__ == "__main__":
    check_example_and_get_actual_answer(example_data, example_answer, parsing_config, solve)
