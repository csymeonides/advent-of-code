from utils import run, ParsingConfig, Example

example_answer = 70

example_data = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""


def find_common_element(group):
    sets = [set(sack) for sack in group]
    element = set.intersection(*sets).pop()
    return get_value(element)


def get_value(char: str):
    if char.lower() == char:
        return ord(char) - ord("a") + 1
    else:
        return ord(char) - ord("A") + 27


parsing_config = ParsingConfig(
    parser_func=find_common_element,
    multi_line=3,
    single_field=True,
)


def solve(data):
    return sum(data)


if __name__ == "__main__":
    run([Example(answer=example_answer, data=example_data)], parsing_config, solve)
