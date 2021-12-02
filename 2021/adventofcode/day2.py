from __future__ import annotations
from dataclasses import dataclass
from functools import reduce

from common import day, Dataset, Solution

Instruction = tuple[str, int]


def parse(data: Dataset):
    return list(map(parse_line, data))


def parse_line(line: str) -> tuple[int, int]:
    '''
    Execute a command and return the movement of the submarine
    '''
    direction, delta = tuple(map(str.strip, line.split()))
    return (direction, int(delta))


@dataclass
class Position:
    width: int
    depth: int

    def apply(self, instruction: Instruction):
        match instruction:
            case ('forward', delta):
                self.width += delta
            case ('up', delta):
                self.depth -= delta
            case ('down', delta):
                self.depth += delta
    
    def apply_all(self, instructions: list[Instruction]):
        for instruction in instructions:
            self.apply(instruction)
    
    @property
    def value(self):
        return self.width * self.depth


class AimPosition(Position):
    aim: int = 0

    def apply(self, instruction: Instruction):
        match instruction:
            case ('forward', delta):
                self.width += delta
                self.depth += self.aim * delta
            case ('up', delta):
                self.aim -= delta
            case ('down', delta):
                self.aim += delta


def final_position(data: Dataset, position_class):
    position = position_class(0, 0)

    position.apply_all(parse(data))
    return position.value


def run() -> tuple(Solution, Solution):
    data = day(2)
    return (
        final_position(data, position_class=Position),
        final_position(data, position_class=AimPosition)
    )

print(run())