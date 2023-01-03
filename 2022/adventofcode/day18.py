from __future__ import annotations
from dataclasses import dataclass

from aoc import load_day


__day__ = 18

def part1(data):

    points = set(data)
    return sum(len([face for face in each.neighbors() if face not in points]) for each in data)


def part2(data):
    
    points = set(data)
    pockets: set[Point3D] = set()
    window_min = Point3D(min(p.x for p in data), min(p.y for p in data), min(p.z for p in data))
    window_max = Point3D(max(p.x for p in data), max(p.y for p in data), max(p.z for p in data))

    def check_pocket(start: Point3D) -> bool:
        nonlocal pockets

        queue = [start]
        visited: set[Point3D] = set()

        while queue:
            point = queue.pop()
        
            if ((not window_min.x < point.x < window_max.x)
                or not (window_min.y < point.y < window_max.y)
                or not (window_min.z < point.z < window_max.z)):

                # we reached outside
                return False

            visited.add(point)
            queue += [n for n in point.neighbors() if n not in points and n not in visited]

        pockets = pockets | visited
        return True
    

    for point in data:
        for n in point.neighbors():
            if n not in pockets:
                check_pocket(n)

    return sum(len([face for face in each.neighbors() if face not in points and face not in pockets]) for each in data)


@dataclass(frozen=True)
class Point3D:
    x: int
    y: int
    z: int

    def neighbors(self) -> list[Point3D]:
        return [
            Point3D(self.x + x, self.y + y, self.z + z)
            for x, y, z in (
                (-1, 0, 0), (1, 0, 0),
                (0, -1, 0), (0, 1, 0),
                (0, 0, -1), (0, 0, 1),
            )
        ]
    
    @classmethod
    def parse(cls, line: str) -> Point3D:
        return Point3D(*(int(each.strip()) for each in line.split(',')))


def parse_input(data) -> list[Point3D]:
    return [Point3D.parse(line) for line in data]


data = parse_input(load_day(__day__))


if __name__ == '__main__':
    print(f'Day {__day__}: {part1(data)}, {part2(data)}')
