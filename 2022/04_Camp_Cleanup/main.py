#
# https://adventofcode.com/2022/day/4
#

t1, t2 = 0, 0
with open('input.txt') as input:
    for line in input:
        line = line.strip()
        A, B = line.split(',')
        i, j = [int(x) for x in A.split('-')]
        u, v = [int(x) for x in B.split('-')]
        t1 += (i <= u and v <= j) or (u <= i and j <= v)
        t2 += not (j < u) and not (v < i) # ⭐️ inversion: p is true if not p is impossible, ie. if i..j is not before inclusive-or not after u..v, then i..j and u..v must overlap
print(f'part 1: {t1}')
print(f'part 2: {t2}')
# part 1: 459
# part 2: 779