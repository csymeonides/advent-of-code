from src.utils import check_example_and_get_actual_answer, ParsingConfig

example_answer = 5

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
        if start[X] == end[X]:
            x = start[X]
            for y in range(min(start[Y], end[Y]), max(start[Y], end[Y]) + 1):
                self.mark((x, y))
        elif start[Y] == end[Y]:
            y = start[Y]
            for x in range(min(start[X], end[X]), max(start[X], end[X]) + 1):
                self.mark((x, y))
        return self

    def mark(self, point):
        count = self.counts.get(point, 0)
        self.counts[point] = count + 1


parsing_config = ParsingConfig(
    parser_class=Board,
    field_separator=" -> ",
    value_converter=lambda val: tuple([int(n) for n in val.split(",")]),
)


def solve(data):
    counts = data[0].counts
    return len([_ for _, count in counts.items() if count >= 2])


if __name__ == "__main__":
    check_example_and_get_actual_answer(example_data, example_answer, parsing_config, solve)
