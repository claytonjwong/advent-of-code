from heapq import heappop, heappush

A = []
with open('input.txt') as input:
    for line in input:
        A.append([int(x) for x in line.strip()])
M, N = len(A), len(A[0])

def run(lo, hi):
    def enqueue(q, dist, i, j, du, dv, step):
        u = i + du
        v = j + dv
        if 0 <= u < M and 0 <= v < N:
            heappush(q, (dist + A[u][v], u, v, du, dv, step))
    q, seen = [(0, 0, 0, 0, 0, 0)], set()  # dist, i, j, di, dj, step
    while q:
        dist, i, j, di, dj, step = heappop(q)
        if lo <= step and i == M - 1 and j == N - 1:                # 🎯 target: 🚫 lo step minimum constraint
            return dist
        if (i, j, di, dj, step) in seen:
            continue
        seen.add((i, j, di, dj, step))
        if step < hi and (di, dj) != (0, 0):                        # same direction (di, dj): 🚫 hi step maximum contraint
            enqueue(q, dist, i, j, di, dj, step + 1)
        if lo <= step or (di, dj) == (0, 0):
            for du, dv in [(-1, 0), (0, 1), (1, 0), (0, -1)]:       # diff direction (du, dv): 🌱 first step
                if (du, dv) != (di, dj) and (du, dv) != (-di, -dj):
                    enqueue(q, dist, i, j, du, dv, step=1)

print(f'part 1: {run(1, 3)}')
print(f'part 2: {run(4, 10)}')
# part 1: 635
# part 2: 734
