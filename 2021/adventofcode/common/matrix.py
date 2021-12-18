from .typing import Point


class Matrix:

    def __init__(self, data):
        self.matrix = list(map(list.copy, data))
        self.height = len(data)
        self.width = len(data[0]) if len(data) > 0 else 0
    
    def __iter__(self):
        return self.matrix.__iter__()

    def at(self, point: Point, new_value=None) -> int:
        x, y = point
        if new_value is not None:
            self.matrix[x][y] = new_value
        return self.matrix[x][y]

    def add_at(self, point: Point, value):
        return self.at(point, self.at(point) + value)

    def is_inside_matrix(self, point: Point):
        x, y = point
        return (
            0 <= x < self.width and
            0 <= y < self.height
        )
    
    def neighbor_positions(self, point: Point):
        x, y = point
        return ((x-1, y), (x+1, y), (x, y-1), (x, y+1))

    def neighbors(self, point: Point):
        return filter(
            self.is_inside_matrix,
            self.neighbor_positions(point)
        )

    def __str__(self, apply=lambda e, _: e) -> str:
        return '\n'.join(''.join(apply(str(value), (x, y))
            for x, value in enumerate(line))
            for y, line in enumerate(self.matrix))


class DiagonalNeighborsMatrix(Matrix):

    def neighbor_positions(self, point: Point):
        x, y = point
        return (
            (x-1, y), (x+1, y),
            (x, y-1), (x, y+1),
            (x+1, y+1), (x-1, y-1),
            (x+1, y-1), (x-1, y+1)
        )
