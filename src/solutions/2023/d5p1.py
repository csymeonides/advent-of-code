import math
from dataclasses import dataclass
from typing import List, Tuple

from utils import run, ParsingConfig, Example

example_answer = 35

example_data = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""


@dataclass
class Mapping:
    dest_start: int
    source_start: int
    range_length: int


def _make_mapping(strings: List[str]) -> Mapping:
    return Mapping(*[int(s) for s in strings])


class Mapper:
    def __init__(self):
        self.seeds = []
        self.mappings = {}

    def parse(self, lines: List[List[str]]):
        if lines[0][0] == "seeds:":
            self.seeds = [int(x) for x in lines[0][1:]]
        else:
            map_type = lines[0][0]
            mappings = [_make_mapping(line) for line in lines[1:]]
            self.mappings[map_type] = mappings

    def map(self, map_type: str, source: int) -> int:
        for mapping in self.mappings[map_type]:
            diff = source - mapping.source_start
            if 0 <= diff < mapping.range_length:
                return mapping.dest_start + diff
        return source


parsing_config = ParsingConfig(
    parser_class=Mapper,
    multi_line=True,
)


def solve(mapper: Mapper):
    min_location = math.inf
    for seed in mapper.seeds:
        soil = mapper.map("seed-to-soil", seed)
        fertilizer = mapper.map("soil-to-fertilizer", soil)
        water = mapper.map("fertilizer-to-water", fertilizer)
        light = mapper.map("water-to-light", water)
        temperature = mapper.map("light-to-temperature", light)
        humidity = mapper.map("temperature-to-humidity", temperature)
        location = mapper.map("humidity-to-location", humidity)
        min_location = min(min_location, location)
    return min_location


if __name__ == "__main__":
    run(
        examples=[Example(answer=example_answer, data=example_data)],
        parsing_config=parsing_config,
        solve=solve,
        real_answer=278755257,
    )
