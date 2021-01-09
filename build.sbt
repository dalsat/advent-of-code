lazy val root = (project in file("."))
  .settings(
    name := "advent-of-code",

    version := "0.1",

    //scalaVersion := "2.13.4"
    scalaVersion := "3.0.0-M3",
    //    useScala3doc := true,
    idePackagePrefix := Some("me.dalsat.adventofcode"),

    libraryDependencies ++= Seq(
      "org.scala-lang.modules" %% "scala-parallel-collections" % "1.0.0",
      "org.scalactic" %% "scalactic" % "3.2.3",
      "org.scalatest" %% "scalatest" % "3.2.3" % "test",
    )
  )
