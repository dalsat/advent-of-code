from collections.abc import Generator
from functools import reduce
from itertools import chain
from typing import override

from common import Matrix, Point, all_of, day


class HeatMap:
    def __init__(self, heat_map) -> None:
        self.heat_map = Matrix(heat_map)

    def is_local_minimum(self, point: Point) -> bool:
        neighbors = self.heat_map.neighbors(point)

        def lower_than(other):
            return self.heat_map.at(point) < self.heat_map.at(other)

        return all_of(neighbors, lower_than)

    def risk_factor(self) -> int:
        return sum(self.heat_map.at(point) + 1 for point in self.low_points())

    def low_points(self) -> Generator[tuple[int, int]]:
        for y in range(self.heat_map.height):
            for x in range(self.heat_map.width):
                point = (x, y)
                if self.is_local_minimum(point):
                    yield point

    def three_biggest_basins(self) -> int:
        basins = sorted(map(len, self.basins()), reverse=True)[:3]
        return reduce(lambda acc, x: acc * x, basins)

    def basins(self) -> list[set[Point]]:
        return [self.expand_basin(seed) for seed in self.low_points()]

    def expand_basin(self, seed: Point) -> set[Point]:

        basin = set()
        frontier = {seed}
        while frontier:
            next_point = frontier.pop()
            if self.heat_map.at(next_point) < 9 and next_point not in basin:
                basin.add(next_point)
                frontier.update(self.heat_map.neighbors(next_point))
        return basin

    @override
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
            return f"\033[1;{color}m{value}\033[0m"

        return "\n".join(
            "".join(colored(value, (x, y)) for x, value in enumerate(line))
            for y, line in enumerate(self.heat_map)
        )


def run() -> tuple[int, int]:
    data = day(9, apply=lambda line: list(map(int, list(line))))
    hm = HeatMap(data)
    print(hm)
    return (hm.risk_factor(), hm.three_biggest_basins())


print(run())
