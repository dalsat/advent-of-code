package me.dalsat.adventofcode

import scala.annotation.tailrec

object Day3 extends Solution(3):

  override def part1 = results(1).toLong

  override def part2 = results.product.toLong

  val w = new World(new DiscreteSledge(3, 1))

  val sledges = List(
    //  Right 1, down 1.
    new DiscreteSledge(1, 1),
    //  Right 3, down 1. (This is the slope you already checked.)
    new DiscreteSledge(3, 1),
    //  Right 5, down 1.
    new DiscreteSledge(5, 1),
    //  Right 7, down 1.
    new DiscreteSledge(7, 1),
    //  Right 1, down 2.
    new DiscreteSledge(1, 2)
  )

  val results: List[BigInt] = sledges.map(new World(_).count())


  class World(sledge: Sledge):

    var currentPosition: Position = Position(0, 0)
    val map: TrackMap = new TrackMap(input)

    def count(): Int = {
      @tailrec
      def loop(position: Position, count: Int): Int = if (map.isInside(position)) {
        if (map.isTree(position)) loop(sledge.next(position), count + 1)
        else loop(sledge.next(position), count)
      } else count

      loop(Position(0, 0), 0)
    }


  case class Position(x: Int, y: Int)


  class TrackMap(val rows: Seq[String]):

    val width: Int = rows.head.length
    val height: Int = rows.length

    def apply(position: Position): Option[Char] =
      if (position.y < height)
        Some(rows(position.y)(position.x % width))
      else None

    def apply(x: Int, y: Int): Option[Char] = apply(Position(x, y))

    def isTree(position: Position): Boolean = this (position).contains('#')

    def isInside(position: Position): Boolean = this (position).isDefined

    override def toString: String = "Map " + width + "x" + height + "\n" + rows.mkString("\n")


  class Sledge(val strategy: Position => Position):
    def next(position: Position): Position = strategy(position)


  class DiscreteSledge(x: Int, y: Int) extends Sledge(p => Position(p.x + x, p.y + y))
