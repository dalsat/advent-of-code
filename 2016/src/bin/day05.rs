use std::fmt;
use md5::{Md5, Digest};
use aoc::{read_day, Solution};


fn main() {
    println!("Solution for day 5: {}", day5());
}

pub fn day5() -> Solution<String> {
    let input = read_day(5);
    Solution::new(
        part1(&input),
        part2(&input)
    )
}

fn part1(base_key: &String) -> String {
    let mut key = Code::new();
    let mut next_char_index: usize = 0;
    println!("Searching key for part 1");

    for hash in HashIter::new(base_key) {
        let value = hash.chars().nth(5).expect("error reading hash");
        key.put_at(value, next_char_index);
        next_char_index += 1;
        println!("match found: {key} ({hash})");
        if next_char_index >= 8 {
            return format!("{key}")
        }
    }
    panic!("key not found")
}

fn part2(base_key: &String) -> String {
    let mut key = Code::new();
    let mut found_chars: u8 = 0;
    println!("Searching key for part 1");

    for hash in HashIter::new(base_key) {
        match hash.chars().nth(5).expect("error reading index").to_string().parse() {
            Ok(index) => {
                let value = hash.chars().nth(6).expect("error reading value");
                if (index < 8) && (!key.has_at(index)) {
                    key.put_at(value, index);
                    found_chars += 1;
                    println!("match found: {key} ({hash})");
                }
            }
            _ => {}
        }
        if found_chars >= 8 {
            return format!("{key}")
        }
    }
    panic!("key not found")
}


struct HashIter<'a> {
    base_key: &'a str,
    padding: u32,
}

impl <'a> HashIter<'a> {
    const INTERESTING_STRING: &str = "00000";

    fn new(base_key: &'a str) -> Self {
        HashIter { base_key: &base_key, padding: 0 }
    }
}

impl <'a> Iterator for HashIter<'a> {

    type Item = String;

    fn next(&mut self) -> Option<Self::Item> {
        loop {
            let next_hash = format!("{:x}", Md5::digest(format!("{}{}", self.base_key, self.padding.to_string())));
            self.padding += 1;
            if next_hash.starts_with(Self::INTERESTING_STRING) {
                return Some(next_hash);
            }
        }
    }
}


struct Code([char; 8]);

impl Code {
    const DEFAULT: char = '*';

    fn new() -> Self {
        Code([Self::DEFAULT; 8])
    }

    fn has_at(&self, index: usize) -> bool {
        (self.0)[index] != Self::DEFAULT
    }

    fn put_at(&mut self, value: char, index: usize) {
        self.0[index] = value
    }
}

impl fmt::Display for Code {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        let mut display = String::new();
        for c in self.0 {
            display.push(c);
        }
        write!(f, "{display}")
    }
}