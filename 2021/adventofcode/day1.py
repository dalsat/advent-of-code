from itertools import pairwise

from common import count, day


def triples(items: list[int]) -> list[tuple[int, int, int]]:
    return [
        (one, two, three) for one, (two, three) in zip(items, list(pairwise(items[1:])))
    ]


def is_increasing(couple: tuple[int, int]) -> bool:
    first, second = couple
    return first < second


def count_increasing(data: list[int]) -> int:
    return count(pairwise(data), is_increasing)


def count_increasing_triples(data: list[int]) -> int:
    avg_values = [first + second + third for first, second, third in triples(data)]
    return count(pairwise(avg_values), is_increasing)


def run() -> tuple[int, int]:
    data = day(1, apply=int)
    return (
        count_increasing(data),
        count_increasing_triples(data),
    )


print(run())
