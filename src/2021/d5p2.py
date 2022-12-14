from src.utils import run, ParsingConfig

example_answer = 12

example_data = """
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""


X = 0
Y = 1


class Board:
    def __init__(self):
        self.counts = {}

    def parse(self, start, end):
        x, y = start
        x_end, y_end = end

        x_inc = 0 if x == x_end else 1 if x < x_end else -1
        y_inc = 0 if y == y_end else 1 if y < y_end else -1

        while True:
            self.mark((x, y))
            if (x, y) == end:
                break
            x += x_inc
            y += y_inc

    def mark(self, point):
        count = self.counts.get(point, 0)
        self.counts[point] = count + 1


parsing_config = ParsingConfig(
    parser_class=Board,
    field_separator=" -> ",
    value_converter=lambda val: tuple([int(n) for n in val.split(",")]),
)


def solve(board: Board):
    counts = board.counts
    return len([_ for _, count in counts.items() if count >= 2])


if __name__ == "__main__":
    run(example_data, example_answer, parsing_config, solve)
