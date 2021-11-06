package me.dalsat.adventofcode

import me.dalsat.adventofcode.Solution

import scala.annotation.tailrec


object Day12 extends Solution(12):

  override def part1 = new BaseShip(input).distance
  override def part2 = new WaypointShip(input).distance


  trait Ship:
    def navigate: (Int, Int)

    def next: Ship

    def distance: Int =
      val navigateCache = navigate
      navigateCache._1.abs + navigateCache._2.abs


  class BaseShip(val x: Int, val y: Int, val degrees: Int, val instructions: Seq[Instruction]) extends Ship {

    def this(dataset: Dataset) = this(0, 0, 90, BaseShip.parseInstructions(dataset))

    def this(position: (Int, Int, Int), instructions: Seq[Instruction]) =
      this(position._1, position._2, position._3, instructions)

    def navigate: (Int, Int) =
      if (instructions.isEmpty) (x, y)
      else next.navigate

    def next: BaseShip =
      new BaseShip(updatePosition(instructions.head), instructions.tail)


    override def toString: String = s"Ship (${x}, ${y}, ${degrees}) => ${Math.abs(x) + Math.abs(y)}"

    private def updatePosition(instruction: Instruction): (Int, Int, Int) = instruction.direction match {
      case Direction.North => (x, y + instruction.value, degrees)
      case Direction.South => (x, y - instruction.value, degrees)
      case Direction.East => (x + instruction.value, y, degrees)
      case Direction.West => (x - instruction.value, y, degrees)
      case Direction.Left => (x, y, degrees - instruction.value)
      case Direction.Right => (x, y, degrees + instruction.value)
      case Direction.Forward => (
        x + (instruction.value * Math.sin(Math.toRadians(degrees))).toInt,
        y + (instruction.value * Math.cos(Math.toRadians(degrees))).toInt, degrees)
    }

  }

  object BaseShip {
    def parseInstructions(dataset: Dataset): Seq[Instruction] =
      dataset map (parseInstruction(_))

    def parseInstruction(line: String) = Instruction.fromString(line)
  }


  enum Direction:
    case North, South, East, West, Forward, Left, Right


  object Direction:

    def fromString(from: Char): Direction = from match {
      case 'N' => Direction.North
      case 'S' => Direction.South
      case 'E' => Direction.East
      case 'W' => Direction.West
      case 'F' => Direction.Forward
      case 'L' => Direction.Left
      case 'R' => Direction.Right
    }


  case class Instruction(direction: Direction, value: Int):
    def destinationFor(x: Int, y: Int, degrees: Int): (Int, Int, Int) = ???


  case object Instruction:
    def fromString(from: String) = Instruction(Direction.fromString(from.head), from.tail.toInt)


  /**
   * Part 2 using a waypoint
   *
   * Action N means to move the waypoint north by the given value.
   * Action S means to move the waypoint south by the given value.
   * Action E means to move the waypoint east by the given value.
   * Action W means to move the waypoint west by the given value.
   * Action L means to rotate the waypoint around the ship left (counter-clockwise) the given number of degrees.
   * Action R means to rotate the waypoint around the ship right (clockwise) the given number of degrees.
   * Action F means to move forward to the waypoint a number of times equal to the given value.
   */
  case class WaypointShip(x: Int, y: Int, wx: Int, wy: Int, instructions: Seq[Instruction]) extends Ship {

    def this(dataset: Dataset) = this(0, 0, 10, 1, BaseShip.parseInstructions(dataset))

    def this(position: (Int, Int, Int, Int), instructions: Seq[Instruction]) =
      this(position._1, position._2, position._3, position._4, instructions)

    def updatePosition(instruction: Instruction): (Int, Int, Int, Int) = instruction.direction match {
      case Direction.North => (x, y, wx, wy + instruction.value)
      case Direction.South => (x, y, wx, wy - instruction.value)
      case Direction.East => (x, y, wx + instruction.value, wy)
      case Direction.West => (x, y, wx - instruction.value, wy)
      case Direction.Left => rotateWaypointLeft(instruction.value)
      case Direction.Right => rotateWaypointRight(instruction.value)
      case Direction.Forward => ((1 to instruction.value) foldLeft (x, y, wx, wy)) { case ((x, y, wx, wy), _) => (x + wx, y + wy, wx, wy) }
    }

    override def next: WaypointShip =
      new WaypointShip(updatePosition(instructions.head), instructions.tail)


    /**
     * Rotate left the waypoint
     */
    def rotateWaypointRight(rotation: Int): (Int, Int, Int, Int) =
      rotation match {
        case 90 => (x, y, wy, -wx)
        case 180 => (x, y, -wx, -wy)
        case 270 => (x, y, -wy, wx)
      }


    def rotateWaypointLeft(rotation: Int): (Int, Int, Int, Int) = rotateWaypointRight(360 - rotation)


    override def navigate: (Int, Int) =
      if instructions.isEmpty then (x, y)
      else next.navigate


    override def toString: String = s"Ship (x=${x}, y=${y}, wx=${wx}, wy=${wy}) => ${Math.abs(x) + Math.abs(y)}"
  }
