import math
from dataclasses import dataclass
from typing import List, Tuple

from utils import run, ParsingConfig

example_answer = 71503

example_data = """
Time:      7  15   30
Distance:  9  40  200
"""


class Parser:
    time: int
    distance: int

    def parse(self, *line):
        if "Time" in line[0]:
            self.time = int("".join(line[1:]))
        else:
            self.distance = int("".join(line[1:]))


parsing_config = ParsingConfig(
    parser_class=Parser,
)


def solve(parser: Parser):
    result = 0
    for hold_time in range(parser.time):
        distance = (parser.time - hold_time) * hold_time
        if distance > parser.distance:
            result += 1
    return result


if __name__ == "__main__":
    run(
        example_data=example_data,
        example_answer=example_answer,
        parsing_config=parsing_config,
        solve=solve,
        real_answer=23632299,
    )
