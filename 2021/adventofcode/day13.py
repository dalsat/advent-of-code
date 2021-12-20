from __future__ import annotations

from common.typing import Char, Point
from common import day, Dataset, Solution, parse_numbers

Instruction = tuple[Char, int]

def parse_data(data):
    lines = iter(data)

    points: list[Point] = []
    while line := next(lines):
        points.append(tuple(parse_numbers(line)))
    
    folds: list[Instruction] = []
    while line := next(lines, None):
        axis, position = tuple(line.split()[-1].split('='))
        folds.append((axis, int(position)))
    
    return (points, folds)


def fold_all(points: list[Point], folds: list[Instruction], number_of_folds=None):
    points = set(points)

    if number_of_folds:
        folds = folds[:number_of_folds]
    for fold in folds:
        points = fold_points(points, fold)
    
    return points
        

def fold_points(points: set[Point], fold: Instruction):
    axis, position = fold
    new_points = points.copy()

    for point in points:
        x, y = point
        if axis == 'x' and x > position:
            x = 2 * position - x
            new_points.remove(point)
            new_points.add((x, y))
        elif axis == 'y' and y > position:
            y = 2 * position - y
            new_points.remove(point)
            new_points.add((x, y))
    return new_points


def print_code(points):
    max_x = max(map(lambda p: p[0], points))
    max_y = max(map(lambda p: p[1], points))

    return '\n'.join(
        ''.join('*' if (x, y) in points else ' '
        for x in range(max_x + 1))
        for y in range(max_y + 1)
    )


def run() -> tuple(Solution, Solution):
    data: Dataset = day(13)
    points, folds = parse_data(data)
    return (
        len(fold_all(points, folds, 1)),
        print_code(fold_all(points, folds)),
    )

print(run())
