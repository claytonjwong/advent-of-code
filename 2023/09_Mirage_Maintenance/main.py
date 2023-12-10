from collections import deque

t1 = 0
t2 = 0
with open('input.txt') as input:
    for line in input:
        A = [deque([int(s) for s in line.split()])]
        while not all([not x for x in A[-1]]):
            A.append(deque([A[-1][i] - A[-1][i - 1] for i in range(1, len(A[-1]))]))
        for i in reversed(range(len(A) - 1)):
            A[i].appendleft(A[i][0] - A[i + 1][0])
        t1 += sum(row[-1] for row in A)
        t2 += A[0][0]

print(f'part 1: {t1}')
print(f'part 2: {t2}')
# part 1: 1955513104
# part 2: 1131
