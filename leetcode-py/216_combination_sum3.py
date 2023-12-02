#
# 216. Combination Sum III
#
# Q: https://leetcode.com/problems/combination-sum-iii/
# A: https://leetcode.com/problems/combination-sum-iii/discuss/843173/Javascript-Python3-C%2B%2B-DFS-%2B-BT-solutions
#

from typing import List

class Solution:
    def combinationSum3(self, N: int, T: int) -> List[List[int]]:
        paths = []
        def go(n = N, t = T, path = []):
            if not n and not t:
                paths.append(path.copy())         # 🎯 unique path of N nums with T sum
                return
            if not n or not t:
                return
            for i in range(path[-1] + 1 if len(path) else 1, 10):
                if 0 <= t - i:
                    go(n - 1, t - i, path + [i])  # 🚀 recursively explore path with 👀 implicit forward/back-tracking
            return paths
        return go()
