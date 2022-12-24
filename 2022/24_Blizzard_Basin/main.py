#
# https://adventofcode.com/2022/day/24
#

import os
os.chdir('/Users/claytonjwong/sandbox/advent-of-code/2022/24_Blizzard_Basin')

from collections import deque

A = []
with open('input.txt') as input:
    for line in input:
        A.append(list(line.strip()))
M, N = len(A), len(A[0])

class Blizzard:
    def __init__(self, i, j, d):
        self.i = i
        self.j = j
        self.di = -1 if d == '^' else 1 if d == 'v' else 0
        self.dj = -1 if d == '<' else 1 if d == '>' else 0
    def step(self):
        self.i += self.di
        self.j += self.dj
        if A[self.i][self.j] == '#': # wrap-around assuming no up/down in source, target columns
            self.i += self.di
            self.j += self.dj
            if self.i < 0: self.i = M - 2
            if self.j < 0: self.j = N - 2
            if self.i == M: self.i = 1
            if self.j == N: self.j = 1
        return (self.i, self.j)

B = []
for i in range(1, M - 1):
    for j in range(1, N - 1):
        if A[i][j] != '.':
            B.append(Blizzard(i, j, A[i][j]))

S, T = (0, A[0].index('.')), (M - 1, A[M - 1].index('.')) # source, target
cur, step = set([S]), -1
while len(cur):
    step += 1
    bliz, next = set([b.step() for b in B]), set()
    for i, j in cur:
        if (i, j) == T:
            next = set()
            break
        for u, v in [(i, j), (i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)]:
            if 0 <= u < M and 0 <= v < N and A[u][v] != '#' and (u, v) not in bliz:
                next.add((u, v))
    cur = next
print(f'part 1: {step}')