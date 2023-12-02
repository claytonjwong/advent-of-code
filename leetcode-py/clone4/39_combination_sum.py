#
# 39. Combination Sum
#
# Q: https://leetcode.com/problems/combination-sum/
# A: https://leetcode.com/problems/combination-sum/discuss/506331/Javascript-Python3-C%2B%2B-DFS-%2B-BT-solutions
#

from typing import List

class Solution:
    def combinationSum(self, A: List[int], T: int) -> List[List[int]]:
        paths = []
        def go(start = 0, t = T, path = []):
            if not t:
                paths.append(path.copy())              # 🎯 unique path with target sum T
                return
            for i in range(start, len(A)):
                if 0 <= t - A[i]:
                    go(i, t - A[i], path + [ A[i] ])   # 🚀 recursively explore path with implicit 👀 forward/back-tracking
            return paths
        return go()
