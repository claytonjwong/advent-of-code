#
# https://adventofcode.com/2020/day/2
#

from collections import Counter

A = []
with open('./input.txt') as input:
    A = [line.strip() for line in input]

one = 0
two = 0
for range, ch, word in [line.split(' ') for line in A]:
    lo, hi = map(int, range.split('-'))
    ch = ch[0]  # ignore ':'
    m = Counter(word)
    if ch in m and lo <= m[ch] <= hi:
        one += 1
    if (lo <= len(word) and ch == word[lo - 1]) ^ (hi <= len(word) and ch == word[hi - 1]):
        two += 1
print(f'Part 1: {one}')  # Part 1: 460
print(f'Part 2: {two}')  # Part 2: 251
