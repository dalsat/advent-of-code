from __future__ import annotations

import itertools
from enum import Enum

from aoc import Point, load_day


__day__ = 17

def part1(data):
    pushes = itertools.cycle(data)


def part2(data):
    ...


class Rock:
    rock_templates = [
        [[0, 0], [0, 1], [0, 2], [0, 3]],
        [[[1, 0], [0, 1], [1, 1], [2, 1], [1, 2]]],
        [[2, 0], [2, 1], [0, 2], [1, 2], [2, 2]],
        [[0, 0], [0, 1], [0, 2], [0, 3]],
        [[0, 0], [0, 1], [1, 0], [1, 1]],
    ]

    class Direction(Enum):
        DOWN = lambda p: (p[0], p[1] + 1)
        LEFT = lambda p: (p[0] - 1, p[1])
        RIGHT = lambda p: (p[0] + 1, p[1])
        

    # transforms = {
    #     'down': lambda p: (p[0], p[1] + 1),
    #     'left': lambda p: (p[0] - 1, p[1]),
    #     'right': lambda p: (p[0] + 1, p[1]),
    # }

    rock_generator = itertools.cycle(rock_templates)

    def __init__(self, points=None) -> None:
        if points is None:
            points = next(self.rock_generator)
        self.points: list[Point] = points
        self._backtrack: list[Point] | None = None

    def move(self, direction: Direction):
        self._backtrack = self.points
        self.points = [direction.value(point) for point in self.points]

    def backtrack(self):
        assert self.backtrack is not None
        self.points = self._backtrack
        self._backtrack = None


data = load_day(__day__)

sample = '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'

if __name__ == '__main__':
    print(f'Day {__day__}: {part1(data)}, {part2(data)}')
