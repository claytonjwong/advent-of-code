/*
 * Day 12: The N-Body Problem
 *
 * Q: https://adventofcode.com/2019/day/12
 * A: https://claytonjwong.github.io/advent-of-code/2019/#day-12-the-n-body-problem
 */ 
let fs = require('fs');
let M = 4, N = 3; // 4 moons each with 3 positions (x, y, z)
let P = fs.readFileSync('input.txt', 'utf-8').split('\n')
  .map(line => line.substring(0, line.length - 1).substring(1))
  .map(line => line.split(','))
  .map(A => A.map(s => Number(s.trim().substring(2))));
let V = [...Array(4)].map(row => new Array(3).fill(0));
let gravity = (P, V) => {
  for (let u = 0; u < M; ++u)
    for (let v = 0; v < M; ++v)
      for (let j = 0; u != v && j < N; ++j) {
        if (P[u][j] < P[v][j]) ++V[u][j];
        if (P[u][j] > P[v][j]) --V[u][j];
      }
}
let velocity = (P, V) => {
  for (let i = 0; i < M; ++i)
    for (let j = 0; j < N; ++j)
      P[i][j] += V[i][j];
}
let k = 1000; // k-steps
while (k--)
  gravity(P, V),
  velocity(P, V);
let sum = A => A.reduce((a, b) => Math.abs(a) + Math.abs(b));
let energy = (P, V) => sum(P) * sum(V);
let total = 0;
for (let i = 0; i < M; ++i)
  total += energy(P[i], V[i]);
console.log(`Part 1: ${total}`);
 // Part 1: 8742