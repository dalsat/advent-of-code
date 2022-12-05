import functools

from aoc import load_day


__day__ = 3


def score_for(item: str) -> int:
    code = ord(item)
    if code >= 97:
        return code - 96
    else:
        return code - 38  # 65 - 27 = 38


def part1(data):

    def split_line(line: str) -> tuple[str, str]:
        mid = len(line) // 2
        return (line[:mid], line[mid:])

    def parse_input(lines: list[str]) -> list[tuple[str, str]]:
        return list(map(split_line, lines))

    def find_common(rucksack):
        common_items = (set(rucksack[0]).intersection(set(rucksack[1])))
        assert len(common_items) == 1
        return list(common_items)[0]
    
    return sum(score_for(find_common(item)) for item in parse_input(data))



def part2(data):

    def parse_input(data):
        elves = iter(filter(lambda x: x, data))
        try:
            while elves:
                yield next(elves), next(elves), next(elves)
        except StopIteration:
            pass

    def find_common(group):
        common_item = functools.reduce(lambda a, b: set(a).intersection(set(b)), group)
        assert len(common_item) == 1
        return list(common_item)[0]

    return sum(score_for(find_common(item)) for item in parse_input(data))



data = load_day(__day__)

if __name__ == '__main__':
    print(f'Day {__day__}: {part1(data)}, {part2(data)}')
