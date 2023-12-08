from functools import cmp_to_key
from collections import Counter, defaultdict

def kind(hand):
    cnt = Counter(hand).values()
    if 5 in cnt: return 'five of a kind'
    if 4 in cnt: return 'four of a kind'
    if 2 in cnt and 3 in cnt: return 'full house'
    if 3 in cnt: return 'three of a kind'
    if 2 in cnt:
        return 'one pair' if len([freq for freq in cnt if freq == 2]) == 1 else 'two pair'
    return 'high card'

def joke(hand):
    J = len([c for c in hand if c == 'J'])
    if type(hand) == 'high card' and J: return 'one pair'
    if type(hand) == 'one pair' and J: return 'three of a kind'
    if type(hand) == 'two pair' and J: return 'full house' if J == 1 else 'four of a kind'
    if type(hand) == 'three of a kind' and J: return 'four of a kind'
    if type(hand) == 'full house' and J: return 'five of a kind'
    if type(hand) == 'four of a kind' and J: return 'five of a kind'
    return type(hand)

A = []
with open('input.txt') as input:
    for line in input:
        hand, bid = line.split()
        A.append((hand, int(bid)))
m1 = defaultdict(list)
m2 = defaultdict(list)
for hand, bid in A:
    m1[kind(hand)].append((hand, bid))
    m2[joke(hand)].append((hand, bid))

def compare(a, b, points):
    for x, y in zip(a[0], b[0]):
        if points[x] < points[y]: return -1
        if points[x] > points[y]: return 1
    return 0
comp1 = lambda a, b: compare(a, b, { str(i): i for i in range(2, 10) } | { 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14 })
comp2 = lambda a, b: compare(a, b, { str(i): i for i in range(2, 10) } | { 'T': 10, 'J':  1, 'Q': 12, 'K': 13, 'A': 14 })

order1 = []
order2 = []
for k in ['high card', 'one pair', 'two pair', 'three of a kind', 'full house', 'four of a kind', 'five of a kind']:
    for hand, bid in sorted(m1[k], key = cmp_to_key(comp1)): order1.append(bid)
    for hand, bid in sorted(m2[k], key = cmp_to_key(comp2)): order2.append(bid)
t1 = sum((i + 1) * bid for i, bid in enumerate(order1))
t2 = sum((i + 1) * bid for i, bid in enumerate(order2))
print(f'part 1: {t1}')
print(f'part 2: {t2}')
# part 1: 248113761
# part 2: 246285222
