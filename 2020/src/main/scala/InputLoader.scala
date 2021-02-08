package me.dalsat.adventofcode

import scala.io.Source


abstract class InputLoader(val day: Int) extends App {

  type Dataset = Seq[String]

  protected val inputDirectory: String = s"input/day-${day}"
  lazy val sample: Dataset = readSample()
  lazy val input: Dataset = readInput()

  @deprecated var dataset: Dataset = sample

  @deprecated def setSample(): Unit = dataset = sample
  @deprecated def setInput(): Unit = dataset = input

  def readFromFile(filename: String): Dataset = Source.fromResource(s"${inputDirectory}/${filename}").getLines().toList

  def readSample(): Dataset = readFromFile("sample.txt")

  def readInput(): Dataset = readFromFile("input.txt")

  def done: Unit = println(s"Day ${day} done")
}
