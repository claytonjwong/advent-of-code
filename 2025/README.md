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
