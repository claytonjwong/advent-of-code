#
# https://adventofcode.com/2025/day/2
#

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
