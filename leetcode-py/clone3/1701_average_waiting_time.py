#
# 1701. Average Waiting Time
#
# Q: https://leetcode.com/problems/average-waiting-time/
# A: https://leetcode.com/problems/average-waiting-time/discuss/987309/Kt-Js-Py3-Cpp-Average-Wait-Time
#

from typing import List

class Solution:
    def averageWaitingTime(self, A: List[List[int]], time = 0, last = 0) -> float:
        wait = []
        for i, j in A:
            time = max(i, last)
            last = time + j
            wait.append(last - i)
        return sum(wait) / len(wait)
