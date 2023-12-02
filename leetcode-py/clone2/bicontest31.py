#
# https://leetcode.com/contest/biweekly-contest-31/ranking/106/
#
# Rank          Name           Score   Finish Time    Q1 (3)     Q2 (4)       Q3 (5)    Q4 (7)
# 2636 / 8677   claytonjwong   12      1:16:49        0:05:09    1:11:49 *1   0:41:05
#
# Screenshare: https://www.youtube.com/watch?v=zdqg0ERZk_I&feature=youtu.be
#

#
# 1523. Count Odd Numbers in an Interval Range
#
# Q: https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/
# A: https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/discuss/754764/Javscript-Python3-C%2B%2B-1-Liners
#
class Solution:
    def countOdds(self, i: int, j: int) -> int:
        return max(0, (j - i - 1) // 2) + (i % 2) + (j % 2) + (not (i % 2) and not (j % 2)) - (i == j)


#
# 1524. Number of Sub-arrays With Odd Sum
#
# Q: https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/
# A: https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/discuss/754751/Javascript-Python3-C%2B%2B-count-of-evenodd-sums
#
class Solution:
    def numOfSubarrays(self, A: List[int]) -> int:
        sum = 0
        cnt = [1, 0]
        for i in range(len(A)):
            sum += A[i]
            cnt[sum % 2] += 1
        return (cnt[0] * cnt[1]) % int(1e9 + 7)

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
