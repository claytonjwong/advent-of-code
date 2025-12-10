#
# https://adventofcode.com/2025/day/10
#

from collections import deque

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
        key = lambda state: ','.join(str(x) for x in state)
        start, finish = [0] * len(self.joltages), self.joltages  # start with 0 counts
        q, seen, depth = deque([start]), set([key(start)]), 0
        while q:
            k = len(q)
            for _ in range(k):
                cur = q.popleft()
                if key(cur) == key(finish):
                    return depth
                for toggles in self.buttons:
                    next = cur[:]
                    for i in toggles:
                        next[i] += 1
                    if key(next) not in seen and all(next[i] <= finish[i] for i in range(len(finish))):
                        q.append(next); seen.add(key(next))
            depth += 1
        return -1

A = []
with open('example.txt') as input:
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

# part1: 512
