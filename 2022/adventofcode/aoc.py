import re
from typing import Any, Callable


Point = tuple[int, int]
Interval = tuple[int, int]


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


def parse_number(line: str) -> int:
    numbers = parse_numbers(line)
    assert len(numbers) == 1
    return numbers[0]


def count(elements: list, predicate: Callable[[Any], bool]=bool) -> int:
    return sum(1 for each in elements if predicate(each))
