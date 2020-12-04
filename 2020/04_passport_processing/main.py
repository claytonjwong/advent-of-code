#
# https://adventofcode.com/2020/day/4
#

import re

A = []
with open('./input.txt') as input:
    A = [line.strip() for line in input]
A.append('')  # sentinel delimiter

m = {}
one = 0
two = 0
ok1 = lambda m: 'byr' in m and 'iyr' in m and 'eyr' in m and 'hgt' in m and 'hcl' in m and 'ecl' in m and 'pid' in m
byr = lambda m: 'byr' in m and 1920 <= int(m['byr']) <= 2002
iyr = lambda m: 'iyr' in m and 2010 <= int(m['iyr']) <= 2020
eyr = lambda m: 'eyr' in m and 2020 <= int(m['eyr']) <= 2030
def hgt(m):
    if not 'hgt' in m:
        return False
    height = m['hgt']
    val = height[:-2]
    unit = height[-2:]
    if unit == 'cm': return 150 <= int(val) <= 193
    if unit == 'in': return 59 <= int(val) <= 76
    return False
def hcl(m):
    if not 'hcl' in m:
        return False
    match = re.search('^#[0-9a-f]{6}$', m['hcl'])
    return True if match else False
ecl = lambda m: 'ecl' in m and m['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
def pid(m):
    if not 'pid' in m:
        return False
    match = re.search('^[0-9]{9}$', m['pid'])
    return True if match else False
ok2 = lambda m: byr(m) and iyr(m) and eyr(m) and hgt(m) and hcl(m) and ecl(m) and pid(m)
for line in A:
    if not len(line):
        if ok1(m): one += 1
        if ok2(m): two += 1
        m = {}
    else:
        for pair in line.split(' '):
            key, val = pair.split(':')
            m[key] = val

print(f'Part 1: {one}')  # Part 1: 182
print(f'Part 2: {two}')  # Part 2: 109
