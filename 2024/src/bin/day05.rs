use std::collections::{HashMap, HashSet};

type Page = u32;
// type ManualUpdate = Vec<Page>;

#[derive(Debug)]
struct Rule(Page, Page);

#[derive(Debug)]
struct ManualUpdate {
    pages: Vec<Page>,
}

#[derive(Debug)]
struct Manuals {
    rules: Vec<Rule>,
    updates: Vec<ManualUpdate>,
}

impl Manuals {
    fn from(data: &String) -> Self {
        let mut raw_data = data
            .split("\n\n")
            .map(|each| each.lines().map(|line| line.trim()).collect::<Vec<&str>>());

        let rules = Self::parse_rules(raw_data.next().unwrap());
        let updates = Self::parse_manual_updates(raw_data.next().unwrap());

        Manuals { rules, updates }
    }

    fn parse_rules(lines: Vec<&str>) -> Vec<Rule> {
        lines.iter().map(|line| Rule::from(line)).collect()
    }

    fn parse_manual_updates(lines: Vec<&str>) -> Vec<ManualUpdate> {
        lines.iter().map(|line| ManualUpdate::from(line)).collect()
    }

    fn ordered_updates(&self) -> Vec<&ManualUpdate> {
        let validator = OrderValidator::from(self);

        self.updates
            .iter()
            .filter(|each| each.is_ordered())
            .collect()
    }
}

impl ManualUpdate {
    fn from(line: &str) -> Self {
        Self {
            pages: line.split(",").map(|each| each.parse().unwrap()).collect(),
        }
    }

    fn mid_page(&self) -> Page {
        self.pages[self.pages.len() / 2]
    }

    // bruteforce approach: Iterate all values
    fn is_ordered(&self) -> bool {
        // for (index, value) in self.pages.iter().enumerate() {
        //     if
        // }
        true
    }
}

impl Rule {
    fn from(line: &str) -> Rule {
        let components = line
            .split("|")
            .map(|each| each.trim().parse().unwrap())
            .collect::<Vec<u32>>();
        assert!(
            components.len() == 2,
            "Component should have 2 tokens (found {:?})",
            components
        );
        Self(components[0], components[1])
    }
}

struct OrderValidator<'validator> {
    manuals: &'validator Manuals,
    pages_before: HashMap<Page, HashSet<Page>>,
    pages_after: HashMap<Page, HashSet<Page>>,
}

impl<'validator> OrderValidator<'validator> {
    fn is_before(&self, page: Page, page_before: Page) -> bool {
        match self.pages_before.get(&page) {
            Some(values_set) => values_set.contains(&page_before),
            None => false,
        }
    }
    fn is_after(&self, page: Page, page_after: Page) -> bool {
        match self.pages_after.get(&page) {
            Some(values_set) => values_set.contains(&page_after),
            None => false,
        }
    }

    fn from(manuals: &'validator Manuals) -> Self {
        let pages_before = OrderValidator::build_ordering_map(&manuals.rules, false);
        let pages_after = OrderValidator::build_ordering_map(&manuals.rules, true);

        OrderValidator {
            manuals,
            pages_before: pages_before,
            pages_after: pages_after,
        }
    }

    // Visit the rules left-to-right and build the total ordering
    fn build_ordering_map(rules: &Vec<Rule>, reverse: bool) -> HashMap<u32, Vec<u32>> {
        // let (all_before, all_after): (HashSet<Page>, HashSet<Page>) = rules
        //     .iter()
        //     .map(|Rule(a, b)| if reverse { (b, a) } else { (a, b) })
        //     .unzip();
        // let starting_nodes = all_before.difference(&all_after);

        let mut ordering_map: HashMap<Page, HashSet<Page>> = HashMap::new();

        for Rule(before, after) in rules {
            if !ordering_map.contains_key(before) {
                ordering_map.insert(*before, HashSet::new());
            }
            match ordering_map.get_mut(before) {
                Some(container) => {
                    container.insert(*after);
                }
                None => {
                    ordering_map.insert(*before, HashSet::from(vec![*after]));
                }
            }
        }
        ordering_map
    }

    // fn pages_before_for(&self, page: &Page) -> HashSet<Page> {
    //     self.search_pages_before(page)
    //     // match self.pages_before.get(page) {
    //     //     Some(value) => value.clone(),
    //     //     None => self.search_pages_before(page),
    //     // }
    // }

    // fn search_pages_before(&self, page: &Page) -> HashSet<Page> {
    //     let all_pages_before: HashSet<Page> = self
    //         .manuals
    //         .rules
    //         .iter()
    //         .filter_map(|Rule(page_before, page_after)| {
    //             if page_after == page {
    //                 Some(*page_before)
    //             } else {
    //                 None
    //             }
    //         })
    //         // .flat_map(|page_before| self.search_pages_before(&page_before))
    //         .collect();

    //     for page_before in all_pages_before {
    //         self.search_pages_before(&page_before);
    //     }

    //     // let new_pages_before = all_pages_before.clone();
    //     // self.pages_before.insert(*page, all_pages_before.clone());
    //     all_pages_before
    // }
}

fn part_1(manuals: &Manuals) -> u32 {
    manuals
        .ordered_updates()
        .iter()
        .map(|each| each.mid_page())
        .sum()
}

// fn part_2(data: &String) -> u32 {}

fn main() {
    let mut solution = aoc::Solution::day(5);
    let data = String::from(
        "47|53
    97|13
    97|61
    97|47
    75|29
    61|13
    75|53
    29|13
    97|29
    53|29
    61|53
    97|53
    61|29
    47|13
    75|47
    97|75
    47|61
    75|61
    47|29
    75|13
    53|13

    75,47,61,53,29
    97,61,53,29,13
    75,29,13
    75,97,47,61,53
    61,13,29
    97,13,75,29,47",
    );
    // let data = solution.data();

    // process_data(&data);
    let manuals = Manuals::from(&data);
    println!("{manuals:?}");
    solution
        .part1(part_1(&manuals))
        // .part2(part_2(&manuals))
        .print();
}
