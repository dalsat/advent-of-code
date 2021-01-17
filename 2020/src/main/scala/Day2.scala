package me.dalsat.adventofcode.day2

import me.dalsat.adventofcode.InputLoader


object Day2 extends InputLoader(2) {

  val pc = new PasswordChecker()

  println(pc.validPasswords(sample))
  println(pc.countValidPasswords(sample))
  
  println(pc.countValidPasswords(input))

  done
}


class PasswordChecker {

  def countValidPasswords(dataset: Day2.Dataset): Int = validPasswords(dataset).count(e => e)

  def validPasswords(dataset: Day2.Dataset): Seq[Boolean] = parseAll(dataset) map (_.validate)

  private def parseAll(lines: Day2.Dataset) = lines.map(parseLine)

  private def parseLine(line: String) = line.split("[ :-]") match {
    case Array(min, max, letter, _, password) => Line(Policy(letter(0), Integer.parseInt(min), Integer.parseInt(max)), password)
  }

}


case class Line(policy: Policy, password: String) {
  def validate: Boolean = policy.validate2(password)
}

case class Policy(letter: Char, min: Int, max: Int) {

  def validate(password: String): Boolean = {
    val count = password.count(c => letter.equals(c))
    min <= count && count <= max
  }

  def validate2(password: String): Boolean =
    (password.length > min - 1 && password(min - 1) == letter) ^
      (password.length > max - 1 && password(max - 1) == letter)
}
