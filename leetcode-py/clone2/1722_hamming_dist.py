#
# 1722. Minimize Hamming Distance After Swap Operations
#
# Q: https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/
# A: https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/discuss/1009782/Kt-Js-Py3-Cpp-Union-Find-%2B-Set-Diff
#

from collections import Counter

class Solution:
    def minimumHammingDistance(self, s: List[int], t: List[int], A: List[List[int]]) -> int:
        N = len(s)
        P = [i for i in range(N)]  #  🔗  N disjoint parent representatives of unioned indices
        def find(x):
            P[x] = x if P[x] == x else find(P[x])
            return P[x]
        def union(a, b):
            a = find(a)
            b = find(b)
            P[a] = b  # 🎲 arbitrary choice
        for i, j in A:
            union(i, j)
        ms, mt = {}, {}
        for i in range(N):
            x = find(P[i])
            if x not in ms: ms[x] = []
            if x not in mt: mt[x] = []
            ms[x].append(s[i])
            mt[x].append(t[i])
        diff = lambda x: sum((Counter(ms[x]) - Counter(mt[x])).values())
        return sum(diff(x) for x in set(find(x) for x in P))
