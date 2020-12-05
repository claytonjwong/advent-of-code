# AoC 2020
* [adventofcode.com/2020](https://adventofcode.com/2020)

## [Day 1: Report Repair](https://adventofcode.com/2020/day/1)

```python
A = []
with open('./input.txt') as input:
    A = [int(line.strip()) for line in input]

def sum2(exclude = -1, t = 2020, seen = set()):
    for i, x in enumerate(A):
        if i == exclude:
            continue
        y = t - x
        if y in seen:
            return x * y
        seen.add(x)
    return -1

def sum3(t = 2020):
    for i, x in enumerate(A):
        y = t - x
        z = sum2(i, y)
        if z != -1:
            return x * z
    return -1

print(f'Part 1: {sum2()}')  # Part 1: 1006875
print(f'Part 2: {sum3()}')  # Part 2: 165026160 
```

## [Day 2: Password Philosophy](https://adventofcode.com/2020/day/2)

```python
from collections import Counter

A = []
with open('./input.txt') as input:
    A = [line.strip() for line in input]

one = 0
two = 0
for range, ch, word in [line.split(' ') for line in A]:
    lo, hi = map(int, range.split('-'))
    ch = ch[0]  # ignore ':'
    m = Counter(word)
    if ch in m and lo <= m[ch] <= hi:
        one += 1
    if (lo <= len(word) and ch == word[lo - 1]) ^ (hi <= len(word) and ch == word[hi - 1]):
        two += 1
print(f'Part 1: {one}')  # Part 1: 460
print(f'Part 2: {two}')  # Part 2: 251
```

## [Day 3: Toboggan Trajectory](https://adventofcode.com/2020/day/3)

```python
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
```

## [Day 4: Passport Processing](https://adventofcode.com/2020/day/4)

```python
import re

A = []
with open('./input.txt') as input:
    A = [line.strip() for line in input]
A.append('')  # sentinel delimiter

m = {}
one = 0
two = 0
ok1 = lambda m: 'byr' in m and 'iyr' in m and 'eyr' in m and 'hgt' in m and 'hcl' in m and 'ecl' in m and 'pid' in m
byr = lambda m: 'byr' in m and 1920 <= int(m['byr']) <= 2002
iyr = lambda m: 'iyr' in m and 2010 <= int(m['iyr']) <= 2020
eyr = lambda m: 'eyr' in m and 2020 <= int(m['eyr']) <= 2030
def hgt(m):
    if not 'hgt' in m:
        return False
    height = m['hgt']
    val = height[:-2]
    unit = height[-2:]
    if unit == 'cm': return 150 <= int(val) <= 193
    if unit == 'in': return 59 <= int(val) <= 76
    return False
def hcl(m):
    if not 'hcl' in m:
        return False
    match = re.search('^#[0-9a-f]{6}$', m['hcl'])
    return True if match else False
ecl = lambda m: 'ecl' in m and m['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
def pid(m):
    if not 'pid' in m:
        return False
    match = re.search('^[0-9]{9}$', m['pid'])
    return True if match else False
ok2 = lambda m: byr(m) and iyr(m) and eyr(m) and hgt(m) and hcl(m) and ecl(m) and pid(m)
for line in A:
    if not len(line):
        if ok1(m): one += 1
        if ok2(m): two += 1
        m = {}
    else:
        for pair in line.split(' '):
            key, val = pair.split(':')
            m[key] = val

print(f'Part 1: {one}')  # Part 1: 182
print(f'Part 2: {two}')  # Part 2: 109
```

## [Day 5: Binary Boarding](https://adventofcode.com/2020/day/5)

```python
A = []
with open('./input.txt') as input:
    A = [line.strip() for line in input]

def row(s):
    i = 0
    j = 128
    for c in s:
        k = (i + j) // 2
        if c == 'B': i = k
        if c == 'F': j = k
    return i

def col(s):
    i = 0
    j = 8
    for c in s:
        k = (i + j) // 2
        if c == 'R': i = k
        if c == 'L': j = k
    return i

best = 0
seats = []
for s in A:
    seat = 8 * row(s) + col(s)
    best = max(best, seat)
    seats.append(seat)

target = 0
seats.sort()
for i in range(1, len(seats)):
    if abs(seats[i - 1] - seats[i]) == 2:
        target = seats[i - 1] + 1
        break

print(f'Part 1: {best}')    # Part 1: 953
print(f'Part 2: {target}')  # Part 2: 615

```
