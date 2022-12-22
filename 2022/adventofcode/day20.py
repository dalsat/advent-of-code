from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from aoc import load_day


__day__ = 20


def part1(data):

    m = Mixing(data)
    m.mix()
    return m.decrypt()


def part2(data):
    decryption_key = 811589153
    m = Mixing([each * decryption_key for each in data])
    for _ in range(10):
        m.mix()
    return m.decrypt()



@dataclass
class Number:
    value: int
    normalized_value: int
    left: Optional[Number] = None
    right: Optional[Number] = None

    def move(self):
        if self.value == 0 or self.normalized_value == 0:
            return None

        if self.value < 0:
            step = lambda node: node.left
        elif self.value > 0:
            step = lambda node: node.right

        current = self.left
        self.right.link_left(self.left)

        for _ in range(abs(self.normalized_value)):
            current = step(current)
        self.insert_after(current)
        return current


    def insert_after(self, node):
        self.left = node
        self.right = node.right

        self.left.right = self
        self.right.left = self
    
    def link_left(self, other):
        self.left = other
        other.right = self

    def link_right(self, other):
        self.right = other
        other.left = self


class Mixing:

    def __init__(self, data) -> None:
        self.size = len(data)
        self.numbers = [Number(value, abs(value) % (self.size -1)) for value in data]

        self.head = self.numbers[0]

        for i, number in enumerate(self.numbers):
            number.link_left(self.numbers[i-1])
            if number.right is None:
                number.link_right(self.numbers[i+1])


    def at(self, index):
        index = index % self.size
        for i, node in enumerate(self):
            if i == index:
                return node
        
    def mix(self):
        for number in self.numbers:
            if number == self.head:
                if number.value < 0:
                    self.head = number.left
                elif number.value > 0:
                    self.head = number.right
            if number.move() == self.head:  # the current number landed in the head position
                self.head = number


    def index(self, value):
        for i, node in enumerate(self):
            if node.value == value:
                return i
        raise ValueError(f'value {value} not found')

    def decrypt(self):
        offset = self.index(0)
        values = list(self.at(each + offset).value for each in [1000, 2000, 3000])
        return sum(values)

    def __iter__(self):
        current = self.head
        while True:
            yield current
            current = current.right
            if current == self.head:
                break

    def values(self):
        return [(each.value, each.normalized_value) for each in self]

    def __str__(self):
        return ', '.join(str(each.value) for each in iter(self))


def parse_input(data):
    return [int(each) for each in data]

data = parse_input(load_day(__day__))


if __name__ == '__main__':
    print(f'Day {__day__}: {part1(data)}, {part2(data)}')
