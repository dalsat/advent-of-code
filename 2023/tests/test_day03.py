from adventofcode.day03 import Day03

input1 = str(
    """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
).split('\n')

input2 = input1

result1 = 4361
result2 = 467835


def test_part1():
    result = Day03(input1).part1()
    assert result == result1


def test_valid_numbers():
    inputs = (
        (['35-....661'], 35),
        (['35.....662'], 0),
        (['35....663-'], 663),
        (['35....-664'], 664),
        (['35....665.-2.'], 2),
    )

    for input, expected in inputs:
        actual = Day03(input).part1()
        assert actual == expected


def test_part2():
    result = Day03(input2).part2()
    assert result == result2
