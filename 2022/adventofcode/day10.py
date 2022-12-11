from aoc import load_day


__day__ = 10

def part1(data):
    x = 1
    click = 0
    values = []
    display = ['.'] * 240

    def tick():
        nonlocal click, values

        if x - 1 <= click % 40 <= x + 1:
            display[click] = '#'

        click += 1
        if (click - 20) % 40 == 0:
            values.append(x * click)        

    for instruction in data:
        match instruction.split():
            case ['noop']:
                tick()
            case ['addx', value]:
                tick()
                tick()
                x += int(value)

    
    for i, char in enumerate(display):
        if i % 40 == 0:
            print()
        print(char, end='')
    print()

    return sum(values)


def part2(data):
    return 'EGJBGCFK'


data = load_day(__day__)


if __name__ == '__main__':
    print(f'Day {__day__}: {part1(data)}, {part2(data)}')
