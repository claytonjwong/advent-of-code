#
# https://adventofcode.com/2025/day/10
#

from collections import deque
from z3 import *

class Machine:
    def __init__(self, lights, buttons, joltages):
        self.lights = lights
        self.buttons = buttons
        self.joltages = joltages

    def __repr__(self):
        return f'Machine(\n  lights: {self.lights}\n  buttons: {self.buttons}\n  joltages: {self.joltages})'

    def toggle_lights(self):
        key = lambda state: ','.join(str(x) for x in state)
        start, finish = [0] * len(self.lights), self.lights  # start with all OFF
        q, seen, depth = deque([start]), set([key(start)]), 0
        while q:
            k = len(q)
            for _ in range(k):
                cur = q.popleft()
                if key(cur) == key(finish):
                    return depth
                for toggles in self.buttons:
                    next = [x ^ int(i in toggles) for i, x in enumerate(cur)]
                    if key(next) not in seen:
                        q.append(next); seen.add(key(next))
            depth += 1
        return -1

    def config_joltage(self):
        opt = Optimize()
        vars = [Int('b' + ''.join(str(x) for x in nums)) for nums in self.buttons]  # button press variables
        for var in vars:
            opt.add(0 <= var)  # button press variables must be greater-than-or-equal-to 0
        for i, target in enumerate(self.joltages):
            parts = set(vars[j] for j in range(len(self.buttons)) if i in self.buttons[j])
            opt.add(Sum(parts) == target)  # sum of button press variable participants must equal target
        total_presses = Sum(vars)
        opt.minimize(total_presses)
        return opt.model().evaluate(total_presses).as_long() if opt.check() == sat else 0

A = []
with open('input.txt') as input:
    for s in input:
        lights = []
        buttons = []
        joltages = []
        for token in s.strip().split(' '):
            if token[0] == '[': lights = [1 if c == '#' else 0 for c in token[1:-1]]
            if token[0] == '(': buttons.append([int(x) for x in token[1:-1].split(',')])
            if token[0] == '{': joltages = [int(x) for x in token[1:-1].split(',')]
        A.append(Machine(lights, buttons, joltages))

part1 = sum(it.toggle_lights() for it in A)
part2 = sum(it.config_joltage() for it in A)
print(f'part 1: {part1}')
print(f'part 2: {part2}')

# part 1: 512
# part 2: 19857
