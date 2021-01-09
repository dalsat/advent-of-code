package me.dalsat.adventofcode

import scala.annotation.tailrec


object Day9 extends App {

  //  val c = new Cypher(5)

  val c = new Cypher(25)
  c.setInput()

  val target = c.findFirstInvalid
  println(target)

  val result = c.findContiguousNumbersSummingTo(target)
  println(result)
  println((result.map(v => v._1 + v._2)).get)

  println("Day 9 done")
}


class Cypher(val preambleSize: Int = 25) extends InputLoader(9) {

  lazy val intDataset: Seq[Long] = dataset map (_.toLong)

  /**
   * Validate the number at index using the values from (index - 1 - preambleSize) to (index - 1) as preamble
   */
  def validateAt(index: Int): Boolean = {
    val preamble = intDataset.slice(index - preambleSize, index)
    //    println(s"validating ${intDataset(index)} with preamble: ${preamble}")
    preamble.combinations(2).find(each => (each(0) != each(1)) && each(0) + each(1) == intDataset(index)).isDefined
  }

  def findFirstInvalid: Long = intDataset(((preambleSize to intDataset.length) find (!validateAt(_))).get)

  //  def findInvalid: Seq[Long] = ((preambleSize to intDataset.length) map (!validateAt(_))).filter(e => e).map(e => intDataset(e))
  def findContiguousNumbersSummingTo(target: Long) = {

    @tailrec
    def testIntervalFrom(sequence: List[Long], values: Seq[Long]): List[Long] =
      if (((values.head :: sequence).sum) == target) {
        println(s"match: sum=${(values.head :: sequence)}, target=${target}, head=${values.head}")
        (values.head :: sequence)
      }
      else if (((values.head :: sequence).sum) > target) Nil
      else testIntervalFrom((values.head :: sequence), values.tail)


    def iterateValues(values: Seq[Long]): Option[(Long, Long)] = values match {
      case Nil => None
      case x :: xs => {
        val result = testIntervalFrom(Nil, x :: xs)
        if (!result.isEmpty) Some(result.min, result.max)
        else iterateValues(xs)
      }
    }

    iterateValues(intDataset)
  }
}

