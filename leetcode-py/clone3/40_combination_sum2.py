#
# 40. Combination Sum II
#
# Q: https://leetcode.com/problems/combination-sum-ii/
# A: https://leetcode.com/problems/combination-sum-ii/discuss/506360/Javascript-Python3-C%2B%2B-DFS-%2B-BT-solutions
#

from typing import List

class Solution:
    def combinationSum2(self, A: List[int], T: int) -> List[List[int]]:
        seen, paths = set(), []
        def go(start = 0, t = T, path = []):
            if not t:
                key = str(sorted(path))
                if key not in seen:
                    paths.append(path.copy())             # 🎯 unique path with target sum T
                seen.add(key)
                return
            for i in range(start, len(A)):
                if 0 <= t - A[i]:
                    go(i + 1, t - A[i], path + [ A[i] ])  # 🚀 recursively explore path with implicit 👀 forward/back-tracking
            return paths
        return go()
