import math
from dataclasses import dataclass
from typing import List, Tuple

from utils import run, ParsingConfig, Example

example_answer = 6

example_data = """
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""


class Parser:
    def __init__(self):
        self.instruction = ""
        self.left = {}
        self.right = {}

    def parse(self, *line):
        if not line:
            return
        if len(line) == 1:
            self.instruction = line[0]
        else:
            self.left[line[0]] = line[2][1:4]
            self.right[line[0]] = line[3][:3]


parsing_config = ParsingConfig(
    parser_class=Parser,
)


def solve(parser):
    pos = "AAA"
    steps = 0
    while pos != "ZZZ":
        if parser.instruction[steps % len(parser.instruction)] == "R":
            pos = parser.right[pos]
        else:
            pos = parser.left[pos]
        steps += 1
    return steps


if __name__ == "__main__":
    run(
        examples=[Example(answer=example_answer, data=example_data)],
        parsing_config=parsing_config,
        solve=solve,
        real_answer=20513,
    )
