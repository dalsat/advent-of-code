use std::fs;

// Load the input file from disk for the given day.
pub fn read_file(day: u8) -> String {
    let path = format!("input/day{day:02}.txt");
    return fs::read_to_string(path).expect("Input file not found");
}
