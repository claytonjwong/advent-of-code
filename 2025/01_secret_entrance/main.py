#
# https://adventofcode.com/2025/day/1
#

dial = 50
part1 = 0
part2 = 0
with open('input.txt') as input:
    for s in input:
        x = int(s[1:])
        dx = -1 if s[0] == 'L' else 1
        while x:
            dial += dx; x -= 1
            if dial == 100:
                dial = 0
            if dial == -1:
                dial = 99
            if not dial:
                part2 += 1
        if not dial:
            part1 += 1
print(f'part 1: {part1}')
print(f'part 2: {part2}')

# part 1: 1071
# part 2: 6700
