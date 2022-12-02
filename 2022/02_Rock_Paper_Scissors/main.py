#
# https://adventofcode.com/2022/day/2
#

cost = {
    'X': 1, 'lose': 0,
    'Y': 2, 'tie': 3,
    'Z': 3, 'win': 6,
}
m = {
    # lose
    'BX': cost['lose'] + cost['X'],
    'CY': cost['lose'] + cost['Y'],
    'AZ': cost['lose'] + cost['Z'],
    # tie
    'AX': cost['tie'] + cost['X'],
    'BY': cost['tie'] + cost['Y'],
    'CZ': cost['tie'] + cost['Z'],
    # win
    'CX': cost['win'] + cost['X'],
    'AY': cost['win'] + cost['Y'],
    'BZ': cost['win'] + cost['Z'],
}
lose = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y',
}
win = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X',
}
tie = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z',
}
t1, t2 = 0, 0
with open('input.txt') as input:
    for line in input:
        play = ''.join(line.strip().split(' '))
        t1 += m[play]
        a, b = list(play)
        if b == 'X': t2 += cost['lose'] + cost[lose[a]]
        if b == 'Y': t2 += cost['tie'] + cost[tie[a]]
        if b == 'Z': t2 += cost['win'] + cost[win[a]]
print(f'part 1: {t1}')
print(f'part 2: {t2}')
# part 1: 12855
# part 2: 13726