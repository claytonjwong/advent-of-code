#
# https://adventofcode.com/2022/day/20
#

A = []
with open('input.txt') as input:
    for line in input:
        A.append(int(line))
N = len(A)

def mix(A, cnt = 1, key = 1):
    A = [x * key for x in A]
    I = [i for i in range(N)]
    for _ in range(cnt):
        for i, steps in enumerate(A):
            if not steps:
                continue
            j = I.index(i)
            k = (j + steps) % (N - 1)
            l = I.pop(j)
            I.insert(k, l)
    return [A[i] for i in I]

def run(A, cnt = 1, key = 1):
    A = mix(A, cnt, key)
    i = A.index(0)
    return sum(A[(i + k) % N] for k in range(3000 + 1) if k in [1000, 2000, 3000])

print(f'part 1: {run(A[:])}')
print(f'part 2: {run(A[:], 10, 811589153)}')
# part 1: 3346
# part 2: 4265712588168