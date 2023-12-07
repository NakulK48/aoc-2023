from __future__ import annotations
from collections import Counter
from dataclasses import dataclass
from enum import IntEnum
from typing import TypeAlias

import utils


def card_value(card: str, joker: bool = False) -> int:
    if card.isdigit():
        return int(card)
    return {"T": 10, "J": 0 if joker else 11, "Q": 12, "K": 13, "A": 14}[card]


class HandType(IntEnum):
    HIGH_CARD = 0
    PAIR = 1
    TWO_PAIR = 2
    THREE_OF_A_KIND = 3
    FULL_HOUSE = 4
    FOUR_OF_A_KIND = 5
    FIVE_OF_A_KIND = 6


HAND_TYPES = {
    (5,): HandType.FIVE_OF_A_KIND,
    (4, 1): HandType.FOUR_OF_A_KIND,
    (3, 2): HandType.FULL_HOUSE,
    (3, 1, 1): HandType.THREE_OF_A_KIND,
    (2, 2, 1): HandType.TWO_PAIR,
    (2, 1, 1, 1): HandType.PAIR,
    (1, 1, 1, 1, 1): HandType.HIGH_CARD,
}

FiveTuple = tuple[int, int, int, int, int]


@dataclass
class Hand:
    raw_hand: str
    hand_type: HandType
    card_nums: FiveTuple
    bet: int

    def from_line_a(line: str) -> Hand:
        raw_hand, raw_bet = line.split()
        bet = int(raw_bet)
        card_nums = [card_value(x) for x in raw_hand]
        counter = Counter(card_nums)
        freqs = tuple(sorted(list(counter.values()), reverse=True))
        return Hand(
            raw_hand=raw_hand,
            card_nums=card_nums,
            hand_type=HAND_TYPES[freqs],
            bet=bet,
        )

    def from_line_b(line: str) -> Hand:
        raw_hand, raw_bet = line.split()
        bet = int(raw_bet)
        card_nums = [card_value(x, joker=True) for x in raw_hand]
        counter = Counter(card_nums)
        joker_count = counter.pop(0, 0)
        if joker_count:
            if not counter:
                counter = {14: 5}
            else:
                max_elem = max(counter, key=lambda x: (counter[x], x))
                counter[max_elem] += joker_count
        freqs = tuple(sorted(list(counter.values()), reverse=True))
        return Hand(
            raw_hand=raw_hand,
            card_nums=card_nums,
            hand_type=HAND_TYPES[freqs],
            bet=bet,
        )

    def __lt__(self, other: Hand) -> bool:
        if self.hand_type != other.hand_type:
            return self.hand_type < other.hand_type
        return self.card_nums < other.card_nums

    def __str__(self) -> str:
        return f"{self.raw_hand} {self.hand_type.name}"


def part_a():
    lines = utils.get_lines(7)
    hands: list[Hand] = sorted(Hand.from_line_a(line) for line in lines)
    return sum(hand.bet * (idx + 1) for idx, hand in enumerate(hands))


print(part_a())


def part_b():
    lines = utils.get_lines(7)
    hands: list[Hand] = sorted(Hand.from_line_b(line) for line in lines)
    return sum(hand.bet * (idx + 1) for idx, hand in enumerate(hands))


print(part_b())
