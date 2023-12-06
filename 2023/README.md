# AoC 2023
* [adventofcode.com/2023](https://adventofcode.com/2023)

---

## [Day 1: Trebuchet?!](https://adventofcode.com/2023/day/1)
* [🎨 YouTube ScreenShare 👀](https://www.youtube.com/watch?v=PWZwvm19qoQ)

```python
t1 = 0
t2 = 0
with open('input.txt') as input:
    m1 = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    m2 = m1 | {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    for s in input:
        d1 = []
        d2 = []
        for i in range(len(s)):
            for k in range(1, len(s) + 1 - i):
                it = s[i:i + k]
                if it in m1: d1.append(m1[it])
                if it in m2: d2.append(m2[it])
        t1 += int(f'{d1[0]}{d1[-1]}')
        t2 += int(f'{d2[0]}{d2[-1]}')
print(f'part 1: {t1}')
print(f'part 2: {t2}')
# part 1: 55017
# part 2: 53539
```

---

## [Day 2: Cube Conundrum](https://adventofcode.com/2023/day/2)

* [🎨 YouTube ScreenShare 👀](https://www.youtube.com/watch?v=upnpeBNr7p0)

```python
from collections import Counter

def needs(subset):
    need = Counter()
    for group in subset.split(','):
        cnt, color = group.split()
        need[color] = int(cnt)
    return need

t1, t2 = 0, 0
with open('input.txt') as input:
    for line in input:
        game, values = line.split(':')
        num = int(game.split()[1])
        subsets, ok = values.split(';'), True
        r, g, b = 1, 1, 1
        for subset in subsets:
            need = needs(subset)
            ok = ok and need['red'] <= 12 and need['green'] <= 13 and need['blue'] <= 14
            r, g, b = max(r, need['red']), max(g, need['green']), max(b, need['blue'])
        t1 += num if ok else 0
        t2 += r * g * b

print(f'part 1: {t1}')
print(f'part 2: {t2}')
# part 1: 3059
# part 2: 65371
```

---

## [Day 3: Gear Ratios](https://adventofcode.com/2023/day/3)

* [🎨 YouTube ScreenShare 👀](https://www.youtube.com/watch?v=0c697p_l3_g)

```python
import copy, functools, operator

A = []
with open('input.txt') as input:
    for line in input:
        A.append(line.strip())
M, N, adj = len(A), len(A[0]), lambda i, j: [(u, v) for u, v in [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j + 1), (i + 1, j + 1), (i + 1, j), (i + 1, j - 1), (i, j - 1)] if 0 <= u < M and 0 <= v < N]

class Number:
    def __init__(self):
        self.val = 0; self.cells = set()
    ok = lambda self: any(not A[u][v].isdigit() and A[u][v] != '.' for i, j in self.cells for u, v in adj(i, j))

last, nums = Number(), []
for i in range(M):
    for j in range(N):
        if A[i][j].isdigit():
            last.val = 10 * last.val + int(A[i][j]); last.cells.add((i, j))
        else:
            nums.append(copy.deepcopy(last)); last = Number()
t1 = sum(num.val for num in nums if num.ok())

t2, gear = 0, [(i, j) for i in range(M) for j in range(N) if A[i][j] == '*']
for i, j in gear:
    take = set(num for u, v in adj(i, j) if A[u][v].isdigit() for num in nums if (u, v) in num.cells)
    if len(take) == 2:
        t2 += functools.reduce(operator.mul, [num.val for num in take])

print(f'part 1: {t1}')
print(f'part 2: {t2}')
# part 1: 539713
# part 2: 84159075
```

---

## [Day 4: Scratchcards](https://adventofcode.com/2023/day/4)

* [🎨 YouTube ScreenShare 👀](https://www.youtube.com/watch?v=PDMwycgQ9uo)

```python
from collections import Counter

t1 = 0
cnt, hi = Counter(), 0
with open('input.txt') as input:
    for line in input:
        L, R = line.strip().split('|')
        card = int([s for s in L.split(':')[0].split()][1]); cnt[card] += 1; hi = max(hi, card)
        need = set(int(s) for s in L.split(':')[1].split())
        have = set(int(s) for s in R.split())
        same = len(need & have)
        t1 += 1 << same - 1 if same else 0
        for i in range(same):
            take = card + i + 1
            cnt[take] += cnt[card]
t2 = sum(freq for card, freq in cnt.items() if card <= hi)

print(f'part 1: {t1}')
print(f'part 2: {t2}')
# part 1: 25571
# part 2: 8805731
```

---

## [Day 5: If You Give A Seed A Fertilizer](https://adventofcode.com/2023/day/5)

* [🎨 YouTube ScreenShare 👀](https://www.youtube.com/watch?v=kyng4JvDpXA)

```python
S1, S2 = [], []  # seeds for part 1 and part 2
soil = []
fert = []
water = []
light = []
temp = []
humid = []
place = []
A = None
with open('input.txt') as input:
    for line in input:
        line = line.strip()
        if not len(line):
            continue
        if line.startswith('seeds:'):
            _, values = line.split(':')
            for s in values.split():
                S1.append(int(s))
            for i in range(1, len(values), 2):
                S2.append((values[i - 1], values[i - 1] + values[i]))
        elif line.startswith('seed-to-soil map:'): A = soil
        elif line.startswith('soil-to-fertilizer map:'): A = fert
        elif line.startswith('fertilizer-to-water map:'): A = water
        elif line.startswith('water-to-light map:'): A = light
        elif line.startswith('light-to-temperature map:'): A = temp
        elif line.startswith('temperature-to-humidity map:'): A = humid
        elif line.startswith('humidity-to-location map:'): A = place
        else:
            dst, src, size = [int(s) for s in line.split()]
            offset = dst - src
            beg, end = src, src + size
            A.append((beg, end, offset))

def go(A, x):
    for beg, end, offset in A:
        if beg <= x < end:
            return x + offset
    return x

def f(x):
    x = go(soil, x)
    x = go(fert, x)
    x = go(water, x)
    x = go(light, x)
    x = go(temp, x)
    x = go(humid, x)
    x = go(place, x)
    return x

cand = [f(x) for x in S1]
best = min(cand)
print(f'part 1: {best}')
# part 1: 388071289

cand = [f(x) for x in range(beg, end) for beg, end in S2]
best = min(cand)
print(f'part 2: {best}')
# part 2: question -- how to find minimum in a reasonable amount of time?
# TODO: I think it's obvious, we must use overlapping intervals instead of trying hundreds of millions of different seeds!
```

---

## [Day 6: Wait For It](https://adventofcode.com/2023/day/6)

* [🎨 YouTube ScreenShare 👀](https://www.youtube.com/watch?v=51nP8lQuaL4)

```python
import operator
from functools import reduce

T, D = [], []  # time and distance
wins = []
with open('input.txt') as input:
    for time, dist in zip(input, input):
        for t in time.split(':')[1].split(): T.append(int(t))
        for d in dist.split(':')[1].split(): D.append(int(d))
    for t, d in zip(T, D):
        wins.append(len([x for x in range(1, t) if d < x * (t - x)]))
print(wins)
part1 = reduce(operator.mul, wins)

print(f'part 1: {part1}')
# part 1: 503424

# TODO: for part 2 we will try binary search to find the point where we start succeeding
# FFFFFFFTTTTTTTTTTTTFFFFFFFFF
# goal   ^   👈 use binary search to find this point which we use to derive the answer for part2
#        ^^^^^^^^^^^  symmetric bell curve for TRUE
```
