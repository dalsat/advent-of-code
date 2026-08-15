use aoc_2025::read_file;
use std::convert::From;

#[derive(Debug)]
enum Direction {
    LEFT,
    RIGHT,
}

#[derive(Debug)]
struct Move {
    direction: Direction,
    distance: u16,
}

impl Move {
    fn eval(&self) -> i32 {
        match self.direction {
            Direction::LEFT => i32::from(self.distance) * -1,
            Direction::RIGHT => i32::from(self.distance),
        }
    }
}

impl From<&str> for Move {
    fn from(token: &str) -> Self {
        let direction_token = &token[0..1];
        let direction = if direction_token == "L" {
            Direction::LEFT
        } else if direction_token == "R" {
            Direction::RIGHT
        } else {
            panic!("unknown direction: {}", direction_token)
        };

        let distance = token[1..].parse::<u16>().unwrap();

        Move {
            direction,
            distance,
        }
    }
}

type DialType = u8;

struct Dial {
    value: DialType,
    count_zero: u16,
    pass_by_zero: u16,
}

impl Dial {
    const DIAL_SIZE: DialType = 100;

    fn new() -> Self {
        Dial {
            value: 50,
            count_zero: 0,
            pass_by_zero: 0,
        }
    }

    fn add(&mut self, a_move: &Move) {
        let mut new_value: i32 = self.value as i32 + a_move.eval();

        while new_value >= Dial::DIAL_SIZE as i32 {
            new_value -= Dial::DIAL_SIZE as i32;
            self.pass_by_zero += 1;
        }

        while new_value < 0 {
            new_value += Dial::DIAL_SIZE as i32;
            self.pass_by_zero += 1;
        }

        if self.value == 0 && matches!(a_move.direction, Direction::LEFT) {
            // We are starting the rotation in position 0 and we are going left.
            // This means that we will trigger a "pass by zero" count that we already
            // counted in the previous iteration.
            // We remove the extra count.
            self.pass_by_zero -= 1;
        }

        if new_value == 0 {
            self.count_zero += 1;
            if matches!(a_move.direction, Direction::LEFT) {
                self.pass_by_zero += 1;
            }
        }

        self.value = new_value as DialType;
    }
}

fn main() {
    let input = read_file(1);

    let moves: Vec<Move> = input.lines().map(str::trim).map(Move::from).collect();

    let mut dial = Dial::new();

    for each in moves {
        dial.add(&each);
    }

    println!("Part 1: {}", dial.count_zero);
    println!("Part 2: {}", dial.pass_by_zero);
}
