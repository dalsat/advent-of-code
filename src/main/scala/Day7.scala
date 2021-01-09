package me.dalsat.adventofcode

import scala.annotation.tailrec


object Day7 extends App {

  val rp = new RuleParser

  //  println(rp.parse(rp.sample))
  println(rp.parse(rp.input))


  //  rp.parse()

  println(rp.contains)
  println(rp.containedBy)

  println(rp.needsToContain("shiny gold") - 1)


  //  println(rp.containersFor("shiny gold"))
  //  println(rp.countContainersFor("shiny gold"))
  //  println(rp.parseRule("light red bags contain 1 bright white bag, 2 muted yellow bags."))
  println("Day 7 done")
}


class RuleParser extends InputLoader(7) {

  var contains: Map[String, Seq[Bag]] = Map()
  //  var containedBy: Map[String, Seq[String]] = Map()
  var containedBy = List()


  def parse(dataset: Dataset): Unit = {
    contains = (dataset flatMap parseLine).groupMap(_._1)(_._2)
    //    containedBy = (contains map { case (key, value) => value map (e => e.color -> key) }).toList//.groupMap(_._1)(_._2)
  }


  def needsToContain(container: String): Int =
    if (contains.contains(container))
      (contains(container) foldLeft 1) ((sum, eachBag) =>
        sum + (needsToContain(eachBag.color) * eachBag.number))
    else 1


  private def parseLine(rule: String) = {
    val Array(container, content) = rule.split("\\s*bags contain\\s*")
    parseContentList(content) map (container -> _)
  }


  private def parseContentList(contentList: String) = contentList.slice(0, contentList.length - 1)
    .split(",\\s+")
    .toList
    .map(Bag.fromDescription)
    .filter(_.isDefined)
    .map(_.get)

  private def parseContent(content: String) = try {
    val tokens = "(\\d+) (.+) bag(s?)".r findAllIn content
    Some(tokens.group(2))
  } catch {
    case _: RuntimeException => None
  }


  //  def containersFor(target: String): Set[String] = {
  //
  //    def loop(currentBag: String): Set[String] =
  //      (containedBy.get(currentBag).map(containers => containers flatMap loop).getOrElse(Nil) appended currentBag).toSet
  //
  //    loop(target) - target
  //    //    ((index.get(target) map { _ map loop }).get)
  //  }

  //  def countContainersFor(target: String): Int = containersFor(target).size

}

case class Bag(color: String, number: Int)


object Bag {
  def fromDescription(description: String): Option[Bag] = {
    try {
      val tokens = "(\\d+) (.+) bag(s?)".r findAllIn description
      Some(Bag(tokens.group(2), tokens.group(1).toInt))
    } catch {
      case _: RuntimeException => None
    }
  }

}
