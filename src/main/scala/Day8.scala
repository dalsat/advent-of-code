package me.dalsat.adventofcode.day8

import me.dalsat.adventofcode.InputLoader

import scala.annotation.tailrec


object Day8 extends App {

  val vm = new VirtualMachine

  println(vm.debug(vm.parse(vm.sample)))
  println(vm.debug(vm.parse(vm.input)))

  println(vm.fuzzer(vm.parse(vm.sample)))
  println(vm.fuzzer(vm.parse(vm.input)))

  println("Day 8 done")
}


class VirtualMachine extends InputLoader(8) {

  type Program = Seq[Instruction]

  def parse(dataset: Dataset) = dataset map parseLine

  def parseLine(line: String) = {
    val Array(command, value) = line.split("\\s+")
    command match {
      case "nop" => Nop(value.toInt)
      case "acc" => Acc(value.toInt)
      case "jmp" => Jmp(value.toInt)
    }
  }



  def debug(program: Program): Int = execute(program)._2


  def execute(program: Program): (Boolean, Int) = {

    @tailrec
    def nextInstruction(index: Int, acc: Int, executed: Set[Int]): (Boolean, Int) = {
      if (index == program.length) (true, acc)
      else if (index > program.length) (false, acc)
      else if (executed.contains(index)) (false, acc)
      else
        program(index) match {
          case Nop(_) => nextInstruction(index + 1, acc, executed + index)
          case Acc(value) => nextInstruction(index + 1, acc + value, executed + index)
          case Jmp(value) => nextInstruction(index + value, acc, executed + index)
        }
    }

    nextInstruction(0, 0, Set())
  }


  def fuzzer(program: Program): Option[(Boolean, Int)] = program.indices map (flipAndRun(program, _)) find (_._1)


  private def flipAndRun(program: Program, index: Int): (Boolean, Int) = program(index) match {
    case Nop(value) => execute(program.updated(index, Jmp(value)))
    case Jmp(value) => execute(program.updated(index, Nop(value)))
    case _ => (false, -1)
  }
}



abstract class Instruction

case class Acc(value: Int) extends Instruction

case class Nop(value: Int) extends Instruction

case class Jmp(value: Int) extends Instruction
