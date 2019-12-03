/*
 * Day 2: 1202 Program Alarm
 *
 * Q: https://adventofcode.com/2019/day/2
 * A: https://www.reddit.com/r/adventofcode/comments/e51rat/2019_day_2_javascript_solution/
 */
let fs = require('fs');
let input = fs.readFileSync('input.txt', 'utf-8').split(",").map(x => parseInt(x));
let gravityAssist = (noun, verb, ...A) => {
    A[1] = noun, A[2] = verb;
    for (let i=0; i < A.length; i += 4) {
        let [op,u,v,w] = [A[i], A[i+1], A[i+2], A[i+3]];
        if (op == 99)
            break;
        if (op == 1) A[w] = A[u] + A[v];
        if (op == 2) A[w] = A[u] * A[v];
    }
    return A[0];
};
console.log(`Part 1: ${gravityAssist(12, 2, ...input)}`);
for (let i=0; i < 100; ++i)
    for (let j=0; j < 100; ++j)
        if (gravityAssist(i, j, ...input) == 19690720)
            console.log(`Part 2: ${i}${j}`);
// Part 1: 5098658
// Part 2: 5064