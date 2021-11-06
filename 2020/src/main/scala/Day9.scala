package me.dalsat.adventofcode

import scala.annotation.tailrec


object Day9 extends Solution(9):


  override def part1 = target

  override def part2 = c.findContiguousNumbersSummingTo(target).map(v => v._1 + v._2).get

  val c = new Cypher(25)(input)

  val target = c.findFirstInvalid


  class Cypher(val preambleSize: Int = 25)(dataset: Dataset):

    lazy val intDataset: Seq[Long] = dataset map (_.toLong)

    /**
     * Validate the number at index using the values from (index - 1 - preambleSize) to (index - 1) as preamble
     */
    def validateAt(index: Int): Boolean = {
      val preamble = intDataset.slice(index - preambleSize, index)
      preamble.combinations(2).find(each => (each(0) != each(1)) && each(0) + each(1) == intDataset(index)).isDefined
    }

    def findFirstInvalid: Long = intDataset(((preambleSize to intDataset.length) find (!validateAt(_))).get)

    def findContiguousNumbersSummingTo(target: Long) = {

      @tailrec
      def testIntervalFrom(sequence: List[Long], values: Seq[Long]): List[Long] =
        if ((values.head :: sequence).sum) == target then
          (values.head :: sequence)
        else if ((values.head :: sequence).sum) > target then
          Nil
        else
          testIntervalFrom((values.head :: sequence), values.tail)


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
