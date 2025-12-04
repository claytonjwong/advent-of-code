#
# https://adventofcode.com/2025/day/3
#

A = []
with open('input.txt') as input:
    for s in input:
        A.append([int(c) for c in s.strip()])

def greedy_reduce(A, K):
    best = A[:K]
    for x in A[K:]:
        best.append(x); found = False
        for i in range(1, len(best)):
            if best[i - 1] < best[i] or found:
                best[i - 1] = best[i]; found = True
        best.pop()
    return int(''.join(str(x) for x in best))

part1 = sum(greedy_reduce(row, 2) for row in A)
part2 = sum(greedy_reduce(row, 12) for row in A)

print(f'part 1: {part1}')
print(f'part 2: {part2}')

# part 1: 17142
# part 2: 169935154100102
