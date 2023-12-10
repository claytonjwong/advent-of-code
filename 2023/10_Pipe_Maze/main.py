# 8:08am - time to read the problem statement

# 8:11am - ~3 minutes to read it

# game plan:

# 8:36am => ~25 minutes for the implementation in Python3
# 8:40am => debugging
# 8:45am => debugging
# 8:51am => part 1 AC :)

# ~43 minutes -> read problem statement, come up with a game plan (which changed slightly along the way), implementation, validation on small input,
# fix bugs! 🐞 (oops), then sumbit

# 8:52am - part 2 -> read problem statement

# 9:20am -> reached point of diminishing returns => TODO: properly handle the "squeezed" use case...

from collections import deque

A = []
with open('/Users/claytonjwong/sandbox/advent-of-code/2023/10_Pipe_Maze/input.txt') as input:
    for line in input:
        A.append(line.strip())
M, N = len(A), len(A[0])

q, seen, depth = deque([(i, j) for i in range(M) for j in range(N) if A[i][j] == 'S']), set(), 0
while q:
    ok = False
    for _ in range(len(q)):
        i, j = q.pop()
        if (i, j) in seen:
            continue
        seen.add((i, j))

        # .....
        # .F-7.
        # .|.|.
        # .L-J.
        # .....
        UP = set(['F','|','7'])
        DOWN = set(['L','|','J'])
        LEFT = set(['L','-','F'])
        RIGHT = set(['7','-','J'])

        u, v = i - 1, j
        if 0 <= u < M and 0 <= v < N and (u, v) not in seen and (A[i][j] in DOWN or A[i][j] == 'S') and A[u][v] in UP:
            q.appendleft((u, v)); ok = True

        u, v = i + 1, j
        if 0 <= u < M and 0 <= v < N and (u, v) not in seen and (A[i][j] in UP or A[i][j] == 'S') and A[u][v] in DOWN:
            q.appendleft((u, v)); ok = True

        u, v = i, j - 1
        if 0 <= u < M and 0 <= v < N and (u, v) not in seen and (A[i][j] in RIGHT or A[i][j] == 'S') and A[u][v] in LEFT:
            q.appendleft((u, v)); ok = True

        u, v = i, j + 1
        if 0 <= u < M and 0 <= v < N and (u, v) not in seen and (A[i][j] in LEFT or A[i][j] == 'S') and A[u][v] in RIGHT:
            q.appendleft((u, v)); ok = True

    depth += int(ok)

print(f'part 1: {depth}')
# part 1: 7173


# part 2: use inversion to derive the count of spaces inside the loop, ie. we count the total number of spaces '.'
# then we use BFS from outwards->in initially from all OOB cells inwards to count the number of spaces '.' adjacent to the "outside"
# space inside loop = total spaces - spaces outside loop

total, outside = len([(i, j) for i in range(M) for j in range(N) if A[i][j] == '.']), 0
top = [(-1, j) for j in range(N)]
bot = [(M, j) for j in range(N)]
left = [(-1, i) for i in range(M)]
right = [(N, i) for i in range(M)]

q = deque(top + bot + left + right)
seen = set()
while q:
    i, j = q.pop()
    if (i, j) in seen:
        continue
    seen.add((i, j))
    outside += int(0 <= i < M and 0 <= j < N and A[i][j] == '.')

    # .....
    # .F-7.
    # .|.|.
    # .L-J.
    # .....
    UP = set(['F','|','7'])
    DOWN = set(['L','|','J'])
    LEFT = set(['L','-','F'])
    RIGHT = set(['7','-','J'])

    u, v = i - 1, j
    if 0 <= u < M and 0 <= v < N and (u, v) not in seen and (A[u][v] in UP or A[u][v] == '.'):
        q.appendleft((u, v))

    u, v = i + 1, j
    if 0 <= u < M and 0 <= v < N and (u, v) not in seen and (A[u][v] in DOWN or A[u][v] == '.'):
        q.appendleft((u, v))

    u, v = i, j - 1
    if 0 <= u < M and 0 <= v < N and (u, v) not in seen and (A[u][v] in LEFT or A[u][v] == '.'):
        q.appendleft((u, v))

    u, v = i, j + 1
    if 0 <= u < M and 0 <= v < N and (u, v) not in seen and (A[u][v] in RIGHT or A[u][v] == '.'):
        q.appendleft((u, v))

print(f'total: {total}')
print(f'outside: {outside}')

inside = total - outside
print(f'part 2: {inside}')
