/*
 * Day 6: Universal Orbit Map
 *
 * Q: https://adventofcode.com/2019/day/6
 * A: https://claytonjwong.github.io/advent-of-code/2019/#day-6-universal-orbit-map
 */ 
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
for (let i=0;; ++i) {
    if (path.you[i] != path.san[i]) {
        ancestor = path.you[i-1]; // same as path_san[i-1] (ie. you and san share this first common ancestor)
        break;
    }
}
let steps = { you: 0, san: 0 };
[you, san] = [edges.get('YOU'), edges.get('SAN')];
while (you != ancestor) ++steps.you, you = edges.get(you);
while (san != ancestor) ++steps.san, san = edges.get(san);
console.log(`Part 2: ${steps.you + steps.san}`);