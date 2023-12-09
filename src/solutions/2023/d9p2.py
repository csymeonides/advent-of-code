import math
from dataclasses import dataclass
from typing import List, Tuple

from utils import run, ParsingConfig

example_answer = 2

example_data = """
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""


parsing_config = ParsingConfig(
    value_converter=int,
)


def solve(lines: List[List[int]]) -> int:
    result = 0
    for line in lines:
        vals = line
        result += vals[0]
        multiplier = -1
        while any(v != 0 for v in vals):
            vals = [vals[i+1] - vals[i] for i in range(len(vals) - 1)]
            result = result + (vals[0] * multiplier)
            multiplier *= -1
    return result


if __name__ == "__main__":
    run(
        example_data=example_data,
        example_answer=example_answer,
        parsing_config=parsing_config,
        solve=solve,
        real_answer=864,
    )
