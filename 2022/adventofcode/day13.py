from __future__ import annotations

import functools
import itertools

from aoc import load_day


__day__ = 13

def part1(data):
    return sum(i for i, pair in enumerate(data, 1) if compare(pair))


def part2(data):
    markers = [[[2]], [[6]]]
    packets = list(itertools.chain(*data)) + markers

    def sort_compare(left, right):
        return -1 if compare([left, right]) else 1
        
    packets = sorted(packets, key=functools.cmp_to_key(sort_compare))

    markers_positions = [i for i, packet in enumerate(packets, 1) if packet in markers]
    assert len(markers_positions) == 2
    return functools.reduce(lambda a, b: a * b, markers_positions)


def compare(pair):
    match pair:
        case [left, right] if isinstance(left, int) and isinstance(right, int):
            return left < right
        case [[left, *lt], [right, *rt]] if left == right:
            return compare([lt, rt])
        case [[left, *lt], [right, *rt]]:
            return compare([left, right])
        case [[[], *lt], [[], *rt]] if left == right:
            return compare([lt, rt])
        case [[], _]:
            return True
        case [_, []]:
            return False
        case [left, right] if isinstance(left, int):
            return compare([[left], right])
        case [left, right] if isinstance(right, int):
            return compare([left, [right]])
        case _:
            print(f'error with {pair}')

def process_input(data):
    return [[eval(packet) for packet in couple.strip().split('\n')] for couple in data]


data = process_input(load_day(__day__, separator='\n\n'))


if __name__ == '__main__':
    print(f'Day {__day__}: {part1(data)}, {part2(data)}')
