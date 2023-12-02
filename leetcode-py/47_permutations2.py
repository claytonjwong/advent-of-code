#
# 47. Permutations II
#
# Q: https://leetcode.com/problems/permutations-ii/
# A: https://leetcode.com/problems/permutations-ii/discuss/136432/Kt-Js-Py3-Cpp-DFS-%2B-BT
#

from typing import List

class Solution:
    def permuteUnique(self, A: List[int]) -> List[List[int]]:
        N = len(A)
        ans, path, seen, unique = [], [], set(), set()
        def go():
            if len(path) == N:
                key = ' '.join(str(x) for x in path)
                if key not in unique:
                    unique.add(key)
                    ans.append(path.copy())
                return
            for i in range(N):
                if i not in seen:
                    seen.add(i)
                    path.append(A[i])
                    go()
                    path.pop()
                    seen.remove(i)
        go()
        return ans
