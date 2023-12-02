#
# Weekly Contest 204
#
# Rank            Name             Score    Finish Time    Q1 (3)     Q2 (4)        Q3 (6)    Q4 (7)
# 2025 / 13949    claytonjwong     7        0:50:49        0:17:53    0:40:49 *2
#
# Ranking: https://leetcode.com/contest/weekly-contest-204/ranking/81/
# Screenshare: https://www.youtube.com/watch?v=fPmeK1rsSiY&feature=youtu.be
#


#
# 1566. Detect Pattern of Length M Repeated K or More Times
#
# Q: https://leetcode.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times/
# A: https://leetcode.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times/discuss/819276/Javascript-Python3-C%2B%2B-T-Pieces-Whole
#

from typing import List

class Solution:
    def containsPattern(self, A: List[int], K: int, T: int) -> bool:
        j = K * T
        for i in range(0, len(A) - j + 1):
            piece = A[i:i + K]
            whole = T * piece
            if whole == A[i:i + j]:
                return True
        return False


#
# 1567. Maximum Length of Subarray With Positive Product
#
# Q: https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/
# A: https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/discuss/822464/Javascript-Python3-C%2B%2B-Sliding-Window
#

class Solution:
    def getMaxLen(self, A: List[int], cnt = 0, best = 0) -> int:
        A.append(0)  # ⭐️ sentinel value
        N = len(A)
        i = 0
        j = 0
        while i != N:
            # case 1: ➖ collapse window [i 👉 ..j]
            while j < N and not A[j]:
                while i < j:
                    cnt = cnt - 1 if A[i] < 0 else cnt; i += 1
                    best = best if cnt & 1 else max(best, j - i)
                i = j + 1
                j = j + 1
            # case 2: ➕ expand window [i..j 👉 ]
            while j < N and A[j]:
                cnt = cnt + 1 if A[j] < 0 else cnt; j += 1
                best = best if cnt & 1 else max(best, j - i)
        return best
