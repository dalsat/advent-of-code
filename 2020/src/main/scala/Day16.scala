package me.dalsat.adventofcode

object Day16 extends Solution(16):

  override def part1 = ScanningErrorRateCalculator(tp).errorRate

  override def part2 = TicketDecoder(tp).multipliedValues

  val tp = TicketParser(input)


  type Ticket = Seq[Int]

  class TicketParser(dataset: Dataset):

    val (rules, ticket, otherTickets) = parseDataset(dataset)

    private def parseDataset(dataset: Dataset) =

      val ticketsIndex = dataset indexWhere (_ == "your ticket:")
      val nearbyTicketsIndex = dataset indexWhere (_ == "nearby tickets:")

      (
        parseRules(dataset.slice(0, ticketsIndex)),
        parseTicket(dataset.slice(ticketsIndex + 1, nearbyTicketsIndex).head),
        parseOtherTickets(dataset.slice(nearbyTicketsIndex + 1, dataset.size))
      )


    private def parseRules(rules: Seq[String]): RuleSet =
      RuleSet(rules filter (_.nonEmpty) map Rule.parse)

    private def parseTicket(ticket: String): Ticket = ticket.split(",").map(_.toInt)

    private def parseOtherTickets(otherTickets: Seq[String]): Seq[Ticket] =
      otherTickets
        .filter(_.nonEmpty)
        .map(parseTicket(_))


  class RuleSet(val rules: Seq[Rule]):

    def isValid(ticket: Ticket): Boolean = ticket forall isValid

    def isValid(number: Int): Boolean = rules exists (_ isValid number)

    def map[B](f: Rule => B) = rules map f



  case class Rule(name: String, conditions: Seq[Range]):
    def validate(ticket: Ticket) = ticket forall isValid

    def isValid(number: Int) = conditions exists (_ contains number)


  object Rule:
    def parse(rule: String) =
      val Array(name, rawConditions) = rule.split(":")
      val conditions = rawConditions split "or" map parseCondition
      Rule(name, conditions)

    def parseCondition(condition: String) =
      val Array(from, to) = (condition split "-") map (_.strip.toInt)
      from to to


  class ScanningErrorRateCalculator(ticketParser: TicketParser):

    lazy val invalidNumbers =
      ticketParser.otherTickets.flatten filter (!ticketParser.rules.isValid(_))

    lazy val errorRate = invalidNumbers.sum


  class TicketDecoder(ticketParser: TicketParser):

    type Column = Seq[(Int, Seq[Rule])]

    def multipliedValues: Long =
      assignedRules
        .filter { case (rule, index) => relevantFields contains rule.name }
        .map { case (rule, index) => ticketParser.ticket(index).toLong }
        .product

    lazy val validTickets = ticketParser.otherTickets filter ticketParser.rules.isValid

    val columns = (0 to ticketParser.ticket.size - 1) map (index => index -> columnWithIndex(index))

    private def columnWithIndex(index: Int) = validTickets map (_(index))

    def rulesForColumn(index: Int): Seq[Rule] =
      val column = columnWithIndex(index)
      ticketParser.rules.rules filter (_ validate column)

    lazy val validRules: Column = (0 to ticketParser.ticket.size - 1)
      .map(index => index -> rulesForColumn(index))
      .sortBy { case (index, rules) => rules.size }

    lazy val assignedRules =
      (validRules foldLeft Map[Rule, Int]()) { case (acc, (index, rules)) =>
        val nextRules = rules filter (rule => !(acc contains rule))
        assert(nextRules.size == 1)
        acc updated (nextRules.head, index)
      }

    val relevantFields = ticketParser.rules.map(_.name).filter(_ startsWith "departure")