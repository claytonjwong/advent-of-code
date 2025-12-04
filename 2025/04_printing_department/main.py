#
# https://adventofcode.com/2025/day/4
#

A = []
with open('example.txt') as input:
    for s in input:
        A.append(s)
M, N = len(A), len(A[0])

def can_access(i, j):
    if A[i][j] != '@':
        return False
    cnt = 0
    for u, v in [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j + 1), (i + 1, j + 1), (i + 1, j), (i + 1, j - 1), (i, j - 1)]:
        if 0 <= u < M and 0 <= v < N and A[u][v] == '@':
            cnt += 1
    return cnt < 4

lines = []
for i in range(M):
    line = []
    for j in range(N):
        line.append('x' if can_access(i, j) else A[i][j])
    lines.append(''.join(line).strip())
for line in lines:
    print(line)

part1 = sum(int(can_access(i, j)) for i in range(M) for j in range(N))
print(f'part1: {part1}')
