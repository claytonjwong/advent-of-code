# AoC 2022
* [adventofcode.com/2022](https://adventofcode.com/2022)

## [Day 1: Calorie Counting](https://adventofcode.com/2022/day/1)

```python
A = []
with open('input.txt') as input:
    t = 0
    for line in input:
        line = line.strip()
        if len(line):
            t += int(line)
        else:
            A.append(t); t = 0
A.sort()
print(f'part 1: {A[-1]}')
print(f'part 2: {sum(A[-3:])}')
# part 1: 69883
# part 2: 207576
```