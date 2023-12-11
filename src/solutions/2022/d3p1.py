from utils import run, ParsingConfig, Example

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
    parser_func=get_overlap_priority,
)


def solve(data):
    return sum(data)


if __name__ == "__main__":
    run([Example(answer=example_answer, data=example_data)], parsing_config, solve)
