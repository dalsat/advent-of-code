package me.dalsat.adventofcode

object Day18 extends Solution(18) {

  override def part1: SolutionType = Parser.parseAll(input).map(_.eval).sum

  override def part2: SolutionType = 2

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

    def parseAll(dataset: Dataset): Seq[Operation] = dataset map parse

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


//while there are tokens to be read:
//    read a token
//    if the token is:
//    - a number:
//        put it into the output queue
//    - a function:
//        push it onto the operator stack
//    - an operator o1:
//        while (
//            there is an operator o2 other than the left parenthesis at the top
//            of the operator stack, and (o2 has greater precedence than o1
//            or they have the same precedence and o1 is left-associative)
//        ):
//            pop o2 from the operator stack into the output queue
//        push o1 onto the operator stack
//    - a left parenthesis (i.e. "("):
//        push it onto the operator stack
//    - a right parenthesis (i.e. ")"):
//        while the operator at the top of the operator stack is not a left parenthesis:
//            {assert the operator stack is not empty}
//            /* If the stack runs out without finding a left parenthesis, then there are mismatched parentheses. */
//            pop the operator from the operator stack into the output queue
//        {assert there is a left parenthesis at the top of the operator stack}
//        pop the left parenthesis from the operator stack and discard it
//        if there is a function token at the top of the operator stack, then:
//            pop the function from the operator stack into the output queue
///* After the while loop, pop the remaining items from the operator stack into the output queue. */
//while there are tokens on the operator stack:
//    /* If the operator token on the top of the stack is a parenthesis, then there are mismatched parentheses. */
//    {assert the operator on top of the stack is not a (left) parenthesis}
//    pop the operator from the operator stack onto the output queue