use std::fmt;
use std::fmt::Display;
use std::{fs, str::FromStr};

const NOT_IMPLEMENTED: &str = "not implemented";

// Load the input file from disk for the given day.
pub fn read_file(day: u8) -> String {
    let path = format!("input/day{day:02}.txt");
    return fs::read_to_string(path).expect("Input file not found");
}

// Parse all the numbers into a string and ignores the non-numerical tokens.
pub fn parse_numbers<T: FromStr>(line: &str) -> Vec<T> {
    line.split_whitespace()
        .filter_map(|each| each.parse().ok())
        .collect()
}

pub struct Solution {
    day: u8,
    part1: Option<String>,
    part2: Option<String>,
}

impl Solution {
    pub fn day(day: u8) -> Self {
        Self {
            day,
            part1: None,
            part2: None,
        }
    }

    pub fn part1(&mut self, value: impl Display) -> &mut Self {
        self.part1 = Some(value.to_string());
        self
    }

    pub fn part2(&mut self, value: impl Display) -> &mut Self {
        self.part2 = Some(value.to_string());
        self
    }
}

impl Solution {
    pub fn print(&self) {
        println!("{}", self);
    }

    pub fn data(&self) -> String {
        read_file(self.day)
    }
}
impl fmt::Display for Solution {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        writeln!(
            f,
            "Day {:0>2}\n- Part 1: {}\n- Part 2: {}",
            self.day,
            self.part1.clone().unwrap_or(String::from(NOT_IMPLEMENTED)),
            self.part2.clone().unwrap_or(String::from(NOT_IMPLEMENTED))
        )
    }
}
