package me.dalsat.adventofcode

import me.dalsat.adventofcode.Solution


object Day2 extends Solution(2):


  override def part1 = PasswordChecker().countValidPasswords(input)

  override def part2 = NewPasswordChecker().countValidPasswords(input)


  class PasswordChecker:

    def countValidPasswords(dataset: Dataset): Int = validPasswords(dataset).count(e => e)

    def validPasswords(dataset: Dataset): Seq[Boolean] = parseAll(dataset) map (_.validate)

    private def parseAll(lines: Dataset) = lines.map(parseLine)

    protected def parseLine(line: String) = line.split("[ :-]") match {
      case Array(min, max, letter, _, password) =>
        Line(OldPolicy(letter(0), Integer.parseInt(min), Integer.parseInt(max)), password)
    }


  class NewPasswordChecker extends PasswordChecker:

    // TODO: this is ugly, reafctor using implicits
    override def parseLine(line: String): Line = line.split("[ :-]") match {
      case Array(min, max, letter, _, password) =>
        Line(NewPolicy(letter(0), Integer.parseInt(min), Integer.parseInt(max)), password)
    }


  case class Line(policy: Policy, password: String):
    def validate: Boolean = policy.validate(password)


  abstract class Policy:
    def validate(password: String): Boolean

  case class OldPolicy(letter: Char, min: Int, max: Int) extends Policy:

    def validate(password: String): Boolean =
      val count = password.count(c => letter.equals(c))
      min <= count && count <= max


  case class NewPolicy(letter: Char, min: Int, max: Int) extends Policy:

    def validate(password: String): Boolean =
      (password.length > min - 1 && password(min - 1) == letter) ^
        (password.length > max - 1 && password(max - 1) == letter)
