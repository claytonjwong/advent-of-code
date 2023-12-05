# AoC 2023
* [adventofcode.com/2023](https://adventofcode.com/2023)

---

## [Day 1: Trebuchet?!](https://adventofcode.com/2023/day/1)
* [🎨 YouTube ScreenShare 👀](https://www.youtube.com/watch?v=PWZwvm19qoQ)

```python
#
# part 1
#

def f(s, reverse = False):
    n = len(s)
    for i in reversed(range(n)) if reverse else range(n):
        if s[i].isdigit():
            return int(s[i])
    return -1

t = 0
with open('input.txt') as input:
    for s in input:
        beg, end = f(s), f(s, True)
        t += int(f'{beg}{end}')
print(f'part 1: {t}')


#
# part 2
#

def f(s, reverse = False):
    m = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    n = len(s)
    for i in reversed(range(n)) if reverse else range(n):
        if s[i].isdigit():
            return int(s[i])
        for k in m.keys():
            if i + len(k) <= n and s[i:i+len(k)] == k:
                return m[k]
    return -1

t = 0
with open('input.txt') as input:
    for s in input:
        beg, end = f(s), f(s, True)
        t += int(f'{beg}{end}')
print(f'part 2: {t}')
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
