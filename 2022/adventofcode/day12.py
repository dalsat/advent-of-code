from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass
from math import inf

from aoc import load_day


__day__ = 12

def part1(data):
    m = Map(data)
    # m.search()
    print(m)

    print([str(m.get(Pos(x, y))) for x, y in [(0,0), (1,0), (2,0)]])
    # print(m.get(0,0), m.get(0,1), m.get(0,2))
    return m.path_length

def part2(data):
    ...


@dataclass
class Pos:
    x: int
    y: int

    def is_valid(self):
        return 0 <= self.x < self.width and 0 <= self.y < self.height

    def is_between(self, min_x, max_x, min_y, max_y):
        return min_x <= self.x < max_x and min_y <= self.y < max_y

    def neighbors(self):
        x = self.x
        y = self.y
        return [
            Pos(x -1, y -1), Pos(x, y -1), Pos(x +1, y -1),
            Pos(x -1,    y),               Pos(x +1, y   ),
            Pos(x -1, y +1), Pos(x, y +1), Pos(x +1, y +1),
        ]


@dataclass
class Cell:
    OFFSET = ord('a') - 1
    value: int
    weight: int = inf
    start: bool = False
    goal: bool = False

    def __init__(self, char: str) -> None:
        if char == 'S':
            self.start = True
            char = 'a'
        elif char == 'E':
            self.goal = True
            char = 'z'
        self.value = ord(char) - self.OFFSET

    def can_climb(self, other: Cell):
        return other.value - self.value <= 1

    def __str__(self) -> str:
        if self.start:
            return 'S'
        if self.goal:
            return 'E'
        return chr(self.value + self.OFFSET)
    

class Map:

    def __init__(self, data) -> None:
        self.map: list[list[Cell]] = [[Cell(char) for char in row] for row in data]
        self.path: list[Pos] = []
        self.queue: list[Pos] = []
        self.visited: set[Pos] = set()

        for y, row in enumerate(self.map):
            for x, each in enumerate(row):
                if each.start:
                    self.start = Pos(x, y)
                if each.goal:
                    self.goal = Pos(x, y)
        assert self.start
        assert self.goal

        self.path += self.neighbors(self.start)

    @property
    def width(self):
        return len(self.map[0])

    @property
    def height(self):
        return len(self.map)

    @property
    def path_length(self):
        return len(self.path)

    def get(self, position: Pos) -> Cell:
        return self.map[position.y][position.x]

    def neighbors(self, position: Pos):
        return [n for n in position.neighbors() if n.is_between(0, self.width, 0, self.height) and self.get(position) ]

    def search(self, start=None, path=[]):
        
        if not start:
            start = self.start

        if start == self.goal:
            self.path = path
            return path
        

        # return [n for n in filter(lambda n: n not in self.visited, self.neighbors(start)) if n]
        #     if n not in self.visited:
        #         result = self.search(n, path + [n])
        #         if result:
        #             yield result
        

    def __str__(self) -> str:
        def color(cell: Cell, position: Pos):
            if cell.start or cell.goal:
                return f'\033[91m{cell}\033[00m'
            elif position in self.path:
                return f'\033[95m{cell}\033[00m'
            return str(cell)

        return '\n'.join(''.join(color(cell, Pos(x, y)) for x, cell in enumerate(row)) for y, row in enumerate(self.map))


data = load_day(__day__)


if __name__ == '__main__':
    print(f'Day {__day__}: {part1(data)}, {part2(data)}')
