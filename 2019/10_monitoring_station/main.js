/*
 * Day 10: Monitoring Station
 *
 * Q: https://adventofcode.com/2019/day/10
 * A: https://claytonjwong.github.io/advent-of-code/2019/#day-10-monitoring-station
 */
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
// Part 1: 247
