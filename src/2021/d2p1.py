from src.utils import run, ParsingConfig

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


parsing_config = ParsingConfig(
    parser_class=Sub,
)


def solve(sub: Sub):
    return sub.x * sub.y


if __name__ == "__main__":
    run(example_data, example_answer, parsing_config, solve)
