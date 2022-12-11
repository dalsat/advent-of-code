from __future__ import annotations
from aoc import load_day


__day__ = 9

def part1(data):

    r = Rope(2)
    r.move_all(data)
    return len(r.last().visited_positions)

def part2(data):
    r = Rope(10)
    r.move_all(data)
    return len(r.last().visited_positions)


class Rope:

    def __init__(self, size) -> None:
        self.x = 0
        self.y = 0
        self.tail = Rope(size - 1) if size > 1 else None

        self.visited_positions: set[tuple[int, int]] = set()
        self.follow(self.x, self.y)

    def move_all(self, data):
        for move in data:
            self.move(move)
    
    def move(self, move):
        match move.split():
            case ['D', value]:
                self.move_steps(int(value), 0, -1)
            case ['U', value]:
                self.move_steps(int(value), 0, 1)
            case ['L', value]:
                self.move_steps(int(value), -1, 0)
            case ['R', value]:
                self.move_steps(int(value), 1, 0)
            case _:
                print('unknown command', move)

    def move_steps(self, steps, x, y):
        for _ in range(steps):
            self.x += x
            self.y += y
            self.tail.follow(self.x, self.y)
    
    def follow(self, head_x, head_y):
        dx = head_x - self.x
        dy = head_y - self.y
        if abs(dx) > 1:
            self.x += dx // abs(dx)
            if abs(dy) != 0:
                self.y += dy // abs(dy)
        else:
            if abs(dy) > 1:
                self.y += dy // abs(dy)
                if abs(dx) != 0:
                    self.x += dx // abs(dx)

        self.visited_positions.add((self.x, self.y))

        if self.tail:
            self.tail.follow(self.x, self.y)

    def display(self):
        nodes = self.all()
        min_size = 0
        max_size = 6

        ropes = {pos: num for num, pos in reversed(list(enumerate(nodes)))}

        for y in range(max_size -1, min_size -1, -1):
            for x in range(min_size, max_size):
                if (x, y) in ropes:
                    rope_id = ropes[(x, y)]
                    if rope_id == 0:
                        rope_id = 'H'
                    print(rope_id, end='')
                else:
                    print('.', end='')
            print()
        print()

    def all(self) -> list[tuple[int, int]]:
        nodes = [(self.x, self.y)]
        if self.tail:
            nodes += self.tail.all()
        return nodes

    def last(self) -> Rope:
        if not self.tail:
            return self
        return self.tail.last()

    def __str__(self) -> str:
        out = f'({self.x}, {self.y})'
        if self.tail:
            out +=  f' - {self.tail}'
        return out


data = load_day(__day__)


if __name__ == '__main__':
    print(f'Day {__day__}: {part1(data)}, {part2(data)}')
