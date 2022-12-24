#
# https://adventofcode.com/2022/day/24
#

A = []
with open('input.txt') as input:
    A = [list(line.strip()) for line in input]
M, N = len(A), len(A[0])
S, T = (0, A[0].index('.')), (M - 1, A[M - 1].index('.')) # source, target

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
            if self.i == 0: self.i = M - 2
            if self.j == 0: self.j = N - 2
            if self.i == M - 1: self.i = 1
            if self.j == N - 1: self.j = 1
        return (self.i, self.j)
B = [Blizzard(i, j, A[i][j]) for j in range(1, N - 1) for i in range(1, M - 1) if A[i][j] != '.']

def run(S, T):
    cur, step = set([S]), 0
    while len(cur):
        next, bliz = set(), set([b.step() for b in B])
        for i, j in cur:
            if (i, j) == T:
                return step
            for u, v in [(i, j), (i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)]:
                if 0 <= u < M and 0 <= v < N and A[u][v] != '#' and (u, v) not in bliz:
                    next.add((u, v))
        cur = next; step += 1

a = run(S, T)
b = run(T, S) + 1
c = run(S, T) + 1
print(f'part 1: {a}')
print(f'part 2: {a + b + c}')
# part 1: 332
# part 2: 942