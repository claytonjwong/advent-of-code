#
# https://adventofcode.com/2022/day/19
#

import os
os.chdir('/Users/claytonjwong/sandbox/advent-of-code/2022/19_Not_Enough_Minerals')

from collections import deque
import re

REGEX = '^Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.$'
ORE, CLAY, OBS, GEO = 'ore', 'clay', 'obs', 'geo'
ROCKS = [ORE, CLAY, OBS, GEO]

key = lambda have: (have[ORE], have[CLAY], have[OBS], have[GEO])
def obj(key):
    ore, clay, obs, geo = key
    return { ORE: ore, CLAY: clay, OBS: obs, GEO: geo, }

def run(id, rocks, robot, needs, MINUTES = 24):
    # print(f'run(id: {id}, rocks: {rocks}, robot: {robot}, needs: {needs})')
    best = 0
    q, seen = deque([(0, key(rocks), key(robot))]), set()
    while q:
        print(len(q))
        minute, rocks, robot = q.popleft()
        rocks, robot = [obj(have) for have in [rocks, robot]]
        # print(rocks, robot)
        if MINUTES < minute:
            continue
        minute += 1
        # make ore robot
        if needs[ORE][ORE] <= rocks[ORE]:
            next_rocks = rocks.copy(); next_rocks[ORE] -= needs[ORE][ORE]
            next_robot = robot.copy(); next_robot[ORE] += 1
            # collect rocks
            for rock in robot.keys():
                next_rocks[rock] += robot[rock]
            best = max(best, next_rocks[GEO])
            next_state = (minute, key(next_rocks), key(next_robot))
            next_key = (key(next_rocks), key(next_robot))
            if next_key not in seen:
                q.append(next_state); seen.add(next_key)
        # make clay robot
        if needs[CLAY][ORE] <= rocks[ORE]:
            next_rocks = rocks.copy(); next_rocks[ORE] -= needs[CLAY][ORE]
            next_robot = robot.copy(); next_robot[CLAY] += 1
            for rock in robot.keys():
                next_rocks[rock] += robot[rock]
            best = max(best, next_rocks[GEO])
            next_state = (minute, key(next_rocks), key(next_robot))
            next_key = (key(next_rocks), key(next_robot))
            if next_key not in seen:
                q.append(next_state); seen.add(next_key)
        # make obs robot
        if needs[OBS][ORE] <= rocks[ORE] and needs[OBS][CLAY] <= rocks[CLAY]:
            next_rocks = rocks.copy(); next_rocks[ORE] -= needs[OBS][ORE]; next_rocks[CLAY] -= needs[OBS][CLAY]
            next_robot = robot.copy(); next_robot[OBS] += 1
            for rock in robot.keys():
                next_rocks[rock] += robot[rock]
            best = max(best, next_rocks[GEO])
            next_state = (minute, key(next_rocks), key(next_robot))
            next_key = (key(next_rocks), key(next_robot))
            if next_key not in seen:
                q.append(next_state); seen.add(next_key)
        # make geo robot
        if needs[GEO][ORE] <= rocks[ORE] and needs[GEO][OBS] <= rocks[OBS]:
            next_rocks = rocks.copy(); next_rocks[ORE] -= needs[GEO][ORE]; next_rocks[OBS] -= needs[GEO][OBS]
            next_robot = robot.copy(); next_robot[GEO] += 1
            for rock in robot.keys():
                next_rocks[rock] += robot[rock]
            best = max(best, next_rocks[GEO])
            next_state = (minute, key(next_rocks), key(next_robot))
            next_key = (key(next_rocks), key(next_robot))
            if next_key not in seen:
                q.append(next_state); seen.add(next_key)
        # save rocks without buying a robot
        for rock in robot.keys():
            rocks[rock] += robot[rock]
        best = max(best, rocks[GEO])
        next_state = (minute, key(rocks), key(robot))
        next_key = (key(rocks), key(robot))
        if next_key not in seen:
            q.append(next_state); seen.add(next_key)
    # for minute, rocks, robot in seen:
    #     if minute == 11:
    #         print(rocks, robot)
    return best

A = []
with open('input.txt') as input:
    for line in input:
        match = re.search(REGEX, line.strip())
        id = int(match.group(1))
        rocks = {rock: 0 for rock in ROCKS}
        robot = {rock: 0 for rock in ROCKS}; robot[ORE] = 1
        needs = {
            ORE: {
                ORE: int(match.group(2))
            },
            CLAY: {
                ORE: int(match.group(3)),
            },
            OBS: {
                ORE: int(match.group(4)),
                CLAY: int(match.group(5)),
            },
            GEO: {
                ORE: int(match.group(6)),
                OBS: int(match.group(7)),
            },
        }
        geos = run(id, rocks, robot, needs)
        print(f'geos: {geos}')
        A.append(geos)


