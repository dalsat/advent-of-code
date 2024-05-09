from dataclasses import dataclass
from typing import Literal

from adventofcode.aoc import Solution, report


Subset = dict[Literal['red', 'green', 'blue'], int]


@dataclass
class Game:
    game_id: int
    subsets: list[Subset]

    def __init__(self, line: str):
        header, subsets = line.split(':')

        assert header.startswith('Game ')
        self.game_id = int(header[5:])
        self.subsets: list[Subset] = []

        for subset in subsets.split(';'):
            self.parse_subset(subset)

    @staticmethod
    def validate_color(color: str) -> Literal['red', 'green', 'blue']:
        assert color in ('red', 'green', 'blue')
        return color

    def parse_subset(self, subset: str):
        new_subset: Subset = {
            self.validate_color(color): int(number)
            for number, color in (each.split() for each in subset.split(','))
        }
        self.subsets.append(new_subset)

    def is_possible(self, configuration: Subset) -> bool:
        for subset in self.subsets:
            for color, number in configuration.items():
                if number < subset.get(color, 0):
                    return False
        return True

    def minimum_viable_configuration(self) -> Subset:
        return {
            'red': max(each.get('red', 0) for each in self.subsets),
            'green': max(each.get('green', 0) for each in self.subsets),
            'blue': max(each.get('blue', 0) for each in self.subsets),
        }

    def power(self):
        min_config = self.minimum_viable_configuration()
        return min_config['red'] * min_config['green'] * min_config['blue']


class Day02(Solution):
    def __init__(self, data: list[str]):
        self.games = [Game(line) for line in data]
        self.configuration: Subset = {'red': 12, 'green': 13, 'blue': 14}

    def part1(self) -> int:
        possible_games = [game for game in self.games if game.is_possible(self.configuration)]
        return sum(game.game_id for game in possible_games)

    def part2(self) -> int:
        return sum(game.power() for game in self.games)


report(Day02, 2, __name__)
