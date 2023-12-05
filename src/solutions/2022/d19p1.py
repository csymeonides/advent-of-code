from dataclasses import dataclass
from typing import List

from utils import run, ParsingConfig
from utils.utils import to_tuple

example_answer = 33

example_data = """
Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.
"""


MAX_MINUTES = 24


@dataclass
class Cost:
    ore: int = 0
    clay: int = 0
    obsidian: int = 0


@dataclass(frozen=True)
class Robots:
    ore: int = 0
    clay: int = 0
    obsidian: int = 0
    geodes: int = 0


@dataclass(frozen=True)
class State:
    ore: int = 0
    clay: int = 0
    obsidian: int = 0
    geodes: int = 0
    robots: Robots = Robots()
    minutes_remaining: int = 0

    def calc_harvest(self):
        return State(
            ore=self.ore + self.robots.ore,
            clay=self.clay + self.robots.clay,
            obsidian=self.obsidian + self.robots.obsidian,
            geodes=self.geodes + self.robots.geodes,
            robots=self.robots,
            minutes_remaining=self.minutes_remaining - 1,
        )

    def can_afford(self, cost: Cost) -> bool:
        return cost.ore <= self.ore and cost.clay <= self.clay and cost.obsidian <= self.obsidian

    def after_buying(self, cost: Cost, purchase: Robots):
        state = self
        while not state.can_afford(cost) and state.minutes_remaining:
            state = state.calc_harvest()
        if not state.minutes_remaining:
            return None
        return State(
            ore=state.ore - cost.ore + state.robots.ore,
            clay=state.clay - cost.clay + state.robots.clay,
            obsidian=state.obsidian - cost.obsidian + state.robots.obsidian,
            geodes=state.geodes + state.robots.geodes,
            robots=Robots(
                ore=state.robots.ore + purchase.ore,
                clay=state.robots.clay + purchase.clay,
                obsidian=state.robots.obsidian + purchase.obsidian,
                geodes=state.robots.geodes + purchase.geodes,
            ),
            minutes_remaining=state.minutes_remaining - 1,
        )

    @property
    def max_geodes(self) -> int:
        return self.geodes + (self.robots.geodes * self.minutes_remaining)

    @property
    def max_possible_geodes(self) -> int:
        # Ripped off from https://github.com/marcodelmastro/AdventOfCode2022/blob/main/Day19.ipynb
        result = self.geodes
        for i in range(self.minutes_remaining):
            result += (self.robots.geodes + i) * (self.minutes_remaining - i)
        return result


@dataclass
class Blueprint:
    id_: int
    ore_cost: Cost
    clay_cost: Cost
    obsidian_cost: Cost
    geode_cost: Cost

    def quality_level(self, max_minutes: int) -> int:
        return self.id_ * self.get_max_geodes(max_minutes)

    def get_max_geodes(self, max_minutes: int) -> int:
        max_geodes = 0
        queue = [State(robots=Robots(ore=1), minutes_remaining=max_minutes)]
        seen = set()
        while queue:
            state = queue.pop(0)
            seen.add(state)
            if state.max_geodes > max_geodes:
                max_geodes = state.max_geodes
            queue.extend([s for s in self.generate_next_states(state) if s not in seen and s.max_possible_geodes >= max_geodes])
        return max_geodes

    def generate_next_states(self, prev_state: State) -> List[State]:
        # "needs" optimization ripped off from https://github.com/marcodelmastro/AdventOfCode2022/blob/main/Day19.ipynb and https://pastebin.com/KDTmtHCk
        states = []
        buy_geode = prev_state.after_buying(self.geode_cost, Robots(geodes=1))
        if buy_geode:
            states.append(buy_geode)
        if self.needs_obsidian(prev_state):
            buy_obsidian = prev_state.after_buying(self.obsidian_cost, Robots(obsidian=1))
            if buy_obsidian:
                states.append(buy_obsidian)
        if self.needs_clay(prev_state):
            buy_clay = prev_state.after_buying(self.clay_cost, Robots(clay=1))
            if buy_clay:
                states.append(buy_clay)
        if self.needs_ore(prev_state):
            buy_ore = prev_state.after_buying(self.ore_cost, Robots(ore=1))
            if buy_ore:
                states.append(buy_ore)
        return states

    def needs_ore(self, state: State) -> bool:
        return state.robots.ore < max(self.ore_cost.ore, self.clay_cost.ore, self.obsidian_cost.ore, self.geode_cost.ore) and not state.robots.obsidian and state.robots.clay <= 3

    def needs_clay(self, state: State) -> bool:
        return state.robots.clay < self.obsidian_cost.clay and not state.robots.geodes and state.robots.obsidian <= 3

    def needs_obsidian(self, state: State) -> bool:
        return state.robots.obsidian < self.geode_cost.obsidian


def _parse_cost(sentence: str) -> Cost:
    cost = Cost()
    words = sentence.split("costs")[1].replace(".", "").split()
    if "ore" in words:
        cost.ore = int(words[words.index("ore") - 1])
    if "clay" in words:
        cost.clay = int(words[words.index("clay") - 1])
    if "obsidian" in words:
        cost.obsidian = int(words[words.index("obsidian") - 1])
    return cost


def _make_blueprint(*args) -> Blueprint:
    id_ = int(args[0].split()[1])
    ore_cost = _parse_cost(args[1])
    clay_cost = _parse_cost(args[2])
    obsidian_cost = _parse_cost(args[3])
    geode_cost = _parse_cost(args[4])
    return Blueprint(id_=id_, ore_cost=ore_cost, clay_cost=clay_cost, obsidian_cost=obsidian_cost, geode_cost=geode_cost)


parsing_config = ParsingConfig(
    field_separator=r": |\. ",
    parser_func=_make_blueprint,
)


def solve(blueprints: List[Blueprint]) -> int:
    return sum(blueprint.quality_level(MAX_MINUTES) for blueprint in blueprints)


real_answer = 1009


if __name__ == "__main__":
    run(example_data, example_answer, parsing_config, solve, real_answer)
