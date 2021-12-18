from __future__ import annotations

from common import day, Dataset, Solution, Point, DiagonalNeighborsMatrix, all_of


class FlashingMatrix(DiagonalNeighborsMatrix):

    threshold: int = 9

    def __init__(self, data):
        super().__init__(data)
        self.flashes: int = 0

    def run(self, steps=1):
        for _ in range(steps):
            self.step()
        return self.flashes

    def step(self):
        for row_index, row in enumerate(self.matrix):
            for col_index, cell in enumerate(row):
                self.increment((row_index, col_index))
        self.end_step()

    def increment(self, cell: Point):
        if self.at(cell, self.at(cell) + 1) == self.threshold + 1:
            self.flash(cell)

    def flash(self, cell: Point):
        self.flashes += 1
        for neighbor in self.neighbors(cell):
            self.increment(neighbor)
    
    def end_step(self):
        for row_index, row in enumerate(self.matrix):
            for col_index, cell in enumerate(row):
                cell: Point = (col_index, row_index)
                if self.at(cell) > self.threshold:
                    self.at(cell, 0)

    def find_first_synchronized(self):
        step = 0
        while not self.is_synchronized():
            self.step()
            step += 1
        return step

    def is_synchronized(self):
        return all_of(self.matrix, lambda row: all_of(row, lambda cell: cell == 0))

def run() -> tuple(Solution, Solution):
    data: Dataset = day(11, lambda line: list(map(int, list(line))))
    return (
        FlashingMatrix(data).run(100),
        FlashingMatrix(data).find_first_synchronized()
    )

print(run())
