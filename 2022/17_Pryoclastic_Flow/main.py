#
# https://adventofcode.com/2022/day/17
#

class Rock:
    def __init__(self, have):
        self.point = (0, 0) # bottom-left point
        self.have = have    # set of rock points relative to self.point

    def left(self, dj = 0):
        _, j = self.point; j += dj
        return min(j + dj for _, dj in self.have)

    def right(self, dj = 0):
        _, j = self.point; j += dj
        return max(j + dj for _, dj in self.have)

class Chamber:
    def __init__(self):
        self.hi = -1
        self.start = 2
        self.rocks = [
            #    ####
            Rock(set([(0, 0), (0, 1), (0, 2), (0, 3)])),
            #    .#.
            #    ###
            #    .#.
            Rock(set([(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)])),
            #    ..#
            #    ..#
            #    ###
            Rock(set([(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)])),
            #    #
            #    #
            #    #
            #    #
            Rock(set([(0, 0), (1, 0), (2, 0), (3, 0)])),
            #    ##
            #    ##
            Rock(set([(0, 0), (0, 1), (1, 0), (1, 1)]))
        ]
        self.blows = []
        with open('input.txt') as input:
            for line in input:
                self.blows = [-1 if c == '<' else 1 for c in list(line.strip())]
        self.i = 0 # i-th rock
        self.k = 0 # k-th blow
        self.seen = set()

    def dropRock(self):
        rock = self.nextRock()
        while True:
            self.blow(rock)
            if not self.fall(rock): break
        self.mark(rock)

    def nextRock(self):
        rock = self.rocks[self.i]; self.i = (self.i + 1) % len(self.rocks) # i-th rock
        rock.point = (self.hi + 1 + 3, self.start)
        return rock

    def blow(self, rock):
        dj = self.blows[self.k]; self.k = (self.k + 1) % len(self.blows) # k-th blow
        if rock.left(dj) < 0 or 6 < rock.right(dj): # left/right chamber boundaries
            return
        i, j = rock.point; j += dj
        if all((i + di, j + dj) not in self.seen for di, dj in rock.have):
            rock.point = (i, j)

    def fall(self, rock):
        i, j = rock.point; i -= 1
        if any(i + di < 0 or (i + di, j + dj) in self.seen for di, dj in rock.have):
            return False
        rock.point = (i, j)
        return True

    def mark(self, rock):
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

print(f'part 1: {(chamber.hi + 1)}')
# part 1: 3149
