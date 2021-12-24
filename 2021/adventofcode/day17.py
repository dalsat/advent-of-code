from __future__ import annotations

from common import day, Dataset, Solution


def parse_target(line):
    def range_from_string(range_str: str):
        return tuple(map(int, range_str.split('..')))
    return tuple(map(range_from_string, line.split('x=')[1].split(', y=')))


def max_height(target):
    return max(all_hits(target))

def all_hits(target):
    x_threshold = max(map(abs, target[0])) + 1
    y_threshold = max(map(abs, target[1])) + 1

    for dy in range(-y_threshold, y_threshold):
        for dx in range(-x_threshold, x_threshold):
            p = Probe(dx, dy, *target)
            if p.shoot():
                yield p.max_height


class Probe:
    def __init__(self, dx: int, dy: int, target_x: tuple[int], target_y: tuple[int]):
        self.x = 0
        self.y = 0
        self.dx = dx
        self.dy = dy
        self.target_x = target_x
        self.target_y = target_y
        self.max_height = self.y

    @property
    def min_x(self):
        return self.target_x[0]

    @property
    def max_x(self):
        return self.target_x[1]

    @property
    def min_y(self):
        return self.target_y[0]

    @property
    def max_y(self):
        return self.target_y[1]

    def step(self, steps=1):
        for _ in range(steps):
            self.x += self.dx
            self.y += self.dy
            self.dx -= self.dx // max(1, abs(self.dx))
            self.dy -= 1
            self.max_height = max(self.max_height, self.y)
    
    def shoot(self):
        while not self.is_overshot():
            self.step()
            if self.on_target():
                return True
        return False

    def on_target(self):
        return (
            self.min_x <= self.x <= self.max_x and
            self.min_y <= self.y <= self.max_y
        )
    
    def is_overshot(self):
        return self.is_x_overshot() or self.is_y_overshot()

    def is_x_overshot(self):
        return self.x > self.max_x

    def is_y_overshot(self):
        return self.y < self.min_y


def run() -> tuple(Solution, Solution):
    data: Dataset = day(17, parse_target)
    hits = list(all_hits(data))
    return (
        max(hits),
        len(hits)
    )


if __name__ == '__main__':
    print(run())
