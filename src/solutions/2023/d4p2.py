import math
from typing import List, Tuple

from utils import run, ParsingConfig, Example

example_answer = 30

example_data = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""


class CardParser:
    def __init__(self):
        self.card_counts = {}
        self.max_id = 0

    def parse(self, *args) -> None:
        card_id = int(args[1].split(":")[0])
        self.max_id = card_id

        card_count = self.card_counts.get(card_id, 0) + 1
        self.card_counts[card_id] = card_count

        separator = args.index("|")
        winners = set(args[2:separator])
        mine = set(args[separator + 1:])
        my_winners = mine.intersection(winners)
        score = len(my_winners)

        for copy_id in range(card_id + 1, card_id + score + 1):
            self.card_counts[copy_id] = self.card_counts.get(copy_id, 0) + card_count


parsing_config = ParsingConfig(
    parser_class=CardParser,
)


def solve(parser: CardParser):
    return sum(card_count for card_id, card_count in parser.card_counts.items() if card_id <= parser.max_id)


if __name__ == "__main__":
    run(
        examples=[Example(answer=example_answer, data=example_data)],
        parsing_config=parsing_config,
        solve=solve,
        real_answer=5132675,
    )
