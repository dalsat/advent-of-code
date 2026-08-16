from typing import Self

from common import day, parse_numbers


class Aquarium:
    def __init__(self, data):
        fishes = [0] * 10

        for fish in data:
            fishes[fish] = fishes[fish] + 1
        self.fishes = fishes

    def __len__(self) -> int:
        return sum(self.fishes)

    def next_day(self, days=1) -> Self:
        reset_clock = 6
        newborn_clock = 8
        buffer_position = len(self.fishes) - 1
        for _ in range(days):
            fishes = self.fishes
            newborns = fishes[0]
            fishes = fishes[1:] + fishes[:1]
            fishes[reset_clock] = fishes[reset_clock] + fishes[buffer_position]
            fishes[buffer_position] = 0
            fishes[newborn_clock] = newborns
            self.fishes = fishes

        return self


def run() -> tuple[int, int]:
    data = day(6, apply=parse_numbers, one_line=True)
    return (len(Aquarium(data).next_day(80)), len(Aquarium(data).next_day(256)))


print(run())
