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
        x = int(s[1:])
        dx = -1 if s[0] == 'L' else 1
        while x:
            dial += dx; x -= 1
            if dial == 100:
                dial = 0
            if dial == -1:
                dial = 99
            if not dial:
                part2 += 1
        if not dial:
            part1 += 1
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