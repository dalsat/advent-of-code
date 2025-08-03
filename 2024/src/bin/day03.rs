use regex::{Captures, Regex};

enum Instruction {
    Mul(u32, u32),
    Do,
    Dont,
}

fn parse_capture(captures: &Captures) -> Option<Instruction> {
    match captures.get(0).unwrap().as_str() {
        c if c.starts_with("mul(") => Some(Instruction::Mul(
            captures.get(1).unwrap().as_str().parse().unwrap(),
            captures.get(2).unwrap().as_str().parse().unwrap(),
        )),
        c if c.starts_with("do()") => Some(Instruction::Do),
        c if c.starts_with("don't()") => Some(Instruction::Dont),
        _ => None,
    }
}

fn process_data(data: String) -> Vec<Instruction> {
    let pattern = Regex::new(r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)").unwrap();

    pattern
        .captures_iter(data.as_str())
        .filter_map(|each| parse_capture(&each))
        .collect()
}
fn part_1(instructions: &Vec<Instruction>) -> u32 {
    instructions
        .iter()
        .map(|each| match each {
            Instruction::Mul(first, second) => first * second,
            Instruction::Do => 0,
            Instruction::Dont => 0,
        })
        .sum()
}

fn part_2(instructions: &Vec<Instruction>) -> u32 {
    let mut result = 0;
    let mut do_active = true;

    for each in instructions {
        match each {
            Instruction::Mul(first, second) => {
                if do_active {
                    result += first * second
                }
            }
            Instruction::Do => do_active = true,
            Instruction::Dont => do_active = false,
        }
    }
    result
}

fn main() {
    let mut solution = aoc::Solution::day(3);
    let data = solution.data();

    let instructions = process_data(data);
    solution
        .part1(part_1(&instructions))
        .part2(part_2(&instructions))
        .print();
}
