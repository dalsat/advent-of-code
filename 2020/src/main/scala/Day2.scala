package me.dalsat.adventofcode

import me.dalsat.adventofcode.Solution


object Day2 extends Solution(2):


  override def part1 = PasswordChecker(FirstCheckStategy).countValidPasswords(input)

  override def part2 = PasswordChecker(SecondCheckStrategy).countValidPasswords(input)


  class PasswordChecker(val checkStrategy: CheckStrategy):

    def countValidPasswords(dataset: Dataset): Int = validPasswords(dataset).count(e => e)

    def validPasswords(dataset: Dataset): Seq[Boolean] = parseAll(dataset) map checkStrategy.apply

    private def parseAll(lines: Dataset) = lines.map(parseLine)

    def parseLine(line: String): Line = line.split("[ :-]") match {
      case Array(min, max, letter, _, password) =>
        Line(letter(0), Integer.parseInt(min), Integer.parseInt(max), password)
    }


  case class Line(letter: Char, min: Int, max: Int, password: String)

  sealed trait CheckStrategy:
    def apply(line: Line): Boolean

  object FirstCheckStategy extends CheckStrategy:

    def apply(line: Line): Boolean =
      val Line(letter, min, max, password) = line
      val count = password.count(c => letter.equals(c))
      min <= count && count <= max

  object SecondCheckStrategy extends CheckStrategy:
    def apply(line: Line): Boolean =
      val Line(letter, min, max, password) = line
      (password.length > min - 1 && password(min - 1) == letter) ^
        (password.length > max - 1 && password(max - 1) == letter)
