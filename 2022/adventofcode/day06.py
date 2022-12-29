from aoc import load_day


__day__ = 6

def part1(data):
    return CircularBuffer.process_stream(data, 4)

def part2(data):
    return CircularBuffer.process_stream(data, 14)


class CircularBuffer:
    def __init__(self, size):
        self._data = [None] * size
        self._index = 0
        self.size = size
    
    def push(self, element):
        self._data[self._index] = element
        self._index = (self._index + 1) % self.size

    def check_all_different(self) -> bool:
        return len(set(filter(bool, self._data))) == self.size

    def process_stream(stream, size):
        buffer = CircularBuffer(size)
        for i, c in enumerate(data, 1):
            buffer.push(c)
            if buffer.check_all_different():
                return i


data = load_day(__day__)


if __name__ == '__main__':
    print(f'Day {__day__}: {part1(data)}, {part2(data)}')
