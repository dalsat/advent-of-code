from __future__ import annotations

from common import day, Dataset, Solution, parse_numbers


class Aquarium:

    def __init__(self, data):
        fishes = [0] * 10

        for fish in data:
            fishes[fish] = fishes[fish] + 1
        self.fishes = fishes

    def __len__(self):
        return sum(self.fishes)

    def next_day(self, days=1):
        reset_clock = 6
        newborn_clock = 8
        buffer_position = len(self.fishes) - 1
        for day in range(days):
            fishes = self.fishes
            newborns = fishes[0]
            fishes = fishes[1:] + fishes[:1]
            fishes[reset_clock] = fishes[reset_clock] + fishes[buffer_position]
            fishes[buffer_position] = 0
            fishes[newborn_clock] = newborns
            self.fishes = fishes

        return self

def run() -> tuple(Solution, Solution):
    data = day(6, parse_numbers)
    return (
        len(Aquarium(data[0]).next_day(80)),
        len(Aquarium(data[0]).next_day(256))
    )

print(run())
