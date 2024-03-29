from utils import run, ParsingConfig, Example

example_answer = 2

example_data = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""


def make_tuple(value: str):
    return tuple([int(val) for val in value.split("-")])


def has_overlap(first: tuple, second: tuple):
    return first[0] <= second[0] and first[1] >= second[1]


parsing_config = ParsingConfig(
    field_separator=",",
    value_converter=make_tuple,
)


def solve(data):
    items_with_overlap = [
        1
        for (first, second) in data
        if has_overlap(first, second) or has_overlap(second, first)
    ]
    return len(items_with_overlap)


if __name__ == "__main__":
    run([Example(answer=example_answer, data=example_data)], parsing_config, solve)
