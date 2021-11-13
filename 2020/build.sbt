lazy val root = (project in file("."))
  .settings(
    name := "advent-of-code",

    scalaVersion := "3.1.0",
    idePackagePrefix := Some("me.dalsat.adventofcode"),

    libraryDependencies ++= Seq(
      "org.scalactic" %% "scalactic" % "3.2.10",
      "org.scalatest" %% "scalatest" % "3.2.10" % "test",
    )
  )
