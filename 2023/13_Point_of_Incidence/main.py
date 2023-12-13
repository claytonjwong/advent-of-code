# 3:22pm - part 2
# 3:28pm - 3621957 is too high

matrix = []
with open('input.txt') as input:
    A = []
    for line in input:
        if line == '\n':
            matrix.append(A[:]); A = []
        else:
            A.append(list(line.strip()))
if len(A):
    matrix.append(A[:])

def row(A):
    M = len(A)
    for i in range(1, M):
        u = i - 1  # 👍 up
        d = i      # 👎 down
        while 0 <= u and d < M and A[u] == A[d]:
            u -= 1
            d += 1
        if u == -1 or d == M:
            return i
    return 0

rotate = lambda A: [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))][::-1]  # rotate 90 degrees counterclockwise == reversed(transposed(A))
def col(A):
    N = len(A[0])
    j = row(rotate(A))
    return N - j if j else 0

rows1 = sum(row(A) for A in matrix)
cols1 = sum(col(A) for A in matrix)

print(f'part 1: {100 * rows1 + cols1}')
# part 1: 32371
