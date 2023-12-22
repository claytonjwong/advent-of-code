# 9:12am - read problem statement

# game plan:

# kinda lame to see BFS again... same old same old is getting boring, but whatever, let's jam!

# 9:14am - implementation begins
# so I need to track if the steps away from origin are evenly divisible by the number of steps
# ok write distance function and write ok function if distance is evenly divisible

# 9:25am - implementation ended a few minutes ago and automatically
#          logical reasoning + debugging begins, my count of seen is higher than expected 👻 (I see 21 but expect 16)

# 9:45am - oops, ok my ok function was incorrect, instead of taking into account even divisibility, we just need to
#          check if both are even or odd, since we could potentially hop back-and-forth an even amount of steps,
#          ie. 0,2,4,6,etc,steps away are all ok with an even amount of steps from the origin
#              1,3,5,7,etc,steps away are all ok with an odd amount of steps from the origin
# 9:47am - part 1 accpted, yay! 🙂

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
    dist = lambda i, j, u, v: abs(i - u) + abs(j - v)
    ok = lambda i, j, u, v, steps: not dist(i, j, u, v) or ((steps & 1) == (dist(i, j, u, v) & 1))  # both even or both odd
    return len([(i, j) for i, j in seen if ok(i, j, S[0], S[1], steps)])
print(f'part 1: {run(64)}')
