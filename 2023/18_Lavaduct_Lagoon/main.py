import sys
sys.setrecursionlimit(int(1e6))

i, j = 0, 0
have, first = set([(0, 0)]), True
with open('input.txt') as input:
    for line in input:
        d, cnt, color = line.split(); cnt = int(cnt)
        if first:
            cnt -= 1; first = False
        di, dj = (-1, 0) if d == 'U' else (1, 0) if d == 'D' else (0, -1) if d == 'L' else (0, 1)
        for _ in range(cnt):
            i += di
            j += dj
            have.add((i, j))
lo_i, hi_i = min(i for i, _ in have), max(i for i, _ in have)
lo_j, hi_j = min(j for _, j in have), max(j for _, j in have)

def go(i = lo_i + 69, j = lo_j + 69):
    if (i, j) in have:
        return
    have.add((i, j))
    print(f'go({i},{j}) have: {len(have)}')
    for u, v in [(i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)]:
        go(u, v)
go()
print(f'part 1: {len(have)}')
# part 1: 47045
