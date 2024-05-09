from adventofcode.day02 import Day02


input1 = str(
    """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
).split('\n')

input2 = input1

result1 = 8
result2 = 2286


def test_day02_part1():
    result = Day02(input1).part1()
    assert result == result1


def test_day02_part2():
    result = Day02(input2).part2()
    assert result == result2
