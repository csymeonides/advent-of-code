from utils import run, ParsingConfig, Example, get_input_data

example_answer = 36

example_data = """
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
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
    n_knots = 9
    visited = {(0, 0)}
    hx, hy = 0, 0
    tail = [(0, 0) for _ in range(n_knots)]

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

            px, py = hx, hy
            for i in range(n_knots):
                tx, ty = tail[i]
                tail[i] = _follow(tx, ty, px, py)
                px, py = tail[i]
            visited.add(tail[-1])
    return len(visited)


real_answer = 2661


if __name__ == "__main__":
    run([Example(answer=example_answer, data=example_data)], parsing_config, solve, real_answer)
