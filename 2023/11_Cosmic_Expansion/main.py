text = []
with open('input.txt') as input:
    for line in input:
        text.append(line.strip())
m, n = len(text), len(text[0])
row = set(i for i in range(m) if all(c == '.' for j in range(n) for c in text[i][j]))
col = set(j for j in range(n) if all(c == '.' for i in range(m) for c in text[i][j]))
M, N = m + len(row), n + len(col)
A = [['.'] * N for _ in range(M)]

u = 0
for i in range(m):
    v = 0
    for j in range(n):
        if text[i][j] == '#':
            A[u][v] = '#'
        v += 1 + int(j in col)
    u += 1 + int(i in row)

t = 0
V = set((i, j) for i in range(M) for j in range(N) if A[i][j] == '#')
for u in V:
    for v in V:
        if u == v:
            continue
        t += abs(u[0] - v[0]) + abs(u[1] - v[1])  # manhattan distance from u -> v
print(f'part 1: {t // 2}')  # divide by 2 since edges are bidirectional
# part 1: 9608724
