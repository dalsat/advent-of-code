import itertools

from aoc import load_day, parse_numbers


__day__ = 5

def part1(data, maintain_order=False):
    state, moves = parse_input(data)

    def execute_move(move):
        nonlocal state

        times, start, end = move
        popped = [state[start-1].pop() for _ in range(times)]

        if maintain_order:
            popped = reversed(popped)

        for each in popped:
            state[end-1].append(each)

    for move in moves:
        execute_move(move)

    return ''.join(each[-1] for each in state)


def part2(data):
    return part1(data, maintain_order=True)


def parse_input(data):

    def parse_state(initial_state: str):

        def parse_row(row: str):
            return [row[i] if row[i].isalpha() else None for i in range(1, len(row), 4)]

        rows = list(map(parse_row, initial_state.split('\n')[:-1]))
        return list(list(filter(bool, reversed(each))) for each in zip(*rows))
    
    def parse_moves(moves):
        return tuple(parse_numbers(line) for line in moves.split('\n') if line)

    return (parse_state(data[0]), parse_moves(data[1]))


data = load_day(__day__, separator='\n\n')


if __name__ == '__main__':
    print(f'Day {__day__}: {part1(data)}, {part2(data)}')
