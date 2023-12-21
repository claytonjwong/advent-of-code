from collections import Counter, deque
class Module:
    def __init__(self, name='sentinel', kind='!', kids=[]):
        self.name = name
        self.kind = kind
        self.parents, self.kids = {}, kids
        self.state = 0                                # 0 == off  and  1 == on
    def process(self, val, last, next_val = -123):
        if self.kind == '*':                          # 📢 broadcast module
            next_val = val
        if self.kind == '%' and not val:              # 🩴 flip-flop module (🚫 ignore high-pulse, ie. val == 1) 🙃 flip on/off state 👍👎
            next_val = self.state = self.state ^ 1
        if self.kind == '&':                          # 🌈 conjunction module
            self.parents[last] = val
            next_val = int(not all(self.parents.values()))
        return [(kid, next_val, self.name) for kid in self.kids] if next_val != -123 else None

m = {}
with open('input.txt') as input:
    for line in input:
        L, R = line.strip().split(' -> ')
        kind, name = (L[0], L[1:]) if L != 'broadcaster' else ('*', 'broadcaster')
        kids = R.split(', ')
        m[name] = Module(name, kind, kids)
    for name in m.keys():
        for kid in m[name].kids:
            if kid in m:
                m[kid].parents[name] = 0

cnt = Counter()
for _ in range(1000):
    q = deque([('broadcaster', 0, 'Make it so! Engage! 🚀')])  # to name, pulse value, from last name
    while q:
        name, val, last = q.popleft(); cnt[val] += 1
        next = m[name].process(val, last) if name in m else None
        if next:
            q.extend(next)
print(f'part 1: {cnt[0] * cnt[1]}')
# part 1: 1020211150
