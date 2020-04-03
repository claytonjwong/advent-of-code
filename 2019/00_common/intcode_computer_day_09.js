/*
 * Intcode Computer
 *
 * Implementation from 'Day 5: Sunny with a Chance of Asteroids'
 * this common functionality is used by other AoC Days
 */
let run = (A, input, pc = 0) => {
  let pad = cmd => ('00000' + cmd).substring(('00000' + cmd).length - 5);
  let param = (A, mode, x, rel, write = false) => {
    if (write)
      return mode == 0 ? x : x + rel;
    if (mode == 0) return A[x];
    if (mode == 1) return x;
    if (mode == 2) return A[x + rel];
  };
  let iter = input[Symbol.iterator]();
  let op = 0, instructions = [0, 4, 4, 2, 2, 0, 0, 4, 4, 2];
  let rel = 0; // relative base
  for (let i = pc; op != 99; i += instructions[op]) {
    let cmd = pad(A[i]);
    op = Number(cmd.substring(cmd.length - 2));
    let [u, v, w] = [A[i + 1], A[i + 2], A[i + 3]];
    let mode = { u: Number(cmd[2]), v: Number(cmd[1]), w: Number(cmd[0]) };
    u = param(A, mode.u, u, rel, op == 3);
    v = param(A, mode.v, v, rel);
    w = param(A, mode.w, w, rel, true);
    if (op == 1) A[w] = u + v;
    if (op == 2) A[w] = u * v;
    if (op == 3) A[u] = iter.next().value;
    if (op == 4) return u;
    if (op == 5) i = (u != 0) ? v : i + 3;
    if (op == 6) i = (u == 0) ? v : i + 3;
    if (op == 7) A[w] = u < v ? 1 : 0;
    if (op == 8) A[w] = u == v ? 1 : 0;
    if (op == 9) rel += u;
  }
};
module.exports = run;