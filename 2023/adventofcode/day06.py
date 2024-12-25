from dataclasses import dataclass
import functools

from .aoc import Solution, parse_numbers, report


@dataclass
class Race:
    time: int
    distance: int


class Day06(Solution):
    def __init__(self, data) -> None:
        super().__init__(data)
        self.times = parse_numbers(self.data[0])
        self.distances = parse_numbers(self.data[1])

    def is_winning(self, ms_pressed: int, race: Race) -> bool:
        remaining_time = race.time - ms_pressed
        final_distance = ms_pressed * remaining_time
        return final_distance > race.distance

    def winning_combinations(self, race: Race) -> int:
        return sum(1 for ms_pressed in range(race.time) if self.is_winning(ms_pressed, race))

    def part1(self) -> int:
        races: list[Race] = [
            Race(time, distance) for time, distance in zip(self.times, self.distances)
        ]

        all_winning_combinations = [self.winning_combinations(race) for race in races]
        result = functools.reduce(int.__mul__, all_winning_combinations)
        return result

    def part2(self) -> int:
        time = int("".join(map(str, self.times)))
        distance = int("".join(map(str, self.distances)))
        return self.winning_combinations(Race(time, distance))


report(Day06, 6, __name__)
