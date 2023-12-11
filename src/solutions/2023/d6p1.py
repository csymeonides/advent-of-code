import math
from dataclasses import dataclass
from typing import List, Tuple

from utils import run, ParsingConfig, Example

example_answer = 288

example_data = """
Time:      7  15   30
Distance:  9  40  200
"""


class Parser:
    times: List[int]
    distances: List[int]

    def parse(self, *line):
        if "Time" in line[0]:
            self.times = [int(x) for x in line[1:]]
        else:
            self.distances = [int(x) for x in line[1:]]


parsing_config = ParsingConfig(
    parser_class=Parser,
)


def solve(parser: Parser):
    result = 1
    for time, best_distance in zip(parser.times, parser.distances):
        victories = 0
        for hold_time in range(time):
            distance = (time - hold_time) * hold_time
            if distance > best_distance:
                victories += 1
        result *= victories
    return result


if __name__ == "__main__":
    run(
        examples=[Example(answer=example_answer, data=example_data)],
        parsing_config=parsing_config,
        solve=solve,
        real_answer=505494,
    )
