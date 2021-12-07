from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
import itertools

from common import day, Dataset, Solution, count, parse_numbers


Point = tuple[int, int]

@dataclass(frozen=True)
class Line:
    x1: int
    y1: int
    x2: int
    y2: int

    def is_horizontal(self):
        return self.x1 == self.x2 or self.y1 == self.y2

    def points_between(self) -> list[Point]:
        min_x = min(self.x1, self.x2)
        max_x = max(self.x1, self.x2) + 1
        min_y = min(self.y1, self.y2)
        max_y = max(self.y1, self.y2) + 1

        if self.is_horizontal():
            return (
                set((xi, self.y1) for xi in range(min_x, max_x)) |
                set((self.x1, yi) for yi in range(min_y, max_y))
            )
        else:
            delta_x = self.x2 - self.x1
            delta_x = delta_x // abs(delta_x)  # normalize x direction vector
            delta_y = self.y2 - self.y1
            delta_y = delta_y // abs(delta_y)  # normalize y direction vector
            return list(zip(
                range(self.x1, self.x2 + delta_x, delta_x),
                range(self.y1, self.y2 + delta_y, delta_y),
            ))


def max_overlapping_lines(lines: list[Line]):
    return count(
        Counter(itertools.chain(*map(Line.points_between, lines))).items(),
        lambda each: each[1] > 1
    )


def run() -> tuple(Solution, Solution):
    data = day(5, lambda line: Line(*parse_numbers(line)))
    return (
        max_overlapping_lines(filter(Line.is_horizontal, data)),
        max_overlapping_lines(data)
    )

print(run())
