let fs = require('fs');
let A = fs.readFileSync('input.txt', 'utf-8').split(',').map(Number);
let Robot = require('../00_common/Robot');
let run = require('../00_common/intcode_computer_day_13');
let r1 = new Robot();
run([...A], r1);
console.log(`Part 1: ${r1.blocks.size}`);
// Part 1: 260