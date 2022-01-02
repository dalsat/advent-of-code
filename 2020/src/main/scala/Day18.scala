package me.dalsat.adventofcode

object Day18 extends Solution(18) {

  override def part1 = Parser.parseAll(input).map(_.eval).sum

  override def part2 = 2

  println(Parser.parse("((5 + 4 * 5) * 5) + 9 * 7 + 8 * 4 * 9").eval)

  sealed trait Operation:
    def eval: Long

  case class Number(value: Int) extends Operation:
    def eval: Long = value

  case class Sum(left: Operation, right: Operation) extends Operation:
    def eval: Long = left.eval + right.eval


  case class Prod(left: Operation, right: Operation) extends Operation:
    def eval: Long = left.eval * right.eval

  case class Parenthesis(value: Operation) extends Operation:
    def eval: Long = value.eval


  object Parser:

    type Input = Seq[Char]
    type PartialComputation = (Operation, Input)

    def parseAll(dataset: Dataset) = dataset map parse

    def parse(operation: String): Operation =
      parseUnary(operation.toCharArray.filter(!_.isSpaceChar).toList.reverse)._1

    def parseBinary(left: Operation, right: Input): PartialComputation =
      right match {
      case Nil => (left, Nil)
      case '+' :: tail =>
        val (sub, rest) = parseUnary(tail)
        (Sum(left, sub), rest)
      case '*' :: tail =>
        val (sub, rest) = parseUnary(tail)
        (Prod(left, sub), rest)
      case '(' :: tail => (left, tail)
      case _ => throw Error(s"Syntax error parsing binary operation: ${right}" )
    }

    def parseUnary(right: Input): PartialComputation =
      right match {
        case ')' :: tail =>
          val (subexpr, rest) = parseUnary(tail)
          parseBinary(subexpr, rest)
        case value :: tail => parseBinary(Number(value.toString.toInt), tail)
        case _ => throw Error(s"Syntax error parsing unary operation: ${right}" )
      }

}
