#
# https://adventofcode.com/2025/day/9
#

from collections import deque

P = []  # points
with open('input.txt') as input:
    for s in input:
        x, y = map(int, s.strip().split(','))
        P.append((y, x))  # transpose matrix

area = lambda x1, y1, x2, y2: (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)  # +1 for endpoints inclusive

part1 = 0
for i in range(len(P)):
    for j in range(i + 1, len(P)):
        x1, y1 = P[i]
        x2, y2 = P[j]
        part1 = max(part1, area(x1, y1, x2, y2))
print(f'part 1: {part1}')

#
# traverse points by following them sequentially from P[0]..P[N-1] and then back to P[0] to wrap-around to the first point
#
def traverse(P):
    x, y = P[0]
    seen = set([(x, y)])
    for next_x, next_y in P + [P[0]]:  # + [P[0]] to wrap-around to the first point at the end
        dx = 1 if x < next_x else 0 if x == next_x else -1
        dy = 1 if y < next_y else 0 if y == next_y else -1
        while x != next_x or y != next_y:
            x += dx
            y += dy
            seen.add((x, y))
    return seen

I = traverse(P)  # inside

# return True if-and-only-if point (x,y) is an adjacent to a point inside
adjacent = lambda x, y: any((u, v) in I for u, v in [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y + 1), (x + 1, y + 1), (x + 1, y), (x + 1, y - 1), (x, y - 1)])

#
# the outside points "surround" the inside points via BFS
#
x, y = sorted(P)[0]
q = deque([(x - 1, y - 1)])  # -1 for top-left outside
O = set([(x - 1, y - 1)])  # outside
while q:
    x, y = q.popleft()
    for u, v in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:
        if (u, v) not in I and (u, v) not in O and adjacent(u, v):
            q.append((u, v)); O.add((u, v))

#
# consider all rectangles with sides that do NOT have any points in common with any outside points
#
part2 = 0
for i in range(len(P)):
    for j in range(i + 1, len(P)):
        x1, y1 = P[i]
        x2, y2 = P[j]
        sides = set()
        [sides.add((x, y1)) and sides.add((x, y2)) for x in range(min(x1, x2), max(x1, x2) + 1)]
        [sides.add((x1, y)) and sides.add((x2, y)) for y in range(min(y1, y2), max(y1, y2) + 1)]
        if not len(sides & O):  # if there is no intersection between the rectangle sides and outside points
            part2 = max(part2, area(x1, y1, x2, y2))

print(f'part 2: {part2}')

# part 1: 4777816465
# part 2: 1410501884
