from __future__ import annotations

import itertools
from dataclasses import dataclass, field

from aoc import load_day, parse_number


__day__ = 16

def part1(valves):

    # key -> (visited + pressure + time)
    # if key(id, open_valves=), value(pressure<= and time>=) -> drop
    bounds = {}

    def max_flow(node: Valve, pressure: int, open_valves: set[Valve], time_left: int):
        if time_left == 0:
            return pressure
        
        time_left -= 1
        pressure += sum(valve.flow for valve in open_valves)

        # sorted_open_valves = tuple(sorted(v.id for v in open_valves))
        # bound_pressure, bound_time = bounds.get((node.id, sorted_open_valves), (-1, -1))

        # if pressure < bound_pressure and time_left > bound_time:
        #     return -1  # cut the computation
        
        # bounds[(node.id, sorted_open_valves)] = (max(bound_pressure, pressure), max(bound_time, time_left))

        if len(open_valves) == len(valves):  # all valves are open
            return max_flow(node, pressure, open_valves, time_left)

        if node.flow > 0 and node not in open_valves:  # open valve
            return max_flow(node, pressure, open_valves | {node}, time_left)

        max_pressure = max(
            max_flow(valves[tunnel], pressure, open_valves, time_left)
            for tunnel in node.tunnels
        )

        return max_pressure
    
    # return max_flow(valves['AA'], 0, set(), 15)


    def all_sequences():
        all_valves = list(valves.valves.keys())
        
        count = 0
        for p in itertools.permutations(all_valves):
            count += 1
        
        print(f'final count: {count}')
        

    all_sequences()

    # def check_cycles(valve, visited):
    #     if valve in visited:
    #         print(f'cycle detected: {visited}, {valve}')
    #     else:
    #         for tunnel in valve.tunnels:
    #             check_cycles(valves[tunnel], visited + [valve])

    # check_cycles(valves['AA'], [])

def part2(data):
    ...


class Valves:

    def __init__(self, data) -> None:
        valves = [Valve.parse(line) for line in data]
        self.valves: dict[str, Valve] = {valve.id: valve for valve in valves}

    def flow(self, open_valves: set[Valve]):
        return sum(valve.flow for valve in open_valves)
    
    def __len__(self):
        return len(self.valves)
    
    def __getitem__(self, item):
        return self.valves[item]


@dataclass(frozen=True)
class Valve:
    id: str
    flow: int = field(compare=False)
    tunnels: list[str] = field(compare=False)

    @classmethod
    def parse(cls, spec: str):
        tokens = spec.split(' ')
        return cls(
            id = tokens[1],
            flow = int(parse_number(tokens[4])),
            tunnels = [token.strip(',') for token in tokens[9:]]
        )


data = Valves(load_day(__day__))


if __name__ == '__main__':
    print(f'Day {__day__}: {part1(data)}, {part2(data)}')
