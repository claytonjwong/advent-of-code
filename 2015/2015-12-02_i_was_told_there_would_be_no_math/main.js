/*
 * https://adventofcode.com/2015/day/2
 */

let fs = require('fs');

//
// C++ style procedural programming
//

/*
let getArea = (l, w, h) => {
    const s = [(l * w), (w * h), (h * l)]; // 3 sides
    return (s[0] << 1) + (s[1] << 1) + (s[2] << 1) + Math.min(...s); // 2*l*w + 2*w*h + 2*h*l + minimum side area
};

let paper = 0,
    ribbon = 0;
let input = fs.readFileSync('./input.txt', 'utf8');
let dimensions = input.split('\n');
for (let dimension of dimensions) {
    let d = [l, w, h] = dimension.split('x');
    paper += getArea(l, w, h);
    d.sort((a, b) => a - b);
    ribbon += (d[0] << 1) + (d[1] << 1) + (l * w * h);
}
*/


//
// Javascript style functional programming
//
let accumulateArea = A => A.map(x => x << 1).reduce((a, b) => a + b); // accumulate sum of each number x multiplied by 2 in array A

let getArea = (l, w, h) => {
    const d = [(l * w), (w * h), (h * l)]; // 3 dimensions
    return accumulateArea(d) + Math.min(...d); // 2*l*w + 2*w*h + 2*h*l + minimum dimension's area
};

let paper = 0,
    ribbon = 0;
let input = fs.readFileSync('./input.txt', 'utf8');
let dimensions = input.split('\n');
for (let dimension of dimensions) {
    let d = [l, w, h] = dimension.split('x');
    paper += getArea(l, w, h);
    d.sort((a, b) => a - b); d.pop(); // remove the max dimension's area
    ribbon += accumulateArea(d) + (l * w * h);
}

console.log("Answer 1: " + paper);
console.log("Answer 2: " + ribbon);
