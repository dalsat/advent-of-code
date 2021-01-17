package me.dalsat.adventofcode

import me.dalsat.adventofcode.Day11.Dataset

import scala.annotation.tailrec


object Day11 extends InputLoader(11) {

  //  val sm = new SeatingMap(sample, BaseSeatStrategy)
  //  val sm = new SeatingMap(input, BaseSeatStrategy)

//  val sm = new SeatingMap(sample, ExtendedSeatStrategy)
    val sm = new SeatingMap(input, ExtendedSeatStrategy)

  println(sm)
  println()
  println(sm.toFixedPoint)

  println(s"Day ${day} done")
}


class SeatingMap(val seats: Seq[Seq[SeatStatus]], val seatStrategy: SeatStrategy, val epoch: Int) {

  def this(dataset: Dataset, seatStrategy: SeatStrategy) = this(SeatingMap.parseDataset(dataset), seatStrategy, 0)

  lazy val width: Int = seats.length
  lazy val height: Int = seats.head.length

  override def toString: String = s"epoch (${epoch}): ${numberOfOccupiedSeats} occupied seats\n" +
    seats.map(row => row.map(cell => cell.display).mkString("")).mkString("\n")

  def next: SeatingMap = new SeatingMap(nextEpoch, seatStrategy, epoch + 1)

  def nextEpoch: Seq[Seq[SeatStatus]] = seats.zipWithIndex.map {
    case (row, x) => row.zipWithIndex.map {
      case (cell, y) => seatStrategy.next(x, y, this)
    }
  }

  def numberOfNeighboursFor(x: Int, y: Int): Int = neighboursFor(x, y).count(_ == SeatStatus.Occupied)

  def neighboursFor(x: Int, y: Int): Seq[SeatStatus] =
    this (x - 1)(y - 1) :: this (x)(y - 1) :: this (x + 1)(y - 1) ::
      this (x - 1)(y) :: this (x + 1)(y) ::
      this (x - 1)(y + 1) :: this (x)(y + 1) :: this (x + 1)(y + 1) :: Nil

  def apply(x: Int)(y: Int): SeatStatus =
    if (0 <= x && x < width && 0 <= y && y < height) seats(x)(y)
    else SeatStatus.Border

  def seatsEquals(other: SeatingMap): Boolean = seats == other.seats

  @tailrec
  final def toFixedPoint: SeatingMap =
    val nextMap = this.next
    if (seatsEquals(nextMap)) this
    else nextMap.toFixedPoint

  def numberOfOccupiedSeats: Int = seats.flatten.count(_ == SeatStatus.Occupied)
}

object SeatingMap {

  def parseDataset(dataset: Dataset) = dataset map (parseLine(_))

  def parseLine(line: String) = line map (SeatStatus.parse(_))

}

enum SeatStatus(val display: Char) {

  case Empty extends SeatStatus('L')

  case Occupied extends SeatStatus('#')

  case Floor extends SeatStatus('.')

  case Border extends SeatStatus('x')

}

object SeatStatus {
  def parse(char: Char) = char match {
    case 'L' => SeatStatus.Empty
    case '#' => SeatStatus.Occupied
    case '.' => SeatStatus.Floor
  }
}

trait SeatStrategy {
  val maxNumberOfNeighbours: Int

  def next(x: Int, y: Int, seatingMap: SeatingMap): SeatStatus =
    next(seatingMap(x)(y), numberOfNeighboursFor(x, y, seatingMap))

  def next(currentStatus: SeatStatus, numberOfNeightbours: Int): SeatStatus = currentStatus match
    case SeatStatus.Empty if numberOfNeightbours == 0 => SeatStatus.Occupied
    case SeatStatus.Occupied if maxNumberOfNeighbours <= numberOfNeightbours => SeatStatus.Empty
    case _ => currentStatus

  def numberOfNeighboursFor(i: Int, i1: Int, seatingMap: SeatingMap): Int
}


case object BaseSeatStrategy extends SeatStrategy {
  override val maxNumberOfNeighbours: Int = 4

  override def numberOfNeighboursFor(x: Int, y: Int, seatingMap: SeatingMap): Int =
    seatingMap.numberOfNeighboursFor(x, y)
}


case object ExtendedSeatStrategy extends SeatStrategy {

  override val maxNumberOfNeighbours: Int = 5

  private val directions = Seq(
    (0, 1), (0, -1),
    (1, 0), (-1, 0),
    (1, 1), (-1, -1),
    (1, -1), (-1, 1))


  override def numberOfNeighboursFor(x: Int, y: Int, seatingMap: SeatingMap): Int =

    def loopNeighbours(x: Int, y: Int, direction: (Int, Int)): Int = seatingMap(x)(y) match {
      case SeatStatus.Occupied => 1
      case SeatStatus.Empty | SeatStatus.Border => 0
      case SeatStatus.Floor => loopNeighbours(x + direction._1, y + direction._2, direction)
    }

    (directions.map(direction => loopNeighbours(x + direction._1, y + direction._2, direction))).sum
}