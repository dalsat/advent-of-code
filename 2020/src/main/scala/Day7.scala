package me.dalsat.adventofcode

import scala.annotation.tailrec


object Day7 extends Solution(7):

  override def part1 = rp.countContainersFor("shiny gold")

  override def part2 = rp.needsToContain("shiny gold") - 1

  val rp = RuleParser(input)


  class RuleParser(dataset: Dataset):

    private val items = parse(dataset)

    val bagContains: Map[String, Seq[Bag]] = items.groupMap(_._1)(_._2) //parse(dataset)
    var bagContainedIn: Map[String, Seq[String]] = items.groupMap { case (_, Bag(name, count)) => name }(_._1)

    private def parse(dataset: Dataset) =
      (dataset flatMap parseLine)


    private def parseLine(rule: String) =
      val Array(container, content) = rule.split("\\s*bags contain\\s*")
      parseContentList(content) map (container -> _)


    def needsToContain(container: String): Int =
      if bagContains.contains(container) then
        (bagContains(container) foldLeft 1) ((sum, eachBag) =>
          sum + (needsToContain(eachBag.color) * eachBag.number))
      else 1


    private def parseContentList(contentList: String) =
      contentList.slice(0, contentList.length - 1)
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


    def containersFor(target: String): Set[String] =

      def loop(currentBag: String): Set[String] =
        (bagContainedIn.get(currentBag)
          .map(containers => containers flatMap loop)
          .getOrElse(Nil)
          .appended(currentBag))
          .toSet

      loop(target) - target


    def countContainersFor(target: String): Int = containersFor(target).size

  end RuleParser


  case class Bag(color: String, number: Int)

  object Bag:
    def fromDescription(description: String): Option[Bag] =
      try {
        val tokens = "(\\d+) (.+) bag(s?)".r findAllIn description
        Some(Bag(tokens.group(2), tokens.group(1).toInt))
      } catch {
        case _: RuntimeException => None
      }
