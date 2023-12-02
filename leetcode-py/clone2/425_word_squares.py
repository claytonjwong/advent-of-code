#
# 425. Word Squares
#
# Q: https://leetcode.com/problems/word-squares/
# A: https://leetcode.com/problems/word-squares/discuss/871098/Javascript-Python3-C%2B%2B-Map-Prefix-and-DFS-%2B-BT
#

from typing import List

class Solution:
    def wordSquares(self, A: List[str]) -> List[List[str]]:
        m = {}
        for word in A:
            pre = ''
            if pre not in m: m[pre] = []
            m[pre].append(word)
            for c in word:
                pre = pre + c
                if pre not in m: m[pre] = []
                m[pre].append(word)
        N, ans = len(A[0]), []
        def go(path = []):
            i = len(path)
            if i == N:
                ans.append(path.copy())
                return
            pre = ''
            k = i
            for j in range(k):
                pre = pre + path[j][k]
            for word in (m[pre] if pre in m else []):
                go(path + [word])
        go()
        return ans
