/*
 * Intcode Computer
 *
 * Implementation from "Day 5: Sunny with a Chance of Asteroids"
 * this common functionality is used by other AoC Days
 */
let run = (A, input, pc = 0) => {
  let iter = input[Symbol.iterator]();
  let pad = cmd => {
    let padded = '00000' + cmd;
    return padded.substring(padded.length - 5);
  };
  let op = 0, instructions = [0, 4, 4, 2, 2, 0, 0, 4, 4];
  for (let i = pc; op != 99; i += instructions[op]) {
    let cmd = pad(A[i]);
    let [u, v, w] = [A[i + 1], A[i + 2], A[i + 3]];
    u = cmd[2] == 0 ? A[u] : u;
    v = cmd[1] == 0 ? A[v] : v;
    op = parseInt(cmd.substring(cmd.length - 2));
    if (op == 1) A[w] = u + v;
    if (op == 2) A[w] = u * v;
    if (op == 3) w = A[i + 1], A[w] = iter.next().value;
    if (op == 4) return [u, i + 2]; // i + 2 to move past op 4 instructions
    if (op == 5) i = (u != 0) ? v : i + 3;
    if (op == 6) i = (u == 0) ? v : i + 3;
    if (op == 7) A[w] = u < v;
    if (op == 8) A[w] = u == v;
  }
  return [-Infinity, -Infinity];
};
module.exports = run;