import functools
import re
import sys
from collections.abc import Callable, Iterable
from typing import Any, Literal, overload


@overload
def day[T](
    day: int,
    *,
    one_line: Literal[False] = False,
) -> list[str]: ...


@overload
def day[T](
    day: int,
    *,
    one_line: Literal[True],
) -> str: ...


@overload
def day[T](
    day: int,
    *,
    apply: Callable[[str], T] = lambda e: e,
    one_line: Literal[False] = False,
) -> list[T]: ...


@overload
def day[T](
    day: int,
    *,
    apply: Callable[[str], T] = lambda e: e,
    one_line: Literal[True],
) -> T: ...


def day[T](
    day: int,
    *,
    apply: Callable[[str], T] = lambda e: e,
    one_line: bool = False,
) -> T | list[T]:
    try:
        with open(f"input/day-{day}.txt") as file:
            lines = [apply(line.strip()) for line in file]

    except FileNotFoundError as e:
        print(e, file=sys.stderr)
        sys.exit(-1)

    if one_line:
        if len(lines) != 1:
            raise ValueError(f"Input error: Expected 1 line, found {len(lines)} lines")
        return lines[0]
    else:
        if len(lines) == 1:
            print("Warning: Input data is one line")
        return lines


def count(elements: Iterable[Any], predicate=bool) -> int:
    return sum(1 for each in elements if predicate(each))


def any_of(elements: Iterable[Any], predicate=bool) -> bool:
    return next((True for elements in elements if predicate(elements)), False)


def all_of(elements: Iterable[Any], predicate=bool) -> bool:
    return not any_of(elements, lambda x: not predicate(x))


def parse_numbers(line: str) -> list[int]:
    return list(map(int, re.findall(r"-?\d+", line)))


def combine[T](*elements: list[T], function: Callable[[T, T], T]):
    return functools.reduce(
        lambda first, second: (function(a, b) for a, b in zip(first, second)), elements
    )


def sum_all(*elements: list[int]) -> list[int]:
    return list(combine(*elements, function=lambda x, y: x + y))


def mult_all(*elements: list[int]) -> list[int]:
    return list(combine(*elements, function=lambda x, y: x * y))
