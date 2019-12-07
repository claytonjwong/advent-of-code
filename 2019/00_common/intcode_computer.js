/*
 * Intcode Computer
 *
 * Implementation from "Day 5: Sunny with a Chance of Asteroids"
 * this common functionality is used by other AoC Days
 */
let run = (A, input, pc=0) => {
    let iter = input[Symbol.iterator]();
    let pad = cmd => {
        let padded = '00000' + cmd;
        return padded.substring(padded.length - 5);
    };
    for (let i=pc; i < A.length;) {
        let cmd = pad(A[i]);
        let op = parseInt(cmd.substring(cmd.length - 2));
        let mode = { u: cmd[2], v: cmd[1], };
        let param = (A, mode, x) => mode == '0' ? A[x] : x;
        if (op == 1) {
            let [u, v, w] = [A[i+1], A[i+2], A[i+3]];
            A[w] = param(A, mode.u, u) + param(A, mode.v, v);
            i += 4;
        } else if (op == 2) {
            let [u, v, w] = [A[i+1], A[i+2], A[i+3]];
            A[w] = param(A, mode.u, u) * param(A, mode.v, v);
            i += 4;
        } else if (op == 3) {
            let v = iter.next().value;
            let w = A[i+1];
            A[w] = v;
            i += 2;
        } else if (op == 4) {
            let u = A[i+1];
            i += 2;
            return [param(A, mode.u, u), i];
        } else if (op == 5) {
            let [u, v] = [A[i+1], A[i+2]];
            if (param(A, mode.u, u) != 0)
                i = param(A, mode.v, v);
            else
                i += 3;
        } else if (op == 6) {
            let [u, v] = [A[i+1], A[i+2]];
            if (param(A, mode.u, u) == 0)
                i = param(A, mode.v, v);
            else
                i += 3;
        } else if (op == 7) {
            let [u, v, w] = [A[i+1], A[i+2], A[i+3]];
            A[w] = param(A, mode.u, u) < param(A, mode.v, v);
            i += 4;
        } else if (op == 8) {
            let [u, v, w] = [A[i+1], A[i+2], A[i+3]];
            A[w] = param(A, mode.u, u) == param(A, mode.v, v);
            i += 4;
        } else {
            break;
        }
    }
    return [-Infinity, -Infinity];
};
module.exports = run;