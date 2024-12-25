require_relative 'aoc'

# VM class for IntCode
class IntCodeVM
  def initialize(code, noun, verb)
    @code = code.clone
    @code[1] = noun if noun
    @code[2] = verb if verb
    @running = false
  end

  def run
    @running = true
    intcode_processor
  end

  def intcode_processor
    page_size = 4
    ((0..@code.length).step page_size).each do |index|
      run_instruction(index)
      return @code.at 0 unless @running
    end
  end

  def run_instruction(index)
    block = @code[index..index + 3]
    target = block.at 3

    case block.first
    when 1
      @code[target] = @code.at(block.at(1)) + @code.at(block.at(2))
    when 2
      @code[target] = @code.at(block.at(1)) * @code.at(block.at(2))
    when 99
      # @code.at 0
      @running = false
    else
      raise "Unknown operation #{block.first} @#{index}. Context: #{block}"
    end
  end

  def intcode_preprocessor(data, noun, verb)
    code = data.clone
    code[1] = noun
    code[2] = verb
    intcode_processor code
  end
end

# Day02
class Day02 < Solution
  def initialize
    super(separator: ',')
  end

  def process_data(data)
    data.collect { |each| Integer each }
  end

  def part1
    IntCodeVM.new(@data, 12, 2).run
    # intcode_preprocessor(@data, 12, 2)
  end

  def part2
    target_value = 19_690_720
    (0..99).to_a.repeated_permutation(2).each do |noun, verb|
      return 100 * noun + verb if IntCodeVM.new(@data, noun, verb).run == target_value
    end
    raise 'error: target value not found'
  end
end

Day02.run
