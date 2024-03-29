from aoc import load_day


__day__ = 1


def parse_input(input: str):
    return list(
        list(int(each.strip()) for each in group.strip().split("\n")) for group in input
    )


def part1(data: list[list[int]]) -> int:
    return max(map(sum, data))


def part2(data: list[list[int]]) -> int:
    return sum(sorted(map(sum, data), reverse=True)[:3])


data = parse_input(load_day(1, separator="\n\n"))


if __name__ == '__main__':
    print(f'Day {__day__}: {part1(data)}, {part2(data)}')