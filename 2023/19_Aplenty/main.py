workflow, xmas = {'A':'A', 'R':'R'}, []
with open('input.txt') as input:
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
                i = 'xmas'.index(c)
                if op == '<' and vals[i] < val: name = dest; break
                if op == '>' and vals[i] > val: name = dest; break
t1 = sum(sum(row) for row in A)
print(f'part 1: {t1}')
# part 1: 476889
