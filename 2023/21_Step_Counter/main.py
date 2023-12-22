from collections import deque

A = []
with open('input.txt') as input:
    for line in input:
        A.append(line.strip())
M, N = len(A), len(A[0])

def run(steps):
    S = [(i, j) for i in range(M) for j in range(N) if A[i][j] == 'S'][0]
    q = deque([S]); seen = set(q); depth = 0
    while q and depth <= steps:
        next = []
        for _ in range(len(q)):
            i, j = q.popleft()
            for u, v in [(i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)]:
                if 0 <= u < M and 0 <= v < N and (u, v) not in seen and (A[u][v] == '.' or A[u][v] == 'S'):
                    next.append((u, v)); seen.add((u, v))
        q.extend(next); depth += 1
    dist = lambda i, j, u, v: abs(i - u) + abs(j - v)                     # manhattan distance from cell i,j to cell u,v
    ok = lambda i, j, u, v, steps: steps & 1 == dist(i, j, u, v) & 1      # steps and distance are both even inclusive-or both odd, ie. we can step back-and-forth an even amount of times: distances of 0,2,4,6,etc from origin for even steps from origin and distances of 1,3,5,7,etc from origin for odd steps from origin
    return len([(i, j) for i, j in seen if ok(i, j, S[0], S[1], steps)])
print(f'part 1: {run(64)}')
# part 1: 3740
