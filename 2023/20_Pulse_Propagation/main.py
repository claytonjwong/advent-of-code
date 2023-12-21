# 8:58am - read problem statement
# 9:19am - ok done reading and disecting that, so I have game plan to implement...
# 9:20am - implementation begins
# 10:13am - implementation completed a few minutes ago, I lost track, and started debugging LOL
# 10:23am - ok take a break and debug, something is not quite right here...

# 12:39pm - ok simple mistake, I was only counting signals send to output, not all signals sent total between any modules!

# game plan:

# Flip-flop modules (prefix %) are either on or off; they are initially off. If a flip-flop module receives a high pulse, it is ignored and nothing happens. However, if a flip-flop module receives a low pulse, it flips between on and off. If it was off, it turns on and sends a high pulse. If it was on, it turns off and sends a low pulse.

# ie. if input is high-pulse, do nothing
#     otherwise if input is a low-pulse what we do depends on the module state (on xor off), initially off
#       case 1: if off, then turn on and send high-pulse
#       case 2: if  on, then turn off and send low-pulse
#       ie. on/off always flips, so we can xor with 1 and send that out


# Conjunction modules (prefix &) remember the type of the most recent pulse received from each of their connected input modules;
# they initially default to remembering a low pulse for each input.
# When a pulse is received, the conjunction module first updates its memory for that input.
# Then, if it remembers high pulses for all inputs, it sends a low pulse; otherwise, it sends a high pulse.

# ie. all input are high pulse, then send low pulse, otherwise send high pulse
#     this implies a "reverse mapping" between conjunction modules and all their corresponding input modules
#     which tracks the state of each input, initialized with low input


# There is a single broadcast module (named broadcaster). When it receives a pulse, it sends the same pulse to all
# of its destination modules.

# ie. just forward "as is"


# Here at Desert Machine Headquarters, there is a module with a single button on it called, aptly, the button module.
# When you push the button, a single low pulse is sent directly to the broadcaster module.

# ie. start


# After pushing the button, you must wait until all pulses have been delivered and fully handled before pushing it again.
# Never push the button if modules are still processing pulses.

# ie. serially, not in parallel


# Pulses are always processed in the order they are sent. So, if a pulse is sent to modules a, b, and c,
# and then module a processes its pulse and sends more pulses, the pulses sent to modules b and c would have to be handled first.

# ie. fifo queue instead of DFS stack


# The module configuration (your puzzle input) lists each module. The name of the module is preceded by a symbol identifying its type,
# if any. The name is then followed by an arrow and a list of its destination modules. For example:

# broadcaster -> a, b, c
# %a -> b
# %b -> c
# %c -> inv
# &inv -> a

# ie. parse input as an adjacency list

# left/right split on '->'

# left prefix char is the module type/kind
# left remainder (without prefix) is the module name

# right is the adjacent vertex as a commas separated list of module names

# count low/hi pulses send to output and multiply them as the answer for part 1

from collections import Counter, defaultdict, deque
class Module:
    def __init__(self, name='sentinel', kind='!', kids=[]):
        self.name = name
        self.kind = kind
        self.parents, self.kids = {}, kids
        self.state = 0            # 0 == off  and  1 == on
    def process(self, val, last):
        if self.kind == '*':      # 📢 broadcast module
            return [(kid, val, self.name) for kid in self.kids]
        if self.kind == '%':      # 🩴 flip-flop module
            if val == 1:
                return            # 💥 high-pulse is ignored
            self.state ^= 1       # 🙃 flip on/off state 👍👎
            return [(kid, self.state, self.name) for kid in self.kids]
        if self.kind == '&':      # 🌈 conjunction module
            self.parents[last] = val
            return [(kid, 0 if all(self.parents.values()) else 1, self.name) for kid in self.kids]

m = defaultdict(Module)
with open('/Users/claytonjwong/sandbox/advent-of-code/2023/20_Pulse_Propagation/input.txt') as input:
    for line in input:
        L, R = line.strip().split(' -> ')
        kind, name = (L[0], L[1:]) if L != 'broadcaster' else ('*', 'broadcaster')
        kids = R.split(', ')
        m[name] = Module(name, kind, kids)
    for name in m.keys():
        for kid in m[name].kids:
            if kid in m:
                m[kid].parents[name] = 0

cnt = Counter()
def run():
    q = deque([('broadcaster', 0, 'Make it so! Engage! 🚀')])  # to name, pulse value, from last name
    while q:
        name, val, last = q.popleft()
        cnt[val] += 1
        next = m[name].process(val, last)
        if next:
            q.extend(next)
for i in range(1000):
    run()
t = cnt[0] * cnt[1]
print(f'part 1: {t}')
# part 1: 1020211150
