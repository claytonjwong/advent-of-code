/*
 * Day 8: Space Image Format
 *
 * Q: https://adventofcode.com/2019/day/8
 * A: https://claytonjwong.github.io/advent-of-code/2019/#day-8-space-image-format
 */
let fs = require('fs');
let input = fs.readFileSync('input.txt', 'utf-8').split('');
let M = 6, N = 25, K = M * N, L = input.length / K;
let A = []; while (input.length) A.push(input.splice(0, N));
let T = [...Array(L)].map(row => Array(3).fill(0)); // tally of 0, 1, 2
A.forEach((row, i) => {
  let k = Math.floor(i / M); // k-th layer
  T[k][0] += row.filter(x => x == 0).length,
  T[k][1] += row.filter(x => x == 1).length,
  T[k][2] += row.filter(x => x == 2).length;
});
let cnt = T[0][0], min = 0;
for (let i = 1; i < L; ++i)
  if (cnt > T[i][0])
    cnt = T[i][0], min = i;
console.log(`Part 1: ${T[min][1] * T[min][2]}`);
for (let i = 0; i + M < M * L; ++i)
  for (let j = 0; j < N; ++j)
    if (A[i][j] != 2) // naive dp algo (ie. each prev layer is M rows away, only propagate non-transparent)
      A[i + M][j] = A[i][j];
let msg = [];
for (let i = (M * L) - M; i < M * L; ++i) // last layer contains the dp algo result (ie. all layers coalesced)
  msg.push(A[i].join('').replace(/0/g, ' '));
console.log('Part 2: ');
msg.forEach(row => console.log(row));
// Part 1: 1950
// Part 2: FKAHL
// 1111 1  1  11  1  1 1    
// 1    1 1  1  1 1  1 1    
// 111  11   1  1 1111 1    
// 1    1 1  1111 1  1 1    
// 1    1 1  1  1 1  1 1    
// 1    1  1 1  1 1  1 1111 