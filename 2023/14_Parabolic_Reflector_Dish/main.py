A = []
with open('input.txt') as input:
    for line in input:
        A.append([c for c in line.strip()])
M, N = len(A), len(A[0])

total = lambda A: sum(M - i for i in range(M) for j in range(N) if A[i][j] == 'O')

def step(i, j, di, dj):
    if A[i][j] != 'O':
        return
    u, v = i + di, j + dj
    while 0 <= u < M and 0 <= v < N and A[u][v] == '.':
        A[i][j] = '.'; A[u][v] = 'O'
        i, j = u, v; u, v = i + di, j + dj

def north(A):
    for i in range(M):
        for j in range(N):
            step(i, j, di=-1, dj=0)
    return total(A)

def cycle(A):
    for _ in range(1000):
        for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            for i in range(M) if di == -1 else reversed(range(M)):
                for j in range(N) if dj == -1 else reversed(range(N)):
                    step(i, j, di, dj)
    return total(A)

print(f'part 1: {north(A[:])}')
print(f'part 2: {cycle(A[:])}')
# part 1: 109424
# part 2: 102509
