from utils import run, ParsingConfig, Example, Example

examples = [
    Example(
        answer=None,
        data="""
"""
    )
]


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
        examples=examples,
        parsing_config=parsing_config,
        solve=solve,
        # wrong_answers=[],
        # real_answer=None,
    )
