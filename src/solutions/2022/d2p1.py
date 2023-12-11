from typing import Dict

from utils import run, ParsingConfig, Example

example_answer = 15

example_data = """
A Y
B X
C Z
"""


ABC = "ABC"
XYZ = "XYZ"
RPS = ["R", "P", "S"]


def score(opponent, me):
    opp_index = ABC.index(opponent)
    my_index = XYZ.index(me)
    my_value = my_index + 1

    opp_choice = RPS[opp_index]
    my_choice = RPS[my_index]
    winner = RPS[(opp_index + 1) % 3]

    if opp_choice == my_choice:
        result = 3  # draw
    elif winner == my_choice:
        result = 6  # win
    else:
        result = 0  # loss

    return my_value + result


parsing_config = ParsingConfig(
    parser_func=score,
)


def solve(data):
    return sum(data)


if __name__ == "__main__":
    run([Example(answer=example_answer, data=example_data)], parsing_config, solve)
