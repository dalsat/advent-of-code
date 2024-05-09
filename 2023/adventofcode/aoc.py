import abc
import re


def read_lines(file_path: str) -> list[str]:
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]


def input_for_day(day: int) -> list[str]:
    return read_lines(f'data/day{day:02}.txt')


def parse_numbers(line: str) -> list[int]:
    return [int(number) for number in re.findall(r'-?\d+', line)]


class Solution(abc.ABC):
    def __init__(self, data: list[str]) -> None:
        self.data: list[str] = data

    @abc.abstractmethod
    def part1(self) -> int:
        ...

    @abc.abstractmethod
    def part2(self) -> int:
        ...

    def report(self):
        print(f'Part1: {self.part1()}')
        print(f'Part2: {self.part2()}')


def report(solution_class: type[Solution], day: int, __name__: str):
    if __name__ == '__main__':
        data = input_for_day(day)
        print(f'Day {day}')
        solution_class(data).report()
