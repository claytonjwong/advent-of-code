A = []
with open('/Users/claytonjwong/sandbox/advent-of-code/2023/11_Cosmic_Expansion/input.txt') as input:
    for line in input:
        A.append(line.strip())
M, N = len(A), len(A[0])

row, col = [], []
V = set((i, j) for i in range(M) for j in range(N) if A[i][j] == '#')
for u in V:
    for v in V:
        i, j = u
        di = 1 if u[0] < v[0] else -1 if v[0] < u[0] else 0
        dj = 1 if u[1] < v[1] else -1 if v[1] < u[1] else 0
        while i != v[0] or j != v[1]:
            if i != v[0]: i += di; row.append(i)
            if j != v[1]: j += dj; col.append(j)

cost1 = int(2e0)
cost2 = int(1e6)
SPACE_ROW = set(i for i in range(M) if all(c == '.' for j in range(N) for c in A[i][j]))
SPACE_COL = set(j for j in range(N) if all(c == '.' for i in range(M) for c in A[i][j]))
t1 = sum(cost1 if i in SPACE_ROW else 1 for i in row) + sum(cost1 if j in SPACE_COL else 1 for j in col)
t2 = sum(cost2 if i in SPACE_ROW else 1 for i in row) + sum(cost2 if j in SPACE_COL else 1 for j in col)
print(f'part 1: {t1 // 2}')
print(f'part 2: {t2 // 2}')
# part 1: 9608724
# part 2: 904633799472
