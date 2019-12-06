/*
 * Day 5: Sunny with a Chance of Asteroids
 *
 * Q: https://adventofcode.com/2019/day/5
 * A: https://claytonjwong.github.io/advent-of-code/2019/#day-5-sunny-with-a-chance-of-asteroids
 */
let fs = require('fs')
let input = fs.readFileSync('input.txt', 'utf-8').split(",").map(x => parseInt(x));
let run = (id, ...A) => {
    let ans = 0;
    let pad = cmd => {
        let padded = '00000' + cmd;
        return padded.substring(padded.length - 5);
    };
    for (let i=0; i < A.length;) {
        let cmd = pad(A[i]);
        let op = parseInt(cmd.substring(cmd.length - 2));
        let mode = { u: cmd[2], v: cmd[1], };
        let param = {
            u: (A, mode, x) => mode == '0' ? A[x] : x,
            v: (A, mode, x) => mode == '0' ? A[x] : x,
        };
        if (op == 99) {
            break;
        } else if (op == 1) {
            let [u, v, w] = [A[i+1], A[i+2], A[i+3]];
            A[w] = param.u(A, mode.u, u) + param.v(A, mode.v, v);
            i += 4;
        } else if (op == 2) {
            let [u, v, w] = [A[i+1], A[i+2], A[i+3]];
            A[w] = param.u(A, mode.u, u) * param.v(A, mode.v, v);
            i += 4;
        } else if (op == 3) {
            let v = id;
            let w = A[i+1];
            A[w] = v;
            i += 2;
        } else if (op == 4) {
            let u = A[i+1];
            ans = param.u(A, mode.u, u);
            i += 2;
        } else if (op == 5) {
            let [u, v] = [A[i+1], A[i+2]];
            if (param.u(A, mode.u, u) != 0)
                i = param.v(A, mode.v, v);
            else
                i += 3;
        } else if (op == 6) {
            let [u, v] = [A[i+1], A[i+2]];
            if (param.u(A, mode.u, u) == 0)
                i = param.v(A, mode.v, v);
            else
                i += 3;
        } else if (op == 7) {
            let [u, v, w] = [A[i+1], A[i+2], A[i+3]];
            A[w] = param.u(A, mode.u, u) < param.v(A, mode.v, v);
            i += 4;
        } else if (op == 8) {
            let [u, v, w] = [A[i+1], A[i+2], A[i+3]];
            A[w] = param.u(A, mode.u, u) == param.v(A, mode.v, v);
            i += 4;
        }
    }
    return ans;
};
console.log(`Part 1: ${run(1, ...input)}\nPart 2: ${run(5, ...input)}`);
// Part 1: 16574641
// Part 2: 15163975