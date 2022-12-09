from src.utils import run, ParsingConfig

example_answer = 900

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
        self.aim = 0

    def parse(self, direction, distance_str):
        distance = int(distance_str)
        if direction == "forward":
            self.x += distance
            self.y += self.aim * distance
        elif direction == "up":
            self.aim -= distance
        else:
            self.aim += distance
        return self.x, self.y


parsing_config = ParsingConfig(
    parser_class=Sub,
)


def solve(data):
    (x, y) = data[-1]
    return x * y


if __name__ == "__main__":
    run(example_data, example_answer, parsing_config, solve)
