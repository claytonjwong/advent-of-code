# 1:47pm - after lunch break -> start reading problem statement
# 1:51pm - ~4 minutes to read and come up with game plan

# game plan: top-down DP, track current i,j and let k be the amount of continuous hops in the same direction, each next state is left,right,straight
# and straight is only allowed if k < 3


# 1:53pm - start implementation
# 1:57pm - implementation done, let's see what happens...
# 2:09pm - debugging...
# 2:24pm - ok I think I need to start over again, LOL -- the DFS is returning a sub-optimal solution because of the cache
#          and the cache is needed to avoid this thing taking forever!  So this has a funky smell, and I don't like it one bit
#          instead let's use BFS queue, then +1,+2,+3 in same direction, +1 left and +1 right to each potential next step, tracking
#          coordinate values in the queue which have been seen

# queue element can be i,j cell and total to reach it
# seen can be set of seen i,j cells -> we can perform a scan of the matrix in M*N time

# I think that sounds like a better game plan, let's take a break and come back...
# question: how to enforce the 3 in the same direction rule? +onto the queue element the last_i, last_j, and step count ?
# then we can derive the +1 step for steps in the same direction

from functools import cache

INF = int(1e9 + 7)

A = []
with open('input.txt') as input:
    for line in input:
        A.append(line.strip())
M, N = len(A), len(A[0])

seen = set()
@cache
def go(i = 0, j = 0, last_i = -1, last_j = -1, step = 1):
    if i == M - 1 and j == N - 1:
        return int(A[i][j])
    seen.add((i, j))
    best = INF
    for u, v in [(i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)]:
        di = i - last_i
        dj = j - last_j
        du = u - i
        dv = v - j
        same = int((di == du) and (dj == dv))
        if 0 <= u < M and 0 <= v < N and (u, v) not in seen:
            cand = go(u, v, i, j, same + step) if same + step <= 3 else INF
            best = min(best, cand)
    seen.remove((i, j))
    return int(A[i][j]) + best

t1 = go() - int(A[0][0])
print(f'part 1: {t1}')
# part 1: 142  # 🚫 suboptimal solution 😵
