from dataclasses import dataclass
from pathlib import Path
from typing import Self


input_dir = Path("../input")


def read_day(day: int):
    input_file = input_dir / f"day{day:02}.txt"
    return read_data(input_file)


def read_data(path: Path):
    with open(path, "r") as file:
        return file.read()


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def __add__(self, other: Self):
        assert isinstance(other, Point), f"class {other} is not a Point"
        return Point(self.x + other.x, self.y + other.y)
