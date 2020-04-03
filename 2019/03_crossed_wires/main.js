/*
 * Day 3: Crossed Wires
 * 
 * Q: https://adventofcode.com/2019/day/3
 * A: https://claytonjwong.github.io/advent-of-code/2019/#day-3-crossed-wires
 */
let fs = require('fs');
let input = fs.readFileSync('input.txt', 'utf-8');
class Wire {
  constructor(paths) {
    this.seen = new Set();
    this.total = 0;
    this.steps = new Map();
    this.pos = {
      row: 0,
      col: 0
    };
    this.traverse(paths);
  }
  traverse(paths) {
    for (let path of paths)
        this.walk(path);
  }
  walk(path) {
    let [dir, steps] = [path[0], Number(path.slice(1))];
    while (steps--) {
      ++this.total;
      if (dir == 'U') --this.pos.row; if (dir == 'D') ++this.pos.row;
      if (dir == 'L') --this.pos.col; if (dir == 'R') ++this.pos.col;
      let key = `${this.pos.row},${this.pos.col}`;
      this.seen.add(key);
      if (this.steps.get(key) && this.steps.get(key) <= this.total)
        continue; // only add keys which don't exist; only update keys with larger total
      this.steps.set(key, this.total);
    }
  }
}
let [A, B] = input.split('\n')
  .map(line => line.split(','))
  .map(paths => new Wire(paths));
let intersect = [...A.seen].filter(x => B.seen.has(x));
let closest = [...intersect]
  .map((key) => key.split(',').map(Number))
  .map(([i, j]) => Math.abs(i) + Math.abs(j))
  .sort((a, b) => a - b);
let minDelay = [...intersect]
  .map((key) => A.steps.get(key) + B.steps.get(key))
  .sort((a, b) => a - b);
console.log(`Part 1: ${closest[0]}\nPart 2: ${minDelay[0]}`);
// Part 1: 731
// Part 2: 5672