#
# https://adventofcode.com/2022/day/11
#

from collections import deque
import heapq

QUEUES = [
    [98, 70, 75, 80, 84, 89, 55, 98], # 0
    [59],                             # 1
    [77, 95, 54, 65, 89],             # 2
    [71, 64, 75],                     # 3
    [74, 55, 87, 98],                 # 4
    [90, 98, 85, 52, 91, 60],         # 5
    [99, 51],                         # 6
    [98, 94, 59, 76, 51, 65, 75],     # 7
]
A, isDiv3, MOD = [], False, 1

class Monkey:
    def __init__(self, index, fun, target, truthy, falsey):
        self.index = index
        self.fun = fun
        self.target = target
        self.truthy = truthy
        self.falsey = falsey
        self.cnt = 0
    def inspect(self):
        self.cnt += len(A[self.index])
        while len(A[self.index]):
            x = A[self.index].popleft()
            x = self.fun(x)
            x = x // 3 if isDiv3 else x % MOD
            if not (x % self.target):
                A[self.truthy].append(x)
            else:
                A[self.falsey].append(x)

monkeys = [
    Monkey(0, lambda x: x * 2, 11, 1, 4),
    Monkey(1, lambda x: x * x, 19, 7, 3),
    Monkey(2, lambda x: x + 6, 7, 0, 5),
    Monkey(3, lambda x: x + 2, 17, 6, 2),
    Monkey(4, lambda x: x * 11, 3, 1, 7),
    Monkey(5, lambda x: x + 7, 5, 0, 4),
    Monkey(6, lambda x: x + 1, 13, 5, 2),
    Monkey(7, lambda x: x + 5, 2, 3, 6),
]

#
# part 1
#
A, isDiv3, rounds = [deque(q[:]) for q in QUEUES], True, 20
[[monkey.inspect() for monkey in monkeys] for _ in range(rounds)]
a, b = heapq.nlargest(2, [monkey.cnt for monkey in monkeys])
print(f'part 1: {a * b}')

#
# part 2
#
for monkey in monkeys:
    monkey.cnt = 0        # reset counts from part 1
    MOD *= monkey.target  # use rule-of-product to keep worry levels manageable
A, isDiv3, rounds = [deque(q[:]) for q in QUEUES], False, 10000
[[monkey.inspect() for monkey in monkeys] for _ in range(rounds)]
a, b = heapq.nlargest(2, [monkey.cnt for monkey in monkeys])
print(f'part 2: {a * b}')

# part 1: 54253
# part 2: 13119526120