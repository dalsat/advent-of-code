use std::iter::zip;

use aoc_2025::read_file;

// WIP, not yet completed

#[derive(Clone, Copy)]
enum Operator {
    Sum,
    Mult,
}

#[derive(Clone, Copy)]
enum MathMode {
    Normal,
    Cephalopod,
}

impl Operator {
    fn parse(char: &str) -> Self {
        match char {
            "+" => Self::Sum,
            "*" => Self::Mult,
            _ => panic!("Unknown operator {}", char),
        }
    }
}

struct Sheet {
    columns: Vec<Column>,
}

impl Sheet {
    fn eval(&self, mode: MathMode) -> u64 {
        self.columns.iter().map(|e| e.eval(mode)).sum()
    }
}

impl From<&str> for Sheet {
    fn from(text: &str) -> Sheet {
        let rows: Vec<Vec<&str>> = text
            .lines()
            .map(|line| line.split_whitespace().collect())
            .collect();

        let mut columns: Vec<Column> = rows[rows.len() - 1]
            .iter()
            .map(|char| Column::new(Operator::parse(char)))
            .collect();

        for row in &rows[..rows.len() - 1] {
            for (each, column) in zip(row, columns.iter_mut()) {
                column.add_value(each.parse().unwrap());
            }
        }

        Self { columns }
    }
}

struct Column {
    operator: Operator,
    values: Vec<u64>,
}

impl Column {
    fn new(operator: Operator) -> Self {
        Self {
            operator,
            values: vec![],
        }
    }

    fn add_value(&mut self, value: u64) {
        self.values.push(value);
    }

    fn eval(&self, mode: MathMode) -> u64 {
        let column = match mode {
            MathMode::Normal => self,
            MathMode::Cephalopod => &self.as_cephalopod_column(),
        };

        match self.operator {
            Operator::Sum => column.values.iter().sum(),
            Operator::Mult => column.values.iter().fold(1, |total, each| total * each),
        }
    }

    fn as_cephalopod_column(&self) -> Self {
        let values_digits: Vec<Vec<_>> = self
            .values
            .iter()
            .map(|e| {
                e.to_string()
                    .chars()
                    .map(|d| d.to_digit(10).unwrap())
                    .collect()
            })
            .collect();

        let base = values_digits.iter().map(|e| e.len()).max().unwrap();

        let mut new_column = Column::new(self.operator);

        let mut numbers: Vec<u64> = vec![0; self.values.len()];

        for value in &values_digits {
            for position in 0..base {
                match value.get(position) {
                    Some(digit) => numbers[position] = 10 * numbers[position] + *digit as u64,
                    None => numbers[position] *= 10,
                }
            }
        }

        println!("numbers: {numbers:?}");
        for number in numbers {
            new_column.add_value(number);
        }

        new_column
    }
}

fn main() {
    let input = "123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +  ";
    // let input = read_file(6);

    let sheet = Sheet::from(input);

    // for column in sheet.columns {
    //     println!("{}", column.eval());
    // }
    let part_1 = sheet.eval(MathMode::Normal);
    let part_2 = sheet.eval(MathMode::Cephalopod);

    println!("Part 1: {}", part_1);
    println!("Part 2: {}", part_2);
}
