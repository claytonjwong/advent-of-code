# 12:28pm - read problem statement
# 12:32pm - game plan: read input, then create the circle, then fill the circle and return area as cardinality of cells

# 12:33pm - start implementation
# 12:42pm - outer loop done

# start filling in middle -> actually let's just remove outside parts instead (ie. use inversion -> total minus outside == inside)
# i ->  <- j inwards we remove '.' until # is found

# 12:50pm => ~22 minutes for wrong answer

# 12:51pm => oops, I need to remove outside from above and below as well...

# no that was an incorrect algorithm, so instead just flood fill with DFS

# .................................................................#.

# [1, 68]

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

print(f'have: {len(have)}')
print(f'i from {lo_i}..{hi_i}')
print(f'j from {lo_j}..{hi_j}')

# .................................#

import sys
sys.setrecursionlimit(int(1e6))
def go(i = lo_i + 69, j = lo_j + 69):
    have.add((i, j))
    print(f'go({i},{j}) have: {len(have)}')
    for u, v in [(i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)]:
        if (u, v) not in have:
            go(u, v)
go()
# print(f'part 1: {inside}')
# part 1: 68624 is too high
# part 1: 24445 is too low

print(f'part 1: {len(have)}')
