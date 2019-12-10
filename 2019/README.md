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
  for (let i = 0; i < A.length; i += 4) {
    let [op, u, v, w] = [A[i], A[i + 1], A[i + 2], A[i + 3]];
    if (op == 99)
      break;
    if (op == 1) A[w] = A[u] + A[v];
    if (op == 2) A[w] = A[u] * A[v];
  }
  return A[0];
};
console.log(`Part 1: ${gravityAssist(12, 2, ...input)}`);
for (let i = 0; i < 100; ++i)
  for (let j = 0; j < 100; ++j)
    if (gravityAssist(i, j, ...input) == 19690720)
      console.log(`Part 2: ${i}${j}`);
```

## [Day 3: Crossed Wires](https://adventofcode.com/2019/day/3)

```javascript
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
let [A, B] = input.split("\n")
  .map(line => line.split(","))
  .map(paths => new Wire(paths));
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
  return A.every((x, i) => i == 0 || A[i - 1] <= x) &&
    A.some((x, i) => i > 0 && A[i - 1] == x);
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
for (let x = 197487; x < 673251; ++x) {
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
let input = fs.readFileSync('input.txt', 'utf-8').split(",").map(Number);
let run = (id, A, ans = 0) => {
  let pad = cmd => ('00000' + cmd).substring(('00000' + cmd).length - 5);
  let op = 0, instructions = [0, 4, 4, 2, 2, 0, 0, 4, 4];
  for (let i = 0; op != 99; i += instructions[op]) {
    let cmd = pad(A[i]);
    let [u, v, w] = [A[i + 1], A[i + 2], A[i + 3]];
    u = cmd[2] == 0 ? A[u] : u;
    v = cmd[1] == 0 ? A[v] : v;
    op = parseInt(cmd.substring(cmd.length - 2));
    if (op == 1) A[w] = u + v;
    if (op == 2) A[w] = u * v;
    if (op == 3) w = A[i + 1], A[w] = id;
    if (op == 4) ans = u;
    if (op == 5) i = (u != 0) ? v : i + 3;
    if (op == 6) i = (u == 0) ? v : i + 3;
    if (op == 7) A[w] = u < v;
    if (op == 8) A[w] = u == v;
  }
  return ans;
};
console.log(`Part 1: ${run(1, [...input])}\nPart 2: ${run(5, [...input])}`);
```

## [Day 6: Universal Orbit Map](https://adventofcode.com/2019/day/6)

```javascript
let fs = require('fs');
let input = fs.readFileSync('input.txt', 'utf-8').split("\n").map(edge => edge.split(')'));
let edges = new Map(); // lookup parent u by child v: [v, u] (ie. u -> v)
for (let [u, v] of input) edges.set(v, u); // child v has parent u (ie. u -> v)
let go = (edges, v) => !edges.get(v) ? 0 : 1 + go(edges, edges.get(v)); // parent u = edges.get(child v)
let total = [...edges.keys()].map(v => go(edges, v)).reduce((a, b) => a + b);
console.log(`Part 1: ${total}`);
let [you, san] = [edges.get('YOU'), edges.get('SAN')];
let path = { you: [], san: [] };
while (you) path.you.unshift(you), you = edges.get(you); // push you's parents to front of path you
while (san) path.san.unshift(san), san = edges.get(san); // push san's parents to front of path san
let ancestor = null; // traverse paths from root till divergence to find the first common ancestor
for (let i = 0; ; ++i) {
  if (path.you[i] != path.san[i]) {
    ancestor = path.you[i - 1]; // same as path.san[i-1] (ie. you and san share this first common ancestor)
    break;
  }
}
let steps = { you: 0, san: 0 };
[you, san] = [edges.get('YOU'), edges.get('SAN')];
while (you != ancestor) ++steps.you, you = edges.get(you);
while (san != ancestor) ++steps.san, san = edges.get(san);
console.log(`Part 2: ${steps.you + steps.san}`);
```

## [Day 7: Amplification Circuit](https://adventofcode.com/2019/day/7)

* [intcode_computer_day_07.js](00_common/intcode_computer_day_07.js) (slightly modified [Day 5: Sunny with a Chance of Asteroids](#day-5-sunny-with-a-chance-of-asteroids))

```javascript
let fs = require('fs');
let A = fs.readFileSync('input.txt', 'utf-8').split(",").map(Number);
let run = require('../00_common/intcode_computer');
let permutations = A => {
  if (A.length == 1)
    return A;
  return A.reduce((res, x, i, A, B = [...A]) => {
    B.splice(i, 1); // B is A without A[i] (ie. x)
    return res.concat(permutations(B).map(a => [].concat(x, a))); // recursively insert x into all other positions
  }, []);
}
let maxThrust = (A, perms, loopback = false, max = -Infinity) => {
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
let perm1 = permutations([0, 1, 2, 3, 4]),
    perm2 = permutations([5, 6, 7, 8, 9]);
console.log(`Part 1: ${maxThrust(A, perm1)}\nPart 2: ${maxThrust(A, perm2, true)}`);
```

## [Day 8: Space Image Format](https://adventofcode.com/2019/day/8)

```javascript
let fs = require('fs');
let input = fs.readFileSync('input.txt', 'utf-8').split('');
let M = 6, N = 25, K = M * N, L = input.length / K;
let A = []; while (input.length) A.push(input.splice(0, N));
let T = [...Array(L)].map(row => Array(3).fill(0)); // tally of 0, 1, 2
A.forEach((row, i) => {
  let k = Math.floor(i / M); // k-th layer
  T[k][0] += row.filter(x => x == 0).length,
  T[k][1] += row.filter(x => x == 1).length,
  T[k][2] += row.filter(x => x == 2).length;
});
let cnt = T[0][0], min = 0;
for (let i = 1; i < L; ++i)
  if (cnt > T[i][0])
    cnt = T[i][0], min = i;
console.log(`Part 1: ${T[min][1] * T[min][2]}`);
for (let i = 0; i + M < M * L; ++i)
  for (let j = 0; j < N; ++j)
    if (A[i][j] != 2) // naive dp algo (ie. each prev layer is M rows away, only propagate non-transparent)
      A[i + M][j] = A[i][j];
let msg = [];
for (let i = (M * L) - M; i < M * L; ++i) // last layer contains the dp algo result (ie. all layers coalesced)
  msg.push(A[i].join('').replace(/0/g, ' '));
console.log('Part 2: ');
msg.forEach(row => console.log(row));
```

## [Day 9: Sensor Boost](https://adventofcode.com/2019/day/9)

* [intcode_computer_day_09.js](00_common/intcode_computer_day_09.js) (slightly modified [Day 5: Sunny with a Chance of Asteroids](#day-5-sunny-with-a-chance-of-asteroids))

```javascript
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
```

* [main.js](09_sensor_boost/main.js): invoke run()...

```javascript
let fs = require('fs');
let A = fs.readFileSync('input.txt', 'utf-8').split(",").map(Number);
let run = require('../00_common/intcode_computer_day_09');
console.log(`Part 1: ${run(A, [1])}\nPart 2: ${run(A, [2])}`);
```

## [Day 10: Monitoring Station](https://adventofcode.com/2019/day/10)

* Note: I let ```x``` denote the row and ```y``` denote the column, this is opposite per the problem statement (ie. ```y``` is the row and ```x``` is the column).
However, this is irrelevant since I'm consistent with this representation.

```javascript
let fs = require('fs');
let A = fs.readFileSync('input.txt', 'utf-8').split('\n').map(row => row.split(''));
let detect = A => {
  let gcd = (a, b) => b == 0 ? Math.abs(a) : gcd(b, a % b);
  let [M, N] = [A.length, A[0].length];
  let roids = []; for (let i = 0; i < M; ++i) for (let j = 0; j < N; ++j) if (A[i][j] == '#') roids.push([i, j]);
  let K = roids.length;
  let key = roid => `${roid[0]},${roid[1]}`;
  let seen = new Set([...roids].map(roid => key(roid)));
  let all = [];
  for (let u = 0; u < K; ++u) {
    let cnt = 0;
    for (let v = 0; v < K; ++v) {
      if (u == v)
        continue; // do not compare asteroids to themselves
      let A = {}; [A.x, A.y] = [...roids[u]];
      let B = {}; [B.x, B.y] = [...roids[v]];
      let diff = {}; [diff.x, diff.y] = [B.x - A.x, B.y - A.y];
      let div = gcd(diff.x, diff.y);
      let delta = {}; [delta.x, delta.y] = [Math.floor(diff.x / div), Math.floor(diff.y / div)];
      let blocked = false;
      let next = { x: A.x + delta.x, y: A.y + delta.y };
      while (!(next.x == B.x && next.y == B.y)) {
        if (seen.has(key([next.x, next.y])))
          blocked = true;
        next.x += delta.x, next.y +=delta.y
      }
      if (!blocked)
        ++cnt;
    }
    all.push(cnt);
  }
  return all.sort((a, b) => b - a)[0];
}
console.log(`Part 1: ${detect(A)}`);
```