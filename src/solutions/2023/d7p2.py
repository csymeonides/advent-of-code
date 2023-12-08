from itertools import combinations_with_replacement
from dataclasses import dataclass
from typing import List

from utils import run, ParsingConfig

example_answer = 5905

example_data = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""

ORDERED_CARDS = "J23456789TQKA"
ORDERED_HANDS = ["high card", "one pair", "two pair", "three of a kind", "full house", "four of a kind", "five of a kind"]


def _cards_value(cards: str) -> int:
    result = 0
    multiplier = 1
    for card in cards:
        result += multiplier * ORDERED_CARDS.index(card)
        multiplier *= 13
    return result


def _hand_type(cards: str) -> str:
    card_counts = [cards.count(card) for card in ORDERED_CARDS]

    if any(count == 5 for count in card_counts):
        return "five of a kind"
    if any(count == 4 for count in card_counts):
        return "four of a kind"

    three_of_a_kind = next((card for i, card in enumerate(ORDERED_CARDS) if card_counts[i] == 3), None)
    if three_of_a_kind:
        pair = next((card for i, card in enumerate(ORDERED_CARDS) if card_counts[i] == 2 and card != three_of_a_kind), None)
        if pair:
            return "full house"
        else:
            return "three of a kind"

    pairs = [card for i, card in enumerate(ORDERED_CARDS) if card_counts[i] == 2]
    if len(pairs) == 2:
        return "two pair"
    elif len(pairs) == 1:
        return "one pair"

    return "high card"


def _best_hand_type(cards: str) -> str:
    best_hand_type = _hand_type(cards)
    joker_count = len([c for c in cards if c == "J"])
    non_jokers = [c for c in cards if c != "J"]
    non_joker_set = set(non_jokers)
    for joker_allocation in combinations_with_replacement(non_joker_set, joker_count):
        new_cards = "".join(non_jokers + list(joker_allocation))
        new_hand_type = _hand_type(new_cards)
        if ORDERED_HANDS.index(new_hand_type) > ORDERED_HANDS.index(best_hand_type):
            best_hand_type = new_hand_type
    return best_hand_type


def _to_base_13(values: List[int]) -> int:
    result = 0
    for i, value in enumerate(reversed(values)):
        result += value * (13 ** i)
    return result


@dataclass
class Hand:
    cards: str
    bid: int

    @property
    def value(self):
        card_values = [ORDERED_CARDS.index(card) for card in self.cards]
        hand_type_value = ORDERED_HANDS.index(_best_hand_type(self.cards))
        return _to_base_13([hand_type_value] + card_values)


def _make_hand(cards: str, bid_string: str) -> Hand:
    return Hand(cards=cards, bid=int(bid_string))


parsing_config = ParsingConfig(
    parser_func=_make_hand,
)


def solve(hands: List[Hand]):
    sorted_hands = sorted(hands, key=lambda h: h.value)
    return sum(hand.bid * (rank + 1) for rank, hand in enumerate(sorted_hands))


if __name__ == "__main__":
    run(
        example_data=example_data,
        example_answer=example_answer,
        parsing_config=parsing_config,
        solve=solve,
        wrong_answers=[
            254423099,  # too high
        ],
        real_answer=253907829,
    )
