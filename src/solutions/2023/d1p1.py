from utils import run, ParsingConfig

example_answer = 142

example_data = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""


def _safe_int(val: str) -> int:
    try:
        return int(val)
    except:
        return -1


def get_digits(*vals) -> int:
    valid_vals = [val for val in vals if val != -1]
    digits = f"{valid_vals[0]}{valid_vals[-1]}"
    return int(digits)


parsing_config = ParsingConfig(
    parser_func=get_digits,
    field_separator="",
    value_converter=_safe_int,
)


def solve(data):
    return sum(data)


if __name__ == "__main__":
    run(example_data, example_answer, parsing_config, solve)
