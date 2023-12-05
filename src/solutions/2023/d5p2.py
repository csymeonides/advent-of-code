import math
from dataclasses import dataclass
from typing import List, Tuple, Optional

from utils import run, ParsingConfig

example_answer = 46

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


Range = Tuple[int, int]
Ranges = List[Tuple[int, int]]


@dataclass
class Mapping:
    dest_start: int
    source_start: int
    range_length: int


def _make_mapping(strings: List[str]) -> Mapping:
    return Mapping(*[int(s) for s in strings])


def _insert_range(new_range: Range, ranges: Ranges) -> None:
    new_start, new_length = new_range
    new_end = new_start + new_length
    for i, (start, length) in enumerate(ranges):
        end = start + length
        if new_start > end:  # new range is past this range -> skip
            continue
        if new_end < start:  # new range is before this range -> insert
            ranges.insert(i, new_range)
            return
        # There is overlap -> combine
        ranges[i] = (min(start, new_start), max(end, new_end) - min(start, new_start))
        return
    # no matching range found -> append
    ranges.append(new_range)


class Mapper:
    def __init__(self):
        self.seeds = []
        self.mappings = {}

    def parse(self, lines: List[List[str]]):
        if lines[0][0] == "seeds:":
            seed_vals = lines[0][1:]
            seed_ranges = [(int(seed_vals[i]), int(seed_vals[i+1])) for i in range(0, len(seed_vals), 2)]
            self.seeds = sorted(seed_ranges, key=lambda r: r[0])
        else:
            map_type = lines[0][0]
            mappings = [_make_mapping(line) for line in lines[1:]]
            self.mappings[map_type] = sorted(mappings, key=lambda m: m.source_start)

    def map(self, map_type: str, source_ranges: Ranges) -> Ranges:
        dest_ranges = []
        for source_range in source_ranges:
            remainder = source_range
            for mapping in self.mappings[map_type]:
                new_dest_ranges, remainder = self._map_range(mapping, remainder)
                for new_dest_range in new_dest_ranges:
                    _insert_range(new_dest_range, dest_ranges)
                if not remainder:
                    break
            if remainder:
                _insert_range(remainder, dest_ranges)
        return dest_ranges

    def _map_range(self, mapping: Mapping, source_range: Range) -> Tuple[Ranges, Optional[Range]]:
        source_start, source_length = source_range
        source_end = source_start + source_length
        mapping_end = mapping.source_start + mapping.range_length
        if source_start > mapping_end:  # source starts after mapping -> all remainder
            return [], source_range
        elif source_end < mapping.source_start:  # source ends before mapping -> all dest
            return [source_range], None
        # source overlaps with mapping
        dest_ranges = []
        remainder = None
        if source_start < mapping.source_start:
            dest_ranges.append((source_start, mapping.source_start - source_start))
            dest_start = mapping.dest_start
        else:
            dest_start = mapping.dest_start + (source_start - mapping.source_start)
        if source_end > mapping_end:
            remainder = (mapping_end, source_end - mapping_end)
            dest_end = mapping.dest_start + mapping.range_length
        else:
            dest_end = dest_start + source_length
        dest_ranges.append((dest_start, dest_end - dest_start))
        return dest_ranges, remainder


parsing_config = ParsingConfig(
    parser_class=Mapper,
    multi_line=True,
)


def solve(mapper: Mapper):
    soil_ranges = mapper.map("seed-to-soil", mapper.seeds)
    fertilizer_ranges = mapper.map("soil-to-fertilizer", soil_ranges)
    water_ranges = mapper.map("fertilizer-to-water", fertilizer_ranges)
    light_ranges = mapper.map("water-to-light", water_ranges)
    temperature_ranges = mapper.map("light-to-temperature", light_ranges)
    humidity_ranges = mapper.map("temperature-to-humidity", temperature_ranges)
    location_ranges = mapper.map("humidity-to-location", humidity_ranges)
    return location_ranges[0][0]


if __name__ == "__main__":
    run(
        example_data=example_data,
        example_answer=example_answer,
        parsing_config=parsing_config,
        solve=solve,
        real_answer=26829166,
    )
