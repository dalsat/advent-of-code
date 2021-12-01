from itertools import pairwise

from common import count, day, Dataset, Solution


def triples(items: list):
    return [(one, two, three) for one, (two, three) in zip(items, list(pairwise(items[1:])))]


def is_increasing(couple):
    first, second = couple
    return first < second


def find_increasing(data: Dataset) -> Solution:
    return count(is_increasing, pairwise(data))


def find_increasing_triples(data: Dataset) -> Solution:
    avg_values = [first + second + third for first, second, third in triples(data)]
    return count(is_increasing, pairwise(avg_values))


def run():
    data = day(1, apply=int)
    return (
        find_increasing(data),
        find_increasing_triples(data)
    )

print(run())