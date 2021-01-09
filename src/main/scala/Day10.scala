package me.dalsat.adventofcode

import scala.annotation.tailrec


object Day10 extends App {

  val as = new AdapterSearch

  as.setInput()

  println(s"Part one: ${as.solutionOne}")

  println(s"Part two: ${as.search}")

  println("Day 10 done")
}


class AdapterSearch extends InputLoader(10) {

  lazy val adapters: List[Int] = dataset.map(_.toInt).sorted.toList

  lazy val fullChain = 0 :: adapters ::: List(targetJoltage)

  lazy val targetJoltage: Int = adapters.max + 3

  private var cache = collection.mutable.Map.empty[Int, Long]

  def differences: List[Int] = couples.map { case (first, second) => first - second }

  def couples: List[(Int, Int)] = (adapters ::: List(targetJoltage)) zip (0 :: adapters)

  def countDifferenceAdapter(difference: Int) = differences.count(_ == difference)

  def solutionOne = countDifferenceAdapter(1) * countDifferenceAdapter(3)

  def search: Long =

    def searchLoop(currentAdapter: Int): Long =
      cache.getOrElseUpdate(currentAdapter, {
        if (currentAdapter == targetJoltage) 1
        else validValuesFor(currentAdapter).map(searchLoop(_)).sum
      })

    searchLoop(0)

  def validValuesFor(adapter: Int): Seq[Int] = fullChain filter (validateConnection(adapter, _))

  def validateConnection(current: Int, next: Int): Boolean = (current < next) && (next - current) <= 3

}

