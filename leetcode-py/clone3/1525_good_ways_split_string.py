#
# 1525. Number of Good Ways to Split a String
#
# Q: https://leetcode.com/problems/number-of-good-ways-to-split-a-string/
# A: https://leetcode.com/problems/number-of-good-ways-to-split-a-string/discuss/754776/Javascript-Python3-C%2B%2B-count-uniques-from-leftright
#
class Solution:
    def numSplits(self, s: str, cnt = 0) -> int:
        N = len(s)
        L, R = [0] * N, [0] * N
        uniqueL = set()
        uniqueR = set()
        for i in range(N):             # unique counts from Left-to-right 👉
            uniqueL.add(s[i])
            L[i] = len(uniqueL)
        for j in range(N - 1, -1, -1): # unique counts from Right-to-left 👈
            uniqueR.add(s[j])
            R[j] = len(uniqueR)
        for i in range(1, N):
            if L[i - 1] == R[i]:
                cnt += 1
        return cnt
