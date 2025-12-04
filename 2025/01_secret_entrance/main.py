#
# https://adventofcode.com/2025/day/1
#

dial = 50
part1 = 0
part2 = 0
with open('input.txt') as input:
    for s in input:
        n = int(s[1:])
        dx = -1 if s[0] == 'L' else 1
        for _ in range(n):
            dial += dx
            if dial == -1: dial = 99  # wrap-around left
            if dial == 100: dial = 0  # wrap-around right
            part2 += 1 if not dial else 0
        part1 += 1 if not dial else 0
print(f'part 1: {part1}')
print(f'part 2: {part2}')

# part 1: 1071
# part 2: 6700
