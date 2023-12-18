# 8:37am - read problem statement
# 8:40am - ~3 minutes for game plan:

# game plan: perform hash on all commas separated values of the input

# 8:40am - implementation begins
# 8:43am - implementation ends - run it!
# 8:44am - part 1 AC ~7 minutes, yay! :)

# 8:45am - part 2 - read problem statement
# 8:53am - I got a little distracted LOL, wanted to skip ahead a skim and bit, but ended up going back and re-reading
# what I tried to "distractedly read" (ie. no comprehension, no reading! haha)

# 9:03am - I had to re-read to find out how to determine the box number, oops!  I missed that the first few times around,
# so we run the HASH algorithm from part 1 on the label of each comma separated string, where the label is the left-hand-side of the '-' xor '='

# 8:54am - game plan:
# create an array for box from 0..255 inclusive
# each box will contain an array of pairs label, value

# TODO: re-read the insertion part, there's 2 use cases to consider there

# 9:06am - implementation begins to run hash algo on the label for part 2
# 9:23am - debugging...
# 9:31am - part 2 accepted, yay! :)

from collections import Counter

A = []
with open('/Users/claytonjwong/sandbox/advent-of-code/2023/15_Lens_Library/input.txt') as input:
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
        print(f'remove key {k} from box {i}')
        box[i] = [(key, val) for key, val in box[i] if key != k]
        print(f'box[{i}]: {box[i]}')
    else:
        k, v = s.split('=')
        i = f(k)
        print(f'add key {k} to box {i} with value {v}')
        found = False
        for j, (key, val) in enumerate(box[i]):
            if key == k:
                box[i][j] = (k, int(v)); found = True
        if not found:
            box[i].append((k, int(v)))
        print(f'box[{i}]: {box[i]}')
    print()

t2 = 0
for i in range(len(box)):
    for j in range(len(box[i])):
        _, v = box[i][j]
        t2 += (i + 1) * (j + 1) * v
print(f'part 2: {t2}')
# part 2: 244199
