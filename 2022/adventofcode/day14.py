from __future__ import annotations

import functools
import itertools

from aoc import Point, load_day


__day__ = 14

def part1(cave):
    result = cave.simulate()
    # cave.print()
    return result


def part2(cave):
    cave.with_floor = True
    result = cave.simulate()
    # cave.print()
    return result


class Cave:

    def __init__(self, with_floor=False) -> None:
        self.walls: set[Point] = set()
        self.min_x = 500
        self.max_x = 500
        self.min_y = 0
        self.max_y = 0
    
        self.sand: set[Point] = set()
        self.with_floor = with_floor


    def update_boundaries(self, x, y):
        self.min_x = min(self.min_x, x)
        self.max_x = max(self.max_x, x)
        self.min_y = min(self.min_y, y)
        self.max_y = max(self.max_y, y)

    def add_line(self, start: Point, end: Point):
        x1, y1 = start
        x2, y2 = end

        self.update_boundaries(x1, y1)
        self.update_boundaries(x2, y2)

        if x1 == x2:
            self.walls.update([(x1, each) for each in range(min(y1, y2), max(y1, y2)+1)])
        else:
            self.walls.update([(each, y1) for each in range(min(x1, x2), max(x1, x2)+1)])

    def is_free(self, point):
        if self.with_floor and point[1] == self.max_y + 2:
            return False
        return point not in self.walls and point not in self.sand

    def simulate(self):
        while True:
            x = 500
            y = 0

            while True:
                try:
                    x, y = next(filter(self.is_free, [(x, y+1), (x-1, y+1), (x+1, y+1)]))
                except StopIteration:
                    self.sand.add((x, y))

                    if x == 500 and y == 0:
                        return len(self.sand)
                    else:
                        break
                if not self.with_floor and y > self.max_y:
                    return len(self.sand)
        

    def print(self):
        for y in range(self.min_y - 5, self.max_y + 5):
            for x in range(self.min_x - 5, self.max_x + 5):
                if (x, y) in self.walls:
                    value = '#'
                elif (x, y) in self.sand:
                    value = 'o'
                elif x == 500 and y == 0:
                    value = '+'
                else:
                    value = ' '
                print(value, end='')
            print()


    @classmethod
    def parse(cls, data):
        walls = cls()

        for wall in data:
            chain = [[int(each.strip()) for each in point.split(',')] for point in wall.split('->')]
            
            for start, end in itertools.pairwise(chain):
                walls.add_line(start, end)
        return walls


data = Cave.parse(load_day(__day__))


if __name__ == '__main__':
    print(f'Day {__day__}: {part1(data)}, {part2(data)}')
