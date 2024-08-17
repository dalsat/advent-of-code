use std::{collections::HashMap, cmp::Ordering};
use aoc::{read_day, Solution};


fn main() {
    println!("Solution for day 4: {}", day4());
}

pub fn day4() -> Solution<u32> {
    let codes = parse_input(read_day(4));
    Solution::new(part1(&codes), part2(&codes))
}

fn parse_input(input: String) -> Vec<Code> {
    input
        .split("\n")
        .filter(|row| { !row.is_empty() })
        .map(|raw| {Code::from(raw)})
        .collect()
}

fn part1(codes: &Vec<Code>) -> u32 {
    codes.iter()
        .filter(|code| {code.is_valid()})
        .map(|c| c.sector)
        .sum()
}

fn part2(codes: &Vec<Code>) -> u32 {
    let target_room = "northpoleobjectstorage";
    let code: Vec<&Code> = codes.iter()
        .filter(|c| c.is_valid())
        .filter(|c| c.decypher() == target_room)
        .collect();
    code[0].sector()
}


struct Code {
    chars: Vec<char>,
    sector: u32,
    checksum: String,
}

impl Code {
    fn from(raw_code: &str) -> Self {
        const SPLIT_PATTERNS: [char; 2] = ['[', '-'];
        let mut tokens = raw_code
            .trim_end_matches(']')
            .split(SPLIT_PATTERNS)
            .collect::<Vec<&str>>();
        // assert_eq!(tokens.len(), 2);
        Code{
            checksum: tokens.pop()
                .expect("malformed checksum").to_string(),
            sector: tokens.pop()
                .expect("malformed sector").parse().expect("parsing error"),
            chars: tokens.iter().flat_map(|t| {t.chars()}).collect(),
        }
    }

    fn compute_checksum(&self) -> String {
        let counts: HashMap<char, u32> = self.chars.iter()
            .fold(HashMap::new(), |mut map, c| {
                *map.entry(*c).or_insert(0) += 1;
                map
            });

        let mut freqs: Vec<(char, u32)> = counts
            .into_iter()
            .collect::<Vec<(char, u32)>>();
        
        freqs.sort_by(|a, b| Code::compare_chars(*a, *b));
        freqs.iter().map(|(char, _)| char).take(5).collect()
    }

    fn compare_chars(token1: (char, u32), token2: (char, u32)) -> Ordering {
        match token2.1.cmp(&token1.1) {
            Ordering::Equal => token1.0.cmp(&token2.0),
            other => other,
        }
    }

    fn is_valid(&self) -> bool {
        self.checksum == self.compute_checksum()
    }

    fn decypher(&self) -> String {
        self.chars.iter()
            .map(|c| self.decypher_char(*c))
            .collect::<String>()
    }

    fn decypher_char(&self, c: char) -> char {
        ((c as u32 + self.sector - 97) % (123 - 97) + 97) as u8 as char
    }

    fn sector(&self) -> u32 {
        self.sector
    }
}
