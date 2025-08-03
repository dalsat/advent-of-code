use std::collections::HashMap;

// Process the input text, split into rows and parse them by column into the two lists.
fn process_data(contents: String) -> (Vec<u32>, Vec<u32>) {
    contents
        .lines()
        .map(|line| aoc::parse_numbers::<u32>(line))
        .map(|each| (each[0], each[1]))
        .unzip()
}

// Calculate the similarity score by calculating the distance of all the sorted pairs.
fn part_1(data: &(Vec<u32>, Vec<u32>)) -> u32 {
    let (left, right) = data;
    let mut left = left.to_vec();
    let mut right = right.to_vec();

    left.sort();
    right.sort();

    left.iter()
        .zip(right)
        .map(|(each_first, each_second)| each_first.abs_diff(each_second))
        .sum()
}

// Calculate the similarity score by multiplying each number on the left list by the number of
// they appear on the right list, then add them together.
fn part_2(data: &(Vec<u32>, Vec<u32>)) -> u32 {
    let (left, right) = data;
    // build the index with counts of the elements in the right list
    let mut counts: HashMap<u32, u32> = HashMap::new();
    for each in right {
        counts
            .entry(*each)
            .and_modify(|value| *value += 1)
            .or_insert(1);
    }

    left.iter()
        .map(|each| each * counts.get(each).unwrap_or(&0))
        .sum()
}

fn main() {
    let mut solution = aoc::Solution::day(1);
    let data = process_data(solution.data());
    solution.part1(part_1(&data)).part2(part_2(&data)).print();
}
