use std::collections::HashMap;

use aoc::{parse_input, read_day, Solution};

type Id = u8;

fn main() {
    println!("Solution for day 9: {}", solve());
}

pub fn solve() -> Solution<u32> {
    let input = parse_input(read_day(10));
    Solution::new(part1(&input), part2(&input))
}

fn part1(input: &Vec<String>) -> u32 {
    let plan = Plan::from(input);
    // let tasks: Vec<Source> = input.iter()
    //     .map(|e| { Source::new(e) })
    //     .collect();
    // println!("{:?}", plan.inputs);
    0
}

fn part2(input: &Vec<String>) -> u32 {
    0
}

struct Plan {
    values: Vec<Value>,
    bots: HashMap<Id, Bot>,
    queue: Vec<Value>,
}

impl Plan {
    fn new() -> Self {
        Self { values: Vec::new(), bots: HashMap::new(), queue: Vec::new() }
    }

    fn from(specs: &Vec<String>) -> Self {
        let mut new_plan = Self::new();
        specs.iter().for_each(|e| new_plan.parse(e));
        new_plan
    }

    fn parse(&mut self, spec: &str) {
        match spec.split_whitespace().collect::<Vec<&str>>() {
            tokens if tokens[0] == "value" => self.values.push(Value {
                value: tokens[1].parse().unwrap(), target: tokens[5].parse().unwrap(),
            }),
            tokens if tokens[0] == "bot" => {
                let new_bot = Bot {
                    id: tokens[1].parse().unwrap(),
                    low: Target::from(tokens[5], tokens[6].parse().unwrap()),
                    high: Target::from(tokens[10], tokens[11].parse().unwrap()),
                    values: Vec::with_capacity(2),
                };
                self.bots.insert(new_bot.id, new_bot);
            }
            _ => panic!("unrecognized command {}", spec)
        }
    }

    fn propagate(&mut self) {
        for value in &self.values {
            let bot = &mut *self.bots.get(&value.target).unwrap();
            bot.add_value(value.value);
            if bot.is_ready() {
                self.propagate_bot(&mut bot);
            }
        }
    }
    
    fn propagate_bot(&mut self, bot: &Bot) {

    }
}


struct Value { value: u8, target: Id }
struct Bot { id: Id, low: Target, high: Target, values: Vec<u8> }

impl Bot {
    fn add_value(&mut self, value: u8) {
        assert!(self.values.len() <= 2);
        self.values.push(value);
    }

    fn is_ready(&self) -> bool {
        self.values.len() == 2
    }
}

enum Target {
    Bot(Id),
    Output(Id),
}

impl Target {
    fn from(target_type: &str, id: Id) -> Self {
        match target_type {
            "bot" => Self::Bot(id),
            "output" => Self::Output(id),
            any => panic!("unrecognized target {any}")
        }
    }
}