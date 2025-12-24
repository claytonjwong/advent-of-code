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
            part2 += int(dial == 0)
        part1 += int(dial == 0)
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
            if dp[i - 1][j]:  # Part 1: if we can reach the splitter (ie. num ways above '^' is strictly greater-than 0), then add cell (i,j) to set S
                S.add((i, j))
            if 0 <= j - 1: dp[i][j - 1] += dp[i - 1][j]  # num ways to-the-left of '^' += num ways above '^'
            if j + 1 < N: dp[i][j + 1] += dp[i - 1][j]  # num ways to-the-right of '^' += num ways above '^'

print(f'part 1: {len(S)}')
print(f'part 2: {sum(dp[M - 1])}')

# part 1: 1581
# part 2: 73007003089792
```

## [Day 8: Playground](https://adventofcode.com/2025/day/8)

```python
from collections import Counter
from heapq import heappop, heappush
from functools import reduce

A = []
with open('input.txt') as input:
    for s in input:
        x, y, z = map(int, s.strip().split(','))
        A.append((x, y, z))
N = len(A)

P = [i for i in range(N)]  # track parent representatives of N-disjoint sets

def find(x):
    if P[x] != x:
        P[x] = find(P[x])
    return P[x]

def union(a, b):
    a = find(a)
    b = find(b)
    P[a] = b  # 🎲 arbitrary choice
    return a != b

def connected_components():
    for i in range(N):
        find(i)
    return len(set(P))

def distances():
    distance = lambda i, j: (A[i][0] - A[j][0]) ** 2 + (A[i][1] - A[j][1]) ** 2 + (A[i][2] - A[j][2]) ** 2
    q = []
    for i in range(N):
        for j in range(i + 1, N):
            dist = distance(i, j)
            heappush(q, (dist, i, j))
    return q

q = distances()
for _ in range(1000):
    _, i, j = heappop(q)
    union(i, j)
for i in range(N):
    find(i)
top3 = lambda: reduce(lambda a, b: a * b, sorted(Counter(P).values())[-3:])
print(f'part 1: {top3()}')

while 1 < connected_components():
    _, i, j = heappop(q)
    union(i, j)
print(f'part 2: {A[i][0] * A[j][0]}')

# part 1: 103488
# part 2: 8759985540
```

## [Day 9: Movie Theater](https://adventofcode.com/2025/day/9)

```python
from collections import deque

P = []  # points
with open('input.txt') as input:
    for s in input:
        x, y = map(int, s.strip().split(','))
        P.append((y, x))  # transpose matrix

area = lambda x1, y1, x2, y2: (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)  # +1 for endpoints inclusive

part1 = 0
for i in range(len(P)):
    for j in range(i + 1, len(P)):
        x1, y1 = P[i]
        x2, y2 = P[j]
        part1 = max(part1, area(x1, y1, x2, y2))
print(f'part 1: {part1}')

#
# traverse points by following them sequentially from P[0]..P[N-1] and then back to P[0] to wrap-around to the first point
#
def traverse(P):
    x, y = P[0]
    seen = set([(x, y)])
    for next_x, next_y in P + [P[0]]:  # + [P[0]] to wrap-around to the first point at the end
        dx = 1 if x < next_x else 0 if x == next_x else -1
        dy = 1 if y < next_y else 0 if y == next_y else -1
        while x != next_x or y != next_y:
            x += dx
            y += dy
            seen.add((x, y))
    return seen

I = traverse(P)  # inside

# return True if-and-only-if point (x,y) is an adjacent to a point inside
adjacent = lambda x, y: any((u, v) in I for u, v in [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y + 1), (x + 1, y + 1), (x + 1, y), (x + 1, y - 1), (x, y - 1)])

#
# the outside points "surround" the inside points via BFS
#
x, y = sorted(P)[0]
q = deque([(x - 1, y - 1)])  # -1 for top-left outside
O = set([(x - 1, y - 1)])  # outside
while q:
    x, y = q.popleft()
    for u, v in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:
        if (u, v) not in I and (u, v) not in O and adjacent(u, v):
            q.append((u, v)); O.add((u, v))

#
# consider all rectangles with sides that do NOT have any points in common with any outside points
#
part2 = 0
for i in range(len(P)):
    for j in range(i + 1, len(P)):
        x1, y1 = P[i]
        x2, y2 = P[j]
        ok =    not any((x, y1) in O or (x, y2) in O for x in range(min(x1, x2), max(x1, x2) + 1)) \
            and not any((x1, y) in O or (x2, y) in O for y in range(min(y1, y2), max(y1, y2) + 1))
        if ok:  # ok if there is no intersection between the rectangle sides and outside points
            part2 = max(part2, area(x1, y1, x2, y2))
print(f'part 2: {part2}')

# part 1: 4777816465
# part 2: 1410501884
```

## [Day 10: Factory](https://adventofcode.com/2025/day/10)
```python
from collections import deque
from z3 import *

class Machine:
    def __init__(self, lights, buttons, joltages):
        self.lights = lights
        self.buttons = buttons
        self.joltages = joltages

    def __repr__(self):
        return f'Machine(\n  lights: {self.lights}\n  buttons: {self.buttons}\n  joltages: {self.joltages})'

    def toggle_lights(self):
        key = lambda state: ','.join(str(x) for x in state)
        start, finish = [0] * len(self.lights), self.lights  # start with all OFF
        q, seen, depth = deque([start]), set([key(start)]), 0
        while q:
            k = len(q)
            for _ in range(k):
                cur = q.popleft()
                if key(cur) == key(finish):
                    return depth
                for toggles in self.buttons:
                    next = [x ^ int(i in toggles) for i, x in enumerate(cur)]
                    if key(next) not in seen:
                        q.append(next); seen.add(key(next))
            depth += 1
        return -1

    def config_joltage(self):
        opt = Optimize()
        vars = [Int('b' + ''.join(str(x) for x in nums)) for nums in self.buttons]  # button press variables
        for var in vars:
            opt.add(0 <= var)  # button press variables must be greater-than-or-equal-to 0
        for i, target in enumerate(self.joltages):
            parts = set(vars[j] for j in range(len(self.buttons)) if i in self.buttons[j])
            opt.add(Sum(parts) == target)  # sum of button press variable participants must equal target
        total_presses = Sum(vars)
        opt.minimize(total_presses)
        return opt.model().evaluate(total_presses).as_long() if opt.check() == sat else 0

A = []
with open('input.txt') as input:
    for s in input:
        lights = []
        buttons = []
        joltages = []
        for token in s.strip().split(' '):
            if token[0] == '[': lights = [1 if c == '#' else 0 for c in token[1:-1]]
            if token[0] == '(': buttons.append([int(x) for x in token[1:-1].split(',')])
            if token[0] == '{': joltages = [int(x) for x in token[1:-1].split(',')]
        A.append(Machine(lights, buttons, joltages))

part1 = sum(it.toggle_lights() for it in A)
part2 = sum(it.config_joltage() for it in A)
print(f'part 1: {part1}')
print(f'part 2: {part2}')

# part 1: 512
# part 2: 19857
```

## [Day 11: Reactor](https://adventofcode.com/2025/day/11)

```python
from collections import defaultdict
from functools import cache

E = defaultdict(set)  # edges
with open('input.txt') as input:
    for s in input:
        beg, ends = s.strip().split(':')
        for end in ends.split(' '):
            E[beg].add(end)

@cache
def go(u, target):
    return 1 if u == target else sum(go(v, target) for v in E[u])

part1 = go('you', 'out')
print(f'part 1: {part1}')

part2 = go('svr', 'fft') \
      * go('fft', 'dac') \
      * go('dac', 'out')
print(f'part 2: {part2}')

# part 1: 466
# part 2: 549705036748518
```

## [Day 12: Christmas Tree Farm](https://adventofcode.com/2025/day/12)

```python
from collections import defaultdict

cnt = defaultdict(int)
puzzles = []
with open('input.txt') as input:
    text = input.read()
    chunks = text.split('\n\n')
    for chunk in chunks:
        lines = chunk.splitlines()
        if lines[0].endswith(':'):  # shape
            id = int(lines[0][:-1])
            cnt[id] = sum(int(c == '#') for line in lines for c in line)  # shape id '#' count
        else:  # puzzles
            for line in lines:
                dims, ids = line.split(':')  # dimensions MxN and list of shape ids
                M, N = map(int, dims.split('x'))
                ids = list(map(int, ids.split()))
                puzzles.append((M, N, ids))

part1 = 0
ratio = 1.2  # suboptimal packing overhead per count of '#' in each shape, ie. ratio == 1.0 if we can perfectly pack
for puzzle in puzzles:
    M, N, ids = puzzle
    have = M * N
    need = ratio * sum(cnt[id] * quantity for id, quantity in enumerate(ids))
    part1 += int(need <= have)  # do we have what we need?
print(f'part 1: {part1}')
# part 1: 406
```
