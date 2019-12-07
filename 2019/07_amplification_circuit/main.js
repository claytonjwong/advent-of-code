/*
 * Day 7: Amplification Circuit
 *
 * Q: https://adventofcode.com/2019/day/7
 * A: https://claytonjwong.github.io/advent-of-code/2019/#day-7-amplification-circuit
 */
let fs = require('fs');
let A = fs.readFileSync('input.txt', 'utf-8').split(",").map(Number);
let run = require('../00_common/intcode_computer');
let permutations = A => {
    if (A.length == 1)
        return A;
    return A.reduce((res, x, i, A, B=[...A]) => {
        B.splice(i, 1); // B is A without A[i] (ie. x)
        return res.concat(permutations(B).map(a => [].concat(x, a))); // recursively insert x into all other positions
    }, []);
}
let maxThrust = (A, perms, loopback=false, max=-Infinity) => {
    for (let perm of perms) {
        let output = 0, pc = [];
        let amp = [...Array(5)].map(row => [...A]);
        perm.forEach((phase, i) => {
            let j = 0;
            [output, j] = run(amp[i], [phase, output]);
            pc.push(j);
            max = Math.max(max, output);
        });
        if (!loopback)
            continue;
        for (let i = 0; output > -Infinity; i = (i + 1) % 5) {
            [output, pc[i]] = run(amp[i], [output], pc[i]);
            max = Math.max(max, output);
        }
    }
    return max;
};
let perm1 = permutations([0,1,2,3,4]),
    perm2 = permutations([5,6,7,8,9]);
console.log(`Part 1: ${maxThrust(A, perm1)}\nPart 2: ${maxThrust(A, perm2, true)}`);
// Part 1: 117312
// Part 2: 1336480