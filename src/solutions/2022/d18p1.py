from utils import run, ParsingConfig
from utils.utils import to_tuple

example_answer = 64

example_data = """
2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5
"""


parsing_config = ParsingConfig(
    parser_func=to_tuple,
    field_separator=",",
    value_converter=int,
)


def solve(data):
    total = 0
    for (x, y, z) in data:
        if (x + 1, y, z) not in data:
            total += 1
        if (x - 1, y, z) not in data:
            total += 1
        if (x, y + 1, z) not in data:
            total += 1
        if (x, y - 1, z) not in data:
            total += 1
        if (x, y, z + 1) not in data:
            total += 1
        if (x, y, z - 1) not in data:
            total += 1
    return total


real_answer = 3522


if __name__ == "__main__":
    run(example_data, example_answer, parsing_config, solve, real_answer)
