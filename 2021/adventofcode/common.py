import sys


Dataset = list[str]
Solution = str


def day(day: int, apply=lambda e: e) -> Dataset:
    try:
        with open(f'input/day-{day}.txt') as file:
            return list([apply(line.strip()) for line in file.readlines()])
    except FileNotFoundError as e:
        print(e, file=sys.stderr)
        sys.exit(-1)


def count(function, data):
    return len(list(filter(function, data)))
