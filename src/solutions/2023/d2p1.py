import math

from utils import run, ParsingConfig, Example

example_answer = 8

example_data = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""


LIMITS = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def parse(*args) -> int:
    id_ = int(args[1].split(":")[0])
    i = 2
    while i < len(args):
        count = int(args[i])
        colour = args[i+1]
        if i + 2 < len(args):
            colour = colour[:-1]
        if count > LIMITS[colour]:
            return 0
        i += 2
    return id_


parsing_config = ParsingConfig(
    parser_func=parse,
)


def solve(data):
    return sum(data)


if __name__ == "__main__":
    run(
        examples=[Example(answer=example_answer, data=example_data)],
        parsing_config=parsing_config,
        solve=solve,
        # real_answer=54824,
    )
