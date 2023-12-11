A = []
with open('/Users/claytonjwong/sandbox/advent-of-code/2023/11_Cosmic_Expansion/input.txt') as input:
    for line in input:
        A.append(line.strip())
M, N = len(A), len(A[0])
row = set(i for i in range(M) if all(c == '.' for j in range(N) for c in A[i][j]))
col = set(j for j in range(N) if all(c == '.' for i in range(M) for c in A[i][j]))
cost = int(1e6)
# cost = 2

t = 0
V = set((i, j) for i in range(M) for j in range(N) if A[i][j] == '#')
for u in V:
    for v in V:
        if u == v:
            continue
        di = 1 if u[0] < v[0] else -1 if v[0] < u[0] else 0
        dj = 1 if u[1] < v[1] else -1 if v[1] < u[1] else 0
        i, j = u
        while i != v[0] or j != v[1]:
            if i != v[0]:
                i += di
                # print(f'i: {i}')
                # if i in row:
                #     print(f'i: {i} in row')
                t += cost if i in row else 1
            if j != v[1]:
                j += dj
                # print(f'j: {j}')
                # if j in col:
                #     print(f'j: {j} in col')
                t += cost if j in col else 1
        # t += sum(cost if i in row else 1 for i in range(min(u[0], v[0]), max(u[0], v[0]) + 1))
        # t += sum(cost if j in col else 1 for j in range(min(u[1], v[1]), max(u[1], v[1]) + 1))
print(t)

print(f'part 1: {t // 2}')  # divide by 2 since edges are bidirectional
# part 1: 9608724
# part 2: 904633799472