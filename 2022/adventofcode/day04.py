import functools

from aoc import load_day


__day__ = 4

def part1(data):
    def intervals_overlap(first, second) -> bool:
        return (
            (first[0] <= second[0] and second[1] <= first[1])
            or (second[0] <= first[0] and first[1] <= second[1])
        )
    return sum(1 for first, second in data if intervals_overlap(first, second))


def part2(data):
    def intervals_overlap(first, second) -> bool:
        return bool(set(range(first[0], first[1] + 1)).intersection(set(range(second[0], second[1] + 1))))
    
    return sum(1 for first, second in data if intervals_overlap(first, second))

def parse_input(data):
    def parse_row(row: str):
        return tuple(tuple(map(int, token.split('-'))) for token in row.split(','))

    return list(parse_row(row) for row in data)

data = parse_input(load_day(__day__))
# data = parse_input('''2-4,6-8
# 2-3,4-5
# 5-7,7-9
# 2-8,3-7
# 6-6,4-6
# 2-6,4-8'''.split('\n'))

if __name__ == '__main__':
    print(f'Day {__day__}: {part1(data)}, {part2(data)}')
