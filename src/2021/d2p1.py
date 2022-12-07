from src.utils import check_example_and_get_actual_answer, ParsingConfig

example_answer = 150

example_data = """
forward 5
down 5
forward 8
up 3
down 8
forward 2
"""


class Sub:
    def __init__(self):
        self.x = 0
        self.y = 0

    def parse(self, direction, distance_str):
        distance = int(distance_str)
        if direction == "forward":
            self.x += distance
        elif direction == "up":
            self.y -= distance
        else:
            self.y += distance
        return self.x, self.y


parsing_config = ParsingConfig(
    parser_class=Sub,
)


def solve(data):
    (x, y) = data[-1]
    return x * y


if __name__ == "__main__":
    check_example_and_get_actual_answer(example_data, example_answer, parsing_config, solve)
