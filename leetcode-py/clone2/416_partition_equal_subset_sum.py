#
# 416. Partition Equal Subset Sum
#
# Q: https://leetcode.com/problems/partition-equal-subset-sum/
# A: https://leetcode.com/problems/partition-equal-subset-sum/discuss/617275/Kt-Js-Py3-Cpp-The-ART-of-Dynamic-Programming
#

from typing import List

# top-down
class Solution:
    def canPartition(self, A: List[int]) -> bool:
        total = sum(A)
        if total & 1:                                   # ❌ odd total cannot be evenly divided by 2
            return False
        target = total // 2
        def go(i = 0, t = 0):
            if i == len(A) or target < t:               # 🛑 base case: target not reached
                return False
            if t == target:                             # 🎯 target reached
                return True
            return go(i + 1, t + A[i]) or go(i + 1, t)  # 🚀 explore ✅ with xor 🚫 without A[i]
        return go()

# memo
class Solution:
    def canPartition(self, A: List[int]) -> bool:
        m = {}
        total = sum(A)
        if total & 1:                                         # ❌ odd total cannot be evenly divided by 2
            return False
        target = total // 2
        def go(i = 0, t = 0):
            key = f'{i},{t}'
            if key in m:                                      # 🤔 memo
                return m[key]
            if i == len(A) or target < t:                     # 🛑 base case: target not reached
                m[key] = False
            if t == target:                                   # 🎯 target reached
                m[key] = True
            if key not in m:
                m[key] = go(i + 1, t + A[i]) or go(i + 1, t)  # 🚀 explore ✅ with xor 🚫 without A[i]
            return m[key]
        return go()

# bottom-up
class Solution:
    def canPartition(self, A: List[int]) -> bool:
        total = sum(A)
        if total & 1:                            # ❌ odd total cannot be evenly divided by 2
            return False
        target = total // 2
        dp = [0] * (target + 1)                  # 🤔 memo
        dp[0] = 1                                # 🛑 base case: we can reach target 0
        for x in A:                              # 🤔 if we can reach t 🚫 without x, then we can reach t ✅ with x
            for t in range(target, x - 1, -1):
                if dp[t - x]:
                    dp[t] = 1
        return dp[target]                        # 🎯 target reached?
