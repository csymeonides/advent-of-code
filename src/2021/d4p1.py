from src.utils import run, ParsingConfig

example_answer = 4512

example_data = """
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""


class Bingo:
    def __init__(self):
        self.numbers = None

    def parse(self, record):
        if self.numbers:
            board = Board(record)
            for n in self.numbers:
                board.mark(n)
                if board.has_bingo():
                    break
            return board
        else:
            self.numbers = [int(n) for n in record[0][0].split(",")]
            return self.numbers


class Board:
    def __init__(self, grid):
        self.grid = [[int(n) for n in row] for row in grid]
        self.marks = [[False for _ in row] for row in grid]
        self.nums_to_win = 0
        self.last_num = 0

    def mark(self, n):
        self.nums_to_win += 1
        self.last_num = n
        for i, row in enumerate(self.grid):
            for j, val in enumerate(row):
                if val == n:
                    self.marks[i][j] = True

    def has_bingo(self):
        return any(all(row) for row in self.marks) or any(all(row[i] for row in self.marks) for i in range(len(self.marks[0])))

    def get_score(self):
        total_unmarked = sum(n for i, row in enumerate(self.grid) for j, n in enumerate(row) if not self.marks[i][j])
        return total_unmarked * self.last_num


parsing_config = ParsingConfig(
    parser_class=Bingo,
    multi_line=True,
)


def solve(data):
    winner = min(data[1:], key=lambda b: b.nums_to_win)
    return winner.get_score()


if __name__ == "__main__":
    run(example_data, example_answer, parsing_config, solve)
