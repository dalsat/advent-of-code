from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

from aoc import Interval, Point, any_of, load_day, parse_numbers


__day__ = 15

def part1(data):
    row_number = 2_000_000
    row = Row(intervals=[sensor.without_beacon(row_number) for sensor in data])
    beacons = set(each.beacon_x for each in data if each.beacon_y == row_number and each.beacon_x in row)
    return len(row) - len(beacons)


def part2(data):
    window = (0, 4_000_000)
    window_size = window[1] - window[0] + 1

    for row_number in range(*window):
        row = Row(intervals=[sensor.without_beacon(row_number) for sensor in data], window=window)
        if len(row) < window_size:
            missing = row.missing(window)
            assert len(missing) == 1
            encoded = 4_000_000 * missing[0] + row_number
            return encoded


class Sensor:

    def __init__(self, position: Point, closest_beacon: Point) -> None:
        self.x = position[0]
        self.y = position[1]
        self.beacon_x = closest_beacon[0]
        self.beacon_y = closest_beacon[1]
        self.radius = self.distance(closest_beacon)

    def distance(self, point: Point):
        return (
            abs(self.x - point[0])
            + abs(self.y - point[1])
        )

    def is_in_radius(self, point: Point):
        return self.distance(point) <= self.radius

    def without_beacon(self, row: int) -> Interval:
        number_free = self.radius - abs(self.y - row)
        return (self.x - number_free, self.x + number_free)
    
    def __str__(self) -> str:
        return f'Sensor at x={self.x}, y={self.y}: closest beacon is at x={self.beacon_x}, y={self.beacon_y} (radius={self.radius})'


@dataclass
class Row:
    intervals: list[Interval]
    window: Optional[Interval]

    def __init__(self, intervals, window=None):
        self.window = window
        self.intervals = [self.normalize_interval(interval) for interval in intervals if self.is_valid_interval(self.normalize_interval(interval))]
        self.merge()

    def normalize_interval(self, interval: Interval) -> Interval:
        if not self.window:
            return interval
        return (max(self.window[0], interval[0]), min(self.window[1], interval[1]))

    def is_valid_interval(self, interval: Interval) -> bool:
        return interval[0] < interval[1]

    def merge(self):
        if self.intervals:
            sorted_intervals = sorted(self.intervals, key=lambda e: e[0])
            self.intervals = []
            previous = sorted_intervals.pop(0)
            for interval in sorted_intervals:
                if previous[1] < interval[0]:  # disjoint intervals
                    self.intervals.append(previous)
                    previous = interval
                else:  # merge intervals
                    previous = (previous[0], max(previous[1], interval[1]))
            self.intervals.append(previous)

    def missing(self, window: Interval):
        return [e for e in range(*window) if e not in self]

    def __contains__(self, item: int) -> bool:
        return any_of(self.intervals, lambda e: e[0] <= item <= e[1])

    def __len__(self) -> int:
        values = list(1 + interval[1] - interval[0] for interval in self.intervals)
        return sum(values)


def parse_input(data: list[str]) -> list[Sensor]:
    def parse_row(row: str) -> Sensor:
        numbers = parse_numbers(row)
        return Sensor((numbers[0], numbers[1]), (numbers[2], numbers[3]))
    
    return [parse_row(row) for row in data]


data = parse_input(load_day(__day__))


if __name__ == '__main__':
    print(f'Day {__day__}: {part1(data)}, {part2(data)}')
