#
# https://adventofcode.com/2023/day/2
#

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
