package me.dalsat.adventofcode

import me.dalsat.adventofcode.Solution

import scala.annotation.tailrec


object Day15 extends Solution(15):

  override def part1 = ElvesGame(input.head).lastSpokenNumber(2020)

  override def part2 = ElvesGame(input.head).lastSpokenNumber(30000000)


  class ElvesGame(numbersString: String):

    private val numbers: List[Int] = numbersString.split(",").map(_.toInt).toList
    private val initialTurn: Int = numbers.size + 1
    private val initialMemory = numbers.zip(1 to initialTurn).toMap

    def computeNextNumber(turn: Int, lastSpokenNumber: Int, memory: Map[Int, Int]): Int =
      if memory contains lastSpokenNumber then
        turn - memory(lastSpokenNumber)
      else
        0

    def lastSpokenNumber(targetTurn: Int): Int = {

      @tailrec
      def loop(turn: Int, lastSpokenNumber: Int, memory: Map[Int, Int]): Int =
        if turn >= targetTurn then lastSpokenNumber
        else
          val nextNumber = computeNextNumber(turn, lastSpokenNumber, memory)
          loop(turn + 1, nextNumber, memory + (lastSpokenNumber -> turn))

      loop(initialTurn, 0, this.initialMemory)
    }

