/*
 * Day 1: The Tyranny of the Rocket Equation
 *
 * Q: https://adventofcode.com/2019/day/1
 * A: https://claytonjwong.github.io/advent-of-code/2019/#day-1-the-tyranny-of-the-rocket-equation
 */ 

let fs = require('fs');
let input = fs.readFileSync('input.txt', 'utf8');
let f = x => Math.floor(x / 3) - 2;
let go = x => f(x) <= 0 ? 0 : f(x) + go(f(x));
let run = func => input.split('\n').map(x => func(x)).reduce((a, b) => a + b);
console.log(`Part 1: ${run(f)}\nPart 2: ${run(go)}`);
// Part 1: 3376997
// Part 2: 5062623