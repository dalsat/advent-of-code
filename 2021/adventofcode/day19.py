from __future__ import annotations

from common import day, Dataset, Solution


def parse_input(line):
    def range_from_string(range_str: str):
        return tuple(map(int, range_str.split('..')))
    return tuple(map(range_from_string, line.split('x=')[1].split(', y=')))


def max_height(target):
    return max(all_hits(target))

def all_hits(target):
    x_threshold = max(map(abs, target[0])) + 1
    y_threshold = max(map(abs, target[1])) + 1

    for dy in range(-y_threshold, y_threshold):
        for dx in range(-x_threshold, x_threshold):
            p = Probe(dx, dy, *target)
            if p.shoot():
                yield p.max_height


def run() -> tuple(Solution, Solution):
    data: Dataset = day(19, parse_input)
    hits = list(all_hits(data))
    return (
        max(hits),
        len(hits)
    )


if __name__ == '__main__':
    print(run())
