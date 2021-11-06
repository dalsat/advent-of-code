package me.dalsat.adventofcode


object Day1 extends Solution(1):

  val cc = new CurrencyCalculator(2020)

  override def part1 = cc.find(input)

  override def part2 = cc.find3(input)


  class CurrencyCalculator(target: Int):

    def find(dataset: Dataset) =
      find2(dataset.map(_.toInt).toSet) match {
        case Some(number) => computeResult(number)
        case _ => throw new RuntimeException("Element not found")
      }


    def find2(items: Set[Int]): Option[Int] = items.find(each => items contains (target - each))

    protected def computeResult(number: Int): Int = {
      number * (target - number)
    }


    def find3(items: Seq[String]): Int = find3(items.map(_.toInt).toSet)

    private def find3(items: Set[Int]): Int =
      for (
        first <- items;
        second <- items
      ) {
        val third = target - (first + second)
        if items.contains(third) && first != second && second != third then
          return first * second * third
        //        println(s"${first}, ${second}, ${third}")
        //        println(first * second * third)
      }
      throw Error("value not found")
