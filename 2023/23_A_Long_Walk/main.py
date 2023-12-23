import sys
sys.setrecursionlimit(int(1e5))

A = []
with open('input.txt') as input:
    for line in input:
        A.append(line.strip())
M, N = len(A), len(A[0])

S = (0, [j for j in range(N) if A[0][j] == '.'][0])
T = (M - 1, [j for j in range(N) if A[M - 1][j] == '.'][0])

seen = set()
def go(i = S[0], j = S[1], k = 0):
    if (i, j) == T:
        return k
    if i < 0 or j < 0 or i == M or j == N or A[i][j] == '#' or (i, j) in seen:
        return 0
    best = 0
    seen.add((i, j))
    if   A[i][j] == '^': best = go(i - 1, j, k + 1)
    elif A[i][j] == '>': best = go(i, j + 1, k + 1)
    elif A[i][j] == 'v': best = go(i + 1, j, k + 1)
    elif A[i][j] == '<': best = go(i, j - 1, k + 1)
    else: best = max(go(u, v, k + 1) for u, v in [(i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)])
    seen.remove((i, j))
    return best
print(f'part 1: {go()}')
# part 1: 2254
