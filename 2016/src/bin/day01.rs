use std::collections::HashSet;
use aoc::{read_day, Solution};


type Directions = Vec<(String, i32)>;

fn main() {
    println!("Solution for day 1: {}", day1());
}

pub fn day1() -> Solution<i32> {
    let directions: Directions = parse_input(read_day(1));
    Solution::new(part1(&directions), part2(&directions))
}

fn parse_input(input: String) -> Directions {
    input
        .split(",")
        .map(str::trim)
        .map(|s| { s.split_at(1) })
        .map(|(direction, distance)| {(
            direction.to_string(),
            distance.parse().expect("unable to parse value")
        )})
        .collect()
}


fn part1(directions: &Directions) -> i32 {

    let mut position = Position::new();

    for (turn, distance) in directions.iter() {
        position.step(turn, *distance);
    }

    position.distance()
}


fn part2(directions: &Directions) -> i32 {
    let mut position = Position::new();
    let mut visited_positions = HashSet::new();
    visited_positions.insert(position.current_position());

    for (turn, distance) in directions {
        let steps = distance;
        position.step(turn, 0);
        for _ in 0..*steps {
            position.step("", 1);
            let current_position = position.current_position();
            if visited_positions.contains(&current_position) {
                return position.distance()
            }
            visited_positions.insert(current_position);
        }
    }

    panic!("no solution found");
}


struct Position {
    x:  i32,
    y:  i32,
    dx: i32,
    dy: i32,
}

impl Position {
    fn new() -> Self {
        Position{x: 0, y: 0, dx: 0, dy: 1}
    }

    fn step(&mut self, turn: &str, distance: i32) {
        match turn {
            "R" => self.right(),
            "L" => self.left(),
            "" => {},
            _ => panic!("unable to parse value: {turn}"),
        }
        self.walk(distance)
    }

    fn right(&mut self) {
        if self.dx == 0 && self.dy == 1 { self.dx = 1; self.dy = 0 }
        else if self.dx == 1 && self.dy == 0 { self.dx = 0; self.dy = -1 }
        else if self.dx == 0 && self.dy == -1 { self.dx = -1; self.dy = 0 }
        else if self.dx == -1 && self.dy == 0 { self.dx = 0; self.dy = 1 }
    }

    fn left(&mut self) {
        if self.dx == 0 && self.dy == 1 { self.dx = -1; self.dy = 0 }
        else if self.dx == -1 && self.dy == 0 { self.dx = 0; self.dy = -1 }
        else if self.dx == 0 && self.dy == -1 { self.dx = 1; self.dy = 0 }
        else if self.dx == 1 && self.dy == 0 { self.dx = 0; self.dy = 1 }
    }

    fn walk(&mut self, distance: i32) {
        self.x += distance * self.dx;
        self.y += distance * self.dy;
    }

    fn current_position(&self) -> (i32, i32) {
        (self.x, self.y)
    }

    fn distance(&self) -> i32 {
        return self.x.abs() + self.y.abs();
    }
}
