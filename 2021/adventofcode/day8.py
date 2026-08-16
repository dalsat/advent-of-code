from itertools import chain
from operator import itemgetter

from common import count, day

type Digits = list[str]

numbers_mapping = (
    (1, ("a", "b")),
    (2, ("a", "c", "d", "f", "g")),
    (3, ("a", "b", "c", "d", "f")),
    (4, ("a", "b", "e", "f")),
    (5, ("b", "c", "d", "e", "f")),
    (6, ("b", "c", "d", "e", "f", "g")),
    (7, ("a", "b", "d")),
    (8, ("a", "b", "c", "d", "e", "f", "g")),
    (9, ("a", "b", "c", "d", "e", "f")),
)


def parse_dataset(data: list[str]) -> list[tuple[Digits, Digits]]:
    return [parse_line(each) for each in data]


def parse_line(line: str) -> tuple[Digits, Digits]:
    parsed_line = tuple(each.strip().split() for each in line.split("|"))
    assert len(parsed_line) == 2
    return parsed_line


def find_simple_occurrences(lines: list[tuple[Digits, Digits]]) -> int:
    simple_numbers = filter(lambda e: e[0] in (1, 4, 7, 8), numbers_mapping)
    outputs = list(chain(*map(itemgetter(1), lines)))
    return sum(
        count(outputs, lambda e: len(e) == len(segments))
        for _, segments in simple_numbers
    )


def mapping_from(signals):
    """
    Mapping:

     dddd
    e    a
    e    a
     ffff
    g    b
    g    b
     cccc

    0  1  2  3  4  5  6
    a, b, c, d, e, f, g
    """
    mapping = [{"a", "b", "c", "d", "e", "f", "g"}] * 7

    print(mapping)

    return {}


def decode_number(signals, output):
    mapping = mapping_from(signals)

    def decode_digit(digit):
        sorted_segments = "".join(sorted(digit))
        return mapping.get(sorted_segments, sorted_segments)

    # return int(''.join(decode_digit(digit) for digit in output))
    print([decode_digit(digit) for digit in output])
    return 1


def sum_all_numbers(data):
    return sum(decode_number(signals, output) for signals, output in data)


def run() -> tuple[int, int]:
    data = day(8, apply=parse_line)
    return (find_simple_occurrences(data), sum_all_numbers(data[:1]))


print(run())
