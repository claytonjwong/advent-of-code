# 12:28pm - read problem statement
# 12:32pm - game plan: read input, then create the circle, then fill the circle and return area as cardinality of cells

# 12:33pm - start implementation
# 12:42pm - outer loop done

# start filling in middle -> actually let's just remove outside parts instead (ie. use inversion -> total minus outside == inside)
# i ->  <- j inwards we remove '.' until # is found

# 12:50pm => ~22 minutes for wrong answer

# 12:51pm => oops, I need to remove outside from above and below as well...

i, j = 0, 0
have, first = set([(0, 0)]), True
with open('input.txt') as input:
    for line in input:
        d, cnt, color = line.split(); cnt = int(cnt)
        if first:
            cnt -= 1; first = False
        di, dj = (-1, 0) if d == 'U' else (1, 0) if d == 'D' else (0, -1) if d == 'L' else (0, 1)
        for _ in range(cnt):
            i += di
            j += dj
            have.add((i, j))

lo_i, hi_i = min(i for i, _ in have), max(i for i, _ in have)
lo_j, hi_j = min(j for _, j in have), max(j for _, j in have)

for i in range(lo_i, hi_i + 1):
    print(''.join(['#' if (i, j) in have else '.' for j in range(lo_j, hi_j + 1)]))

# t, outside = (hi_i - lo_i + 1) * (hi_j - lo_j + 1), 0
# for i in range(lo_i, hi_i + 1):
#     for j in range(lo_j, hi_j + 1):
#         if (i, j) in have:
#             break
#         outside += 1
#     for j in reversed(range(lo_j, hi_j + 1)):
#         if (i, j) in have:
#             break
#         outside += 1
# for j in range(lo_j, hi_j + 1):
#     for i in range(lo_i, hi_i + 1):
#         if (i, j) in have:
#             break
#         outside += 1
#     for i in reversed(range(lo_i, hi_i + 1)):
#         if (i, j) in have:
#             break
#         outside += 1
# inside = t - outside
# print(f'part 1: {inside}')
# part 1: 68624 is too high
# part 1: 24445 is too low
