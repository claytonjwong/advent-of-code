# AoC 2019
* [adventofcode.com/2019](https://adventofcode.com/2019)

## [Day 1: The Tyranny of the Rocket Equation](https://adventofcode.com/2019/day/1)

```javascript
let fs = require('fs');
let input = fs.readFileSync('input.txt', 'utf8');
let f = x => Math.floor(x / 3) - 2;
let go = x => f(x) <= 0 ? 0 : f(x) + go(f(x));
let run = func => input.split("\n").map(x => func(x)).reduce((a, b) => a + b);
console.log(`Part 1: ${run(f)}\nPart 2: ${run(go)}`);
```

## [Day 2: 1202 Program Alarm](https://adventofcode.com/2019/day/2)

```javascript
let fs = require('fs');
let input = fs.readFileSync('input.txt', 'utf-8').split(",").map(x => parseInt(x));
let gravityAssist = (noun, verb, ...A) => {
    A[1] = noun, A[2] = verb;
    for (let i=0; i < A.length; i += 4) {
        let [op, u, v, w] = [A[i], A[i+1], A[i+2], A[i+3]];
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
```

## [Day 3: Crossed Wires](https://adventofcode.com/2019/day/3)

```javascript
let fs = require('fs');
let input = fs.readFileSync('input.txt', 'utf-8');
class Wire {
  constructor(input) {
    this.input = input;
    this.seen = new Set();
    this.total = 0;
    this.steps = new Map();
    this.pos = {
      row: 0,
      col: 0
    };
    this.traverse();
  }
  traverse() {
    for (let path of this.input)
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
      if (!this.steps.get(key) || (this.steps.get(key) && this.steps.get(key) > this.total))
        this.steps.set(key, this.total);
    }
  }
}
let [A, B] = input.split("\n").map(list => list.split(",")).map(array => new Wire(array));
let intersect = [...A.seen].filter(x => B.seen.has(x));
let closest = [...intersect]
  .map((key) => key.split(",").map(Number))
  .map(([i, j]) => Math.abs(i) + Math.abs(j))
  .sort((a, b) => a - b);
let minDelay = [...intersect]
  .map((key) => A.steps.get(key) + B.steps.get(key))
  .sort((a, b) => a - b);
console.log(`Part 1: ${closest[0]}\nPart 2: ${minDelay[0]}`);
```