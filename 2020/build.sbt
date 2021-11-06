lazy val root = (project in file("."))
  .settings(
    name := "advent-of-code",

//    version := "0.1",

    scalaVersion := "3.0.2",
    idePackagePrefix := Some("me.dalsat.adventofcode"),

    libraryDependencies ++= Seq(
//      "org.scala-lang.modules" %% "scala-parallel-collections" % "1.0.0",
      "org.scalactic" %% "scalactic" % "3.2.10",
      "org.scalatest" %% "scalatest" % "3.2.10" % "test",
    )
  )
