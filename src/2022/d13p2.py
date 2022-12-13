import math
from functools import cmp_to_key

from src.utils import run, ParsingConfig

example_answer = 140

example_data = """
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
"""


parsing_config = ParsingConfig(
    value_converter=eval,
    single_field=True,
)


def get_ordering(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return left - right

    elif isinstance(left, list) and isinstance(right, list):
        i = 0
        while i < max(len(left), len(right)):
            if i == len(left):
                return -1
            elif i == len(right):
                return 1
            else:
                ordering = get_ordering(left[i], right[i])
                if ordering != 0:
                    return ordering
            i += 1
        return 0

    elif isinstance(left, int):
        return get_ordering([left], right)
    else:
        return get_ordering(left, [right])


def solve(data):
    dividers = [[[2]], [[6]]]
    sorted_data = sorted(data + dividers, key=cmp_to_key(get_ordering))
    divider_indices = [sorted_data.index(d) + 1 for d in dividers]
    return math.prod(divider_indices)


real_answer = 22932


if __name__ == "__main__":
    run(example_data, example_answer, parsing_config, solve, real_answer)
