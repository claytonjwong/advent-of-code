#
# https://adventofcode.com/2025/day/12
#

from collections import defaultdict

m = defaultdict(list)
puzzles = []
with open('example.txt') as input:
    id, shape = 0, []
    for s in input:
        s = s.strip()
        if ':' in s:
            tokens = [tok for tok in s.split(':') if len(tok)]
            if len(tokens) == 1:
                id = int(tokens[0])
            if len(tokens) == 2:
                dimensions, ids = s.split(':')
                cols, rows = map(int, dimensions.split('x'))
                ids = [int(id) for id in ids.split(' ') if len(id)]
                puzzles.append((rows, cols, ids))
        elif len(s):
            shape.append(list(s))
        else:
            m[id].append(shape); shape = []

def pretty_print(shape):
    for row in shape:
        print(''.join(row))
    print()

def rotate(shape):
    rotated = [['.'] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            rotated[j][3 - 1 - i] = shape[i][j]
    return rotated

key = lambda shape: ','.join(''.join(row) for row in shape)

for id, shapes in m.items():
    rotated, seen = [], set()
    for shape in shapes:
        seen.add(key(shape))
        for _ in range(3):
            shape = rotate(shape)
            if key(shape) not in seen:
                rotated.append(shape); seen.add(key(shape))
    shapes.extend(rotated)

for id, shapes in m.items():
    print(f'id: {id} has {len(shapes)} shapes')
    for shape in shapes:
        pretty_print(shape)

def add(A, i, j, shape):
    M, N = len(A), len(A[0])
    if not (i + 3 <= M) or not (j + 3 <= N):
        return False
    for u in range(3):
        for v in range(3):
            A[i + u][j + v] = shape[u][v]
    return True

def remove(A, i, j, shape):
    M, N = len(A), len(A[0])
    if not (i + 3 <= M) or not (j + 3 <= N):
        return False
    ok = True
    for u in range(3):
        for v in range(3):
            if A[i + u][j + v] != shape[u][v]:
                ok = False
    if not ok:
        return False
    for u in range(3):
        for v in range(3):
            A[i + u][j + v] = '.' if shape[u][v] == '#' else A[i + u][j + v]
    return True

for puzzle in puzzles:
    print(puzzle)
