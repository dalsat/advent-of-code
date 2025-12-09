use aoc_2025::read_file;

#[derive(Debug)]
struct Battery(String);

impl Battery {
    fn find_highest_value(&self, number_of_bits: usize) -> u64 {
        let mut digits: Vec<u32> = vec![];

        let mut start_index = 0;

        for nth in (0..number_of_bits).rev() {
            let last_index = self.0.len() - nth;
            let (new_latest_index, next_digit) =
                self.find_highest_bit_in_interval(start_index, last_index);
            digits.push(next_digit);
            start_index = new_latest_index + 1;
        }

        let mut result: u64 = 0;

        for digit in digits {
            result = 10 * result + digit as u64
        }
        result
    }

    fn find_highest_bit_in_interval(&self, start: usize, end: usize) -> (usize, u32) {
        let mut chars = self.0[..end].chars().enumerate();

        let (mut highest_index, mut highest_digit) = chars
            .nth(start)
            .map(|(index, value)| (index, value.to_digit(10).unwrap()))
            .unwrap();

        for (index, char) in chars {
            let digit = char.to_digit(10).unwrap();
            if digit > highest_digit {
                highest_index = index;
                highest_digit = digit;
                if highest_digit == 9 {
                    break;
                }
            }
        }
        (highest_index, highest_digit)
    }
}

fn parse_lines<'a>(text: &str) -> Vec<&str> {
    text.lines()
        .map(|line| line.trim())
        .filter(|line| !line.is_empty())
        .collect()
}

fn main() {
    let input = read_file(3);
    let batteries: Vec<Battery> = parse_lines(&input)
        .into_iter()
        .map(|e| Battery(String::from(e)))
        .collect();

    let part1 = batteries
        .iter()
        .map(|battery| battery.find_highest_value(2))
        .sum::<u64>();

    let part2 = batteries
        .iter()
        .map(|battery| battery.find_highest_value(12))
        .sum::<u64>();

    println!("Part 1: {}", part1);
    println!("Part 2: {}", part2);
}
