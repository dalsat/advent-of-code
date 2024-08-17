use std::fs;
use std::fmt::{Display, Formatter, Result};


pub fn read_day(day: u8) -> String {
    let file_path = format!("resources/input/day{:02}.txt", day);
    fs::read_to_string(&file_path)
        .expect(format!("file not found: {}", &file_path).as_str())
}

pub struct Solution<T> (T, T);

impl<T> Solution<T> {
    pub fn new(part1: T, part2: T) -> Solution<T> {
        Self(part1, part2)
    }
}

impl<T: Display> Display for Solution<T> {
    fn fmt(&self, f: &mut Formatter) -> Result {
        write!(f, "Part 1: {}, Part 2: {}", self.0, self.1)
    }
}

pub fn parse_input<'a>(input: String) -> Vec<String> {
    input
        .split("\n")
        .map(str::to_string)
        .filter(|s| {!s.is_empty()})
        .collect()
}
