from dataclasses import dataclass
from typing import override

from common import day

type Instruction = tuple[str, int]


def parse(data: list[str]) -> list[tuple[str, int]]:
    return list(map(parse_line, data))


def parse_line(line: str) -> tuple[str, int]:
    direction, delta = tuple(map(str.strip, line.split()))
    return (direction, int(delta))


@dataclass
class Position:
    width: int
    depth: int

    def apply(self, instruction: Instruction) -> None:
        match instruction:
            case ("forward", delta):
                self.width += delta
            case ("up", delta):
                self.depth -= delta
            case ("down", delta):
                self.depth += delta

    def apply_all(self, instructions: list[Instruction]) -> None:
        for instruction in instructions:
            self.apply(instruction)

    @property
    def value(self) -> int:
        return self.width * self.depth


@dataclass
class AimPosition(Position):
    aim: int = 0

    @override
    def apply(self, instruction: Instruction) -> None:
        match instruction:
            case ("forward", delta):
                self.width += delta
                self.depth += self.aim * delta
            case ("up", delta):
                self.aim -= delta
            case ("down", delta):
                self.aim += delta


def final_position(data: list[str], position_class: type[Position]) -> int:
    position = position_class(0, 0)

    position.apply_all(parse(data))
    return position.value


def run() -> tuple[int, int]:
    data = day(2)
    return (
        final_position(data, position_class=Position),
        final_position(data, position_class=AimPosition),
    )


print(run())
