from collections.abc import Callable

from common import day, parse_numbers


def linear_cost_function(start: int, end: int) -> int:
    return abs(start - end)


def quadratic_cost_function(start: int, end: int) -> int:
    distance = linear_cost_function(start, end)
    return (distance + 1) * distance // 2


def local_search(data: list[int], cost_at: Callable[[int], int]) -> int:

    def min_neighbor(index):
        neighbors = (
            (cost_at(index + delta), delta)
            for delta in (-1, 1)
            if 0 <= index + delta < len(data)
        )
        return min(neighbors, key=lambda t: t[0])

    index = len(data) // 2
    while True:
        current_cost = cost_at(index)
        neighbor_cost, neighbor_index = min_neighbor(index)
        if neighbor_cost < current_cost:
            index += neighbor_index
        else:
            return current_cost


def find_optimal_position(
    data: list[int], cost_function: Callable[[int, int], int]
) -> int:
    cumulative_cost_function: Callable[[int], int] = lambda index: sum(
        cost_function(index, each) for each in data
    )

    min_neighbor = local_search(data, cumulative_cost_function)
    return min_neighbor


def run() -> tuple[int, int]:
    data = day(7, apply=parse_numbers, one_line=True)
    return (
        find_optimal_position(data, linear_cost_function),
        find_optimal_position(data, quadratic_cost_function),
    )


print(run())
