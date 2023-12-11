import math

from utils import run, ParsingConfig, Example

example_answer = 93

example_data = """
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
"""


class Cave:
    def __init__(self):
        self.min_x = math.inf
        self.max_x = -math.inf
        self.max_y = -math.inf
        self.occupied = set()

    def parse(self, *data):
        points = [tuple(int(n) for n in p.split(",")) for p in data]
        px, py = points[0]
        self.occupied.add((px, py))
        for x, y in points:
            self.min_x = min(self.min_x, x)
            self.max_x = max(self.max_x, x)
            self.max_y = max(self.max_y, y)
            while px != x or py != y:
                if px > x:
                    px -= 1
                elif px < x:
                    px += 1
                elif py < y:
                    py += 1
                else:
                    py -= 1
                self.occupied.add((px, py))
            px, py = x, y

    def move(self, sand):
        x, y = sand
        new_sand = (x, y + 1)
        if new_sand in self.occupied:
            new_sand = (x - 1, y + 1)
            if new_sand in self.occupied:
                new_sand = (x + 1, y + 1)
                if new_sand in self.occupied:
                    return sand
        return new_sand

    def add(self, sand):
        self.occupied.add(sand)


parsing_config = ParsingConfig(
    parser_class=Cave,
    field_separator=" -> ",
)


def solve(cave: Cave):
    finished = False
    count = 0
    while not finished:
        sand = (500, 0)
        while True:
            new_sand = cave.move(sand)
            if new_sand == (500, 0):
                finished = True
                count += 1
                break
            elif new_sand == sand or new_sand[1] == cave.max_y + 1:
                cave.add(new_sand)
                count += 1
                break
            else:
                sand = new_sand

    return count


real_answer = 32041


if __name__ == "__main__":
    run([Example(answer=example_answer, data=example_data)], parsing_config, solve, real_answer)
