# 2:32pm

# from collections import deque

import sys
sys.setrecursionlimit(int(1e6))

A = []
with open('input.txt') as input:
    for line in input:
        A.append(line.strip())
M, N = len(A), len(A[0])

# S = (0, [j for j in range(N) if A[0][j] == '.'][0])
# T = (M - 1, [j for j in range(N) if A[M - 1][j] == '.'][0])

# q, seen, step = deque([S]), set([(S[0], S[1])]), 0
# while q:
#     for _ in range(len(q)):
#         i, j = q.popleft()
#         if (i, j) == T:
#             print(f'reached target in {step} steps')
#             continue
#         if A[i][j] == '.':
#             for u, v in [(i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)]:
#                 if 0 <= u < M and 0 <= v < N and A[u][v] != '#' and (u, v) not in seen:
#                     q.append((u, v)); seen.add((u, v))
#         else:
#             u, v = (i - 1, j) if A[i][j] == '^' else (i, j + 1) if A[i][j] == '>' else (i + 1, j) if A[i][j] == 'v' else (i, j - 1)
#             if 0 <= u < M and 0 <= v < N and A[u][v] != '' and (u, v) not in seen:
#                     q.append((u, v)); seen.add((u, v))
#     step += 1

# print(f'part 1: {step}')


# DFS + BT?

# 2:13pm - implementation beings
# 2:27pm - implementation ends
# no that didn't work, let's use queue instead... wait, let's come back here, I think this makes more sense now, LOL...

# 2:56pm - yay!, ok that's accepted for part 1 for ~43 minutes, oops -- oh well, looks like I took the scenic route :)

beg = (0, [j for j in range(N) if A[0][j] == '.'][0])
end = (M - 1, [j for j in range(N) if A[M - 1][j] == '.'][0])
seen = set()
def go(i = beg[0], j = beg[1], step = 0):
    k = (i, j)
    if k == end:
        return step
    if i < 0 or j < 0 or i == M or j == N or A[i][j] == '#' or k in seen:
        return 0
    seen.add(k)
    best = 0
    if   A[i][j] == '^': best = go(i - 1, j, step + 1)
    elif A[i][j] == '>': best = go(i, j + 1, step + 1)
    elif A[i][j] == 'v': best = go(i + 1, j, step + 1)
    elif A[i][j] == '<': best = go(i, j - 1, step + 1)
    else:
        for u, v in [(i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)]:
            best = max(best, go(u, v, step + 1))
    seen.remove(k)
    return best
best = go()
print(f'part 1: {best}')
