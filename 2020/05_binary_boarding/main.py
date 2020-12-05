#
# https://adventofcode.com/2020/day/5
#

A = []
with open('./input.txt') as input:
    A = [line.strip() for line in input]

def row(s):
    i = 0
    j = 128
    for c in s:
        k = (i + j) // 2
        if c == 'B': i = k
        if c == 'F': j = k
    return i

def col(s):
    i = 0
    j = 8
    for c in s:
        k = (i + j) // 2
        if c == 'R': i = k
        if c == 'L': j = k
    return i

best = 0
seats = []
for s in A:
    seat = 8 * row(s) + col(s)
    best = max(best, seat)
    seats.append(seat)

target = 0
seats.sort()
for i in range(1, len(seats)):
    if abs(seats[i - 1] - seats[i]) == 2:
        target = seats[i - 1] + 1
        break

print(f'Part 1: {best}')    # Part 1: 953
print(f'Part 2: {target}')  # Part 2: 615
