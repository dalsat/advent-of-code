import re
from typing import Any


def load_day(day: int, separator="\n", extract_singleton=True):
    with open(f"input/day-{str(day).zfill(2)}.txt", "r") as f:
        data: Any = f.read()

    if separator:
        data = [line for line in data.split(separator) if line]
    
    if extract_singleton and len(data) == 1:
        data = data[0]

    return data


def parse_numbers(line: str) -> list[int]:
    return list(map(int, re.findall(r'-?\d+', line)))


def count(elements: list, predicate=bool) -> int:
    return sum(1 for each in elements if predicate(each))


def any_of(elements: list, predicate=bool) -> bool:
    return next((True for elements in elements if predicate(elements)), False)


def all_of(elements: list, predicate=bool) -> bool:
    return not any_of(elements, lambda x: not predicate(x))
