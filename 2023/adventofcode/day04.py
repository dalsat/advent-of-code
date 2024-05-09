from array import array
from dataclasses import dataclass

from .aoc import Solution, parse_numbers, report


@dataclass(frozen=True)
class Ticket:
    id: int
    winning_numbers: set[int]
    card_numbers: set[int]

    def matches(self):
        return len(self.winning_numbers & self.card_numbers)

    def points(self) -> int:
        number_of_matches = self.matches()
        if not number_of_matches:
            return 0
        return 2 ** (number_of_matches - 1)


class Day04(Solution):
    def __init__(self, data: list[str]):
        self.tickets = [self._parse_line(line) for line in data]

    def part1(self) -> int:
        return sum(ticket.points() for ticket in self.tickets)

    def part2(self) -> int:
        counts = array('L')
        for ticket in sorted(self.tickets, key=lambda t: t.id, reverse=True):
            matches = ticket.matches()
            if not matches:
                counts.append(1)
            else:
                counts.append(sum(counts[-matches:]) + 1)

        return sum(counts)

    @staticmethod
    def _parse_line(line: str) -> Ticket:
        id_branch, rest = line.split(':')
        winning_numbers_branch, ticket_numbers_branch = rest.split('|')
        return Ticket(
            id=parse_numbers(id_branch)[0],
            winning_numbers=set(parse_numbers(winning_numbers_branch)),
            card_numbers=set(parse_numbers(ticket_numbers_branch)),
        )


report(Day04, 4, __name__)
