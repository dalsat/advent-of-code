from __future__ import annotations
import itertools

from common import day, Dataset, Solution


class Graph:

    def __init__(self, paths):
        self.edges = {}
        self.parse_paths(paths)

    def parse_paths(self, paths):
        for start, end in paths:
            if start not in self.edges:
                self.edges[start] = set()
            if end not in self.edges:
                self.edges[end] = set()

            if start != 'end' and end != 'start':
                self.edges[start].add(end)
            if start != 'start' and end != 'end':
                self.edges[end].add(start)

    def number_of_paths(self, with_second_visit=False):
        return len(self.all_paths(with_second_visit))

    def all_paths(self, with_second_visit):
        return list(self.find_paths('start', ['start'], set(), with_second_visit))

    def find_paths(self, current_node, current_path, tabu, with_second_visit):
        if current_node == 'end':
            return [current_path]
        
        if current_node.islower():
                tabu.add(current_node)

        next_paths = []
        for next_node in self.edges[current_node]:
            next_with_second_visit = with_second_visit
            if with_second_visit or next_node not in tabu:
                if next_node in tabu:
                    next_with_second_visit = False
                
                next_paths += self.find_paths(
                    next_node, current_path + [next_node],
                    tabu.copy(), next_with_second_visit)
                
        return next_paths


def run() -> tuple(Solution, Solution):
    data: Dataset = day(12, lambda line: line.split('-'))
    caves = Graph(data)
    return (
        caves.number_of_paths(),
        caves.number_of_paths(with_second_visit=True)
    )

print(run())
