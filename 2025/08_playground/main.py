#
# https://adventofcode.com/2025/day/8
#

from collections import Counter
from heapq import heappop, heappush
from functools import reduce

A = []
with open('input.txt') as input:
    for s in input:
        x, y, z = map(int, s.strip().split(','))
        A.append((x, y, z))
N = len(A)

P = [i for i in range(N)]  # track parent representatives of N-disjoint sets

def find(x):
    if P[x] != x:
        P[x] = find(P[x])
    return P[x]

def union(a, b):
    a = find(a)
    b = find(b)
    P[a] = b  # 🎲 arbitrary choice
    return a != b

def connected_components():
    for i in range(N):
        find(i)
    return len(set(P))

def distances():
    distance = lambda i, j: (A[i][0] - A[j][0]) ** 2 + (A[i][1] - A[j][1]) ** 2 + (A[i][2] - A[j][2]) ** 2
    q = []
    for i in range(N):
        for j in range(i + 1, N):
            dist = distance(i, j)
            heappush(q, (dist, i, j))
    return q

q = distances()
for _ in range(1000):
    _, i, j = heappop(q)
    union(i, j)
for i in range(N):
    find(i)
top3 = lambda: reduce(lambda a, b: a * b, sorted(Counter(P).values())[-3:])
print(f'part 1: {top3()}')

while 1 < connected_components():
    _, i, j = heappop(q)
    union(i, j)
print(f'part 2: {A[i][0] * A[j][0]}')

# part 1: 103488
# part 2: 8759985540
