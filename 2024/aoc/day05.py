from __future__ import annotations

from collections import UserDict, UserList, defaultdict
from dataclasses import dataclass
from typing import Self

from rich import print

from aoc.core import read_day

type Node = int


class Update(UserList):
    def middle_page(self):
        assert len(self) % 2 != 0
        return self[len(self) // 2]

    @classmethod
    def parse(cls, a_string: str) -> Self:
        return cls(int(each) for each in a_string.split(","))


class RuleSet[T]:
    def __init__(self):
        self.inbound: defaultdict[list[T], T] = defaultdict(list)
        self.outbound: defaultdict[list[T], T] = defaultdict(list)

    def add_edge(self, source: T, destination: T) -> None:
        self.outbound[source].append(destination)
        self.inbound[destination].append(source)

    def ordered(self):
        return sorted((k, len(v)) for k, v in self.inbound.items())


def parse_data(data: str):
    rules, pages = data.split("\n\n")

    return (parse_rules(rules), parse_pages(pages))


def parse_rules(rules: str):
    rule_set = RuleSet()
    for line in rules.splitlines():
        key, value = line.split("|")
        rule_set.add_edge(int(key), int(value))
    return rule_set


def parse_pages(pages: str):
    return [Update.parse(line) for line in pages.splitlines()]


data = read_day(5)
rules, pages = parse_data(data)

print(rules)
print(pages)
print(rules.ordered())

print(rules.outbound)
