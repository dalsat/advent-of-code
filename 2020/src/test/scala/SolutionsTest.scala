package me.dalsat.adventofcode

import org.scalatest.flatspec.AnyFlatSpec
import org.scalatest.matchers.should


class SolutionsTest extends AnyFlatSpec with should.Matchers:

  Map(
    Day1 -> (468051, 272611658),
    Day2 -> (600, 245),
    Day3 -> (259, 2224913600L),
    Day4 -> (237, 172),
    Day5 -> (965, 524),
    Day6 -> (6625, 3360),
    Day7 -> (259, 45018),
    Day8 -> (1939, 2212),
    Day9 -> (1492208709L, 238243506L),
    Day10 -> (2312, 12089663946752L),
    Day11 -> (2281, 2085),
    Day12 -> (2297, 89984),
    Day13 -> (3385, 600689120448303L),
    Day14 -> (11926135976176L, 4330547254348L),
    Day15 -> (1015, 201),
    Day16 -> (22073, 1346570764607L),
    Day17 -> (265, 1936),
    //      Day18 -> (1, 2),
    //      Day19 -> (1, 2),
    //      Day20 -> (1, 2),
    //      Day21 -> (1, 2),
    //      Day22 -> (1, 2),
    //      Day23 -> (1, 2),
    //      Day24 -> (1, 2),
    //      Day25 -> (1, 2)
  ) foreach { case (day, (part1, part2)) =>
    day.getClass.toString should "give the correct solution" in {
      day.part1 should be(part1)
      day.part2 should be(part2)
    }
  }