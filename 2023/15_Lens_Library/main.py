A = []
with open('input.txt') as input:
    for line in input:
        A = line.strip().split(',')

def f(s, t = 0):
    for c in s:
        t = ((t + ord(c)) * 17) % 256
    return t

t1 = sum(f(s) for s in A)
print(f'part 1: {t1}')
# part 1: 514281

box = [[] for _ in range(256)]
for s in A:
    if s.endswith('-'):
        k = s[:-1]
        i = f(k)
        box[i] = [(key, val) for key, val in box[i] if key != k]
    else:
        k, v = s.split('=')
        i = f(k)
        found = False
        for j, (key, val) in enumerate(box[i]):
            if key == k:
                box[i][j] = (k, int(v)); found = True
        if not found:
            box[i].append((k, int(v)))

t2 = 0
for i in range(len(box)):
    for j in range(len(box[i])):
        _, v = box[i][j]
        t2 += (i + 1) * (j + 1) * v
print(f'part 2: {t2}')
# part 2: 244199
