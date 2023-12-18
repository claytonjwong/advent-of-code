# 8:37am - read problem statement
# 8:40am - ~3 minutes for game plan:

# game plan: perform hash on all commas separated values of the input

# 8:40am - implementation begins
# 8:43am - implementation ends - run it!
# 8:44am - part 1 AC ~7 minutes, yay! :)

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
