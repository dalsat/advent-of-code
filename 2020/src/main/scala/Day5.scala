package me.dalsat.adventofcode

import scala.annotation.tailrec
import scala.math.pow

object Day5  extends Solution(5):


  override def part1 = sd.findMax

  override def part2 = missing.max

  val sd = SeatDecoder(input)

  val full = (0 to 965).toSet

  val passes = sd.decodeAll().toSet

  val missing = full removedAll passes


  class SeatDecoder(dataset: Dataset):

    private case class Range(low: Int, high: Int):

      private def halfDelta: Int = (high - low) / 2

      def left: Range = Range(low, high - halfDelta)

      def right: Range = Range(low + halfDelta, high)


    def decode(code: String): Int =
      val positions = code.splitAt(7)
      seatHash(decodeSubstring(positions._1), decodeSubstring(positions._2))


    private def seatHash(row: Int, column: Int) = row * 8 + column


    private[adventofcode] def decodeSubstring(code: String): Int =
      loop(code.toList, Range(0, pow(2, code.length).toInt))

    @tailrec
    private def loop(code: List[Char], range: Range): Int = code match {
      case Nil => range.low
      case ('F' | 'L') :: xs => loop(xs, range.left)
      case ('B' | 'R') :: xs => loop(xs, range.right)
      case _ => throw Error("Impossible case reached")
    }

    def decodeAll(): Seq[Int] = dataset.map(decode)

    def findMax: Int = decodeAll().max
