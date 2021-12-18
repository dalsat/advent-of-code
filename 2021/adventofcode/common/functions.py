import functools
import re
import sys

from .typing import Dataset

def day(day: int, apply=lambda e: e) -> Dataset:
    try:
        with open(f'input/day-{day}.txt') as file:
            return list([apply(line.strip()) for line in file.readlines()])
    except FileNotFoundError as e:
        print(e, file=sys.stderr)
        sys.exit(-1)


def count(elements: list, predicate=bool) -> int:
    return sum(1 for each in elements if predicate(each))


def any_of(elements: list, predicate=bool) -> bool:
    return next((True for elements in elements if predicate(elements)), False)


def all_of(elements: list, predicate=bool) -> bool:
    return not any_of(elements, lambda x: not predicate(x))


def parse_numbers(line: str) -> list[int]:
    return list(map(int, re.findall(r'-?\d+', line)))


def combine(*elements: list, function):
    return functools.reduce(
        lambda first, second: (function(a, b) for a, b in zip(first, second)),
        elements)


def sum_all(*elements: list[int]):
    return list(combine(*elements, function=lambda x, y: x + y))


def mult_all(*elements: list[int]):
    return list(combine(*elements, function=lambda x, y: x * y))
