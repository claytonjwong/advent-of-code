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
