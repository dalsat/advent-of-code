use aoc::{parse_input, read_day, Solution};

fn main() {
    println!("Solution for day 9: {}", solve());
}

pub fn solve() -> Solution<usize> {
    let input = parse_input(read_day(9));
    Solution::new(part1(&input), part2(&input))
}

fn part1(input: &Vec<String>) -> usize {    
    UnzipBuffer::from(&input[0]).count(false)
}

fn part2(input: &Vec<String>) -> usize {
    UnzipBuffer::from(&input[0]).count(true)
}

struct UnzipBuffer {
    buffer: Vec<u8>,
    count: usize,
}

impl UnzipBuffer {

    fn from(data: &str) -> Self {
        Self::new(data.bytes().rev().collect::<Vec<u8>>())
    }

    fn new(data: Vec<u8>) -> Self {
        Self {
            buffer: data,
            count: 0,
        }
    }

    fn count(&mut self, full_unzip: bool) -> usize {

        loop {
            match self.buffer.pop() {
                Some(b'(') => { self.pop_marker(full_unzip); },
                Some(_) => { self.count += 1; },
                None => break,
            }
        }
        self.count
    }

    fn pop_marker(&mut self, full_unzip: bool) {
        let region_size = self.pop_number();
        let repetitions = self.pop_number() as usize;

        let mut region = Vec::new();
        for _ in 0..region_size {
            region.push(self.buffer.pop().expect("unexpected end of stream"));
        }
        region.reverse();

        self.count += if full_unzip {
            repetitions * UnzipBuffer::new(region).count(full_unzip)
        } else {
            repetitions * region.len()
        }
    }

    fn pop_number(&mut self) -> u32 {
        let mut next_char = self.buffer.pop().expect("unexpected enf of input");
        let mut number_buffer = String::new();
        while next_char.is_ascii_digit() {
            number_buffer.push(next_char as char);
            next_char = self.buffer.pop().expect("unexpected enf of input");
        }
        number_buffer.parse().expect("error parsing number")
    }
}
