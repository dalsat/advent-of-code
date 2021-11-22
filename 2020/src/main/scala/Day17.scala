package me.dalsat.adventofcode


object Day17 extends Solution(17):

  override def part1 = pocketDimension3.execute(6).numberOfActiveCubes

  override def part2 = pocketDimension4.execute(6).numberOfActiveCubes

  val pocketDimension3 = PocketDimension.from(input)(3)
  val pocketDimension4 = PocketDimension.from(input)(4)


  type Cube = Seq[Int]


  class PocketDimension(val activeCubes: Set[Cube]):

    def numberOfActiveCubes: Long = activeCubes.size

    def neighbors(cube: Cube): Seq[Cube] =

      def loop(head: List[Int], tail: List[Int]): Seq[Seq[Int]] = tail match {
        case Nil => List(head.reverse)
        case x :: xs => (x - 1 to x + 1) flatMap (each => loop(each :: head, xs))
      }

      loop(Nil, cube.toList) filter (_ != cube)
    end neighbors

    def activeNeighborsFor(cube: Cube) =
      neighbors(cube) filter (activeCubes contains _)

    def isActive(cube: Cube): Boolean =
      val activeNeighbors = activeNeighborsFor(cube).size
      (activeNeighbors == 3) || (activeNeighbors == 2 && (activeCubes contains cube))

    def nextEpoch: PocketDimension =
      val newActiveCubes = for (
        activeCube <- activeCubes;
        nextCube <- activeCube +: neighbors(activeCube)
        if isActive(nextCube)
      ) yield nextCube

      PocketDimension(newActiveCubes)

    def execute(epochs: Int): PocketDimension =
      if epochs == 0 then
        this
      else
        nextEpoch.execute(epochs - 1)


    def from(dataset: Dataset) = PocketDimension(parse(dataset))

    private def parse(dataset: Dataset): Set[Cube] =
      dataset.zipWithIndex.flatMap((line, index) => parseLine(line, index)).toSet

    private def parseLine(line: String, lineNumber: Int): Seq[Cube] =
      line.zipWithIndex
        .map ((each, index) =>
          if each == '#' then
            Some(List(index, lineNumber, 0))
          else
            None)
        .filter(_.isDefined)
        .map(_.get)

  end PocketDimension


  object PocketDimension:

    def from(dataset: Dataset)(size: Int) = PocketDimension(parse(dataset)(size))

    private def parse(dataset: Dataset)(size: Int): Set[Cube] =
      dataset.zipWithIndex.flatMap((line, index) => parseLine(line, index)(size)).toSet

    private def parseLine(line: String, lineNumber: Int)(size: Int): Seq[Cube] =
      line.zipWithIndex
        .map ((each, index) =>
          if each == '#' then
            Some(List(index, lineNumber) ++ (3 to size map (_ => 0)))
          else
            None
        )
        .filter(_.isDefined)
        .map(_.get)
