package me.dalsat.adventofcode

import org.scalatest.flatspec.AnyFlatSpec
import org.scalatest.matchers.should


class Day5Test extends AnyFlatSpec with should.Matchers {

  "A SeatDecoder" should "decode all the seats in the input" in {
    val sd = new SeatDecoder
    sd.dataset = sd.sample

    sd.decode("BFFFBBFRRR") should be(567)
    sd.decode("FFFBBBFRRR") should be(119)
    sd.decode("BBFFBBFRLL") should be(820)
  }

  "A SeatDecoder" should "decode the correct row" in {
    val sd = new SeatDecoder
    sd.dataset = sd.sample

    sd.decodeSubstring("BFFFBBF") should be(70)
    sd.decodeSubstring("FFFBBBF") should be(14)
    sd.decodeSubstring("BBFFBBF") should be(102)
  }

  "A SeatDecoder" should "decode the correct column" in {
    val sd = new SeatDecoder
    sd.dataset = sd.sample

    sd.decodeSubstring("RRR") should be(7)
    sd.decodeSubstring("RLL") should be(4)
  }


  "A SeatDecoder" should "find the correct max seat value in the sample" in {
    val sd = new SeatDecoder
    sd.dataset = sd.sample

    sd.findMax() should be(820)
  }

}
