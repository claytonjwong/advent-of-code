from heapq import heappop, heappush

A = []
with open('/Users/claytonjwong/sandbox/advent-of-code/2023/17_Clumsy_Crucible/input.txt') as input:
    for line in input:
        A.append([int(x) for x in line.strip()])
M, N = len(A), len(A[0])

q, seen = [(0, 0, 0, 0, 0, 0)], set()  # dist, i, j, di, dj, step

def enqueue(q, dist, i, j, du, dv, step):
    u = i + du
    v = j + dv
    if 0 <= u < M and 0 <= v < N:
        heappush(q, (dist + A[u][v], u, v, du, dv, step))

t1 = 0
while q:
    dist, i, j, di, dj, step = heappop(q)
    if i == M - 1 and j == N - 1:
        t1 = dist; break
    if (i, j, di, dj, step) in seen:
        continue
    seen.add((i, j, di, dj, step))
    if step < 3 and (di, dj) != (0, 0):                       # same direction (di, dj): three step max
        enqueue(q, dist, i, j, di, dj, step + 1)
    for du, dv in [(-1, 0), (0, 1), (1, 0), (0, -1)]:         # diff direction (du, dv): first step
        if (du, dv) != (di, dj) and (du, dv) != (-di, -dj):
            enqueue(q, dist, i, j, du, dv, step=1)

print(f'part 1: {t1}')
# part 1: 635
