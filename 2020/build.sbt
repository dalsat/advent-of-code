lazy val root = (project in file("."))
  .settings(
    name := "advent-of-code",

    scalaVersion := "3.2.1",
    idePackagePrefix := Some("me.dalsat.adventofcode"),

    libraryDependencies ++= Seq(
      "org.scalactic" %% "scalactic" % "3.2.14",
      "org.scalatest" %% "scalatest" % "3.2.14" % "test",
    )
  )
