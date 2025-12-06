#
# https://adventofcode.com/2025/day/4
#

A = []
with open('input.txt') as input:
    for s in input:
        A.append(list(s))
M, N = len(A), len(A[0])

def ok(i, j):
    if A[i][j] != '@':
        return False
    cnt = 0
    for u, v in [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j + 1), (i + 1, j + 1), (i + 1, j), (i + 1, j - 1), (i, j - 1)]:
        if 0 <= u < M and 0 <= v < N and A[u][v] == '@':
            cnt += 1
    return cnt < 4

def reduce_rolls():
    cnt, found = 0, True
    while found:
        found = False
        for i in range(M):
            for j in range(N):
                if ok(i, j):
                    A[i][j] = '.'; cnt += 1; found = True
    return cnt

part1 = sum(ok(i, j) for i in range(M) for j in range(N))
part2 = reduce_rolls()

print(f'part 1: {part1}')
print(f'part 2: {part2}')

# part 1: 1389
# part 2: 9000
