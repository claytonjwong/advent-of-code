#
# https://adventofcode.com/2022/day/21
#

from collections import defaultdict

adj, val = defaultdict(list), {}
with open('input.txt') as input:
    for line in input:
        key, eq = line.strip().split(':')
        eq = eq.strip().split(' ')
        if len(eq) == 1:
            val[key] = int(eq[0])
        else:
            adj[key] = eq

def go(key = 'root', part2 = False):
    if key in val:
        return val[key]
    a, op, b = adj[key]
    a = go(a)
    b = go(b)
    if key == 'root' and part2:
        return (a, b)
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/': return a // b

print(f'part 1: {go()}')

i = int(3e12 + 4e11 + 2e10 + 9e9 + 4e8 + 1e7 + 1e6 + 1e5 - 4e4)
j = int(3e12 + 4e11 + 2e10 + 9e9 + 4e8 + 1e7 + 1e6 + 1e5 - 3e4)
while True:
    k = (i + j) // 2
    val['humn'] = k
    a, b = go('root', True)
    if a == b:
        print(f'part 2: {k}')
        break
    if a < b: j = k - 1
    if b < a: i = k + 1

# part 1: 82225382988628
# part 2: 3429411069028