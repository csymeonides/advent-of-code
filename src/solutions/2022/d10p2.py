from utils import run, ParsingConfig, Example

example_answer = """
##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....
"""

example_data = """
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
"""


def parse(_, num=None):
    if num is None:
        return 0, 1
    return num, 2


parsing_config = ParsingConfig(
    parser_func=parse,
    value_converter=[None, int],
)


def solve(data):
    x = 1
    i = 0
    crt = ""
    for clock in range(240):
        pos = clock % 40
        if pos == 0:
            crt += "\n"
        pixel = "#" if abs(pos-x) <= 1 else "."
        crt += pixel

        x_inc, ticks = data[i]
        if ticks > 1:
            data[i] = x_inc, ticks-1
        else:
            x += x_inc
            i += 1
    return crt + "\n"


real_answer = """
###..###....##.#....####.#..#.#....###..
#..#.#..#....#.#....#....#..#.#....#..#.
###..#..#....#.#....###..#..#.#....#..#.
#..#.###.....#.#....#....#..#.#....###..
#..#.#.#..#..#.#....#....#..#.#....#....
###..#..#..##..####.#.....##..####.#....
"""


if __name__ == "__main__":
    run([Example(answer=example_answer, data=example_data)], parsing_config, solve, real_answer)
