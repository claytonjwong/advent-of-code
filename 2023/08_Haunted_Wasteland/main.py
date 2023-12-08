class Node:
    def __init__(self, name, L = None, R = None):
        self.name = name
        self.L = L
        self.R = R

dirs, nodes = [], {}
with open('input.txt') as input:
    first = True
    for line in input:
        line = ''.join([c for c in line if not c.isspace() and c != '(' and c != ')'])
        if first:
            dirs = line; first = False
        elif len(line):
            P, kids = line.split('=')  # parent, left/right kids
            L, R = kids.split(',')
            if P not in nodes: nodes[P] = Node(P)
            if L not in nodes: nodes[L] = Node(L)
            if R not in nodes: nodes[R] = Node(R)
            nodes[P].L = nodes[L]
            nodes[P].R = nodes[R]

step, node = 0, nodes['AAA']
while node.name != 'ZZZ':
    i = step % len(dirs); step += 1
    if dirs[i] == 'L': node = node.L
    if dirs[i] == 'R': node = node.R
print(f'part 1: {step}')
# part 1: 13301

step, pre = 0, [node for name, node in nodes.items() if name[-1] == 'A']
while not all(node.name[-1] == 'Z' for node in pre):
    i = step % len(dirs); step += 1; cur = []
    if not (step % len(dirs)):
        print(f'step {step}: A: {[node.name for node in pre]}')
    for node in pre:
        if dirs[i] == 'L': cur.append(node.L)
        if dirs[i] == 'R': cur.append(node.R)
    pre = cur
print(f'part 2: {step}')
# TODO: this step is taking forever to run, maybe look for alternative patterns such as pisano period to derive a solution?
