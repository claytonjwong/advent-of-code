import copy, functools, operator

A = []
with open('input.txt') as input:
    for line in input:
        A.append(line.strip())
M, N = len(A), len(A[0])

class Number:
    def __init__(self):
        self.val = 0
        self.cells = set()
    def ok(self):
        for i, j in self.cells:
            for u, v in [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j + 1), (i + 1, j + 1), (i + 1, j), (i + 1, j - 1), (i, j - 1)]:
                if 0 <= u < M and 0 <= v < N and not A[u][v].isdigit() and A[u][v] != '.':
                    return True
        return False

last, nums, gears = Number(), [], []
for i in range(M):
    for j in range(N):
        if A[i][j].isdigit():
            last.val = 10 * last.val + int(A[i][j])
            last.cells.add((i, j))
        else:
            nums.append(copy.deepcopy(last))
            last = Number()
            if A[i][j] == '*':
                gears.append((i, j))

t1 = sum(num.val for num in nums if num.ok())
t2 = 0
for i, j in gears:
    take = set()
    for u, v in [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j + 1), (i + 1, j + 1), (i + 1, j), (i + 1, j - 1), (i, j - 1)]:
        if 0 <= u < M and 0 <= v < N and A[u][v].isdigit():
            for num in nums:
                if (u, v) in num.cells:
                    take.add(num)
    if len(take) == 2:
        t2 += functools.reduce(operator.mul, [num.val for num in take])

print(f'part 1: {t1}')
print(f'part 2: {t2}')
# part 1: 539713
# part 2: 84159075
