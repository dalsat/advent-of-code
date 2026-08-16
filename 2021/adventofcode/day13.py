from collections.abc import Iterable

from common import day, parse_numbers
from common.typing import Char, Point

Instruction = tuple[Char, int]


def parse_data(data: list[str]) -> tuple[list[Point], list[tuple[Char, int]]]:
    lines = iter(data)

    points: list[Point] = []
    while line := next(lines):
        point = tuple(parse_numbers(line))
        assert len(point) == 2
        points.append(point)

    folds: list[Instruction] = []
    while line := next(lines, None):
        axis, position = tuple(line.split()[-1].split("="))
        folds.append((axis, int(position)))

    return (points, folds)


def fold_all(
    points: Iterable[Point], folds: list[Instruction], number_of_folds=None
) -> list[Point]:
    points = set(points)

    if number_of_folds:
        folds = folds[:number_of_folds]
    for fold in folds:
        points = fold_points(points, fold)

    return list(points)


def fold_points(points: set[Point], fold: Instruction) -> set[Point]:
    axis, position = fold
    new_points = points.copy()

    for point in points:
        x, y = point
        if axis == "x" and x > position:
            x = 2 * position - x
            new_points.remove(point)
            new_points.add((x, y))
        elif axis == "y" and y > position:
            y = 2 * position - y
            new_points.remove(point)
            new_points.add((x, y))
    return new_points


def print_code(points) -> str:
    max_x = max(p[0] for p in points)
    max_y = max(p[1] for p in points)

    return "\n".join(
        "".join("*" if (x, y) in points else " " for x in range(max_x + 1))
        for y in range(max_y + 1)
    )


def run() -> tuple[int, str]:
    data = day(13)
    points, folds = parse_data(data)
    return (
        len(fold_all(points, folds, 1)),
        print_code(fold_all(points, folds)),
    )


print(run())
