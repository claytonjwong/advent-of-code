#
# https://adventofcode.com/2025/day/5
#

from sortedcontainers import SortedDict

A = []
seen = set()
with open('input.txt') as input:
    for s in input:
        s = s.strip()
        if not len(s):
            continue
        if 0 <= s.find('-'):
            i, j = map(int, s.split('-'))
            A.append((i, j))
        else:
            seen.add(int(s))

m = SortedDict()

def merge(i, j, u, v):
    ok = lambda i, j, u, v: max(i, u) <= min(j, v)  # ok to merge intervals i..j and u..v?
    if not ok(i, j, u, v):
        return False
    if m.get(i): m.pop(i)
    if m.get(u): m.pop(u)
    m[min(i, u)] = max(j, v)
    return True

for i, j in A:
    found = True
    while found:
        found = False
        m[i] = max(j, m.get(i) or 0)
        k = m.bisect_left(i)
        for cand in [k - 1, k + 1]:  # merge candidates u..v adjacent to i..j interval insertion index k
            if 0 <= cand < len(m):
                u, v = m.peekitem(cand)
                if merge(i, j, u, v):
                    found = True
                    i = min(i, u)
                    j = max(j, v)

part1 = len([k for i, j in m.items() for k in seen if i <= k <= j])
part2 = sum(j - i + 1 for i, j in m.items())  # +1 for i..j inclusive

print(f'part 1: {part1}')
print(f'part 2: {part2}')

# part 1: 848
# part 2: 334714395325710
