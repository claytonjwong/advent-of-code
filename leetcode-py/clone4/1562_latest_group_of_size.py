#
# 1562. Find Latest Group of Size M
#
# Q: https://leetcode.com/problems/find-latest-group-of-size-m/
# A: https://leetcode.com/problems/find-latest-group-of-size-m/discuss/810189/Javascript-Python3-C%2B%2B-Union-Find
#

from typing import List

class Solution:
    def findLatestStep(self, A: List[int], T: int, last = -1) -> int:
        seen, ok = set(), set()
        A = [i - 1 for i in A]      # ⭐️ -1 for 0-based indexing
        N = len(A)
        P = [i for i in range(N)]   # 🙂 parent representative sets
        L = [1] * N                 # 🤥 length of each representative set
        def find(x):
            if x != P[x]:
                P[x] = find(P[x])
            return P[x]
        def union(a, b):
            a = find(a)
            b = find(b)
            P[b] = a                # 🔗 arbitrary choice for parent representative
            L[a] += L[b]
            return L[a]
        step = 1
        for i in A:
            seen.add(i)
            if 0 < i     and find(P[i - 1]) in ok: ok.remove(find(P[i - 1]))
            if i + 1 < N and find(P[i + 1]) in ok: ok.remove(find(P[i + 1]))
            if i - 1 in seen: L[i] = union(i, i - 1)
            if i + 1 in seen: L[i] = union(i, i + 1)
            if L[i] == T:
                ok.add(i)          # ✅ i is the parent reprentative of the set with 🎯 target T length
            if len(ok):
                last = step
            step += 1
        return last
