#
# https://adventofcode.com/2022/day/7
#

from bisect import bisect_left

class Node:
    def __init__(self, parent = None):
        self.size = 0
        self.kids = {}
        self.parent = parent

root = Node()
node = root
with open('input.txt') as input:
    for line in input:
        A = line.strip().split(' ')
        if A[1] == 'cd':
            f = A[2]
            if f == '/': node = root
            elif f == '..': node = node.parent
            else:
                if f not in node.kids:
                    node.kids[f] = Node(node)
                node = node.kids[f]
        elif A[0].isdigit():
            node.size += int(A[0])

class Accumulator:
    def __init__(self):
        self.part1 = 0
        self.A = []
        self.go()
        self.part2 = self.delete()
    def go(self, node = root):
        for kid in node.kids.values():
            node.size += self.go(kid)
        if node.size <= 1e5:
            self.part1 += node.size  # part 1: accumulate total of all folders of size <= 1e5
        self.A.append(node.size)     # part 2: append candidate node size to array
        return node.size
    def delete(self):
        self.A.sort()
        space = 7e7 - self.A[-1]
        target = 3e7 - space
        i = bisect_left(self.A, target)
        return self.A[i]

acc = Accumulator()
print(f'part 1: {acc.part1}')
print(f'part 2: {acc.part2}')
# part 1: 1391690
# part 2: 5469168