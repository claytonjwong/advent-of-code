#
# https://adventofcode.com/2022/day/8
#

A = []
with open('input.txt') as input:
    for line in input:
        A.append([int(x) for x in line.strip()])
M, N = len(A), len(A[0])

#
# part 1
#
seen, key = set(), lambda i, j: f'{i},{j}'
for i in range(M):
    l, r = -1, -1 # left/right
    for j in range(N):
        k = N - 1 - j
        if l < A[i][j]: l = A[i][j]; seen.add(key(i, j))
        if r < A[i][k]: r = A[i][k]; seen.add(key(i, k))
for j in range(N):
    u, d = -1, -1 # up/down
    for i in range(M):
        k = M - 1 - i
        if u < A[i][j]: u = A[i][j]; seen.add(key(i, j))
        if d < A[k][j]: d = A[k][j]; seen.add(key(k, j))

#
# part 2
#
best = 0
for i in range(1, M - 1):
    for j in range(1, N - 1):
        l, k = 0, j - 1 # left
        while 0 <= k:
            l += 1
            if A[i][j] <= A[i][k]: break
            k -= 1
        r, k = 0, j + 1 # right
        while k < N:
            r += 1
            if A[i][j] <= A[i][k]: break
            k += 1
        u, k = 0, i - 1 # up
        while 0 <= k:
            u += 1
            if A[i][j] <= A[k][j]: break
            k -= 1
        d, k = 0, i + 1 # down
        while k < M:
            d += 1
            if A[i][j] <= A[k][j]: break
            k += 1
        cand = l * r * u * d
        best = max(best, cand)

print(f'part 1: {len(seen)}')
print(f'part 2: {best}')
# part 1: 1681
# part 2: 201684