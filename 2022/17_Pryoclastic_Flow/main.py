#
# https://adventofcode.com/2022/day/17
#

import os
os.chdir('/Users/claytonjwong/sandbox/advent-of-code/2022/17_Pryoclastic_Flow')

class Rock:
    def __init__(self, have):
        self.point = (0, 0) # bottom-left point
        self.have = have    # set of rock points relative to self.point

    def left(self, dj = 0):
        _, j = self.point
        j += dj
        lo = min(j + dj for _, dj in self.have)
        return lo

    def right(self, dj = 0):
        _, j = self.point
        j += dj
        hi = max(j + dj for _, dj in self.have)
        return hi

class Chamber:
    def __init__(self):
        self.hi = -1
        self.start = 2
        self.rocks = [
            #
            #    ####
            #
            Rock(set([(0, 0), (0, 1), (0, 2), (0, 3)])),
            #
            #    .#.
            #    ###
            #    .#.
            #
            Rock(set([(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)])),
            #
            #    ..#
            #    ..#
            #    ###
            #
            Rock(set([(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)])),
            #
            #    #
            #    #
            #    #
            #    #
            #
            Rock(set([(0, 0), (1, 0), (2, 0), (3, 0)])),
            #
            #    ##
            #    ##
            #
            Rock(set([(0, 0), (0, 1), (1, 0), (1, 1)]))
        ]
        self.i = 0
        self.seen = set()
        self.blows = []
        with open('input.txt') as input:
            for line in input:
                self.blows = [-1 if c == '<' else 1 for c in list(line.strip())]
        self.k = 0

    def nextRock(self):
        rock = self.rocks[self.i]; self.i = (self.i + 1) % len(self.rocks)
        rock.point = (self.hi + 1 + 3, self.start)
        return rock

    def blow(self, rock):
        dj = self.blows[self.k]; self.k = (self.k + 1) % len(self.blows)
        L, R = 0, 6 # left/right chamber boundaries
        l, r = rock.left(dj), rock.right(dj)
        if l < L: return
        if R < r: return
        i, j = rock.point
        j += dj
        for di, dj in rock.have:
            u = i + di
            v = j + dj
            if (u, v) in self.seen:
                return
        rock.point = (i, j)

    def fall(self, rock):
        i, j = rock.point
        i -= 1
        for di, dj in rock.have:
            u = i + di
            v = j + dj
            if (u, v) in self.seen or u < 0:
                return False
        rock.point = (i, j)
        return True

    def dropRock(self):
        rock = self.nextRock()
        while True:
            self.blow(rock)
            if not self.fall(rock):
                break
        i, j = rock.point
        for di, dj in rock.have:
            u = i + di
            v = j + dj
            self.seen.add((u, v))
            self.hi = max(self.hi, u)

chamber = Chamber()
ROCKS = 2022
for _ in range(ROCKS):
    chamber.dropRock()

print(f'part 1: {chamber.hi + 1}')
# part 1: 3149