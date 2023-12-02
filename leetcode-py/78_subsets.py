#
# 78. Subsets
#
# Q: https://leetcode.com/problems/subsets/
# A: https://leetcode.com/problems/subsets/discuss/731155/Kt-Js-Py3-Cpp-DFS-%2B-BT
#

from typing import List

class Solution:
    def subsets(self, A: List[int]) -> List[List[int]]:
        paths = []
        N = len(A)
        def go(i = 0, path = []):
            if i == N:
                paths.append(path.copy())  # 🛑 base case: add the unique path onto the answer
                return
            go(i + 1, path + [A[i]])       # ✅ with A[i]
            go(i + 1, path)                # 🚫 without A[i]
        go()
        return paths
