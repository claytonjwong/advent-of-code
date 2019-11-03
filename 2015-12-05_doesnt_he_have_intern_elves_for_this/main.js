/*
 * https://adventofcode.com/2015/day/5
 */

const vowels = new Set(['a','e','i','o','u']);

let isNice1 = (s) => {
    let cnt = 0;
    let pre = '\0',
        cur = '\0';
    let found = false;
    for (let c of s) {
        if (vowels.has(c))
            ++cnt;
        pre = cur;
        cur = c;
        if (pre == cur)
            found = true;
        else if ((pre == 'a' && cur == 'b') || (pre == 'c' && cur == 'd') || (pre == 'p' && cur == 'q') || (pre == 'x' && cur == 'y'))
            return false;
    }
    return cnt >= 3 && found;
}

let isNice2 = (s) => {
    let match = false,
        repeat = false;
    let kmer = new Map(); // track last index of each unique kmer seen
    for (let i=0; i + 1 < s.length; ++i) {
        let key = s.substr(i, 2);
        if (kmer.has(key))
            match |= i - kmer.get(key) > 1;
        else
            kmer.set(key, i);
    }
    for (let i=2; i < s.length; ++i)
        if (s[i-2] == s[i])
            repeat = true;
    return match && repeat;
}

let cnt1 = 0,
    cnt2 = 0;
let fs = require('fs');
let input = fs.readFileSync('./input.txt', 'utf-8');
let lines = input.split('\n');
for (let line of lines) {
    if (isNice1(line)) ++cnt1;
    if (isNice2(line)) ++cnt2;
}
console.log(`Answer 1: ${cnt1}`);
console.log(`Answer 2: ${cnt2}`);
    