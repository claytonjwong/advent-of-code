# 6:32am - read problem statement
# 6:41am - ok game plan is brute-force for each time and dist consider all all holds from 1..time - 1 to accumulate "wins" (strictly greater-than dist)
# 6:42am - implementation begins
# 6:54am - 288 is too low 👉 oops, this was the sample input (which produces correct output)
# 6:55am - AC part1
# 6:56am - read problem statement for part2

# Time:        49     87     78     95     ->           49 877 895
# Distance:   356   1378   1502   1882     ->  356 137 815 021 882

# part 2: binary search?  find the point where we start winning in logarithmic time (since linear time for ~1000T input will take forever)

# ~9 minutes to understand the problem

# 7
# 0 -> nothing

# hold for 1, then go 1 * (7 - 1) = 1 * 6 = 6
# hold for 2, then go 2 * (7 - 2) = 2 * 5 = 10
# hold for 3, then go 3 * (7 - 3) = 3 * 4 = 12
# hold for 4, then go 4 * (7 - 4) = 4 * 3 = 12
# hold for 5, then go 5 * (7 - 5) = 5 * 2 = 10
#

# t = 7
# x = how long we hold

# x * (t - x)
# tx - x^2

# t = 7
# x = 3

# 3 * (7 - 3) = 12

# 21 - 9 = 12

# So, because the first race lasts 7 milliseconds, you only have a few options:

# Don't hold the button at all (that is, hold it for 0 milliseconds) at the start of the race. The boat won't move; it will have traveled 0 millimeters by the end of the race.
# Hold the button for 1 millisecond at the start of the race. Then, the boat will travel at a speed of 1 millimeter per millisecond for 6 milliseconds, reaching a total distance traveled of 6 millimeters.
# Hold the button for 2 milliseconds, giving the boat a speed of 2 millimeters per millisecond. It will then get 5 milliseconds to move, reaching a total distance of 10 millimeters.
# Hold the button for 3 milliseconds. After its remaining 4 milliseconds of travel time, the boat will have gone 12 millimeters.
# Hold the button for 4 milliseconds. After its remaining 3 milliseconds of travel time, the boat will have gone 12 millimeters.
# Hold the button for 5 milliseconds, causing the boat to travel a total of 10 millimeters.
# Hold the button for 6 milliseconds, causing the boat to travel a total of 6 millimeters.
# Hold the button for 7 milliseconds. That's the entire duration of the race. You never let go of the button. The boat can't move until you let go of the button. Please make sure you let go of the button so the boat gets to move. 0 millimeters.

import operator
from functools import reduce

T, D = [], []  # time and distance
wins = []
with open('input.txt') as input:
    for time, dist in zip(input, input):
        for t in time.split(':')[1].split(): T.append(int(t))
        for d in dist.split(':')[1].split(): D.append(int(d))
    for t, d in zip(T, D):
        wins.append(len([x for x in range(1, t) if d < x * (t - x)]))
part1 = reduce(operator.mul, wins)

print(f'part 1: {part1}')
# part 1: 503424

# TODO: for part 2 we will try binary search to find the point where we start succeeding
# FFFFFFFTTTTTTTTTTTTFFFFFFFFF
# goal   ^   👈 use binary search to find this point which we use to derive the answer for part2
#        ^^^^^^^^^^^  symmetric bell curve for TRUE