from __future__ import annotations
from queue import PriorityQueue

from common import day, Dataset, Solution, Point


class Map:
    def __init__(self, grid, extended=1):
        self.grid = grid
        self.extended = extended
        self.small_size = len(grid)
        self.size = self.small_size * extended

    def at(self, node: Point) -> int:
        x, y = node
        assert x < self.size and y < self.size, f'invalid position ({x}, {y})'
        new_value = (
            self.grid[y % self.small_size][x % self.small_size] +
            x // self.small_size + y // self.small_size
        )
        
        while new_value >= 10:
            new_value = new_value % 10 + 1
        return new_value

    def shortest_path(self):
        INF = 10 * self.size ** 2
        queue = PriorityQueue()
        visited_nodes = set()
        distances = {}

        def neighbors(node):
            x, y = node
            return (
                (x1, y1)
                for x1, y1 in ((x-1, y), (x+1, y), (x, y-1), (x, y+1))
                if 0 <= x1 < self.size and 0 <= y1 < self.size and (x1, y1) not in visited_nodes
            )

        queue.put((0, (0, 0)))
        distances[(0, 0)] = 0

        while not queue.empty():
            distance, node = queue.get()
            visited_nodes.add(node)
            for neighbor in neighbors(node):
                new_distance = distance + self.at(neighbor)
                if new_distance < distances.get(neighbor, INF):
                    distances[neighbor] = new_distance
                    queue.put((new_distance, neighbor))
        
        return distances[(self.size-1, self.size-1)]


def run() -> tuple(Solution, Solution):
    data: Dataset = day(15, lambda row: list(map(int, list(row))))
    m = Map(data, 5)
    return (
        Map(data).shortest_path(),
        Map(data, 5).shortest_path(),
    )

print(run())
