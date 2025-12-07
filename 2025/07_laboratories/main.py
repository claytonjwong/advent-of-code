#
# https://adventofcode.com/2025/day/7
#

A = []
with open('input.txt') as input:
    for s in input:
        A.append(s.strip())
M, N = len(A), len(A[0])

# state

# let dp[i][j] denote the number of ways to each cell A[i][j] of the input array A
# then the cell A[0][j] == 'S' is initialized to 1, while all other cells are initialized to 0

# recurrence relation

# build each current dp[i + 1][j] from previous dp[i][j]
# note: this is the same as current dp[i][j] and previous dp[i - 1][j] -- let's use whichever makes our life more simple! remember KISS == keep it super simple

S = set()
dp = [[int(A[i][j] == 'S') for j in range(N)] for i in range(M)]  # Part 2: num ways to each cell (i,j)
for i in range(1, M):
    for j in range(N):
        if A[i][j] == '.':
            dp[i][j] += dp[i - 1][j]
        if A[i][j] == '^':
            if dp[i - 1][j]:  # Part 1: if we can reach the splitter (ie. num ways above '^' is greater than 0), then add cell (i,j) to set S
                S.add((i, j))
            if 0 <= j - 1: dp[i][j - 1] += dp[i - 1][j]  # num ways to-the-left of '^' += num ways above '^'
            if j + 1 < N: dp[i][j + 1] += dp[i - 1][j]  # num ways to-the-right of '^' += num ways above '^'

print(f'part 1: {len(S)}')
print(f'part 2: {sum(dp[M - 1])}')

# part 1: 1581
# part 2: 73007003089792
