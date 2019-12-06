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
      if (this.steps.get(key) && this.steps.get(key) <= this.total)
        continue; // only add keys which don't exist; only update keys with larger total
      this.steps.set(key, this.total);
    }
  }
}
let [A, B] = input.split("\n")
  .map(list => list.split(","))
  .map(array => new Wire(array));
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

## [Day 4: Secure Container](https://adventofcode.com/2019/day/4)

```javascript
let ok1 = x => {
    let A = x.toString().split('').map(Number);
    return A.every((x, i) => i == 0 || A[i-1] <= x) &&
           A.some((x, i) => i > 0 && A[i-1] == x);
}
let ok2 = x => {
    let A = x.toString().split('').map(Number);
    let cnt = new Map();
    for (let val of A) {
        if (cnt.has(val))
            cnt.set(val, 1 + cnt.get(val));
        else
            cnt.set(val, 1);
    }
    for (let [key, val] of cnt)
        if (val == 2)
            return true;
    return false;
}
let part1 = 0, part2 = 0;
for (let x=197487; x < 673251; ++x) {
    if (ok1(x))
        ++part1;
    if (ok1(x) && ok2(x))
        ++part2;
}
console.log(`Part 1: ${part1}\nPart 2: ${part2}`);
```

## [Day 5: Sunny with a Chance of Asteroids](https://adventofcode.com/2019/day/5)

```javascript
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
```
