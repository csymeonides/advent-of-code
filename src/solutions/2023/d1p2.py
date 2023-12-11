import math

from utils import run, ParsingConfig, Example

example_answer = 281

example_data = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""


NUMBERS = [
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
]
DIGITS = [str(i) for i in range(1, 10)]


def _find_first_digit(line: str) -> str:
    first_index = math.inf
    first_digit = ""
    for digit in DIGITS:
        index = line.find(digit)
        if index != -1 and index < first_index:
            first_index = index
            first_digit = digit
    for i, num in enumerate(NUMBERS):
        index = line.find(num)
        if index != -1 and index < first_index:
            first_index = index
            first_digit = DIGITS[i]
    return first_digit


def _find_last_digit(line: str) -> str:
    last_index = -1
    last_digit = ""
    for digit in DIGITS:
        index = line.rfind(digit)
        if index != -1 and index > last_index:
            last_index = index
            last_digit = digit
    for i, num in enumerate(NUMBERS):
        index = line.rfind(num)
        if index != -1 and index > last_index:
            last_index = index
            last_digit = DIGITS[i]
    return last_digit


def get_digits(line: str) -> int:
    first_digit = _find_first_digit(line)
    last_digit = _find_last_digit(line)
    if not first_digit or not last_digit:
        raise ValueError(f"Invalid output: {first_digit} {last_digit} for line: {line}")
    return int(f"{first_digit}{last_digit}")


parsing_config = ParsingConfig(
    parser_func=get_digits,
    single_field=True,
)


def solve(data):
    return sum(data)


if __name__ == "__main__":
    run(
        examples=[Example(answer=example_answer, data=example_data)],
        parsing_config=parsing_config,
        solve=solve,
        real_answer=54824,
    )
