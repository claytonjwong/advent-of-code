#
# https://adventofcode.com/2022/day/12
#

from collections import deque

A = []
with open('input.txt') as input:
    A = [list(line.strip()) for line in input]

beg, end, alt = deque(), deque(), []
M, N = len(A), len(A[0])
for i in range(M):
    for j in range(N):
        if A[i][j] == 'S': beg.append((i, j)); A[i][j] = 'a'
        if A[i][j] == 'E': end.append((i, j)); A[i][j] = 'z'
        if A[i][j] == 'a': alt.append(deque([(i, j)]))

def bfs(start):
    q, seen, depth = start, set(start), 0
    while q:
        for _ in range(len(q)):
            i, j = q.popleft()
            if (i, j) in end:
                return depth
            for u, v in [[i - 1, j], [i, j + 1], [i + 1, j], [i, j - 1]]:
                if 0 <= u < M and 0 <= v < N and ord(A[u][v]) <= ord(A[i][j]) + 1 and (u, v) not in seen:
                    q.append((u, v)); seen.add((u, v))
        depth += 1
    return float('inf')

print(f'part 1: {bfs(beg)}')
print(f'part 2: {min([bfs(cand) for cand in alt])}') # alternative candidates for optimal begin
# part 1: 370
# part 2: 363