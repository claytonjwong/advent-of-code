A = []
with open('input.txt') as input:
    for line in input:
        S, T = line.split()  # String, Target
        S = [c if c != '.' else ' ' for c in S]
        T = [int(x) for x in T.split(',')]
        A.append((S, T))

def go(S, T, i = 0, t = 0):
    if i == len(S):
        return [len(it) for it in ''.join(S).split()] == T
    if S[i] != '?':
        return go(S, T, i + 1)
    last = S[i]
    for next in ['#', ' ']:
        S[i] = next
        t += go(S, T, i + 1)
    S[i] = last
    return t

t1 = sum(go(S, T) for S, T in A)
print(f'part 1: {t1}')
# part 1: 8180
