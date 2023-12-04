from collections import Counter

t1 = 0
cnt, hi = Counter(), 0
with open('input.txt') as input:
    for line in input:
        L, R = line.strip().split('|')
        num = int([s for s in L.split(':')[0].split()][1]); cnt[num] += 1; hi = max(hi, num)
        need = set(int(s) for s in L.split(':')[1].split())
        have = set(int(s) for s in R.split())
        same = need & have
        t1 += 1 << (len(same) - 1) if len(same) else 0
        for i in range(len(same)):
            take = num + i + 1
            cnt[take] += cnt[num]
t2 = sum(freq for num, freq in cnt.items() if num <= hi)

print(f'part 1: {t1}')
print(f'part 2: {t2}')
# part 1: 25571
# part 2: 8805731
