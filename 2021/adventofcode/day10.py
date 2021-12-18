from __future__ import annotations
from functools import reduce

from common import day, Dataset, Solution


mapping = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}

openings = set(mapping.values())
closings = set(mapping.keys())


def validate_line(line):
    stack = []

    for current in line:
        if current in openings:
            stack.append(current)
        else:
            matched = stack.pop()
            if mapping[current] != matched:
                return (False, current)
    return (True, stack)

def corrupted_score(data: Dataset) -> Solution:
    scores = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    return sum(scores[each] for valid, each in map(validate_line, data) if not valid)


def score_incomplete_line(chars):
    scores = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4
    }
    
    score = reduce(lambda acc, each: acc * 5 + scores[each], chars, 0)
    return score


def autocomplete(data: Dataset):
    return list(score_incomplete_line(list(reversed(line)))
        for valid, line in map(validate_line, data) if valid)

def autocomplete_score(data: Dataset) -> Solution:
    scores = sorted(autocomplete(data))
    middle = len(scores) // 2
    return scores[middle]

def run() -> tuple(Solution, Solution):
    data = day(10)
    return (
        corrupted_score(data),
        autocomplete_score(data)
    )

print(run())
