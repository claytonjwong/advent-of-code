import copy, functools, operator

A = []
with open('input.txt') as input:
    for line in input:
        A.append(line.strip())
M, N, adj = len(A), len(A[0]), lambda i, j: [(u, v) for u, v in [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j + 1), (i + 1, j + 1), (i + 1, j), (i + 1, j - 1), (i, j - 1)] if 0 <= u < M and 0 <= v < N]

class Number:
    def __init__(self):
        self.val = 0; self.cells = set()
    ok = lambda self: any(not A[u][v].isdigit() and A[u][v] != '.' for i, j in self.cells for u, v in adj(i, j))

last, nums = Number(), []
for i in range(M):
    for j in range(N):
        if A[i][j].isdigit():
            last.val = 10 * last.val + int(A[i][j]); last.cells.add((i, j))
        else:
            nums.append(copy.deepcopy(last)); last = Number()
t1 = sum(num.val for num in nums if num.ok())

t2, gear = 0, [(i, j) for i in range(M) for j in range(N) if A[i][j] == '*']
for i, j in gear:
    take = set(num for u, v in adj(i, j) if A[u][v].isdigit() for num in nums if (u, v) in num.cells)
    if len(take) == 2:
        t2 += functools.reduce(operator.mul, [num.val for num in take])

print(f'part 1: {t1}')
print(f'part 2: {t2}')
# part 1: 539713
# part 2: 84159075
