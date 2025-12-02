use aoc_2025::read_file;

struct TokenRange {
    current: u64,
    end: u64,
}

impl TokenRange {
    fn new(start: u64, end: u64) -> Self {
        TokenRange {
            current: start,
            end,
        }
    }

    fn from(range_str: &str) -> Self {
        let tokens = range_str.split("-").collect::<Vec<_>>();
        assert!(tokens.len() == 2, "{tokens:?}");
        let start = tokens[0].parse().unwrap();
        let end = tokens[1].parse().unwrap();

        TokenRange::new(start, end)
    }
}
impl Iterator for TokenRange {
    type Item = u64;

    fn next(&mut self) -> Option<Self::Item> {
        if self.current <= self.end {
            let next_value = self.current;
            self.current += 1;
            return Some(next_value);
        } else {
            return None;
        }
    }
}

fn is_token_valid(token: &u64) -> bool {
    let token_string = token.to_string();
    if token_string.len() % 2 != 0 {
        return true;
    }
    let mid_point = token_string.len() / 2;
    let first_token = &token_string[..mid_point];
    let second_token = &token_string[mid_point..];

    !(first_token == second_token)
}

fn has_repeated_sequence(token: &u64) -> bool {
    let token_string = token.to_string();

    for length in 1..token_string.len() + 1 {
        if has_repeated_sequence_of_length(&token_string, length) {
            return true;
        }
    }
    false
}

fn has_repeated_sequence_of_length(token: &String, length: usize) -> bool {
    if token.len() % length != 0 {
        return false;
    }

    let mut repetitions = 0;
    let mut buffer = String::with_capacity(length);
    let mut first_token: Option<String> = None;

    for char in token.chars() {
        buffer.push(char);
        if buffer.len() >= length {
            match &first_token {
                Some(value) if *value == buffer => repetitions += 1,
                Some(_) => return false,
                None => first_token = Some(buffer.clone()),
            }
            buffer.clear();
        }
    }

    return repetitions > 0;
}

fn main() {
    let input = read_file(2);

    let tokens: Vec<u64> = input
        .trim()
        .split(",")
        .map(|e| e.trim())
        .filter(|e| !e.is_empty())
        .flat_map(|e| TokenRange::from(e))
        .collect();

    let part1: u64 = tokens.iter().filter(|token| !is_token_valid(token)).sum();

    let part2: u64 = tokens
        .iter()
        .filter(|token| has_repeated_sequence(token))
        .sum();

    println!("Part 1: {}", part1);
    println!("Part 2: {}", part2);
}
