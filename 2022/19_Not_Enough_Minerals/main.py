#
# https://adventofcode.com/2022/day/19
#

from collections import deque
import re

def run(ore_cost_ore, clay_cost_ore, obs_cost_ore, obs_cost_clay, geo_cost_ore, geo_cost_obs, T):
    best = 0
    # state is (ore, clay, obs, geo, r1, r2, r3, r4, time)
    state = (0, 0, 0, 0, 1, 0, 0, 0, T)
    q, seen = deque([state]), set()
    while q:
        state = q.popleft()
        ore, clay, obs, geo, r1, r2, r3, r4, t = state
        best = max(best, geo)
        if not t:
            continue

        # BFS pruning
        hi = max([ore_cost_ore, clay_cost_ore, obs_cost_ore, geo_cost_ore])
        if r1 >= hi:
            r1 = hi
        if r2 >= obs_cost_clay:
            r2 = obs_cost_clay
        if r3 >= geo_cost_obs:
            r3 = geo_cost_obs
        if ore >= t * hi - r1 * (t - 1):
            ore = t * hi - r1 * (t - 1)
        if clay >= t * obs_cost_clay - r2 * (t - 1):
            clay = t * obs_cost_clay - r2 * (t - 1)
        if obs >= t * geo_cost_obs - r3 * (t - 1):
            obs = t * geo_cost_obs - r3 * (t - 1)

        state = (ore, clay, obs, geo, r1, r2, r3, r4, t)
        if state in seen:
            continue
        seen.add(state)

        # buy nothing
        q.append((ore + r1, clay + r2, obs + r3, geo + r4, r1, r2, r3, r4, t - 1))
        # buy ore robot
        if ore_cost_ore <= ore: q.append((ore - ore_cost_ore + r1, clay + r2, obs + r3, geo + r4, r1 + 1, r2, r3, r4, t - 1))
        # buy clay robot
        if clay_cost_ore <= ore: q.append((ore - clay_cost_ore + r1, clay + r2, obs + r3, geo + r4, r1, r2 + 1, r3, r4, t - 1))
        # buy obs robot
        if obs_cost_ore <= ore and obs_cost_clay <= clay: q.append((ore - obs_cost_ore + r1, clay - obs_cost_clay + r2, obs + r3, geo + r4, r1, r2, r3 + 1, r4, t - 1))
        # buy geo robot
        if geo_cost_ore <= ore and geo_cost_obs <= obs: q.append((ore - geo_cost_ore + r1, clay + r2, obs - geo_cost_obs + r3, geo + r4, r1, r2, r3, r4 + 1, t - 1))
    return best

part1, part2 = 0, 1
with open('input.txt') as input:
    for i, line in enumerate(input):
        REGEX = '^Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.$'
        m = re.search(REGEX, line.strip())
        id = int(m.group(1))
        ore_cost_ore = int(m.group(2))
        clay_cost_ore = int(m.group(3))
        obs_cost_ore = int(m.group(4))
        obs_cost_clay = int(m.group(5))
        geo_cost_ore = int(m.group(6))
        geo_cost_obs = int(m.group(7))
        best = run(ore_cost_ore, clay_cost_ore, obs_cost_ore, obs_cost_clay, geo_cost_ore, geo_cost_obs, 24)
        part1 += id * best
        if i < 3:
            best = run(ore_cost_ore, clay_cost_ore, obs_cost_ore, obs_cost_clay, geo_cost_ore, geo_cost_obs, 32)
            part2 *= best
print(f'part 1: {part1}')
print(f'part 2: {part2}')
# part 1: 1264
# part 2: 13475