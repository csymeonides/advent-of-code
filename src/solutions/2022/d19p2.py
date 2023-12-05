import math
from typing import List
from d19p1 import Blueprint, parsing_config

from utils import run

example_answer = 56 * 62

example_data = """
Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.
"""


MAX_MINUTES = 32


def solve(blueprints: List[Blueprint]) -> int:
    return math.prod(blueprint.get_max_geodes(MAX_MINUTES) for blueprint in blueprints[:3])


real_answer = None


if __name__ == "__main__":
    run(example_data, example_answer, parsing_config, solve, real_answer)
