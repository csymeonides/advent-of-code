from utils import run, ParsingConfig

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
    run(
        example_data=example_data,
        example_answer=example_answer,
        parsing_config=parsing_config,
        solve=solve,
        # real_answer=None,
    )
