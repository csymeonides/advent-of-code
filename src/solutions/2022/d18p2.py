from utils import run, ParsingConfig, Example
from utils.utils import to_tuple

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
    parser_func=to_tuple,
    field_separator=",",
    value_converter=int,
)


# Pretty much a copy of https://github.com/silentw0lf/advent_of_code_2022/blob/main/18/solve.py
def solve(data):
    total = 0

    # min/max bounds + 1 point out
    min_x = min(x for x, _, _ in data) - 1
    max_x = max(x for x, _, _ in data) + 1
    min_y = min(y for _, y, _ in data) - 1
    max_y = max(y for _, y, _ in data) + 1
    min_z = min(z for _, _, z in data) - 1
    max_z = max(z for _, _, z in data) + 1

    # Breadth-first search
    queue = [(min_x, min_y, min_z)]
    seen = set()
    while queue:
        (x, y, z) = queue.pop(0)

        # If I can "touch" lava from this point, it counts as outer area
        if (x, y, z) in data:
            total += 1

        # Else mark this point as "seen" and add all within-bound neighbours to the search
        elif (x, y, z) not in seen:
            seen.add((x, y, z))
            for neighbour in [
                (x+1, y, z),
                (x-1, y, z),
                (x, y+1, z),
                (x, y-1, z),
                (x, y, z+1),
                (x, y, z-1),
            ]:
                if neighbour not in seen and min_x <= neighbour[0] <= max_x and min_y <= neighbour[1] <= max_y and min_z <= neighbour[2] <= max_z:
                    queue.append(neighbour)
    return total


real_answer = 2074


if __name__ == "__main__":
    run([Example(answer=example_answer, data=example_data)], parsing_config, solve, real_answer)
