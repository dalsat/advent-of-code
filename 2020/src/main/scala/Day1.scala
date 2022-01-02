package me.dalsat.adventofcode


object Day1 extends Solution(1):

  val cc = new CurrencyCalculator(input)

  override def part1 = cc.find2(2020).get

  override def part2 = cc.find3(2020)


  class CurrencyCalculator(dataset: Dataset):

    val values = dataset map (_.toInt)

    private def complementsFor(target: Int) = (values map (target - _)).toSet

    def find2(target: Int): Option[Int] =
      val complements = complementsFor(target)
      values find complements.contains map (matched => matched * (target - matched))


    def find3(target: Int): Int =
      values.flatMap(value => find2(target - value) map (_ * value)).head
