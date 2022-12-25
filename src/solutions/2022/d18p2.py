from utils import run, ParsingConfig

example_answer = 58

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
    parser_func=lambda *args: tuple(args),
    field_separator=",",
    value_converter=int,
)


def solve(data):
    total = 0
    min_x = min(x for x, _, _ in data)
    max_x = max(x for x, _, _ in data)
    min_y = min(y for _, y, _ in data)
    max_y = max(y for _, y, _ in data)
    min_z = min(z for _, _, z in data)
    max_z = max(z for _, _, z in data)
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            for z in range(min_z, max_z + 1):
                if (x, y, z) in data:
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


# 2040 too low
real_answer = None


if __name__ == "__main__":
    run(example_data, example_answer, parsing_config, solve, real_answer)
