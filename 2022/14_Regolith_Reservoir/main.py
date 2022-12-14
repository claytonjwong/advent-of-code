#
# https://adventofcode.com/2022/day/14
#

seen = set()
with open('input.txt') as input:
    for line in input:
        P = [[int(x) for x in pair.split(',')][::-1] for pair in line.strip().split(' -> ')]
        for k in range(1, len(P)):
            i, j = P[k - 1]
            u, v = P[k]
            di = 1 if i < u else -1 if u < i else 0
            dj = 1 if j < v else -1 if v < j else 0
            seen.add((i, j))
            while not (i == u and j == v):
                i += di
                j += dj
                seen.add((i, j))
rock = len(seen)
last = max(i for i, _ in seen)

def drop(end, limit, start = (0, 500)):
    i, j = start
    next = lambda i, j: [(i + 1, j), (i + 1, j - 1), (i + 1, j + 1)]
    D, L, R = next(i, j)
    while i < end and not (D in seen and L in seen and R in seen):
        if D not in seen: i += 1
        elif L not in seen: i += 1; j -= 1
        elif R not in seen: i += 1; j += 1
        D, L, R = next(i, j)
    if (i < end and not limit) or (limit and start not in seen):
        seen.add((i, j))
        return True
    return False

def run(end, limit):
    while drop(end, limit):
        pass
    return len(seen) - rock

print(f'part 1: {run(last, False)}')
print(f'part 2: {run(last + 1, True)}')
# part 1: 625
# part 2: 25193