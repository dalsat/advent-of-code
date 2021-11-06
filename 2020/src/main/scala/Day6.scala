package me.dalsat.adventofcode

import scala.annotation.tailrec
import scala.math.pow


object Day6 extends Solution(6):


  override def part1 = CustomCounter(input).count

  override def part2 = AdvancedCustomCounter(input).count


  class CustomCounter(dataset: Dataset):

    def count: Int = groups.map(countGroup).sum

    private def groups = dataset.mkString(" ").split("\\s\\s")

    protected def countGroup(group: String): Int =
      group.split("").filter(!_.isBlank).toSet.size


  class AdvancedCustomCounter(dataset: Dataset) extends CustomCounter(dataset):
    override protected def countGroup(group: String): Int =
      group.split("\\s+").map(_.split("").toSet).reduceLeft((one, two) => one.intersect(two)).size
