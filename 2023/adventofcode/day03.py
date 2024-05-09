from dataclasses import dataclass

from .aoc import Solution, report


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def neighbors(self):
        return [
            Point(self.x + x, self.y + y)
            for y in (-1, 0, 1)
            for x in (-1, 0, 1)
            if not (x == y == 0)
        ]


class Day03(Solution):
    def __init__(self, data: list[str]):
        super().__init__(data)
        self.symbols: dict[Point, str] = {
            Point(x, y): each
            for y, row in enumerate(data)
            for x, each in enumerate(row)
            if not (each.isdigit() or each == '.')
        }
        self.valid_numbers: list[tuple[int, set[Point]]] = self.valid_values()

    def valid_values(self) -> list[tuple[int, set[Point]]]:
        valid_numbers: list[tuple[int, set[Point]]] = []
        for y, row in enumerate(self.data):
            number = 0
            symbols: set[Point] = set()
            for x, each in enumerate(row):
                if each.isdigit():
                    number = number * 10 + int(each)
                    symbols |= self.symbols_next_to(Point(x, y))
                else:
                    if symbols:
                        valid_numbers.append((number, symbols))
                    number = 0
                    symbols = set()
            if symbols:
                valid_numbers.append((number, symbols))
        return valid_numbers

    def symbols_next_to(self, point: Point) -> set[Point]:
        return {each for each in point.neighbors() if each in self.symbols}

    def is_valid(self, point: Point) -> bool:
        return any(each for each in point.neighbors() if each in self.symbols)

    def part1(self) -> int:
        return sum(number for number, _ in self.valid_numbers)

    def part2(self) -> int:
        cogs_map: dict[Point, list[int]] = {}

        print(self.valid_numbers)
        for number, points in self.valid_numbers:
            for point in points:
                if self.symbols[point] == '*':
                    if point not in cogs_map:
                        cogs_map[point] = []
                    cogs_map[point].append(number)

        return sum(numbers[0] * numbers[1] for numbers in cogs_map.values() if len(numbers) == 2)


report(Day03, 3, __name__)
