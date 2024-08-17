use aoc::{read_day, Solution};

type Unit = u32;
struct Triangle (Unit, Unit, Unit);

fn main() {
    println!("Solution for day 3: {}", day3());
}

pub fn day3() -> Solution<u32> {
    let triangles: Vec<Triangle> = parse_input(read_day(3));
    Solution::new(part1(&triangles), part2(&triangles))
}

fn parse_input(input: String) -> Vec<Triangle> {
    input
        .split("\n")
        .filter(|s| {!s.is_empty()})
        .map(parse_line)
        .collect()
}

fn parse_line(line: &str) -> Triangle {    
    let edges: Vec<u32> = line
        .split(char::is_whitespace)
        .filter(|s| {!s.is_empty()})
        .map(|s| {s.parse().expect(format!("unable to parse value {}", s).as_str())})
        .collect();
    Triangle::from(&edges)
}

fn part1(triangles: &Vec<Triangle>) -> u32 {
    number_of_valid_triangles(triangles)
}

fn part2(triangles: &Vec<Triangle>) -> u32 {
    assert!(triangles.len() % 3 == 0);
    number_of_valid_triangles(&(triangles.vertical_iter().collect::<Vec<Triangle>>()))
}

fn number_of_valid_triangles(triangles: &Vec<Triangle>) -> u32 {
    triangles.iter()
        .filter(|t| { t.is_valid() })
        .count() as u32
}


impl Triangle {

    fn from(edges: &Vec<Unit>) -> Self {
        assert!(edges.len() == 3);
        return Triangle(edges[0], edges[1], edges[2])
    }

    fn is_valid(&self) -> bool {
        self.0 < self.1 + self.2 &&
        self.1 < self.0 + self.2 &&
        self.2 < self.0 + self.1
    }
}


struct TriangleVerticalIter {
    transposed_elements: Vec<Triangle>,
}

impl TriangleVerticalIter {
    fn new(elements: &Vec<Triangle>) -> Self {
        TriangleVerticalIter { transposed_elements: (Self::transpose(elements)) }
    }

    fn transpose(input: &Vec<Triangle>) -> Vec<Triangle> {
        let first_column = input.iter()
            .map(|s| {s.0});
    
        let second_column = input.iter()
            .map(|s| {s.1});
    
        let third_column = input.iter()
            .map(|s| {s.2});
    
        let mut all_values = first_column
            .chain(second_column)
            .chain(third_column);
    
        let mut new_triangles: Vec<Triangle> = Vec::new();
    
        loop {
    
            let first = match all_values.next() {
                Some(value) => value,
                None => break,
            };
            let second = all_values.next().expect("error second");
            let third = all_values.next().expect("error third");
    
            let t = Triangle(first, second, third);
            new_triangles.push(t);
        }
    
        new_triangles
    }
    
}

impl Iterator for TriangleVerticalIter {

    type Item = Triangle;

    fn next(&mut self) -> Option<Self::Item> {
        self.transposed_elements.pop()
    }
}

trait VerticalIter {
    
    fn vertical_iter(&self) -> TriangleVerticalIter;
}

impl VerticalIter for Vec<Triangle> {
    fn vertical_iter(&self) -> TriangleVerticalIter {
        TriangleVerticalIter::new(self)
    }
}