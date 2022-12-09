from typing import Dict

from src.utils import run, ParsingConfig

example_answer = 12

example_data = """
A Y
B X
C Z
"""


ABC = "ABC"
XYZ = "XYZ"
RPS = ["R", "P", "S", "R"]


def score(opponent, me):
    opp_index = ABC.index(opponent)

    if me == "X":
        my_index = (opp_index - 1) % 3
    elif me == "Y":
        my_index = opp_index
    else:
        my_index = (opp_index + 1) % 3

    my_value = my_index + 1
    return my_value + (XYZ.index(me) * 3)


parsing_config = ParsingConfig(
    parser_func=score,
)


def solve(data):
    return sum(data)


if __name__ == "__main__":
    run(example_data, example_answer, parsing_config, solve)
