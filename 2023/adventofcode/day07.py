from dataclasses import dataclass, field
from collections import Counter
from enum import IntEnum, auto
from .aoc import Solution, report


class HandStrength(IntEnum):
    HIGH_CARD = auto()
    ONE_PAIR = auto()
    TWO_PAIRS = auto()
    THREE_OF_A_KIND = auto()
    FULL_HOUSE = auto()
    FOUR_OF_A_KIND = auto()
    FIVE_OF_A_KIND = auto()


@dataclass
class Hand:
    cards: str
    bid: int
    strength: HandStrength = field(init=False)
    card_values: list[int] = field(init=False)

    def __post_init__(self) -> None:
        self.strength = self.compute_strength(self.cards)
        self.card_values = [self.compute_card_value(each) for each in self.cards]

    @staticmethod
    def compute_strength(hand: str) -> HandStrength:
        card_counts = [count for _, count in Counter(hand).most_common()]

        match card_counts:
            case [5, *_]:  # five of a kind
                return HandStrength.FIVE_OF_A_KIND
            case [4, *_]:  # four of a kind
                return HandStrength.FOUR_OF_A_KIND
            case [3, 2, *_]:  # full house
                return HandStrength.FULL_HOUSE
            case [3, *_]:  # three of a kind
                return HandStrength.THREE_OF_A_KIND
            case [2, 2, *_]:  # two pair
                return HandStrength.TWO_PAIRS
            case [2, *_]:  # one pair
                return HandStrength.ONE_PAIR
            case [1, *_]:  # high card
                return HandStrength.HIGH_CARD
            case _:
                raise ValueError(f"Unexpected sequence {card_counts}")

    @staticmethod
    def compute_card_value(card: str) -> int:
        match card:
            case "T":
                return 10
            case "J":
                return 11
            case "Q":
                return 12
            case "K":
                return 13
            case "A":
                return 14
            case other:
                value = int(other)
                assert 0 <= value < 10
                return value

    def __lt__(self, other) -> bool:
        if self.strength == other.strength:
            return self.card_values < other.card_values
        return self.strength < other.strength


@dataclass
class HandWithJocker(Hand):
    @staticmethod
    def compute_card_value(card: str) -> int:
        # return super().compute_card_value(card)
        pass


class Day07(Solution):
    def process_data(self, data: list[str]) -> list[Hand]:
        return [Hand(cards, int(bid)) for cards, bid in [row.split() for row in data]]

    def part1(self) -> int:
        hands = self.process_data(self.data)
        return sum(hand.bid * rank for rank, hand in enumerate(sorted(hands), start=1))

    def part2(self) -> int:
        return -1


report(Day07, 7, __name__)
