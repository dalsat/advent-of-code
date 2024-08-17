from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from functools import reduce
from typing import Callable

from common import day, Dataset, Solution


# def parse_line(line: str):
#     return parse_number(eval(line))


# def parse_number(number: str):
#     if type(number) == int:
#         return Number(number)
#     else:
#         return Pair(*(map(parse_number, number)))


# class AbstractPair(ABC):

#     # def __add__(self, other):
#     #     print(f'addition: {self} + {other}')
#     #     return Pair(self, other).reduce()

#     @classmethod
#     @abstractmethod
#     def reduce(cls):
#         pass

#     @property
#     @classmethod
#     @abstractmethod
#     def magnitude(cls) -> int:
#         pass


# @dataclass
# class Pair(AbstractPair):
#     left: AbstractPair
#     right: AbstractPair

#     def reduce(self):
#         return self
    
#     @property
#     def magnitude(self):
#         return (self.left.magnitude * 3) + (self.right.magnitude * 2)
    
#     def __repr__(self):
#         return f'[{self.left}, {self.right}]'


# @dataclass
# class Number(AbstractPair):
#     value: int

#     def reduce(self):
#         return self

#     def split(self):
#         return Pair(Number(self.value //2), Number((self.value +1) //2))
    
#     @property
#     def magnitude(self):
#         return self.value

#     def __repr__(self):
#         return str(self.value)


# def run() -> tuple[Solution, Solution]:
#     data: Dataset = day(18, eval)
#     return (
#         data[0],
#         ''
#     )


# if __name__ == '__main__':
    # print(run())



@dataclass
class Expression:
    content: int | list[Expression]

    def is_number(self) -> bool:
        return isinstance(self.content, int)
    
    def is_pair(self) -> bool:
        return isinstance(self.content, list)

    @property
    def number(self) -> int:
        assert isinstance(self.content, int)
        return self.content

    @number.setter
    def number(self, value) -> None:
        assert isinstance(value, int)
        self.content = value

    @property
    def left(self) -> Expression:
        assert isinstance(self.content, list)
        return self.content[0]

    @property
    def right(self) -> Expression:
        assert isinstance(self.content, list)
        return self.content[1]

    @classmethod
    def parse(cls, expression: list | int):
        if isinstance(expression, int):
            return Expression(expression)
        else:
            left = cls.parse(expression[0])
            right = cls.parse(expression[1])
            return Expression([left, right])

    def __repr__(self):
        if self.is_number():
            return str(self.content)
        else:
            return f'[{self.left}, {self.right}]'



class ExpressionExploder:

    depth_limit = 4

    def __init__(self):
        self.previous: Expression | None = None
        self.explode_root: Expression | None = None
        self.depth = 0



    def visit(self, root: Expression):
        print(f'visit {root} at depth {self.depth}')
        if root.is_number():
            if self.explode_root is not None:
                self.next = root
                self.explode()
            self.previous = root

        else:
            if self.depth >= self.depth_limit:
                self.explode_root = root
                return

            self.depth += 1
            self.visit(root.left)
            self.visit(root.right)
            self.depth -= 1


    def explode(self):
        print('explode')
        assert self.explode_root and self.explode_root.is_pair(), self.explode_root

        if self.previous is not None:
            self.previous.number += self.explode_root.left.number

        if next is not None:
            self.next.number += self.explode_root.right.number

        self.explode_root.content = 0

    @classmethod
    def reduce(cls, expression):
        exploder = ExpressionExploder()
        return exploder.visit(expression)



data = day(18, eval)

expression = Expression.parse(data[0])
# expression = Expression.parse([1, 0])
print(expression)
ExpressionExploder.reduce(expression)
print(expression)


# sample = data[0]

# print(sample)
# print(list(tree_visitor(sample)))



# Pair = list[int, int] } int

# def parse_line(line: list)
# print(type(data[0][0][0][0][0]))


# def parse_number(number: str):
#     if type(number) == int:
#         return Number(number)
#     else:
#         return Pair(*(map(parse_number, number)))



# sample = '''[1,1]
# [2,2]
# [3,3]
# [4,4]'''

# expressions = list(map(parse_line, sample.split('\n')))

# print(expressions)
# print(reduce(lambda a, b: a + b, expressions))

# print(Nothing() + Number(2))