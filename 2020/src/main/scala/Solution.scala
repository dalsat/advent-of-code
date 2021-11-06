package me.dalsat.adventofcode

import scala.io.Source


type Dataset = Seq[String]
type SolutionType = Long


trait Solution(val day: Int):

  lazy val input: Dataset = InputLoader.readInput(day)

  def main(args: Array[String]): Unit = print(report)

  def part1: SolutionType

  def part2: SolutionType

  def report: String =
    s"""Day ${day}\nPart 1: ${part1}\nPart 2: ${part2}\ndone"""

end Solution


object InputLoader:
  protected val inputDirectory: String = "input"

  def readFromFile(filename: String): Dataset =
    Source.fromResource(s"${inputDirectory}/${filename}").getLines().toList

  def readInput(day: Int): Dataset = readFromFile(s"day-${day}.txt")
