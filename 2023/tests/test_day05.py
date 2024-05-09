from adventofcode.day05 import Day05


input1 = str(
    """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""
).split('\n')

input2 = input1

result1 = 35
result2 = -1


def test_part1():
    result = Day05(input1).part1()
    assert result == result1


def test_part2():
    result = Day05(input2).part2()
    assert result == result2


def test_seeds():
    expected = [79, 14, 55, 13]
    day = Day05(input1)
    assert day.seeds == expected
