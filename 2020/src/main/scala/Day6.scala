package me.dalsat.adventofcode

import scala.annotation.tailrec
import scala.math.pow

object Day6 extends App {


  val cc = new AdvancedCustomCounter

  println(cc.count)

  cc.setInput()
  println(cc.count)
  println("Day 6 done")
}


class CustomCounter extends InputLoader(6) {

  def count: Int = groups.map(countGroup).sum

  private def groups = dataset.mkString(" ").split("\\s\\s")

  protected def countGroup(group: String): Int = {
    group.split("").filter(!_.isBlank).toSet.size
  }
}


class AdvancedCustomCounter extends CustomCounter {

  override protected def countGroup(group: String): Int =
    group.split("\\s+").map(_.split("").toSet).reduceLeft((one, two) => one.intersect(two)).size
}
