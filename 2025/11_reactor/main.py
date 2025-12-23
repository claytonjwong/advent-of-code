#
# https://adventofcode.com/2025/day/11
#

from collections import defaultdict, deque

E = defaultdict(set)  # edges
with open('input.txt') as input:
    for s in input:
        beg, ends = s.strip().split(':')
        for end in ends.split(' '):
            E[beg].add(end)

S = 'you'  # start
T = 'out'  # target
q, seen = deque([S]), set([S])
dp = defaultdict(int) # let dp[v] denote the number of ways to reach vertex v
dp[S] = 1  # there is 1 way to reach start S
while q:
    u = q.popleft()
    for v in E[u]:  # process each edge u -> v
        dp[v] += dp[u]
        if v not in seen:
            q.append(v); seen.add(v)

print(f'part 1: {dp[T]}')
