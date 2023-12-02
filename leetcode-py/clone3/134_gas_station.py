#
# 134. Gas Station
#
# Q: https://leetcode.com/problems/gas-station/
# A: https://leetcode.com/problems/gas-station/discuss/861437/Javascript-Python3-C%2B%2B-Recursive-Brute-Force
#

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)
        def go(i, total, steps = 0):
            if steps == N:
                return True
            total -= cost[i]
            if total < 0:
                return False
            j = i + 1 if i + 1 < N else 0
            return go(j, total + gas[j], steps + 1)
        for start in range(N):
            if go(start, gas[start]):
                return start
        return -1
