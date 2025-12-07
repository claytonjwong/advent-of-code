# AoC 2025
* [adventofcode.com/2025](https://adventofcode.com/2025)

![](stars.png)

---

## [Day 1: Secret Entrance](https://adventofcode.com/2025/day/1)

```python
dial = 50
part1 = 0
part2 = 0
with open('input.txt') as input:
    for s in input:
        n = int(s[1:])
        dx = -1 if s[0] == 'L' else 1
        for _ in range(n):
            dial += dx
            if dial == -1: dial = 99  # wrap-around left
            if dial == 100: dial = 0  # wrap-around right
            part2 += 1 if not dial else 0
        part1 += 1 if not dial else 0
print(f'part 1: {part1}')
print(f'part 2: {part2}')

# part 1: 1071
# part 2: 6700
```

## [Day 2: Gift Shop](https://adventofcode.com/2025/day/2)

```python
A = []
with open('input.txt') as input:
    for s in input:
        intervals = s.split(',')
        for interval in intervals:
            i, j = map(int, interval.split('-'))
            A.append((i, j))
A.sort()

part1 = 0
part2 = 0
def check_invalid(x):
    global part1, part2
    s = str(x)
    n = len(s)
    found = False
    for k in range(1, n + 1):
        pattern, matches = s[:k], 0
        i = 0
        while i + k <= n and pattern == s[i:i + k]:
            i += k; matches += 1
        if i == n:
            if k == n // 2 and matches == 2:
                part1 += x
            if 1 < matches:
                part2 += x if not found else 0; found = True

[check_invalid(x) for i, j in A for x in range(i, j + 1)]
print(f'part 1: {part1}')
print(f'part 2: {part2}')

# part 1: 44854383294
# part 2: 55647141923
```

## [Day 3: Lobby](https://adventofcode.com/2025/day/3)

<details>
  <summary>👀 See Greedy Reduction Algorithm Details Here 🎯</summary>
<br/>
<p>
It is optimal to perform a reduction if there exists ANY monotonically increasing adjacent value when performing a linear scan from left-to-right, ie. it is ALWAYS beneficial to place a larger value into a more significant digit.

For example, if we have the value 89 and there is another number x to consider then it is ALWAYS optimal to reduce 89 to 9x where x is ANY value 0..9 inclusive (ie. it doesn't matter what x is in order for 89 < 9x).

Greedy reductions make sense because we AWAYS care most about the most significant digits, so we will ALWAYS perform the first reduction possible when performing a linear scan from left-to-right to greedily consume the first found monotonically increasing pair by shifting-left and popping the right-most redundant value, ie. move the larger value at position `i` into the more significant digit at position `i - 1` and "delete" the value which was overwritten at position `i - 1` by shifting-left all values from `i..K - 1` inclusive.

To make life simple, let's always append x and attempt to reduce greedily, there are two use cases to consider, either we found and perform a greedy reduction, or we don't; regardless, we will always pop from what we have:

* Case 1. if found == True, then we "delete" the value at position `i - 1` by left-shifting by one, and then we pop the right-most redundant value
* Case 2. if found == False, then we couldn't make use of x, so discard x
</p>
</details>

```python
A = []
with open('input.txt') as input:
    for s in input:
        A.append([int(c) for c in s.strip()])

def greedy_reduce(A, K):
    best = A[:K]
    for x in A[K:]:
        best.append(x); found = False
        for i in range(1, len(best)):
            if best[i - 1] < best[i] or found:
                best[i - 1] = best[i]; found = True
        best.pop()
    return int(''.join(str(x) for x in best))

part1 = sum(greedy_reduce(row, 2) for row in A)
part2 = sum(greedy_reduce(row, 12) for row in A)

print(f'part 1: {part1}')
print(f'part 2: {part2}')

# part 1: 17142
# part 2: 169935154100102
```

## [Day 4: Printing Department](https://adventofcode.com/2025/day/4)

```python
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
```

## [Day 5: Cafeteria](https://adventofcode.com/2025/day/5)

```python
from sortedcontainers import SortedDict

A = []
seen = set()
with open('input.txt') as input:
    for s in input:
        s = s.strip()
        if not len(s):
            continue
        if 0 <= s.find('-'):
            i, j = map(int, s.split('-'))
            A.append((i, j))
        else:
            seen.add(int(s))

m = SortedDict()

def merge(i, j, u, v):
    ok = lambda i, j, u, v: max(i, u) <= min(j, v)  # ok to merge intervals i..j and u..v?
    if not ok(i, j, u, v):
        return False
    if m.get(i): m.pop(i)
    if m.get(u): m.pop(u)
    m[min(i, u)] = max(j, v)
    return True

for i, j in A:
    found = True
    while found:
        found = False
        m[i] = max(j, m.get(i) or 0)
        k = m.bisect_left(i)
        for cand in [k - 1, k + 1]:  # merge candidates u..v adjacent to i..j interval insertion index k
            if 0 <= cand < len(m):
                u, v = m.peekitem(cand)
                if merge(i, j, u, v):
                    found = True
                    i = min(i, u)
                    j = max(j, v)

part1 = len([k for i, j in m.items() for k in seen if i <= k <= j])
part2 = sum(j - i + 1 for i, j in m.items())  # +1 for i..j inclusive

print(f'part 1: {part1}')
print(f'part 2: {part2}')

# part 1: 848
# part 2: 334714395325710
```

## [Day 6: Trash Compactor](https://adventofcode.com/2025/day/6)

```python
from functools import reduce

A = []
with open('input.txt') as input:
    for s in input:
        A.append(s[:-1])  # -1 to skip the newline '\n' character
M, N = len(A), len(A[0])

part1 = 0
nums = []
for row in A[:M - 1]:
    nums.append([int(num) for num in row.strip().split(' ') if len(num)])
ops = [op for op in A[M - 1].strip().split(' ') if len(op)]

for j in range(len(nums[0])):
    num = 0 if ops[j] == '+' else 1  # initialize num=0 for addition and num=1 for multiplication
    for i in range(len(nums)):
        if ops[j] == '+': num += nums[i][j]
        if ops[j] == '*': num *= nums[i][j]
    part1 += num
print(f'part 1: {part1}')

part2 = 0
num, nums, terminators = 0, [], set([' ', '+', '*'])
for j in reversed(range(N)):
    for i in range(M):
        if num and A[i][j] in terminators:
            nums.append(num); num = 0
        if A[i][j] == '+': part2 += reduce(lambda a, b: a + b, nums); nums = []
        if A[i][j] == '*': part2 += reduce(lambda a, b: a * b, nums); nums = []
        if A[i][j].isdigit(): num = 10 * num + int(A[i][j])
print(f'part 2: {part2}')

# part 1: 4076006202939
# part 2: 7903168391557
```

## [Day 7: Laboratories](https://adventofcode.com/2025/day/7)

```python
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
print(f'part 2: {sum(dp[M - 2])}')

# part 1: 1581
# part 2: 73007003089792
```
