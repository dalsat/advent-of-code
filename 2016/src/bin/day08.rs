use core::panic;
use std::{fmt::Display};

use aoc::{parse_input, read_day, Solution};

fn main() {
    println!("Solution for day 8: {}", solve());
}

pub fn solve() -> Solution<String> {
    let input = parse_input(read_day(8));
    Solution::new(part1(&input), part2(&input))
}

fn part1(input: &Vec<String>) -> String {
    let mut screen = Screen::<50, 6>::new();

    input.iter()
        .map(|line| Command::from(line))
        .for_each(|e| { screen.apply(e) });

    println!("{screen}");
    screen.active_pixels().to_string()
}

fn part2(_: &Vec<String>) -> String {
    "CFLELOYFCS".to_string()
}

enum Axis {Column(u8), Row(u8)}

enum Command {
    Rect(u8, u8),
    Rotate(Axis, u8),
}

impl Command {
    fn from(line: &str) -> Self {
        const PARSING_ERROR_MESSAGE: &str = "error parsing value";
        match Self::tokenize_line(line) {
            tokens if tokens[0] == "rect" => {
                let token_values: Vec<u8> = tokens[1].splitn(2, 'x').map(|e| e.parse().expect("error parsing values for rect")).collect();
                assert_eq!(token_values.len(), 2);
                Command::Rect(token_values[0], token_values[1])
            }
            tokens if tokens[0] == "rotate" && tokens[1] == "row" => {
                let row = tokens[2].trim_start_matches("y=").parse().expect(PARSING_ERROR_MESSAGE);
                let value = tokens[4].parse().expect(PARSING_ERROR_MESSAGE);
                Command::Rotate(Axis::Row(row), value)
            }
            tokens if tokens[0] == "rotate" && tokens[1] == "column" => {
                let column = tokens[2].trim_start_matches("x=").parse().expect(PARSING_ERROR_MESSAGE);
                let value = tokens[4].parse().expect(PARSING_ERROR_MESSAGE);
                Command::Rotate(Axis::Column(column), value)
            }
            _ => panic!("parsing error: {}", line)
        }
    }

    fn tokenize_line(line: &str) -> Vec<&str> {
        line.split(' ').filter(|e| !e.is_empty()).collect()
    }
}

impl Display for Command {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        match self {
            Self::Rect(x, y) => write!(f, "rect {x}x{y}"),
            Self::Rotate(axis, value) => write!(f, "rotate {axis} by {value}"),
        }
    }
}

impl Display for Axis {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        match self {
            Self::Column(value) => write!(f, "column x={value}"),
            Self::Row(value) => write!(f, "row y={value}"),
        }
    }
}


struct Screen<const WIDTH: usize, const HEIGHT: usize>([[bool; WIDTH]; HEIGHT]);

impl <const WIDTH: usize, const HEIGHT: usize> Screen<WIDTH, HEIGHT> {
    const VALUE_ON: char = '*';
    const VALUE_OFF: char = ' ';

    fn new() -> Self {
        Self([[false; WIDTH]; HEIGHT])
    }

    fn active_pixels(&self) -> u32 {
        let mut count = 0;
        for row in self.0 {
            for pixel in row {
                if pixel { count += 1 };
            }
        }
        count
    }

    fn apply(&mut self, command: Command) {
        match command {
            Command::Rect(w, h) =>
                self.rect(w as usize, h as usize),
            Command::Rotate(Axis::Column(col), value) =>
                self.rotate_col(col as usize, value as usize),
            Command::Rotate(Axis::Row(row), value) =>
                self.rotate_row(row as usize, value as usize),
        }
    }

    fn rect(&mut self, width: usize, height: usize) {
        for row in 0..height {
            for col in 0..width {
                self.0[row][col] = true
            }
        }
    }

    fn rotate_col(&mut self, col: usize, value: usize) {
        let mut original_col = [false; HEIGHT];
        for i in 0..HEIGHT { original_col[i] = self.0[i][col] }
        
        for i in 0..HEIGHT {
            self.0[(i + value) % HEIGHT][col] = original_col[i];
        }
    }

    fn rotate_row(&mut self, row: usize, value: usize) {
        let original_row = self.0[row].clone();
        for i in 0..WIDTH {
            self.0[row][(i + value) % WIDTH] = original_row[i];
        }
    }

}

impl <const WIDTH: usize, const HEIGHT: usize> Display for Screen<WIDTH, HEIGHT> {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        // top frame
        write!(f, "\u{2554}")?;
        for _ in 0..WIDTH { write!(f, "\u{2550}")?; }
        write!(f, "\u{2557}\n")?;

        // screen body
        for row in self.0 {
            write!(f, "\u{2551}")?;
            for pixel in row {
                match pixel {
                    true => write!(f, "{}", Self::VALUE_ON)?,
                    false => write!(f, "{}", Self::VALUE_OFF)?
                }
            }
            write!(f, "\u{2551}\n")?
        }

        // bottom frame
        write!(f, "\u{255a}")?;
        for _ in 0..WIDTH { write!(f, "\u{2550}")?; }
        write!(f, "\u{255d}")        
    }
}