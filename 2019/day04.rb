# frozen_string_literal: true

require './aoc'

# TODO: Doc for class
class Validator
  def length?(pwd)
    String(pwd).length == 6
  end

  def consecutives?(pwd)
    String(pwd).chars.each_cons(2).any? { |a, b| a == b }
  end

  def digits_ascending?(pwd)
    pwd.digits.each_cons(2).all? { |a, b| a >= b }
  end

  def valid?(pwd)
    length?(pwd) and consecutives?(pwd) and digits_ascending?(pwd)
  end
end

# TODO: class Doc
class AdvancedValidator < Validator
  def consecutives?(pwd)
    count = 0
    prev = nil

    String(pwd).chars.each do |each|
      if prev == each
        count += 1
      else
        return true if count == 2

        count = 1
      end

      prev = each
    end

    count == 2
  end
end

# Day04
class Day04 < Solution
  def process_data(data)
    data.first.split('-').collect { |each| Integer each }
  end

  def range
    (@data[0]..@data[1])
  end

  def part1
    validator = Validator.new
    range
      .filter { |each| validator.valid? each }
      .length
  end

  def part2
    validator = AdvancedValidator.new
    range
      .filter { |each| validator.valid? each }
      .length
  end
end

Day04.run
