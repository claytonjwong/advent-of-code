# https://en.wikipedia.org/wiki/Monty_Hall_problem

import random

N = int(1e5)

door = [1, 2, 3]

same = 0
diff = 0

for _ in range(N):
    prize = random.choice(door)               # 1. host knows the prize door
    guess = random.choice(door)               # 2. contestant guesses a door
    empty = set(door) - set([prize, guess])   # 3. host opens empty door
    # 4. host asks contestant to keep same door choice or make different door choice
    same += prize == guess  # 🙈 keep same choice
    diff += prize != guess  # 🙉 make diff choice

percent = lambda x: int(100 * x / N)
print(f'same: {same}  {percent(same)}%')
print(f'diff: {diff}  {percent(diff)}%')
# same: 33645  33%
# diff: 66355  66%
