A = []
with open('./input.txt') as input:
    A = [line.strip() for line in input]
M = len(A)
N = len(A[0])

def traverse(down = 1, right = 3):
    cnt = 0
    i = 0
    j = 0
    while i < M:
        if A[i][j] == '#':
            cnt += 1
        i += down
        j += right; j %= N
    return cnt

print(f'Part 1: {traverse()}')
print(f'Part 2: {traverse(1, 1) * traverse(1, 3) * traverse(1, 5) * traverse(1, 7) * traverse(2, 1)}')

# Part 1: 232
# Part 2: 3952291680
