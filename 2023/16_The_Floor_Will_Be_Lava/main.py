# 12:00pm - read problem statement

# 12:04pm - game plan: BFS starting at 0,0

# so the BFS queue per k-th depth contains elements which are the i,j coordinate (row, column correspondingly) and a direction di,dj

# 12:04pm - implementation begins
# 12:33pm - implementation ends, AC for part 1, yay! :)

from collections import deque

A = []
with open('input.txt') as input:
    for line in input:
        A.append(line.strip())
M, N = len(A), len(A[0])

q, seen = deque(), set()
def enqueue(step):
    i, j, _, _ = step
    if step not in seen and 0 <= i < M and 0 <= j < N:
        q.append(step); seen.add(step)
enqueue((0, 0, 0, 1))  # i,j  di,dj
while q:
    i, j, di, dj = q.popleft()
    step = (i + di, j + dj, di, dj)
    U = (i - 1, j, -1, 0)  # up
    D = (i + 1, j,  1, 0)  # down
    L = (i, j - 1, 0, -1)  # left
    R = (i, j + 1, 0,  1)  # right
    if A[i][j] == '.':
        enqueue(step)
    elif A[i][j] == '|':
        if di:
            enqueue(step)
        if dj:
            enqueue(U)
            enqueue(D)
    elif A[i][j] == '-':
        if di:
            enqueue(L)
            enqueue(R)
        if dj:
            enqueue(step)
    elif A[i][j] == '/':
        if di == -1: enqueue(R)  # up -> right
        if di ==  1: enqueue(L)  # down -> left
        if dj == -1: enqueue(D)  # left -> down
        if dj ==  1: enqueue(U)  # right -> up
    elif A[i][j] == '\\':
        if di == -1: enqueue(L)  # up -> left
        if di ==  1: enqueue(R)  # down -> right
        if dj == -1: enqueue(U)  # left -> up
        if dj ==  1: enqueue(D)  # right -> down
t1 = len(set([(i, j) for i, j, _, _ in seen]))
print(f'part 1: {t1}')
# part 1: 7060
