use core::panic;
use std::collections::HashSet;

use aoc::{parse_input, read_day, Solution};

fn main() {
    println!("Solution for day 7: {}", solve());
}

pub fn solve() -> Solution<u32> {
    let input = parse_input(read_day(7));
    Solution::new(part1(&input), part2(&input))
}

fn part1(input: &Vec<String>) -> u32 {
    input.iter()
        .map(|ip| IP::new(ip))
        .filter(|ip| ip.supports_tls())
        .count() as u32
}

fn part2(input: &Vec<String>) -> u32 {
    input.iter()
        .map(|ip| IP::new(ip))
        .filter(|ip| ip.supports_ssl())
        .count() as u32
}


struct IP {
    address: String,
}

impl IP {

    fn new(address: &str) -> Self {
        IP {address: address.to_string()}
    }

    fn supports_tls(&self) -> bool {
        let mut buffer = Buffer::<char, 4>::new();
        let mut in_hypernet = false;
        let mut supports_tls = false;

        for c in self.address.chars() {
            match c {
                '[' => {
                    if in_hypernet { panic!("malformed ip: already in hypernet region") }
                    in_hypernet = true;
                    buffer.clear();
                },
                ']' => {
                    if !in_hypernet { panic!("malformed ip: not in hypernet region") }
                    in_hypernet = false;
                    buffer.clear();
                },
                c => {
                    buffer.push(c);
                    if buffer.is_abba() { 
                        if in_hypernet { return false }
                        else { supports_tls = true };
                    }
                }
            }
        }
        supports_tls
    }

    fn supports_ssl(&self) -> bool {
        let mut buffer = Buffer::<char, 3>::new();
        let mut in_hypernet = false;
        let mut aba_matches = HashSet::new();
        let mut bab_matches = HashSet::new();

        for c in self.address.chars() {
            match c {
                '[' => {
                    if in_hypernet { panic!("malformed ip: already in hypernet region") }
                    in_hypernet = true;
                    buffer.clear();
                },
                ']' => {
                    if !in_hypernet { panic!("malformed ip: not in hypernet region") }
                    in_hypernet = false;
                    buffer.clear();
                },
                c => {
                    buffer.push(c);
                    if buffer.is_bab() {
                        if in_hypernet {
                            bab_matches.insert(buffer.get_bab());
                        } else {
                            aba_matches.insert(buffer.value());
                        }
                    }
                }
            }
        }

        aba_matches.intersection(&bab_matches).next().is_some()
    }
}

struct Buffer<T: Default + Copy + PartialEq, const SIZE: usize>([T; SIZE]);

impl <const SIZE: usize> Buffer<char, SIZE> {
    fn new() -> Self {
        Buffer([char::default(); SIZE])
    }

    fn push(&mut self, new_value: char) {
        for i in 1..self.0.len() {
            self.0[i-1] = self.0[i];
        }
        self.0[self.0.len() - 1] = new_value;
    }

    fn is_abba(&self) -> bool {
        self.0[0] != char::default() &&
        self.0[0] != self.0[1] &&
        self.0[0] == self.0[3] &&
        self.0[1] == self.0[2]
    }

    fn is_bab(&self) -> bool {
        self.0[0] != char::default() &&
        self.0[0] == self.0[2] &&
        self.0[0] != self.0[1]
    }

    fn value(&self) -> String {
        self.0.iter().collect()
    }

    fn get_bab(&self) -> String {
        format!("{}{}{}", self.0[1], self.0[0], self.0[1])
    }

    fn clear(&mut self) {
        for i in &mut self.0 {
            *i = char::default()
        }
    }
}
