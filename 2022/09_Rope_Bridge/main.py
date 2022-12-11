#
# https://adventofcode.com/2022/day/9
#

def run(T):
    A, seen = [[0, 0]], set()
    with open('input.txt') as input:
        for line in input:
            d, steps = line.strip().split(' ')
            di = -1 if d == 'U' else 1 if d == 'D' else 0
            dj = -1 if d == 'L' else 1 if d == 'R' else 0
            for _ in range(int(steps)):
                slide(A, di, dj)
                if len(A) < T and A[-1] != [0, 0]:
                    A.append([0, 0])
                if len(A) == T:
                    seen.add((A[-1][0], A[-1][1]))
    return len(seen)

def slide(A, di, dj):
    i, j = A[0]; A[0] = [i + di, j + dj]
    for k in range(1, len(A)):
        i, j = A[k - 1]
        u, v = A[k]
        du = i - u
        dv = j - v
        if abs(du) == 2 or abs(dv) == 2:
            du = 1 if du == 2 else -1 if du == -2 else du
            dv = 1 if dv == 2 else -1 if dv == -2 else dv
            A[k] = [u + du, v + dv]

print(f'part 1: {run(2)}')
print(f'part 2: {run(10)}')
# part 1: 5883
# part 2: 2367