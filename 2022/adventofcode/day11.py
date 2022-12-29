from __future__ import annotations

import functools
from collections.abc import Callable
from dataclasses import dataclass

from aoc import load_day, parse_number, parse_numbers


__day__ = 11

def part1(data):
    return monkeyPack(data, 20, with_discount=True)


def part2(data):
    return monkeyPack(data, 10_000, with_discount=False)


def monkeyPack(specs, rounds, with_discount):
    index = {}
    divisor = functools.reduce(lambda a, b: a * b, (spec['test_number'] for spec in specs), 1)
    
    @dataclass
    class Monkey:
        id: int
        items: list[int]
        operation: str
        test_number: int
        true_target: int
        false_target: int
        business: int = 0

        def __post_init__(self):
            index[self.id] = self

        def run(self):
            while self.items:
                self.business += 1
                item = self.items.pop()
                item = eval(self.operation, {'old': item})

                if with_discount:
                    item = item // 3
                else:
                    item = item % divisor
                
                target = self.true_target if self.test(item) else self.false_target
                index[target].items.append(item)

        def test(self, item: int) -> bool:
            return item % self.test_number == 0
        
    monkeys = [Monkey(**spec) for spec in specs]

    for _ in range(rounds):
        for monkey in monkeys:
            monkey.run()
    
    most_active = sorted((monkey.business for monkey in monkeys), reverse=True)
    return most_active[0] * most_active[1]


def parse_input(data: list[str]):        
    return [
        {
            'id': parse_number(specs[0]),
            'items': parse_numbers(specs[1]),
            'operation': specs[2].split('=')[-1].strip(),
            'test_number': parse_number(specs[3]),
            'true_target': parse_number(specs[4]),
            'false_target': parse_number(specs[5]),
        }
        for specs in map(str.splitlines, data)
    ]

data = parse_input(load_day(__day__, separator='\n\n'))


if __name__ == '__main__':
    print(f'Day {__day__}: {part1(data)}, {part2(data)}')
