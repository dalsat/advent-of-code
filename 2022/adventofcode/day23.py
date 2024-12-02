from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

from aoc import Point, load_day


__day__ = 23


def part1(data):
    return data


def part2(data):
    ...    


class Map:

    def __init__(self, data) -> None:
        self.elves = {
            (
                Point(x, y)
                for x, each in row
                if data[y][x] == '#'
            )
            for y, row in enumerate(data)
        }

    def __str__(self) -> str:
        return '\n'.join(''.join(each) for each in self.rows)
    
    def at(self, x: int, y: int) -> str:
        return self.rows[y][x]

class Elves:
    
    direction_list = ('N', 'S' ,'W', 'E')
    def __init__(self, map: Map) -> None:
        self.map = map
        # self.direction_list = ['N', 'S' ,'W', 'E']
        self.elves = []

data = Map(load_day(__day__))


if __name__ == '__main__':
    print(f'Day {__day__}: {part1(data)}, {part2(data)}')
