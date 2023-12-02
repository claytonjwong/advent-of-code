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
        cnt, color = group.strip().split(' ')
        need[color] = int(cnt)
    return need

t1, t2 = 0, 0
with open('input.txt') as input:
    for line in input:
        game, values = line.split(':')
        num = int(game.split(' ')[1])
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
