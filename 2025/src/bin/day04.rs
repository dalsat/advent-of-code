use std::collections::HashSet;

use aoc_2025::read_file;

#[derive(Eq, PartialEq, Hash, Debug, Clone)]
struct Point {
    x: i32,
    y: i32,
}

impl Point {
    fn at(x: i32, y: i32) -> Self {
        Self { x, y }
    }

    fn translated_by(&self, point: &Point) -> Self {
        Self {
            x: self.x + point.x,
            y: self.y + point.y,
        }
    }
}

#[derive(Debug, Clone)]
struct Map {
    size: usize,
    rolls: HashSet<Point>,
}

impl Map {
    // Constructors
    fn new(size: usize) -> Self {
        Self {
            size,
            rolls: HashSet::new(),
        }
    }

    // Operations
    fn add_roll(&mut self, position: Point) {
        self.rolls.insert(position);
    }

    fn is_within_boundaries(&self, value: i32) -> bool {
        0 <= value && value < self.size as i32
    }

    fn has_roll_at(&self, position: Point) -> bool {
        self.is_within_boundaries(position.x)
            && self.is_within_boundaries(position.y)
            && self.rolls.contains(&position)
    }

    fn number_of_neighbors(&self, position: &Point) -> u8 {
        [
            Point::at(-1, -1),
            Point::at(0, -1),
            Point::at(1, -1),
            Point::at(-1, 0),
            Point::at(1, 0),
            Point::at(-1, 1),
            Point::at(0, 1),
            Point::at(1, 1),
        ]
        .iter()
        .map(|e| self.has_roll_at(position.translated_by(&e)))
        .filter(|e| *e)
        .count() as u8
    }

    fn accessible_rolls(&self) -> Vec<&Point> {
        self.rolls
            .iter()
            .filter(|e| self.number_of_neighbors(e) < 4)
            .collect()
    }

    fn remove_all_accessible_rolls(&self) -> u32 {
        let mut disposable_map = self.clone();

        let mut total_removed_rolls = 0;
        let mut removed_rolls: usize = disposable_map.rolls.len();

        while removed_rolls != 0 {
            let rolls: Vec<Point> = disposable_map
                .accessible_rolls()
                .into_iter()
                .cloned()
                .collect();
            removed_rolls = rolls.len();
            total_removed_rolls += removed_rolls;

            for roll in rolls {
                disposable_map.rolls.remove(&roll);
            }
        }
        total_removed_rolls as u32
    }
}

impl From<&str> for Map {
    fn from(string: &str) -> Self {
        let lines: Vec<&str> = string.lines().map(|e| e.trim()).collect();
        let mut new_map = Map::new(lines.len());

        for (y, line) in lines.iter().enumerate() {
            for (x, each) in line.char_indices() {
                match each {
                    '@' => new_map.add_roll(Point::at(x as i32, y as i32)),
                    '.' => (),
                    _ => panic!("wtf is this? \"{each}\""),
                }
            }
        }
        new_map
    }
}

fn main() {
    let input = read_file(4);
    let map = Map::from(input.as_str());

    let part1 = map.accessible_rolls().len();

    let part2 = map.remove_all_accessible_rolls();

    println!("Part 1: {part1}");
    println!("Part 2: {part2}");
}
