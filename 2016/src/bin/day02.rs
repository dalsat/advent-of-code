use aoc::{read_day, Solution};
use std::collections::HashMap;


type Code = u32;

fn main() {
    println!("Solution for day 2: {}", day2());
}

pub fn day2() -> Solution<String> {
    let instructions: Vec<String> = parse_input(read_day(2));
    Solution::new(part1(&instructions), part2(&instructions))
}


fn parse_input(input: String) -> Vec<String> {
    input
        .split("\n")
        .map(str::to_string)
        .filter(|s| {!s.is_empty()})
        .collect()
}

fn part1(instructions: &Vec<String>) -> String {
    
    let padlock: HashMap<(Code, char), Code> = HashMap::from([
        ((1, 'R'), 2),
        ((1, 'D'), 4),

        ((2, 'L'), 1),
        ((2, 'R'), 3),
        ((2, 'D'), 5),
        
        ((3, 'L'), 2),
        ((3, 'D'), 6),
        
        ((4, 'U'), 1),
        ((4, 'R'), 5),
        ((4, 'D'), 7),

        ((5, 'U'), 2),
        ((5, 'L'), 4),
        ((5, 'R'), 6),
        ((5, 'D'), 8),

        ((6, 'U'), 3),
        ((6, 'L'), 5),
        ((6, 'D'), 9),

        ((7, 'U'), 4),
        ((7, 'R'), 8),

        ((8, 'L'), 7),
        ((8, 'U'), 5),
        ((8, 'R'), 9),

        ((9, 'U'), 6),
        ((9, 'L'), 8),
    ]);

    compute_code(instructions, padlock)
}


fn part2(instructions: &Vec<String>) -> String {

    let padlock: HashMap<(Code, char), Code> = HashMap::from([
        ((1, 'D'), 0x3),

        ((2, 'R'), 0x3),
        ((2, 'D'), 0x6),
        
        ((3, 'U'), 0x1),
        ((3, 'L'), 0x2),
        ((3, 'R'), 0x4),
        ((3, 'D'), 0x7),
        
        ((4, 'L'), 0x3),
        ((4, 'D'), 0x8),

        ((5, 'R'), 0x6),

        ((6, 'U'), 0x2),
        ((6, 'L'), 0x5),
        ((6, 'R'), 0x7),
        ((6, 'D'), 0xA),

        ((7, 'U'), 0x3),
        ((7, 'L'), 0x6),
        ((7, 'R'), 0x8),
        ((7, 'D'), 0xB),

        ((8, 'U'), 0x4),
        ((8, 'L'), 0x7),
        ((8, 'R'), 0x9),
        ((8, 'D'), 0xC),

        ((9, 'L'), 0x8),

        ((0xA, 'U'), 0x6),
        ((0xA, 'R'), 0xB),

        ((0xB, 'U'), 0x7),
        ((0xB, 'L'), 0xA),
        ((0xB, 'R'), 0xC),
        ((0xB, 'D'), 0xD),

        ((0xC, 'U'), 0x8),
        ((0xC, 'L'), 0xB),

        ((0xD, 'U'), 0xB),
    ]);

    compute_code(instructions, padlock)
}


fn compute_code(instructions: &Vec<String>, padlock: HashMap<(Code, char), Code>) -> String {
    let mut current_value: Code = 5;
    let mut code = String::new();

    for row in instructions {
        for char in row.chars() {
            let key = (current_value, char);
            match padlock.get(&key) {
                Some(&value) => current_value = value,
                None => {},
            }
        }
        code += format!("{:X}", current_value).as_str();
    }
    code
}
