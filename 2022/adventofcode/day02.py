from aoc import load_day

__day__ = 2

data = [tuple(line.split()) for line in load_day(__day__) if line]

points_mapping = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}
    

def score_match(match):
    if match in (('A', 'X'), ('B', 'Y'), ('C', 'Z')):
        return 3
    elif match in (('C', 'X'), ('A', 'Y'), ('B', 'Z')):
        return 6
    else:
        return 0

def score_row(match):
    return score_match(match) + points_mapping[match[1]]


def total_score(matches):
    return sum(map(score_row, matches))


def part1(data):
    return total_score(data)


def part2(data):

    moves = {
        'X': {  # loose
            'A': 'Z',
            'B': 'X',
            'C': 'Y',
        },
        'Y': {  # draw
            'A': 'X',
            'B': 'Y',
            'C': 'Z',
        },
        'Z': {  # win
            'A': 'Y',
            'B': 'Z',
            'C': 'X',
        },
    }

    def select_move(match):
        opponent, outcome = match
        return moves[outcome][opponent]


    return sum(score_row((each[0], select_move(each))) for each in data)



if __name__ == '__main__':
    print(f'Day {__day__}: {part1(data)}, {part2(data)}')