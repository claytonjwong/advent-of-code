/*
 * Day 1: The Tyranny of the Rocket Equation
 *
 * Q: https://adventofcode.com/2019/day/1
 * A: https://www.reddit.com/r/adventofcode/comments/e51aqm/2019_day_1_javascript_solution/
 */ 

let fs = require('fs');
let input = fs.readFileSync('input.txt', 'utf8');
let part1 = (input) => input.split("\n").map(x => Math.floor(x / 3) - 2).reduce((a, b) => a + b);
let go = (x) => {
    let y = Math.floor(x / 3) - 2;
    return y <= 0 ? 0 : y + go(y);
}
let part2 = (input) => input.split("\n").map(x => go(x)).reduce((a, b) => a + b);
console.log(`Part 1: ${part1(input)}\nPart 2: ${part2(input)}`);

// Part 1: 3376997
// Part 2: 5062623