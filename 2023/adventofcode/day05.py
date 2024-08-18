import itertools
from collections.abc import Iterator
from dataclasses import dataclass, field

from .aoc import Solution, report, parse_numbers


@dataclass
class Range:
    start: int
    length: int

    def __contains__(self, value: int) -> bool:
        return 0 <= value - self.start < self.length

    @property
    def end(self) -> int:
        """The end of the interval
        
        Return the end of the interval, computed as the first value greater than the start _not_ in
        the interval.
        """
        return self.start + self.length


@dataclass
class Mapping:
    range: Range
    destination: int


    def map(self, range: Range) -> list[Range]:
        # default case: no overlap
        if range.end < self.range.start or self.range.end < range.end:
            return [range]
        
        return [range]
        # return self.dest - self.source + value


@dataclass
class SeedMap:
    name: str
    ranges: list[Range] = field(default_factory=list)

    def map(self, value: int) -> int:
        mapper = next((range for range in self.ranges if value in range), None)
        return mapper.map(value) if mapper else value


def parse_maps(data: list[str]) -> list[SeedMap]:
    return [parse_block(group) for key, group in itertools.groupby(data, bool) if key]


def parse_block(block: Iterator[str]) -> SeedMap:
    header = next(block)
    ranges = [parse_line(line) for line in block if line]
    seed_map = SeedMap(name=header, ranges=ranges)
    return seed_map


def parse_line(line: str) -> Range:
    dest, source, size = line.split()
    return Range(dest=int(dest), source=int(source), size=int(size))


def expand_seed_ranges(seeds: list[int]) -> Iterator[int]:
    """Turn the list of individual seeds into ranges.
    
    Part 2
    The numbers are grouped in pairs, where the first is the starting seed and the second is the
    length of the interval.
    """
    # split the seeds into the start values and the lenghts
    # then group them into couples using zip
    
    for start, length in sorted(itertools.batched(seeds, 2)):
        yield Range()

    current_seed = 0

    for start, length in couples[:3]:
        end = start + length
        if start < current_seed:
            # we already processed this seed
            start = current_seed
        yield from range(start, end)
        current_seed = max(current_seed, end)

    # return (seed for start, length in couples for seed in range(start, start + length))


class Day05(Solution):
    def __init__(self, data: list[str]):
        super().__init__(data)
        self.seeds = parse_numbers(data[0])
        self.seed_maps: list[SeedMap] = parse_maps(data[1:])

    def map(self, value) -> int:
        seed_value = value
        for mapper in self.seed_maps:
            seed_value = mapper.map(seed_value)
        return seed_value

    def min_seed_location(self, seeds) -> int:
        return min(self.map(seed) for seed in seeds)

    def part1(self) -> int:
        return self.min_seed_location(self.seeds)

    def part2(self) -> int:
        seeds = expand_seed_ranges(self.seeds)
        # return 1
        return sum(1 for _ in seeds)
        # return self.min_seed_location(seeds)


report(Day05, 5, __name__)
