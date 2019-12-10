/*
 * Day 5: Sunny with a Chance of Asteroids
 *
 * Q: https://adventofcode.com/2019/day/5
 * A: https://claytonjwong.github.io/advent-of-code/2019/#day-5-sunny-with-a-chance-of-asteroids
 */
let fs = require('fs')
let input = fs.readFileSync('input.txt', 'utf-8').split(",").map(Number);
let run = (id, A, ans = 0) => {
  let pad = cmd => ('00000' + cmd).substring(('00000' + cmd).length - 5);
  let op = 0, instructions = [0, 4, 4, 2, 2, 0, 0, 4, 4];
  for (let i = 0; op != 99; i += instructions[op]) {
    let cmd = pad(A[i]);
    let [u, v, w] = [A[i + 1], A[i + 2], A[i + 3]];
    u = cmd[2] == 0 ? A[u] : u;
    v = cmd[1] == 0 ? A[v] : v;
    op = parseInt(cmd.substring(cmd.length - 2));
    if (op == 1) A[w] = u + v;
    if (op == 2) A[w] = u * v;
    if (op == 3) w = A[i + 1], A[w] = id;
    if (op == 4) ans = u;
    if (op == 5) i = (u != 0) ? v : i + 3;
    if (op == 6) i = (u == 0) ? v : i + 3;
    if (op == 7) A[w] = u < v;
    if (op == 8) A[w] = u == v;
  }
  return ans;
};
console.log(`Part 1: ${run(1, [...input])}\nPart 2: ${run(5, [...input])}`);
// Part 1: 16574641
// Part 2: 15163975