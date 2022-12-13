#
# https://adventofcode.com/2022/day/13
#

import json

def part1():
    with open('input.txt') as input:
        i, t = 1, 0
        L, R = None, None
        for line in input:
            line = line.strip()
            if line == "":
                L, R = None, None
            elif L == None: L = json.loads(line)
            elif R == None: R = json.loads(line)
            if L != None and R != None:
                if ok(L, R):
                    t += i
                i += 1
        return t

def part2():
    with open('input.txt') as input:
        A = [json.loads(line.strip()) for line in input.readlines() if len(line.strip())] + [[[2]]] + [[[6]]]
        quickSort(A, 0, len(A) - 1, ok)
        a = 1 + A.index([[2]])
        b = 1 + A.index([[6]])
        return a * b

def ok(L, R):
    A = [(L, R, 0)]
    while A:
        L, R, i = A.pop()
        if type(L) == int and type(R) == int:
            if R < L: return False
            if L < R: return True
        elif type(L) == list and type(R) == int: A.append((L, [R], 0))
        elif type(L) == int and type(R) == list: A.append(([L], R, 0))
        elif type(L) == list and type(R) == list:
            if i < len(L) and len(R) <= i:
                return False
            elif len(L) <= i and len(R) <= i:
                continue
            elif len(L) <= i:
                return True
            A.append((L, R, i + 1))
            A.append((L[i], R[i], 0))
    return True

# https://www.geeksforgeeks.org/quicksort-using-random-pivoting/
def quickSort(array, i, j, cmp):
    def partition(A, lo, hi, cmp):
        i, pivot = lo - 1, A[hi]
        for j in range(lo, hi):
            if cmp(A[j], pivot):
                i += 1
                A[i], A[j] = A[j], A[i]
        A[i + 1], A[hi] = A[hi], A[i + 1]
        return i + 1
    A = [(i, j)]
    while A:
        i, j = A.pop()
        if j <= i:
            continue
        k = partition(array, i, j, cmp)
        A.append((i, k - 1))
        A.append((k + 1, j))

print(f'Part 1: {part1()}')
print(f'Part 2: {part2()}')
# Problem 1: 6046
# Problem 2: 21423