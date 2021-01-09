package me.dalsat.adventofcode

import scala.io.Source


object Day1 extends InputLoader(1) {
  
  val cc = new CurrencyCalculator(2020)
  cc.find(sample)
  cc.find3(sample)

  cc.find(input)
  cc.find3(input)

  done
}


class CurrencyCalculator(target: Int) {

  
  def find(dataset: Day1.Dataset) =
    find2(dataset.map(_.toInt).toSet) match {
      case Some(number) => computeResult(number)
      case _ => throw new RuntimeException("Element not found")
    }
  

  def find2(items: Set[Int]): Option[Int] = items.find(each => items contains (target - each))

  protected def computeResult(number: Int): Int = {
    number * (target - number)
  }


  def find3(items: Seq[String]): Unit = find3(items.map(_.toInt).toSet)

  private def find3(items: Set[Int]): Unit = for (
    first <- items;
    second <- items
  ) {
    val third = target - (first + second)
    if (items.contains(third) && first != second && second != third) {
      println(s"${first}, ${second}, ${third}")
      println(first * second * third)
    }
  }

}
