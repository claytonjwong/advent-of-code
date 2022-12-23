#
# https://adventofcode.com/2022/day/22
#

A, dirs = [], []
with open('input.txt') as input:
    for line in input:
        line = list(line[:-1]) # discard trailing newline
        if not len(line):
            continue
        elif line[0] in [' ', '.', '#']:
            A.append(line)
        else:
            steps = 0
            for c in line:
                if c.isdigit():
                    steps = 10 * steps + int(c)
                else:
                    if steps:
                        dirs.append(steps); steps = 0
                    dirs.append(c)
M = len(A)
N = max(len(A[i]) for i in range(M))
for row in A:
    pad = [' '] * (N - len(row))
    row.extend(pad)
R, D, L, U = 0, 1, 2, 3 # right, down, left, up

class Walker:
    def __init__(self):
        self.i = 0
        self.j = A[0].index('.')
        self.d = R
    def turn(self, d):
        if self.d == R:
            if d == 'L': self.d = U
            if d == 'R': self.d = D
        elif self.d == D:
            if d == 'L': self.d = R
            if d == 'R': self.d = L
        elif self.d == L:
            if d == 'L': self.d = D
            if d == 'R': self.d = U
        elif self.d == U:
            if d == 'L': self.d = L
            if d == 'R': self.d = R
    def walk(self, steps):
        di, dj = (0, 1) if self.d == R else (1, 0) if self.d == D else (0, -1) if self.d == L else (-1, 0) # right, down, left, up
        while steps:
            steps -= 1
            u, v = (self.i + di, self.j + dj)
            if self.d == R and not self.step_R(u, v): break
            if self.d == D and not self.step_D(u, v): break
            if self.d == L and not self.step_L(u, v): break
            if self.d == U and not self.step_U(u, v): break
    def step_R(self, u, v):
        if 0 <= v < N and A[u][v] == '.': # step right
            self.j = v
            return True
        if v == N or A[u][v] == ' ': # wrap-around left
            v = 0
            while A[u][v] == ' ':
                v += 1
            if A[u][v] == '.':
                self.j = v
                return True
        return False
    def step_D(self, u, v):
        if 0 <= u < M and A[u][v] == '.': # step down
            self.i = u
            return True
        if u == M or A[u][v] == ' ': # wrap-around up
            u = 0
            while A[u][v] == ' ':
                u += 1
            if A[u][v] == '.':
                self.i = u
                return True
        return False
    def step_L(self, u, v):
        if 0 <= v < N and A[u][v] == '.': # step left
            self.j = v
            return True
        if v < 0 or A[u][v] == ' ': # wrap-around right
            v = N - 1
            while A[u][v] == ' ':
                v -= 1
            if A[u][v] == '.':
                self.j = v
                return True
        return False
    def step_U(self, u, v):
        if 0 <= u < M and A[u][v] == '.': # step up
            self.i = u
            return True
        if u < 0 or A[u][v] == ' ': # wrap-around down
            u = M - 1
            while A[u][v] == ' ':
                u -= 1
            if A[u][v] == '.':
                self.i = u
                return True
        return False

walker = Walker()
for x in dirs:
    if type(x) == int:
        walker.walk(x)
    else:
        walker.turn(x)
part1 = (walker.i + 1) * 1000 + (walker.j + 1) * 4 + walker.d
print(f'part 1: {part1}')
# part 1: 165094