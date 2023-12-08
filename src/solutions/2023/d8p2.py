import math
from dataclasses import dataclass
from typing import List, Tuple

from utils import run, ParsingConfig

example_answer = 6

example_data = """
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
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
    all_pos = [k for k in parser.left.keys() if k[-1] == "A"]
    all_steps = []
    for pos in all_pos:
        steps = 0
        while pos[-1] != "Z":
            if parser.instruction[steps % len(parser.instruction)] == "R":
                pos = parser.right[pos]
            else:
                pos = parser.left[pos]
            steps += 1
        all_steps.append(steps)
    return math.lcm(*all_steps)


if __name__ == "__main__":
    run(
        example_data=example_data,
        example_answer=example_answer,
        parsing_config=parsing_config,
        solve=solve,
        real_answer=15995167053923,
    )
