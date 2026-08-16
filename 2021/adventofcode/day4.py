from collections.abc import Generator, Iterable
from itertools import takewhile

from common import any_of, day, parse_numbers


def parse_data(data: list[list[int]]) -> tuple[list[int], list[Board]]:
    numbers = data[0]
    boards = parse_boards(data[2:])
    return numbers, boards


def parse_boards(lines: list[list[int]]) -> list[Board]:
    def board_generator() -> Iterable[list[list[int]]]:
        lines_iter = iter(lines)
        while lines_iter:
            yield list(takewhile(bool, lines_iter))

    return [Board(each) for each in takewhile(bool, board_generator())]


class Board:
    def __init__(self, board: list[list[int]]):
        self.rows = list(map(set, board))
        transposed_columns = [
            [row[index] for row in board] for index in range(len(board))
        ]
        self.columns = list(map(set, transposed_columns))

    def next_number(self, number: int) -> None:
        for row in self.rows:
            row.discard(number)
        for col in self.columns:
            col.discard(number)

    def is_winning(self) -> bool:
        win_condition = lambda each: not bool(each)
        return any_of(self.rows, win_condition) or any_of(self.columns, win_condition)

    def score(self) -> int:
        return sum(map(sum, self.rows))


def winning_boards(
    boards: list[Board], numbers: list[int]
) -> Generator[tuple[Board, int]]:
    valid_boards = set(boards)
    for number in numbers:
        for board in valid_boards:
            board.next_number(number)
            if board.is_winning():
                valid_boards = valid_boards.copy()
                valid_boards.remove(board)
                yield board, number


def first_winning_score(boards: list[Board], numbers: list[int]) -> int:
    board, number = next(winning_boards(boards, numbers))
    return board.score() * number


def last_winning_score(boards: list[Board], numbers: list[int]) -> int:
    board, number = list(winning_boards(boards, numbers))[-1]
    return board.score() * number


def run() -> tuple[int, int]:
    data = day(4, apply=parse_numbers)

    numbers, boards = parse_data(data)
    return (first_winning_score(boards, numbers), last_winning_score(boards, numbers))


print(run())
