/*
 * https://adventofcode.com/2015/day/6
 */

let coord = coords => coords.split(',').map(x => parseInt(x));

let A = [...Array(1000)].map(() => Array(1000).fill(0));
let mod_A = (A, i, j, cmd, action=null) => {
    if (cmd == 'turn')
        A[i][j] = action == 'on' ? 1 : 0;
    if (cmd == 'toggle')
        A[i][j] ^= 1;
};

let B = [...Array(1000)].map(() => Array(1000).fill(0));
let mod_B = (B, i, j, cmd, action=null) => {
    if (cmd == 'turn')
        B[i][j] = action == 'on' ? B[i][j] + 1 : B[i][j] > 0 ? B[i][j] - 1 : 0;
    if (cmd == 'toggle')
        B[i][j] += 2;
};

let fs = require('fs');
let input = fs.readFileSync('./input.txt', 'utf8');
let lines = input.split('\n');
for (let line of lines) {
    let [a, b, c, d, e] = line.split(' ');
    if (a == 'turn') {
        let [cmd, action, beg, end] = [a, b, c, e];
        let [x1, y1] = coord(beg);
        let [x2, y2] = coord(end);
        for (let i=x1; i <= x2; ++i)
            for (let j=y1; j <= y2; ++j)
                mod_A(A, i, j, cmd, action),
                mod_B(B, i, j, cmd, action);
    }
    if (a == 'toggle') {
        let [cmd, beg, end] = [a, b, d];
        let [x1, y1] = coord(beg),
            [x2, y2] = coord(end);
        for (let i=x1; i <= x2; ++i)
            for (let j=y1; j <= y2; ++j)
                mod_A(A, i, j, cmd),
                mod_B(B, i, j, cmd);
    }
}

let cnt = 0;
for (let row of A)
    cnt += row.filter(a => a == 1).length;
console.log(`Answer 1: ${cnt}`);

let total = 0;
for (let row of B)
    total += row.reduce((a, b) => a + b);
console.log(`Answer 2: ${total}`);