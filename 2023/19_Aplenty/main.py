# 2:16pm - read problem statement

# game plan: parse workflow name{ comma separated rule values which represent a nested if-else and the last rule is the "final catch all" else }

# each rule is a ':' separated if-then, ie. if predicate is true, then go to workflow name

# each workflow name can be stored as an associative array of workflow name -> workflow rules

# parse input as two chunks: first would be the workflows+rules
# second would be the values of each variable -> we can store this in a map also

# print(787 + 2655 + 1222 + 2876) = 7540

# px{a<2006:qkq,m>2090:A,rfg}
# pv{a>1716:R,A}
# lnx{m>1548:A,A}
# rfg{s<537:gd,x>2440:R,A}
# qs{s>3448:A,lnx}
# qkq{x<1416:A,crn}
# crn{x>2662:A,R}
# in{s<1351:px,qqz}
# qqz{s>2770:qs,m<1801:hdj,R}
# gd{a>3333:R,R}
# hdj{m>838:A,pv}

# {x=787,m=2655,a=1222,s=2876}
# {x=1679,m=44,a=2067,s=496}
# {x=2036,m=264,a=79,s=2244}
# {x=2461,m=1339,a=466,s=291}
# {x=2127,m=1623,a=2188,s=1013}

# 2:27pm - implementation begins
# 2:55pm - implementation ends -> ~28 minutes and debugging begins, LOL --> this isn't doing what I want it to do 😵 ... not yet anyhow 👻
# 3:09pm - part 1 accepted, yay 👍

workflow, xmas, index = {'A': 'A', 'R': 'R'}, [], {c: i for i, c in enumerate('xmas')}
with open('/Users/claytonjwong/sandbox/advent-of-code/2023/19_Aplenty/input.txt') as input:
    for line in input:
        line = line.strip()
        if not len(line):
            continue
        if line[0] == '{':
            vals = [int(pair.split('=')[1]) for pair in line[1:-1].split(',')]  # line[1:-1] to exclude prefix and suffix as '{' and '}' correspondingly
            xmas.append(vals)
        else:
            line = line.replace('{', ' ')
            line = line.replace('}', ' ')
            name, rules = line.split()
            workflow[name] = rules.split(',')

A, R = [], []
for vals in xmas:
    name, done = 'in', False
    while not done:
        for rule in workflow[name]:
            if   rule == 'A': A.append(vals); done = True
            elif rule == 'R': R.append(vals); done = True
            elif rule in workflow: name = rule; break
            else:
                pred, dest = rule.split(':')  # predicate, destination workflow name
                c, op, val = pred[0], pred[1], int(pred[2:])
                i = index[c]
                if op == '<' and vals[i] < val: name = dest; break
                if op == '>' and vals[i] > val: name = dest; break
t1 = sum(sum(row) for row in A)
print(f'part 1: {t1}')
