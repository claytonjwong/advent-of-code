from functools import cmp_to_key
from collections import Counter, defaultdict

A = []
with open('/Users/claytonjwong/sandbox/advent-of-code/2023/07_Camel_Cards/input.txt') as input:
    for line in input:
        hand, bid = line.split()
        A.append((hand, int(bid)))

def type(hand):
    cnt = Counter(hand).values()
    if 5 in cnt: return 'five of a kind'
    if 4 in cnt: return 'four of a kind'
    if 2 in cnt and 3 in cnt: return 'full house'
    if 3 in cnt: return 'three of a kind'
    if 2 in cnt:
        pairs = len([freq for freq in cnt if freq == 2])
        return 'one pair' if pairs == 1 else 'two pair'
    return 'high card'

def compare(a, b):
    points = { str(i): i for i in range(2, 10) } | { 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14 }
    for x, y in zip(a[0], b[0]):
        if points[x] < points[y]: return -1
        if points[x] > points[y]: return 1
    return 0

buckets = defaultdict(list)
for hand, bid in A:
    k = type(hand)
    buckets[k].append((hand, bid))

order = []
for k in ['high card', 'one pair', 'two pair', 'three of a kind', 'full house', 'four of a kind', 'five of a kind']:
    for hand, bid in sorted(buckets[k], key = cmp_to_key(compare)):
        order.append(bid)
t1 = sum((i + 1) * bid for i, bid in enumerate(order))
print(f'part 1: {t1}')
# part 1: 248113761
