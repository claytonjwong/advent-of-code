/*
 * Day 4: Secure Container
 * 
 * Q: https://adventofcode.com/2019/day/4
 * A: https://claytonjwong.github.io/advent-of-code/2019/#day-3-crossed-wires
 */
let ok1 = x => {
  let A = x.toString().split('').map(Number);
  return A.every((x, i) => i == 0 || A[i - 1] <= x) &&
    A.some((x, i) => i > 0 && A[i - 1] == x);
}
let ok2 = x => {
  let A = x.toString().split('').map(Number);
  let cnt = new Map();
  for (let val of A)
      cnt.set(val, 1 + (cnt.get(val) || 0));
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
// Part 1: 1640
// Part 2: 1126
