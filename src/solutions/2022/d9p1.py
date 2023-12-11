from utils import run, ParsingConfig, Example, get_input_data

example_answer = 13

example_data = """
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""


parsing_config = ParsingConfig(
    value_converter=[None, int],
)


def _follow(tx, ty, hx, hy):
    if tx == hx:
        if ty < hy-1:
            ty += 1
        elif ty > hy+1:
            ty -= 1
    elif ty == hy:
        if tx < hx-1:
            tx += 1
        elif tx > hx+1:
            tx -= 1
    elif abs(hy-ty) + abs(hx-tx) > 2:
        tx += 1 if tx < hx else -1
        ty += 1 if ty < hy else -1
    return tx, ty


def solve(data):
    visited = {(0, 0)}
    hx, hy = 0, 0
    tx, ty = 0, 0

    for record in data:
        [direction, distance] = record
        for _ in range(distance):
            if direction == "U":
                hy += 1
            elif direction == "D":
                hy -= 1
            elif direction == "L":
                hx -= 1
            else:
                hx += 1
            tx, ty = _follow(tx, ty, hx, hy)
            visited.add((tx, ty))
    return len(visited)


real_answer = 6284


if __name__ == "__main__":
    run([Example(answer=example_answer, data=example_data)], parsing_config, solve, real_answer)
