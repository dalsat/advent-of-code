from adventofcode.day07 import Day07


input1 = str(
    """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""
).split("\n")

input2 = input1

result1 = 6440
result2 = 5905


def test_part1():
    result = Day07(input1).part1()
    assert result == result1


# def test_part2():
#     result = Day07(input2).part2()
#     assert result == result2
