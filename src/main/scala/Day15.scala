package me.dalsat.adventofcode

import me.dalsat.adventofcode.InputLoader


object Day15 extends InputLoader(15) {

  @main def start = {
    
    val eg = ElvesGame(sample(0))
    println(eg.lastSpokenNumber(2020))
    
    done
  }

  
  class ElvesGame(val numbers: Seq[Int], val turn: Int = 0, val memory: Map[Int, Int] = Map()) {
    
    def this(numbers: String) = this(numbers.split(",").map(_.toInt).toList)

    if numbers.nonEmpty then initializeNumbers

    def initializeNumbers: Unit = {}
    
    def sayNumber(number: Int): ElvesGame = ElvesGame(numbers, turn + 1, memory + (number -> turn))
    
    def lastSpokenNumber(lastTurn: Int) = {

      def loop(turn: Int): Int =
        if turn == lastTurn then turn
        else loop(turn + 1)

      loop(0)
    }
  }
}
