use std::collections::HashMap;

use aoc::{parse_input, read_day, Solution};


fn main() {
    println!("Solution for day 6: {}", solve());
}

pub fn solve() -> Solution<String> {
    let input = parse_input(read_day(6));
    let counters = frequencies(&input);
    Solution::new(part1(&counters), part2(&counters))
}

fn part1(counters: &[Counter; 8]) -> String {
    counters.iter()
        .map(|counter| counter.max())
        .collect()
}

fn part2(counters: &[Counter; 8]) -> String {
    counters.iter()
        .map(|counter| counter.min())
        .collect()
}


fn frequencies(codes: &Vec<String>) -> [Counter; 8] {
    let mut counters = [
        Counter::new(), Counter::new(), Counter::new(), Counter::new(),
        Counter::new(), Counter::new(), Counter::new(), Counter::new(),
    ];
    for code in codes.iter() {
        for (char, counter) in code.chars().zip(&mut counters) {
            counter.add(char);
        }
    }
    counters
}

struct Counter {
    values: HashMap<char, u32>,
}

impl Counter {

    fn new() -> Self {
        Counter { values: HashMap::new() }
    }

    fn add(&mut self, key: char) {
        self.values.entry(key).and_modify(|count| *count += 1).or_insert(1);
    }

    fn max(&self) -> char {
        *self.values.iter().reduce(|acc, next| {
            if acc.1 < next.1 { next } else { acc }
        }).expect("should not happen").0
    }

    fn min(&self) -> char {
        *self.values.iter().reduce(|acc, next| {
            if acc.1 > next.1 { next } else { acc }
        }).expect("should not happen").0
    }
}
