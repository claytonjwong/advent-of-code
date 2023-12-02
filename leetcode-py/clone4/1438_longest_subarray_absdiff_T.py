#
# 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
#
# Q: https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/
# A: https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/discuss/751204/Javascript-Python3-C%2B%2B-Map-for-MinMax
#

class Solution:
    def longestSubarray(self, A: List[int], T: int, best = 0) -> int:
        m = collections.Counter()
        N, i, j = len(A), 0, 1 # A[i..j) => i inclusive to j non-inclusive
        m[A[i]] = 1
        while True:
            minmax = list(map(lambda pair: pair[0], sorted(m.items()))) # hack since Python3 lacks an ordered map
            minimum = minmax[0]
            maximum = minmax[-1]
            if maximum - minimum <= T:
                best = max(best, j - i) # 🎯 best, ie. max length from i inclusive to j non-inclusive
                if j == N:
                    break
                m[A[j]] += 1   # "grow" window
                j += 1
            else:
                m[A[i]] -= 1   # "shrink" window
                if not m[A[i]]:
                    del m[A[i]]
                i += 1
        return best
