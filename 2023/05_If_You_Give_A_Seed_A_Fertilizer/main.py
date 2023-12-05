S1, S2 = [], []  # seeds for part 1 and part 2
soil = []
fert = []
water = []
light = []
temp = []
humid = []
place = []
A = None
with open('input.txt') as input:
    for line in input:
        line = line.strip()
        if not len(line):
            continue
        if line.startswith('seeds:'):
            _, values = line.split(':')
            for s in values.split():
                S1.append(int(s))
            for i in range(1, len(values), 2):
                S2.append((values[i - 1], values[i - 1] + values[i]))
        elif line.startswith('seed-to-soil map:'): A = soil
        elif line.startswith('soil-to-fertilizer map:'): A = fert
        elif line.startswith('fertilizer-to-water map:'): A = water
        elif line.startswith('water-to-light map:'): A = light
        elif line.startswith('light-to-temperature map:'): A = temp
        elif line.startswith('temperature-to-humidity map:'): A = humid
        elif line.startswith('humidity-to-location map:'): A = place
        else:
            dst, src, size = [int(s) for s in line.split()]
            offset = dst - src
            beg, end = src, src + size
            A.append((beg, end, offset))

def go(A, x):
    for beg, end, offset in A:
        if beg <= x < end:
            return x + offset
    return x

def f(x):
    x = go(soil, x)
    x = go(fert, x)
    x = go(water, x)
    x = go(light, x)
    x = go(temp, x)
    x = go(humid, x)
    x = go(place, x)
    return x

cand = [f(x) for x in S1]
best = min(cand)
print(f'part 1: {best}')
# part 1: 388071289

cand = [f(x) for x in range(beg, end) for beg, end in S2]
best = min(cand)
print(f'part 2: {best}')
# part 2: question -- how to find minimum in a reasonable amount of time?
# TODO: I think it's obvious, we must use overlapping intervals instead of trying hundreds of millions of different seeds!
