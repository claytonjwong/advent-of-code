/*
 * Day 11: Space Police
 *
 * Q: https://adventofcode.com/2019/day/11
 * A: 
 */
const Robot = require('../00_common/Robot');
let fs = require('fs');
let A = fs.readFileSync('input.txt', 'utf-8').split(',').map(Number);
let run = require('../00_common/intcode_computer_day_11');
let r1 = new Robot();
run(A, r1);
console.log(`Part 1: ${r1.painted.size}`);
let r2 = new Robot(1);
run(A, r2);
let [M, N] = [6, 43]; // I printed the min/max i,j to know these magic numbers
let out = [...Array(M)].map(row => new Array(N).fill(' '));
for (let key of r2.white) {
  let [i, j] = key.split(',').map(Number);
  out[i][j] = '#';
}
console.log('Part 2:');
for (let i = 0; i < 6; ++i) {
  let row = [];
  for (let j = 0; j < 43; ++j)
    row.push(out[i][j]);
  console.log([...row].join(''));
}
// Part 1: 1967
// Part 2:
// ##  # ###  #  # ####  ##  #### ###  #  #   
//  # #  #  # #  # #    #  #    # #  # # #    
//  ##   ###  #  # ###  #      #  ###  ##     
//  # #  #  # #  # #    # ##  #   #  # # #    
//  # #  #  # #  # #    #  # #    #  # # #    
//  #  # ###   ##  ####  ### #### ###  #  #     