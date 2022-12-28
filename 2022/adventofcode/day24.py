from __future__ import annotations

from dataclasses import dataclass, field

from aoc import Point, load_day


__day__ = 24


def part1(data):
    m = Map.parse(data)
    start = (1,0)
    goal = (m.width -2, m.height -1)

    return trip(start, goal, 0)


def part2(data):
    m = Map.parse(data)
    start = (1,0)
    goal = (m.width -2, m.height -1)

    round_1 = trip(start, goal, 0)
    round_2 = trip(goal, start, round_1)
    round_3 = trip(start, goal, round_2)
    return round_3


def trip(start, goal, initial_time):

    queue: list[Position] = []
    index: set[Position] = set()

    def push(position: Point, steps):
        nonlocal queue
        distance = steps + abs(goal[0] - position[0]) + abs(goal[1] - position[1])
        new_position = Position(*position, steps, distance)
        if new_position not in index:
            index.add(new_position)
            queue.append(new_position)
            queue = sorted(queue, key=lambda e: e.distance)
    
    def pop():
        item = queue.pop(0)
        index.remove(item)
        return item

    push(start, initial_time)

    while queue:
        position = pop()
        if (position.x, position.y) == goal:
            return position.steps
        else:
            next_map = Map.after(position.steps + 1)
            for each in next_map.valid_moves((position.x, position.y)):
                push(each, position.steps + 1)


@dataclass(frozen=True)
class Position:
    x: int
    y: int
    steps: int
    distance: int = field(hash=False, compare=False)


class Map:

    cache: dict[int, Map] = {}

    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

        self.up: set[Point] = set()
        self.down: set[Point] = set()
        self.left: set[Point] = set()
        self.right: set[Point] = set()
        self.walls: set[Point] = set()

        self.char_mapping = {
            '^': self.up,
            'v': self.down,
            '<': self.left,
            '>': self.right,
            '#': self.walls,
        }
    
    def is_free(self, p: Point) -> bool:
        return (
            p not in self.up
            and p not in self.down
            and p not in self.left
            and p not in self.right
            and p not in self.walls
            and 0 <= p[0] < self.width
            and 0 <= p[1] < self.height
        )

    def valid_moves(self, position: Point):
        x, y = position
        cells = [
            (x, y-1),
            (x-1, y), (x, y), (x+1, y),
            (x, y+1),
        ]
        return filter(self.is_free, cells)

    @classmethod
    def parse(cls, data):
        new_map = Map(len(data[0]), len(data))

        for y, row in enumerate(data):
            for x, cell in enumerate(row):
                if cell in new_map.char_mapping:
                    new_map.char_mapping[cell].add((x, y))
        
        cls.cache[0] = new_map
        return new_map
    
    def __next__(self):
        new_map = Map(self.width, self.height)

        new_map.up |= {(x, (y-2) % (self.height -2) + 1) for x, y in self.up}
        new_map.down |= {(x, y % (self.height -2) + 1) for x, y in self.down}
        new_map.left |= {((x-2) % (self.width -2) + 1, y) for x, y in self.left}
        new_map.right |= {((x) % (self.width -2) + 1, y) for x, y in self.right}
        new_map.walls |= self.walls
        
        return new_map

    def __str__(self):
        def print_cell(cell: Point):
            for char, mapping in self.char_mapping.items():
                if cell in mapping:
                    return char
            return '.'
        
        return '\n'.join(''.join(print_cell((x, y)) for x in range(self.width)) for y in range(self.height))
    
    @classmethod
    def after(cls, step: int) -> Map:
        '''Return the status of the map after _steps_ number of steps. Results are memoized.'''
        if step not in cls.cache:
            cls.cache[step] = next(cls.after(step - 1))
        return cls.cache[step]


data = load_day(__day__)


if __name__ == '__main__':
    print(f'Day {__day__}: {part1(data)}, {part2(data)}')
