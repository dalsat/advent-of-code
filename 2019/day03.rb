require './aoc'

def parse_wire(wire)
  (wire.split ',').map { |token| [token[0], Integer(token[1..])] }
end

def expand_wire(wire)
  wire_points = {}

  position_x = 0
  position_y = 0
  step = 0

  wire.each do |token|
    token[0]
    steps = token[1]
    delta_x = 0
    delta_y = 0

    case token[0]
    when 'R'
      delta_x = 1
    when 'L'
      delta_x = -1
    when 'U'
      delta_y = 1
    when 'D'
      delta_y = -1
    end

    steps.times do
      position_x += delta_x
      position_y += delta_y
      step += 1
      point = [position_x, position_y]

      wire_points[point] = step unless wire_points.include?(point)
    end
  end

  wire_points
end

# Calculate solutions and cache intermediate results
class Day03 < Solution
  def process_data(data)
    @wires = data.collect { |line| parse_wire line }.collect { |wire| expand_wire wire }
    raise "detected #{@wires.length} wires instead of 2" if @wires.length != 2

    @intersections = @wires[0].keys & @wires[1].keys
  end

  def part1
    @intersections.collect { |each| each[0].abs + each[1].abs }.min
  end

  def part2
    @intersections.collect { |each| @wires[0][each] + @wires[1][each] }.min
  end
end

Day03.new.report
