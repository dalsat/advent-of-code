from dataclasses import dataclass, field
import functools
import itertools
from typing import Iterator

from rich import print

from .aoc import Solution, report, parse_numbers


@dataclass
class Range:
    source: int
    dest: int
    size: int

    def __contains__(self, value: int) -> bool:
        return 0 <= value - self.source < self.size

    def map(self, value: int) -> int:
        return self.dest - self.source + value


@dataclass
class SeedMap:
    name: str
    ranges: list[Range] = field(default_factory=list)

    def map(self, value: int) -> int:
        mapper = next((range for range in self.ranges if value in range), None)
        return mapper.map(value) if mapper else value


class Day05(Solution):
    def __init__(self, data: list[str]):
        super().__init__(data)
        self.seeds = parse_numbers(data[0])
        self.seed_maps: list[SeedMap] = self.parse_maps()
        print(self.seed_maps)

    def parse_maps(self) -> list[SeedMap]:
        print(
            [
                self.parse_block(group)
                for key, group in itertools.groupby(self.data, bool)
                if key
            ]
        )

        # lines_iter = iter(self.data[2:])
        maps: list[SeedMap] = []
        # try:
        #     while lines_iter:
        #         maps.append(self.parse_block(lines_iter))
        # except StopIteration:
        #     pass
        return maps

    def parse_block(self, block) -> SeedMap:
        name = next(block)
        ranges = [
            print(f"split -> {line}")
            # Range(dest=int(dest), source=int(source), size=int(size))
            for line in block
            # for args in line.split("")
        ]
        print(f"{name=}")
        seed_map = SeedMap(name=name, ranges=ranges)

        # while line := next(stream):
        #     dest, source, size = line.split()
        #     seed_map.ranges.append(Range(int(source), int(dest), int(size)))
        return seed_map

    def map(self, value) -> int:
        seed_value = value
        print(f"***{seed_value=}")
        for mapper in self.seed_maps:
            before = seed_value
            seed_value = mapper.map(seed_value)
            print(f"{before} -> {seed_value} {mapper.name}")
        return seed_value
        # return list(functools.reduce(lambda acc, e: e.map(acc), self.seed_maps, value))[-1]

    def part1(self) -> int:
        return min(self.map(seed) for seed in self.seeds)
        # 948577085 too high

    def part2(self) -> int:
        return -1


report(Day05, 5, __name__)
