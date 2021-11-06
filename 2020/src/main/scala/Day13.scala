package me.dalsat.adventofcode

import me.dalsat.adventofcode.Solution

import scala.annotation.tailrec
import scala.concurrent.Future
import concurrent.ExecutionContext.Implicits.global
import scala.concurrent.duration.DurationInt


object Day13 extends Solution(13):

  private val bs = BusScheduler(input)

  override def part1 =
    val result = bs.closestDeparture
    result._1 * result._2


  override def part2 = bs.findPart2Timestamp.toLong


  class BusScheduler(dataset: Dataset):

    val arrivalTime: Int = dataset.head.toInt

    lazy val busList: Seq[String] = dataset.tail.head.split(",").toList
    lazy val indexedBuses: Seq[(Int, Int)] = busList.zipWithIndex.filter((bus, index) => bus != "x").map((bus, index) => (bus.toInt, index))
    lazy val startBus: Int = indexedBuses(0)._1


    def closestDeparture = closestDepartureTo(arrivalTime)

    def closestDepartureTo(time: Int): (Int, Int) = busList.filter(_ != "x").map(_.toInt)
      .map(bus => (bus, bus - (time % bus)))
      .min(Ordering.by(_._2))


    // Part 2
    def findPart2Timestamp =
      @tailrec
      def loop(timestamp: BigInt, currentStep: BigInt, unprocessedBusList: Seq[(Int, Int)]): BigInt =
        unprocessedBusList match {
          case (bus, index) :: tail if (timestamp + index) % bus == 0 =>
            loop(timestamp, lcm(currentStep, bus), tail)
          case Nil => timestamp
          case _ => loop(timestamp + currentStep, currentStep, unprocessedBusList)
        }

      loop(0, 1, indexedBuses)


    def lcm(first: BigInt, second: BigInt): BigInt =
      first * second / gcd(first, second)


    def gcd(first: BigInt, second: BigInt) =
      LazyList
        .iterate((first, second)) { case (x, y) => (y, x % y) }
        .dropWhile(_._2 != 0).head._1.abs
