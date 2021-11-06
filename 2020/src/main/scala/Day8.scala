package me.dalsat.adventofcode

import me.dalsat.adventofcode.Solution

import scala.annotation.tailrec


object Day8 extends Solution(8):


  override def part1 = vm.debug

  override def part2 = vm.fuzzer.get._2

  val vm = new VirtualMachine(input)


  class VirtualMachine(dataset: Dataset):

    val program: Program = parse(dataset)

    type Program = Seq[Instruction]

    def parse(dataset: Dataset) = dataset map parseLine

    def parseLine(line: String) =
      val Array(command, value) = line.split("\\s+")
      command match {
        case "nop" => Nop(value.toInt)
        case "acc" => Acc(value.toInt)
        case "jmp" => Jmp(value.toInt)
      }


    def debug: Int = execute(program)._2


    private def execute(program: Program): (Boolean, Int) =

      @tailrec
      def nextInstruction(index: Int, acc: Int, executed: Set[Int]): (Boolean, Int) =
        if (index == program.length) (true, acc)
        else if (index > program.length) (false, acc)
        else if (executed.contains(index)) (false, acc)
        else
          program(index) match {
            case Nop(_) => nextInstruction(index + 1, acc, executed + index)
            case Acc(value) => nextInstruction(index + 1, acc + value, executed + index)
            case Jmp(value) => nextInstruction(index + value, acc, executed + index)
          }
      end nextInstruction

      nextInstruction(0, 0, Set())
    end execute


    def fuzzer: Option[(Boolean, Int)] = program.indices map (flipAndRun(program, _)) find (_._1)


    private def flipAndRun(program: Program, index: Int): (Boolean, Int) = program(index) match {
      case Nop(value) => execute(program.updated(index, Jmp(value)))
      case Jmp(value) => execute(program.updated(index, Nop(value)))
      case _ => (false, -1)
    }
  end VirtualMachine


  abstract class Instruction

  case class Acc(value: Int) extends Instruction

  case class Nop(value: Int) extends Instruction

  case class Jmp(value: Int) extends Instruction
