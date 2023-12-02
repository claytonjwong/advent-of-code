#
# 952. Largest Component Size by Common Factor
#
# Q: https://leetcode.com/problems/largest-component-size-by-common-factor/
# A: https://leetcode.com/problems/largest-component-size-by-common-factor/discuss/204260/Javascript-Python3-C%2B%2B-Union-Find
#

from typing import List
from math import floor, sqrt

class Solution:
    def largestComponentSize(self, A: List[int], N = 100001) -> int:
        m = {}
        P = [i for i in range(N)]   # 🙂 parent representative of disjoint sets
        L = [1] * N                 # 🤥 length of parent representative's set
        def find(x):
            P[x] = P[x] if x == P[x] else find(P[x])
            return P[x]
        def union(a, b):
            a = find(a)
            b = find(b)
            if a == b:
                return
            P[b] = a  # arbitrary choice
            L[a] += L[b]
        for x in A:
            m[x] = x if x not in m else m[x]; union(m[x], x)      # case 1: x as a factor of itself
            for i in range(2, floor(sqrt(x)) + 1):
                if x % i:
                    continue
                j = x // i
                m[i] = x if i not in m else m[i]; union(m[i], x)  # case 2: i-th factor of x
                m[j] = x if j not in m else m[j]; union(m[j], x)  # case 3: j-th factor of x
        return max(L)  # 🎯 maximum length of any parent representative's set
