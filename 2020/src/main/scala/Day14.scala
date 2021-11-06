package me.dalsat.adventofcode

import me.dalsat.adventofcode.Solution


object Day14 extends Solution(14) {

  override def part1 = DockInterpreter(input, OverwriteMemory()).sums
  override def part2 = DockInterpreter(input, AddressMemory()).sums


  class DockInterpreter(dataset: Dataset, val memory: Memory) {

    lazy val instructions = parse(dataset)

    def parse(dataset: Dataset) = dataset.map(parseLine(_))

    def parseLine(line: String) = line match {
      case s"mask = ${value}" => Mask(value)
      case s"mem[${address}] = ${value}" => Mem(address.toInt, value.toInt)
      case _ => throw RuntimeException(s"unable to read line: ${line}")
    }

    lazy val run: Memory = run(instructions, memory)


    def run(instructions: Seq[Instruction], memory: Memory): Memory = instructions match {
      case instruction :: tail => run(tail, memory.execute(instruction))
      case Nil => memory
    }

    def sums = run.sums
  }


  trait Instruction

  case class Mem(address: Long, value: Long) extends Instruction

  case class Mask(value: String) extends Instruction {

    def applyToValue(number: Long): Long = value.zip(number.toBinary).map((eachMask, eachValue) => eachMask match {
      case 'X' => eachValue
      case '0' | '1' => eachMask
      case _ => throw new RuntimeException(s"unknown mask value ${eachMask}")
    }).mkString("").parseBinary

    def applyToAddress(address: Long): String = value.zip(address.toBinary).map((eachMask, eachValue) => eachMask match {
      case '0' => eachValue
      case _ => eachMask
    }).mkString("")

    def combinationsFor(address: Long): Seq[Long] = {
      def loop(generated: Seq[String], tail: Seq[(Char, Char)]): Seq[String] = tail match {
        case Nil => generated
        case (eachValue, '0') :: nextTail => loop(generated.map(each => each + eachValue), nextTail)
        case (_, '1') :: nextTail => loop(generated.map(each => each + '1'), nextTail)
        case (_, 'X') :: nextTail => loop(generated.flatMap(each => List(each + '0', each + '1')), nextTail)
      }

      loop(List(""), address.toBinary.zip(value).toList).map(_.parseBinary)
    }
  }


  abstract class Memory(val registries: Map[Long, Long], val mask: Mask) {

    lazy val sums = registries.values.sum

    def execute(instruction: Instruction): Memory = instruction match {
      case mask: Mask => executeMask(mask)
      case mem: Mem => executeMem(mem)
    }

    def executeMask(instruction: Mask): Memory

    def executeMem(instruction: Mem): Memory
  }


  class OverwriteMemory(registries: Map[Long, Long] = Map(), mask: Mask = null) extends Memory(registries, mask) {

    override def executeMask(instruction: Mask) = OverwriteMemory(registries, instruction)

    override def executeMem(instruction: Mem) =
      val Mem(address, value) = instruction
      val newValue = mask.applyToValue(value)
      if newValue == 0 then
        OverwriteMemory(registries - address, mask)
      else
        OverwriteMemory(registries + (address -> newValue), mask)
  }


  class AddressMemory(registries: Map[Long, Long] = Map(), mask: Mask = null) extends Memory(registries, mask) {

    override def executeMask(instruction: Mask) = AddressMemory(registries, instruction)

    override def executeMem(instruction: Mem) =
      val Mem(address, value) = instruction
      AddressMemory((registries ++ updateWithAddressMask(address, value)).filter((k, v) => v != 0), mask)
    

    def updateWithAddressMask(address: Long, value: Long): Map[Long, Long] = {
      mask.combinationsFor(address).map((_ -> value)).toMap
    }

  }

  extension (binary: String) def parseBinary: Long = (binary.reverse.zipWithIndex foldLeft (0: Long)) { case (sum, (each, index)) => each.toString.toLong * Math.pow(2, index).toLong + sum }
  
  extension (number: Long) def toBinary: String = number.toBinaryString.reverse.padTo(36, '0').reverse

}
