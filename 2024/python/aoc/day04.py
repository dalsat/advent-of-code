from __future__ import annotations

from abc import abstractmethod
from enum import Enum
from typing import override

from rich import print
from rich.console import Console
from rich.panel import Panel

from aoc.core import read_day, Point


class Direction(Enum):
    N = Point(0, -1)
    NE = Point(1, -1)
    E = Point(1, 0)
    SE = Point(1, 1)
    S = Point(0, 1)
    SW = Point(-1, 1)
    W = Point(-1, 0)
    NW = Point(-1, -1)

    @classmethod
    def diagonals(cls) -> tuple[tuple[Direction, Direction], ...]:
        return ((cls.NE, cls.SW), (cls.NW, cls.SE))


class WordMatrix:
    def __init__(self, input_str: str):
        self.word_to_match = "XMAS"

        self.lines = input_str.splitlines()
        assert len(self.lines) == len(self.lines[0])

        self.matches: int = 0
        self.matched_positions: set[Point] = set()

    def __len__(self):
        return len(self.lines)

    def __repr__(self):
        return f"Matrix({len(self)}x{len(self)})"

    def __str__(self):
        return "\n".join(self.lines)

    def __getitem__(self, position: Point) -> str:
        if not self.is_inside(position):
            raise IndexError(f"position {position} is out of bounds")
        return self.lines[position.y][position.x]

    def is_inside(self, position: Point) -> bool:
        return 0 <= position.x < len(self) and 0 <= position.y < len(self)


class MatchingStrategy:
    style_tag = "red"

    def __init__(self, matrix: WordMatrix) -> None:
        self.matrix = matrix
        self.matches = 0
        self.highlighted: set[Point] = set()

    @abstractmethod
    def match(self) -> int: ...

    def highlight(self, value: str, position: Point) -> str:
        if position in self.highlighted:
            return f"[{self.style_tag}]{value}[/{self.style_tag}]"
        else:
            return value

    def __str__(self) -> str:
        return "\n".join(
            "".join(self.highlight(each, Point(x, y)) for x, each in enumerate(line))
            for y, line in enumerate(self.matrix.lines)
        )


class Part1Strategy(MatchingStrategy):
    word_to_match = "XMAS"

    @override
    def match(self) -> int:
        assert self.matches == 0

        for y, line in enumerate(self.matrix.lines):
            for x, each in enumerate(line):
                if each == self.word_to_match[0]:
                    for direction in Direction:
                        if self.find_match(
                            start_position=Point(x, y), direction=direction
                        ):
                            self.matches += 1

        return self.matches

    def find_match(self, start_position: Point, direction: Direction):
        position = start_position
        matched_positions = set()

        for char_to_match in self.word_to_match:
            if (
                not self.matrix.is_inside(position)
                or char_to_match != self.matrix[position]
            ):
                # no match: quit
                return

            matched_positions.add(position)
            position = position + direction.value

        self.matches += 1
        self.highlighted |= matched_positions


class Part2Strategy(MatchingStrategy):
    word_to_match = "MAS"

    @override
    def match(self) -> int:
        for y, line in enumerate(self.matrix.lines):
            for x, _ in enumerate(line):
                position = Point(x, y)
                if self.match_position(position):
                    self.register_matched_position(position)
        return self.matches

    def match_position(self, position: Point) -> bool:
        try:
            return self.matrix[position] == self.word_to_match[1] and all(
                self.match_diagonal(position, *diagonal)
                for diagonal in Direction.diagonals()
            )
        except IndexError:
            return False

    def match_diagonal(
        self, position: Point, first_direction: Direction, second_direction: Direction
    ) -> bool:
        first_value = position + first_direction.value
        second_value = position + second_direction.value
        return (
            self.matrix[first_value] == self.word_to_match[0]
            and self.matrix[second_value] == self.word_to_match[-1]
        ) or (
            self.matrix[first_value] == self.word_to_match[-1]
            and self.matrix[second_value] == self.word_to_match[0]
        )

    def register_matched_position(self, position: Point) -> None:
        self.matches += 1
        self.highlighted.add(position)
        self.highlighted |= set(
            position + each.value
            for diagonal in Direction.diagonals()
            for each in diagonal
        )


console = Console()

data = read_day(4)
matrix = WordMatrix(data)

part1_matcher = Part1Strategy(matrix)
part2_matcher = Part2Strategy(matrix)

print(part1_matcher.match())
print(part2_matcher.match())

console.print(
    Panel(
        str(part1_matcher),
        title="Part 1",
        subtitle=f"Solution: {part1_matcher.matches}",
    )
)

console.print(
    Panel(
        str(part2_matcher),
        title="Part 2",
        subtitle=f"Solution: {part2_matcher.matches}",
    )
)
