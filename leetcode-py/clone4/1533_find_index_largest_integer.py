#
# 1533. Find the Index of the Large Integer
#
# Q: https://leetcode.com/problems/find-the-index-of-the-large-integer/
# A: https://leetcode.com/problems/find-the-index-of-the-large-integer/discuss/765851/Javascript-Python3-C%2B%2B-binary-search-one-xor-two-%22middles%22
#

class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        N = reader.length()
        i = 0
        j = N - 1
        p = 0                                          # 💎 p is the pivot
        while i <= j:
            k = (i + j) // 2
            if (j - i) % 2:
                p = reader.compareSub(i, k, k + 1, j)  # ⭐️ even subarray has two non-overlapping "middles": k, k + 1
            else:
                p = reader.compareSub(i, k, k, j)      # ⭐️ odd subarray has a single overlapping "middle": k
            if not p: return k   # 🎯 found ✅
            if p < 0: i = k + 1  # 🔍 search 👉
            if 0 < p: j = k      # 🔍 search 👈
        return -1  # 🎯 not found 🚫 (invalid use case)
