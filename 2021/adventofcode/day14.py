from collections import Counter
from itertools import pairwise

from common import day


def parse_data(data):
    return data[0], parse_rules(data[2:])


def parse_rules(rules: list[str]):
    return dict(map(lambda row: row.split(" -> "), rules))


class Reaction:
    def __init__(self, formula, rules):
        self.formula = formula
        self.rules = rules
        self.counts = Counter("".join(e) for e in pairwise(formula))

    def step(self, steps=1):
        for step in range(steps):
            new_counts = Counter()
            for item, count in self.counts.items():
                middle = self.rules[item]
                new_counts[item[0] + middle] += count
                new_counts[middle + item[1]] += count
            self.counts = new_counts
        return self

    def count(self):
        counts = Counter()
        for couple, count in self.counts.items():
            counts[couple[0]] += count
        counts[self.formula[-1]] += 1

        counts = counts.most_common(len(counts))
        _, max_value = counts[0]
        _, min_value = counts[-1]
        return max_value - min_value


def run() -> tuple[int, int]:
    data = day(14)
    formula, rules = parse_data(data)
    return (
        Reaction(formula, rules).step(10).count(),
        Reaction(formula, rules).step(40).count(),
    )


print(run())
