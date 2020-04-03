/*
 * Day 9: Sensor Boost
 *
 * Q: https://adventofcode.com/2019/day/9
 * A: https://claytonjwong.github.io/advent-of-code/2019/#day-9-sensor-boost
 */
let fs = require('fs');
let A = fs.readFileSync('input.txt', 'utf-8').split(',').map(Number);
let run = require('../00_common/intcode_computer_day_09');
console.log(`Part 1: ${run(A, [1])}\nPart 2: ${run(A, [2])}`);
// Part 1: 3460311188
// Part 2: 42202