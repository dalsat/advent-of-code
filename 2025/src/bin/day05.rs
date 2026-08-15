use aoc_2025::read_file;

#[derive(PartialEq, Eq, PartialOrd, Ord, Clone)]
struct Range {
    start: u64,
    end: u64,
}

impl Range {
    fn new(start: u64, end: u64) -> Self {
        Range { start, end }
    }

    fn contains(&self, value: u64) -> bool {
        self.start <= value && value <= self.end
    }

    fn size(&self) -> u64 {
        self.end - self.start + 1
    }
}

struct Intervals {
    intervals: Vec<Range>,
}

impl Intervals {
    fn new() -> Self {
        Self { intervals: vec![] }
    }

    fn add(&mut self, start: u64, end: u64) {
        self.intervals.push(Range::new(start, end));
    }

    fn contains(&self, value: &u64) -> bool {
        self.intervals.iter().any(|e| e.contains(*value))
    }

    fn count_included_indexes(&self) -> u64 {
        let mut number_of_indexes = 0;
        let mut latest_index = 0;

        let mut intervals_copy = self.intervals.clone();
        intervals_copy.sort();

        for interval in intervals_copy {
            if latest_index < interval.end {
                let next_interval_start = interval.start.max(latest_index + 1);
                number_of_indexes += Range::new(next_interval_start, interval.end).size();

                latest_index = interval.end;
            }
        }

        number_of_indexes
    }
}

fn main() {
    let input = read_file(5);

    let sections: Vec<Vec<&str>> = input
        .split("\n\n")
        .map(|e| e.lines().map(str::trim).collect())
        .collect();
    assert!(sections.len() == 2, "Wrong number of sections");

    let raw_intervals: Vec<Vec<u64>> = sections[0]
        .iter()
        .map(|interval| {
            interval
                .split("-")
                .map(|e| e.parse::<u64>().unwrap())
                .collect()
        })
        .collect();

    let ingredients: Vec<u64> = sections[1]
        .iter()
        .map(|e| e.parse::<u64>().unwrap())
        .collect();

    let mut intervals = Intervals::new();
    for interval in raw_intervals {
        intervals.add(interval[0], interval[1]);
    }

    let part_1 = ingredients
        .into_iter()
        .filter(|e| intervals.contains(e))
        .count();

    let part_2 = intervals.count_included_indexes();

    println!("Part 1: {}", part_1);
    println!("Part 2: {}", part_2);
}
