from utils import run, ParsingConfig, Example

example_answer = 3068

example_data = """
>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>
"""


parsing_config = ParsingConfig(
    field_separator="",
)


SHAPES = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],  # horizontal
    [(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)],  # cross
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],  # mirrored L
    [(0, 0), (0, 1), (0, 2), (0, 3)],  # vertical
    [(0, 0), (0, 1), (1, 0), (1, 1)],  # square
]


class Solver:
    def __init__(self, winds):
        self.winds = winds
        self.rocks = {(x, -1) for x in range(7)}
        self.shape_index = -1
        self.wind_index = -1
        self.next_rock = None
        self.record = []

    def solve(self):
        self.select_next_rock()
        while self.shape_index < 2022:
            self.wind_index += 1
            wind = self.winds[self.wind_index % len(self.winds)]
            blown_rock = {(x + (1 if wind == ">" else -1), y) for x, y in self.next_rock}
            if all(p not in self.rocks for p in blown_rock) and all(x in range(7) for x, y in blown_rock):
                self.next_rock = blown_rock

            fallen_rock = {(x, y - 1) for x, y in self.next_rock}
            if all(p not in self.rocks for p in fallen_rock):
                self.next_rock = fallen_rock
            else:
                self.rocks.update(self.next_rock)
                self.select_next_rock()

        return max(y for x, y in self.rocks) + 1

    def select_next_rock(self):
        max_y = max(y for x, y in self.rocks)
        self.shape_index += 1
        self.next_rock = {(x + 2, y + max_y + 4) for x, y in SHAPES[self.shape_index % len(SHAPES)]}

        # for y in range(max(y for x, y in self.next_rock), -1, -1):
        #     for x in range(7):
        #         if (x, y) in self.next_rock:
        #             print("@", end="")
        #         elif (x, y) in self.rocks:
        #             print("#", end="")
        #         else:
        #             print(".", end="")
        #     print()
        # print()


def solve(data):
    return Solver(data[0]).solve()


real_answer = 3127


if __name__ == "__main__":
    run([Example(answer=example_answer, data=example_data)], parsing_config, solve, real_answer)
