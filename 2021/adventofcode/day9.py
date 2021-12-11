from __future__ import annotations
from functools import reduce
from itertools import chain

from common import day, Dataset, Solution, all_of


Point = tuple[int, int]

class HeatMap:

    def __init__(self, heat_map):
        self.heat_map = heat_map
        self.width = len(heat_map[0])
        self.height = len(heat_map)

    def at(self, point: Point) -> int:
        x, y = point
        return self.heat_map[y][x]

    def is_valid_position(self, point: Point):
        x, y = point
        return (
            0 <= x < self.width and
            0 <= y < self.height
        )
    
    def neighbors(self, point: Point):
        x, y = point
        return filter(
            lambda each: self.is_valid_position(each),
            ((x-1, y), (x+1, y), (x, y-1), (x, y+1))
        )

    def lower_neighbors(self, point: Point):
        neighbors = self.neighbors(point)
        lowest_neighbor = min(self.at(each) for each in neighbors)
        return list(each for each in neighbors if self.at(each) == lowest_neighbor)

    def is_local_minimum(self, point: Point):
        neighbors = self.neighbors(point)
        def lower_than(other):
            return self.at(point) < self.at(other)

        return all_of(neighbors, lower_than)

    def risk_factor(self):
        return sum(self.at(point) + 1 for point in self.low_points())

    def low_points(self):
        for y in range(self.height):
            for x in range(self.width):
                point = (x, y)
                if self.is_local_minimum(point):
                    yield point

    def three_biggest_basins(self):
        basins = sorted(map(len, self.basins()), reverse=True)[:3]
        return reduce(lambda acc, x: acc * x, basins)

    def basins(self):
        return list(self.expand_basin(seed) for seed in self.low_points())

    def expand_basin(self, seed: Point):

        basin = set()
        frontier = {seed}
        while frontier:
            next_point = frontier.pop()
            if self.at(next_point) < 9 and next_point not in basin:
                basin.add(next_point)
                frontier.update(self.neighbors(next_point))
        return basin

    def __str__(self) -> str:
        low_points = set(self.low_points())
        points_in_basins = set(chain(*self.basins()))

        def colored(value: int, point) -> str:
            if point in low_points:
                color = 31
            elif point in points_in_basins:
                color = 0
            else:
                color = 32
            return f'\033[1;{color}m{value}\033[0m'
        return '\n'.join(''.join(colored(value, (x, y))
            for x, value in enumerate(line))
            for y, line in enumerate(self.heat_map))


def run() -> tuple(Solution, Solution):
    data = day(9, lambda line: list(map(int, list(line))))
    hm = HeatMap(data)
    print(hm)
    return (
        hm.risk_factor(),
        hm.three_biggest_basins()
    )

print(run())
