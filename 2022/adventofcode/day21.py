from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

from aoc import load_day


__day__ = 21


def part1(data):
    return int(data['root'].value())


def part2(data):
    root = data['root']
    root_monkey = RootMonkey('root2', root.left, root.right, None)

    delta = root_monkey.value()
    delta_previous = delta
    direction = 1
    speed = 1
    temperature = delta

    while delta != 0:
        if abs(delta) - abs(delta_previous) > 0:  # not getting closer
            direction = direction * -1
            speed = 1
            temperature = max(1, temperature // 2)
        else:
            speed += temperature
        
        data['humn'].terminal_value += direction * speed
        human = data['humn'].terminal_value
        delta_previous = delta
        delta = root_monkey.value()
        print(f'delta: {delta}; temperature: {temperature}')

    return int(data['humn'].terminal_value)


@dataclass
class Monkey:
    name: str
    left: str
    right: str
    operation: Callable[[float, float], float]

    def value(self):
        left_monkey = data[self.left].value()
        right_monkey = data[self.right].value()
        return self.operation(left_monkey, right_monkey)


@dataclass
class TerminalMonkey:
    name: str
    terminal_value: int

    def value(self):
        return self.terminal_value


@dataclass
class RootMonkey(Monkey):
    
    def value(self):
        left_monkey = data[self.left].value()
        right_monkey = data[self.right].value()
        return left_monkey - right_monkey


def parse_monkey(monkey: str) -> Monkey | TerminalMonkey:
    match monkey.split(' '):
        case [name, number] if number.isdigit():
            return TerminalMonkey(name[:-1], int(number))
        case [name, left, '+', right]:
            return Monkey(name[:-1], left, right, lambda left, right: left + right)
        case [name, left, '-', right]:
            return Monkey(name[:-1], left, right, lambda left, right: left - right)
        case [name, left, '*', right]:
            return Monkey(name[:-1], left, right, lambda left, right: left * right)
        case [name, left, '/', right]:
            return Monkey(name[:-1], left, right, lambda left, right: left / right)
        case _:
            raise ValueError(f'error parsing command: {monkey}')
    

def parse_input(data):
    return {monkey.name: monkey for monkey in (parse_monkey(monkey) for monkey in data)}


data = parse_input(load_day(__day__))


if __name__ == '__main__':
    print(f'Day {__day__}: {part1(data)}, {part2(data)}')
