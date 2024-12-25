require_relative 'aoc'

def calculate_fuel(mass, recursive = false)
  fuel = mass / 3 - 2

  return 0 if fuel <= 0

  fuel += calculate_fuel(fuel, true) if recursive

  fuel
end

# Day01
class Day01 < Solution
  def part1
    @data.select.collect { |each| calculate_fuel Integer(each) }.sum
  end

  def part2
    @data.select.collect { |each| calculate_fuel Integer(each), true }.sum
  end
end

Day01.run
