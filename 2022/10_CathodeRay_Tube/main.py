#
# https://adventofcode.com/2022/day/10
#

from collections import defaultdict

A = [0]
with open('input.txt') as input:
    for line in input:
        words = line.strip().split(' ')
        A.append(0 if len(words) == 1 else int(words[1]))

m, k = defaultdict(int), 0 # k-th cycle
for x in A:
    k += 1 if not x else 2
    m[k] = x

x = 1
t, take, msg = 0, set([20, 60, 100, 140, 180, 220]), [[]]
for i in range(1, k):
    x += m[i]
    msg[-1].append('#' if abs(x - len(msg[-1])) <= 1 else '.')
    if i in take:
        t += i * x
    if not (i % 40):
        msg.append([])

newline = '\n'
print(f'part 1: {t}')
print(f'part 2:\n{newline.join("".join(row) for row in msg)}')
# part 1: 15260
# part 2:
###...##..#..#.####..##..#....#..#..##..
#..#.#..#.#..#.#....#..#.#....#..#.#..#.
#..#.#....####.###..#....#....#..#.#....
###..#.##.#..#.#....#.##.#....#..#.#.##.
#....#..#.#..#.#....#..#.#....#..#.#..#.
#.....###.#..#.#.....###.####..##...###.