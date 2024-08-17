from __future__ import annotations
from dataclasses import dataclass

from aoc import load_day, parse_numbers


__day__ = 19

def part1(data):
    time = 24
    print(data[0].split(':'))


def part2(data):
    ...


@dataclass
class Blueprint:

    id: int

    @classmethod
    def parse(cls, line) -> Blueprint:
        numbers = parse_numbers(line)
        return cls(numbers[0])


data = load_day(__day__)


if __name__ == '__main__':
    print(f'Day {__day__}: {part1(data)}, {part2(data)}')
