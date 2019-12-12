/*
 * Day 10: Monitoring Station
 *
 * Q: https://adventofcode.com/2019/day/10
 * A: https://claytonjwong.github.io/advent-of-code/2019/#day-10-monitoring-station
 */
let fs = require('fs');
let input = fs.readFileSync('input.txt', 'utf-8').split('\n').map(row => row.split(''));
let detect = A => {
  let gcd = (a, b) => b == 0 ? Math.abs(a) : gcd(b, a % b);
  let delta = (a, b) => {
    let diff = {}; [diff.x, diff.y] = [b.x - a.x, b.y - a.y];
    let gdiv = gcd(diff.x, diff.y);
    return { x: Math.floor(diff.x / gdiv), y: Math.floor(diff.y / gdiv) };
  };
  let [M, N] = [A.length, A[0].length];
  let roids = []; for (let i = 0; i < M; ++i) for (let j = 0; j < N; ++j) if (A[i][j] == '#') roids.push([i, j]);
  let K = roids.length;
  let key = roid => `${roid[0]},${roid[1]}`;
  let seen = new Set([...roids].map(roid => key(roid)));
  let all = [];
  for (let u = 0; u < K; ++u) {
    let a = {}; [a.x, a.y] = [...roids[u]];
    let cand = { x: a.x, y: a.y, seen: new Set() }; // a candidate for best asteroid
    for (let v = 0; v < K; ++v) {
      if (u == v) continue; // do not compare asteroids to themselves
      let b = {}; [b.x, b.y] = [...roids[v]];    
      let d = delta(a, b); // take one step (d.x, d.y) at a time from (a -> b) to find (c)
      let c = { x: a.x + d.x, y: a.y + d.y, isBlocking: false };
      while (!(c.x == b.x && c.y == b.y)) {
        if (seen.has(key([c.x, c.y])))
          c.isBlocking = true;
        c.x += d.x, c.y += d.y;
      }
      if (!c.isBlocking)
        cand.seen.add([b.x, b.y]);
    }
    all.push(cand);
  }
  return all.sort((a, b) => b.seen.size - a.seen.size)[0];
}
let best = detect(input);
console.log(`Part 1: ${best.seen.size}`);
// Part 1: 247