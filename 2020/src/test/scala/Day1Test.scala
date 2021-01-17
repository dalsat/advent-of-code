package me.dalsat.adventofcode

import org.scalatest.flatspec.AnyFlatSpec
import org.scalatest.matchers.should


class Day1Test extends AnyFlatSpec with should.Matchers {

//  "A Stack" should "pop values in last-in-first-out order" in {
//    val stack = new Stack[Int]
//    stack.push(1)
//    stack.push(2)
//    stack.pop() should be(2)
//    stack.pop() should be(1)
//  }
//
//  it should "throw NoSuchElementException if an empty stack is popped" in {
//    val emptyStack = new Stack[Int]
//    a[NoSuchElementException] should be thrownBy {
//      emptyStack.pop()
//    }
//  }

val input = """1721
    979
    366
    299
    675
    1456""".split("\\n")

  "A CurrencyCalculator" should "find the two values that sum to 2000 and multiply them" in {
    val cc = new CurrencyCalculator(2020)
//    cc.find(input) should be(514579)

  }

  "A CurrencyCalculator" should "find the three values that sum to 2000 and multiply them" in {
//    val cc = new CurrencyCalculator3(2020)
//    cc.find(input) should be(514579)

//    cc.findFromFile("day-1/input.txt") should be(468051)
  }

}
