from functools import reduce

A = []
with open('input.txt') as input:
    for line in input:
        A = line.strip().split(',')

f = lambda s: reduce(lambda t, c: (t + ord(c)) * 17 % 256, s, 0)

box = [[] for _ in range(256)]
for s in A:
    if s.endswith('-'):
        k = s[:-1]
        i = f(k)
        box[i] = [(key, val) for key, val in box[i] if key != k]
    else:
        k, v = s.split('='); v = int(v)
        i = f(k)
        found = False
        for j, (key, val) in enumerate(box[i]):
            if key == k:
                box[i][j] = (k, v); found = True
        if not found:
            box[i].append((k, v))

t1 = sum(f(s) for s in A)
t2 = sum((i + 1) * (j + 1) * box[i][j][1] for i in range(len(box)) for j in range(len(box[i])))
print(f'part 1: {t1}')
print(f'part 2: {t2}')
# part 1: 514281
# part 2: 244199
