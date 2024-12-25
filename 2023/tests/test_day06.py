from adventofcode.day06 import Day06


input1 = str(
    """Time:      7  15   30
Distance:  9  40  200"""
).split("\n")

input2 = input1

result1 = 288
result2 = 71503


def test_part1():
    result = Day06(input1).part1()
    assert result == result1


def test_part2():
    result = Day06(input2).part2()
    assert result == result2
