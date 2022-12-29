from __future__ import annotations

from typing import Generator

from aoc import Point, load_day


__day__ = 12

def part1(data):
    m = Map(data)
    return PathFinder(m).find()


def part2(data):
    m = Map(data)
    # m.start = m.goal
    return DownhillPathFinder(m).find()



class PathFinder:

    def __init__(self, map) -> None:
        self.map = map
        self.INFINITY = self.map.height * self.map.width
        self.frontier: list[Point] = [self.start()]
        self.visited: dict[Point, int] = {
            self.start(): 0
        }

    def find(self):
        while self.frontier:
            next_node = self.frontier.pop(0)
            for neighbor in self.valid_moves(next_node):
                if neighbor not in self.visited:
                    self.frontier.append(neighbor)
                self.visited[neighbor] = min(self.visited.get(neighbor, self.INFINITY), self.visited[next_node] + 1)
                if self.is_goal(neighbor):
                    return self.visited[neighbor]                    

        return None

    def start(self):
        return self.map.start
    
    def is_goal(self, point: Point) -> bool:
        return point == self.map.goal

    def valid_moves(self, point: Point) -> Generator[Point, None, None]:
        return (each for each in self.map.neighbors(point) if self.is_valid_move(point, each))

    def is_valid_move(self, start: Point, end: Point) -> bool:
        return self.map.height_at(end) - self.map.height_at(start) <= 1


class DownhillPathFinder(PathFinder):

    def start(self):
        return self.map.goal
    
    def is_valid_move(self, start: Point, end: Point) -> bool:
        return self.map.height_at(start) - self.map.height_at(end) <= 1

    def is_goal(self, point: Point) -> bool:
        return self.map.at(point) == 'a'


class Map:

    def __init__(self, data) -> None:
        self.width: int = len(data[0])
        self.height: int = len(data)
        
        self.start: Point = (-1, -1)
        self.goal: Point = (-1, -1)

        def inspect_cell(cell: str, point: Point):
            if cell == 'S':
                self.start = point
            elif cell == 'E':
                self.goal = point
            return cell
         
        self.map = [
            [
                inspect_cell(each, (x, y))
                for x, each in enumerate(row)]
            for y, row in enumerate(data)
        ]

    def at(self, point: Point) -> str:
        return self.map[point[1]][point[0]]
    
    def height_at(self, point: Point) -> int:
        match self.at(point):
            case 'S':
                return ord('a')
            case 'E':
                return ord('z')
            case letter:
                return ord(letter)
    
    def neighbors(self, point: Point) -> Generator[Point, None, None]:
        return (
            (point[0] + n[0], point[1] + n[1])
            for n in ((-1, 0), (1, 0), (0, -1), (0, 1))
            if 0 <= (point[0] + n[0]) < self.width and 0 <= (point[1] + n[1]) < self.height
        )

    def __str__(self) -> str:
        return '\n'.join(''.join(row) for row in self.map)


data = load_day(__day__)


if __name__ == '__main__':
    print(f'Day {__day__}: {part1(data)}, {part2(data)}')
