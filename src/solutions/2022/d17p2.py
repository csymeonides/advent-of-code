from utils import run, ParsingConfig

example_answer = 1514285714288

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
        self.max_ys = []
        self.mapping = {}
        self.target_shape_index = 1000000000000

    def solve(self):
        self.select_next_rock()
        while self.shape_index < self.target_shape_index:
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

        return self.max_ys[-1] + 1

    def select_next_rock(self):
        max_y = max(y for x, y in self.rocks)
        self.max_ys.append(max_y)
        self.shape_index += 1

        mapping_key = (self.shape_index % len(SHAPES), self.wind_index % len(self.winds))
        if mapping_key in self.mapping:
            max_y_diff = max_y - self.mapping[mapping_key][0]
            shape_index_diff = self.shape_index - self.mapping[mapping_key][1]
            remainder = (self.target_shape_index - self.shape_index) % shape_index_diff
            if remainder == 0:
                multiplier = (self.target_shape_index - self.shape_index) // shape_index_diff
                max_y += multiplier * max_y_diff
                self.shape_index += multiplier * shape_index_diff
                self.max_ys.append(max_y)
            else:
                print(f"NOPE! {self.shape_index=} {self.wind_index=} {max_y=}")
        else:
            self.mapping[mapping_key] = (max_y, self.shape_index)
            print(f"{self.shape_index=} {self.wind_index=} {max_y=}")

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


real_answer = 1542941176480


if __name__ == "__main__":
    run(example_data, example_answer, parsing_config, solve, real_answer)
