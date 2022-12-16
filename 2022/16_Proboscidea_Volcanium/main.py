#
# https://adventofcode.com/2022/day/16
#

from collections import defaultdict

adj, flow = defaultdict(set), defaultdict(int)
with open('input.txt') as input:
    for line in input:
        A = line.strip().split(' ')
        u, w = A[1], int(A[4].split('=')[1][:-1])
        flow[u] = w
        for v in ''.join(A[9:]).split(','):
            adj[u].add(v)
            adj[v].add(u)

best, T = 0, 30
q, seen = [(1, 'AA', 0, ('ZZZ',))], {}
while len(q):
    time, u, score, opened = q.pop()
    open = set([x for x in opened])
    if (time, u) in seen and score <= seen[(time, u)]:
        continue
    seen[(time, u)] = score
    if time == T:
        best = max(best, score)
        continue
    # ✅ include u
    if 0 < flow[u] and u not in open:
        open.add(u)
        new_score = score + sum(flow[x] for x in open)
        new_state = (time + 1, u, new_score, tuple(open))
        q.append(new_state)
        open.discard(u)
    # 🚫 exclude u
    new_score = score + sum(flow[x] for x in open)
    for v in adj[u]:
        new_state = (time + 1, v, new_score, tuple(open))
        q.append(new_state)

print(f'part 1: {best}')
# part 1: 1651