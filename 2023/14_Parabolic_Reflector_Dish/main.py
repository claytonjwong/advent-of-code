# 3:32pm - start reading the problem statement
# 3:41pm - ~9 minutes to read + game plan

# move each O "up" <-- keep it super simple

# 3:42pm -
# 3:49pm - ~7 minutes for the implementation in Python3 which is AC :)

# 3:50pm - part 2

A = []
with open('input.txt') as input:
    for line in input:
        A.append([c for c in line.strip()])
M, N = len(A), len(A[0])

def step(i, j, di, dj):
    u, v = i + di, j + dj
    while 0 <= u < M and 0 <= v < N and A[u][v] == '.':
        A[i][j] = '.'; A[u][v] = 'O'
        i, j = u, v; u, v = i + di, j + dj
for i in range(M):
    for j in range(N):
        if A[i][j] == 'O':
            step(i, j, di=-1, dj=0)

t1 = sum(M - i for i in range(M) for j in range(N) if A[i][j] == 'O')
print(f'part 1: {t1}')
# part 1: 109424
