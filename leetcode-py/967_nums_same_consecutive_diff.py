#
# 967. Numbers With Same Consecutive Differences
#
# Q: https://leetcode.com/problems/numbers-with-same-consecutive-differences/
# A: https://leetcode.com/problems/numbers-with-same-consecutive-differences/discuss/211594/Javascript-Python3-C%2B%2B-DFS-%2B-BT
#

from typing import List

class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        ans = []
        def go(path = []):
            if len(path) == N:
                ans.append(''.join(map(str, path)))
                return
            for i in range(10):
                if not len(path) or i == path[-1] + K or i == path[-1] - K:
                    path.append(i)
                    go(path)
                    path.pop()
        go()
        if N == 1:
            return ans
        return list(filter(lambda s: s[0] != '0', ans))
