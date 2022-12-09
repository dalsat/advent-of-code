from __future__ import annotations
from aoc import load_day, parse_numbers


__day__ = 8

def part1(data):

    return VisibleTreeMap(data).number_of_visible_trees()  # total: 9801


def part2(data):
    
    def scenic_score_direction(tree, r, c, direction):

        # move one step towards the direction
        if direction == 'up':
            r -= 1
        elif direction == 'down':
            r += 1
        elif direction == 'left':
            c -= 1
        elif direction == 'right':
            c += 1
        else:
            raise ValueError(f'invalid direction {direction}')

        # are we inside the boundaries?
        if not (0 <= r < len(data[0]) and 0 <= c < len(data)):
            return 0

        if tree <= data[r][c]:
            return 1
            
        return 1 + scenic_score_direction(tree, r, c, direction)

    def scenic_score(r, c):
        tree = data[r][c]

        return (
            scenic_score_direction(tree, r, c, 'up')
            * scenic_score_direction(tree, r, c, 'down')
            * scenic_score_direction(tree, r, c, 'left')
            * scenic_score_direction(tree, r, c, 'right')
        )

    return max(max(scenic_score(r, c) for c in range(len(data[0]))) for r in range(len(data)))


class VisibleTreeMap:
    def __init__(self, data: list[list[int]]):
        self.data: list[list[int]] = data
        self._visible_trees: set[tuple[int, int]] = set()
        self._visible_trees_horizontal()
        self._visible_trees_vertical()
    
    def _visible_trees_horizontal(self):
        for ri, row in enumerate(data):
            max_left = -1
            for ci, tree in enumerate(row):
                if max_left < tree:
                    self._visible_trees.add((ri, ci))
                    max_left = tree

            max_right = -1
            for ci, tree in reversed(list(enumerate(row))):
                if max_right < tree:
                    self._visible_trees.add((ri, ci))
                    max_right = tree


    def _visible_trees_vertical(self):
        for ci in range(len(data[0])):
            max_up = -1
            for ri in range(len(data)):
                tree = self.data[ri][ci]
                if max_up < tree:
                    self._visible_trees.add((ri, ci))
                    max_up = tree

            max_down = -1
            for ri in range(len(data) -1, -1, -1):
                tree = self.data[ri][ci]
                if max_down < tree:
                    self._visible_trees.add((ri, ci))
                    max_down = tree

    def number_of_visible_trees(self):
        return len(self._visible_trees)

    def __str__(self):
        def color_tree(tree: str, position: tuple[int, int]) -> str:
            if position in self._visible_trees:
                return f'\033[92m{tree}\033[0m'
            else:
                return tree
        
        return '\n'.join(
            [''.join([color_tree(str(each), (ri, ci)) for ci, each in enumerate(row)])
            for ri, row in enumerate(self.data)])

def parse_input(data: list[str]) -> list[list[int]]:
    return [[int(each) for each in line] for line in data]


data = parse_input(load_day(__day__))


if __name__ == '__main__':
    print(f'Day {__day__}: {part1(data)}, {part2(data)}')
