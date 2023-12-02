#
# 131. Palindrome Partitioning
#
# Q: https://leetcode.com/problems/palindrome-partitioning/
# A: https://leetcode.com/problems/palindrome-partitioning/discuss/972094/Kt-Js-Py3-Cpp-DFS-%2B-BT
#

from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        paths = []
        N = len(s)
        ok = lambda A: ''.join(A) == ''.join(reversed(A))
        def go(i = 0, path = []):
            if i == N:
                paths.append(path.copy())
                return
            cand = []
            while i < N:
                cand.append(s[i])
                if ok(cand):
                    go(i + 1, path + [''.join(cand)])
                i += 1
        go()
        return paths
