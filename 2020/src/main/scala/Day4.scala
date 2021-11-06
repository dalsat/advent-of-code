package me.dalsat.adventofcode

import scala.annotation.tailrec

object Day4 extends Solution(4):

  override def part1 = PassportScanner(input).count()

  override def part2 = AdvancedPassportScanner(input).count()


  class PassportScanner(dataset: Dataset):

    def count(): Int = parseAll().count(isValidPassport)

    def parseAll(): Array[Array[Array[String]]] = dataset.mkString(" ")
      .split("\\s{2}")
      .map(parseLine)


    private def parseLine(line: String) = line.split("\\s+")
      .map(_.split(':'))
      .filter(_ (0) != "cid")

    protected def isValidPassport(passport: Array[Array[String]]): Boolean = passport.length == 7


  class AdvancedPassportScanner(dataset: Dataset) extends PassportScanner(dataset):
    override protected def isValidPassport(passport: Array[Array[String]]): Boolean = super.isValidPassport(passport) &&
      passport.map(line => line(0) match {


        //    byr (Birth Year) - four digits; at least 1920 and at most 2002.
        case "byr" => line(1).length == 4 && 1920 <= line(1).toInt && line(1).toInt <= 2002

        //    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        case "iyr" => line(1).length == 4 && 2010 <= line(1).toInt && line(1).toInt <= 2020

        //    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        case "eyr" => line(1).length == 4 && 2020 <= line(1).toInt && line(1).toInt <= 2030

        //    hgt (Height) - a number followed by either cm or in:
        case "hgt" => line(1).matches("\\d+cm") && {
          val value = line(1).slice(0, line(1).length - 2).toInt
          150 <= value && value <= 193
        } ||
          line(1).matches("\\d+in") && {
            val value = line(1).slice(0, line(1).length - 2).toInt
            59 <= value && value <= 76
          }

        //    If cm, the number must be at least 150 and at most 193.
        //    If in, the number must be at least 59 and at most 76.

        //    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        case "hcl" => line(1).matches("#[0-9a-f]{6}")

        //    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        case "ecl" => line(1).matches("(amb|blu|brn|gry|grn|hzl|oth)")

        //    pid (Passport ID) - a nine-digit number, including leading zeroes.
        case "pid" => line(1).matches("\\d{9}")

        //    cid (Country ID) - ignored, missing or not.
        case "cid" => true

        case _ => false
      }).reduceLeft(_ && _)
