#
# https://adventofcode.com/2025/day/6
#

from functools import reduce

A = []
with open('input.txt') as input:
    for s in input:
        A.append(s[:-1])  # -1 to skip the newline '\n' character
M, N = len(A), len(A[0])

part1 = 0
nums = []
for row in A[:M - 1]:
    nums.append([int(num) for num in row.strip().split(' ') if len(num)])
ops = [op for op in A[M - 1].strip().split(' ') if len(op)]

for j in range(len(nums[0])):
    num = 0 if ops[j] == '+' else 1  # initialize num=0 for addition and num=1 for multiplication
    for i in range(len(nums)):
        if ops[j] == '+': num += nums[i][j]
        if ops[j] == '*': num *= nums[i][j]
    part1 += num
print(f'part 1: {part1}')

part2 = 0
num, nums, terminators = 0, [], set([' ', '+', '*'])
for j in reversed(range(N)):
    for i in range(M):
        if num and A[i][j] in terminators:
            nums.append(num); num = 0
        if A[i][j] == '+': part2 += reduce(lambda a, b: a + b, nums); nums = []
        if A[i][j] == '*': part2 += reduce(lambda a, b: a * b, nums); nums = []
        if A[i][j].isdigit(): num = 10 * num + int(A[i][j])
print(f'part 2: {part2}')

# part 1: 4076006202939
# part 2: 7903168391557
