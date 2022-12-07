from src.utils import check_example_and_get_actual_answer, ParsingConfig

example_answer = 157

example_data = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""


def get_overlap_priority(contents):
    size = len(contents) // 2
    first = set(contents[:size])
    second = set(contents[size:])
    overlap = first.intersection(second)
    return get_value(overlap.pop())


def get_value(char: str):
    if char.lower() == char:
        return ord(char) - ord("a") + 1
    else:
        return ord(char) - ord("A") + 27


parsing_config = ParsingConfig(
    # parser_class=None,
    parser_func=get_overlap_priority,
    # field_separator=",",
    # value_converter=int,
    # single_field=True,
    # multi_line=True,
    # strip=False,
)


def solve(data):
    return sum(data)


if __name__ == "__main__":
    check_example_and_get_actual_answer(example_data, example_answer, parsing_config, solve)
