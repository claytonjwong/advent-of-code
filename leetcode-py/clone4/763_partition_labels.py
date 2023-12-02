#
# 763. Partition Labels
#
# Q: https://leetcode.com/problems/partition-labels/
# A: https://leetcode.com/problems/partition-labels/discuss/828605/Javascript-Python3-C%2B%2B-Sliding-Window
#

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        parts = []
        m = {c: i for i, c in enumerate(S)}           # 🚌 linear scan to find each char's right-most index
        i = 0
        while i < len(S):
            j = m[S[i]]
            k = i + 1
            while k < j: j = max(j, m[S[k]]); k += 1  # 👉 slide window from i..j inclusive (expand j "as needed")
            parts.append(j - i + 1)                   # 🎯 partition found: +1 for i..j inclusive
            j += 1; i = j                             # 👉 move i, j forward to beginning of next partition
        return parts
