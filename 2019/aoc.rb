# def read_input(day, separator = ';', strip: true)
#   lines = File.read("data/day#{String(day).rjust(2, '0')}.txt").split separator
#   lines = lines.collect(&:strip) if strip
#   lines
# end

# Class used to expose solutions and to cache intermediate values
class Solution
  def initialize(separator: "\n", strip: true)
    @data = load_data(day, separator, strip)
  end

  def day
    Integer(self.class.name[-2..])
  end

  def part1; end

  def part2; end

  def report
    puts "Day #{day}"
    puts "Part 1: #{part1}; Part 2: #{part2}"
  end

  def self.run
    new.report
  end

  def load_data(day, separator, strip)
    process_data(read_input(day, separator, strip))
  end

  def read_input(day, separator, strip)
    lines = File.read("data/day#{String(day).rjust(2, '0')}.txt").split(separator).filter
    lines = lines.collect(&:strip) if strip
    lines
  end

  def process_data(data)
    data
  end
end
