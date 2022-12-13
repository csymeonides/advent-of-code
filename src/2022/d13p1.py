from src.utils import run, ParsingConfig

example_answer = 13

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
    multi_line=True,
    single_field=True,
)


def get_ordering(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return right - left

    elif isinstance(left, list) and isinstance(right, list):
        i = 0
        while i < max(len(left), len(right)):
            if i == len(left):
                return 1
            elif i == len(right):
                return -1
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
    total = 0
    for i, pair in enumerate(data):
        if get_ordering(*pair) >= 0:
            total += i + 1
    return total


real_answer = 5684


if __name__ == "__main__":
    run(example_data, example_answer, parsing_config, solve, real_answer)
