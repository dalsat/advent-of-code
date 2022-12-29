from __future__ import annotations

from aoc import load_day


__day__ = 25


def part1(data):
    return to_snafu(sum(map(to_decimal, data)))


def part2(data):
    ...


def to_decimal(number: str):
    
    decimal = 0

    def convert_digit(digit: str) -> int:
        match digit:
            case d if d.isdigit():
                return int(d)
            case '-':
                return -1
            case '=':
                return -2
            case _:
                raise ValueError(f'unable to parse character {d}')

    for position, digit in enumerate(reversed(number)):
        decimal += convert_digit(digit) * 5 ** position

    return decimal


def to_snafu(number: int) -> str:
    snafu = []

    char_mapping = {
        -1: '-',
        -2: '=',
    }
    while number > 0:
        digit = number % 5
        if digit > 2:
            number += 5
            digit = char_mapping[digit - 5]
        snafu.append(str(digit))
        number //= 5
    
    return ''.join(reversed(snafu))


data = load_day(__day__)


if __name__ == '__main__':
    print(f'Day {__day__}: {part1(data)}, {part2(data)}')
